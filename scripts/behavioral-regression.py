#!/usr/bin/env python3
"""Behavioral regression: run the *real* skill on eval cases with a real model,
then score the fresh output with a model judge and the deterministic checks.

The recorded-output suite (``eval-suite.py``) guards fixtures; this script
guards the skill itself. It sends ``SKILL.md`` (plus the reference files it
points to) as the system prompt, asks the editor model to perform each case's
``Talep`` on its ``Kaynak``, then:

1. runs ``eval-runner.py`` invariants and ``style-lint.py`` hard-pattern checks
   on the fresh output (deterministic gate);
2. asks a judge model to score the output against the case's ``Korunması
   gerekenler``, ``Kaçınılması gerekenler`` and the shared rubric in
   ``evals/README.md`` (semantic gate). The judge must end with
   ``SONUÇ: GEÇTİ`` or ``SONUÇ: BAŞARISIZ``.

Every run spends real money, so the default case list is the curated
``evals/critical-cases.txt``; CI runs it on a schedule or on demand, never on
every push. Fresh outputs, judge verdicts and a summary are written under
``build/behavioral/``.

Usage:
    python scripts/behavioral-regression.py                # critical cases
    python scripts/behavioral-regression.py --cases evals/akademik.md evals/hukuki.md
    python scripts/behavioral-regression.py --all
    python scripts/behavioral-regression.py --dry-run      # no API calls; prints the plan
    python scripts/behavioral-regression.py --editor-model claude-opus-5 --judge-model claude-opus-5

Credentials come from the Anthropic SDK's usual resolution (``ANTHROPIC_API_KEY``
or an ``ant auth login`` profile).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
BUILD = ROOT / "build" / "behavioral"
DEFAULT_EDITOR = "claude-opus-5"
DEFAULT_JUDGE = "claude-opus-5"
REFERENCE_ORDER = (
    "turkce-oruntuler.md", "retorik-yapilar.md", "yapisal-butunluk.md", "akicilik.md",
    "turkce-ritim-ve-ceviri-kokusu.md", "kanit-ve-kesinlik.md", "sozcuk-birlesimleri.md",
    "metinsel-tutarlilik.md", "rapor-yazimi.md", "kavramsal-girisler.md",
)
VERDICT_RE = re.compile(r"SONUÇ:\s*(GEÇTİ|BAŞARISIZ)", re.IGNORECASE)


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


runner = load_module("eval_runner", "eval-runner.py")
lint = load_module("style_lint", "style-lint.py")


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="backslashreplace")


def section(text: str, heading: str, required: bool = True) -> str:
    try:
        return runner.section(text, heading)
    except ValueError:
        if required:
            raise
        return ""


@dataclass
class CaseResult:
    case: str
    deterministic_ok: bool
    deterministic_problems: list[str]
    judge_verdict: str | None
    judge_report: str
    output: str
    usage: dict[str, int]

    @property
    def passed(self) -> bool:
        return self.deterministic_ok and self.judge_verdict == "GEÇTİ"


def skill_system_prompt(with_references: bool) -> list[dict[str, object]]:
    """SKILL.md first, then the reference files, each as a cached block so a
    run over many cases pays for the skill text once."""
    blocks: list[dict[str, object]] = [{"type": "text", "text": (ROOT / "SKILL.md").read_text(encoding="utf-8")}]
    if with_references:
        for name in REFERENCE_ORDER:
            path = ROOT / "references" / name
            if path.is_file():
                blocks.append({"type": "text", "text": f"\n\n<!-- references/{name} -->\n\n" + path.read_text(encoding="utf-8")})
    blocks[-1]["cache_control"] = {"type": "ephemeral"}
    return blocks


def editor_prompt(case_text: str) -> str:
    return (
        "Aşağıdaki talebi Metinoskop skill'ine göre uygula. Yalnızca düzenlenmiş metni ver; "
        "açıklama, başlık, sohbet girişi ya da kapanış ekleme. Kaynak Markdown yapısı taşıyorsa koru.\n\n"
        f"## Talep\n\n{section(case_text, 'Talep')}\n\n## Kaynak\n\n{section(case_text, 'Kaynak')}"
    )


def judge_prompt(case_text: str, output: str, rubric: str) -> str:
    return (
        "Sen bir Türkçe editörlük hakemisin. Aşağıdaki kaynak ve talep için üretilen çıktıyı, yalnızca verilen "
        "ölçütlere göre değerlendir. Tek bir doğru yeniden yazım yoktur; davranışı puanla. Her ihlali kaynaktan ve "
        "çıktıdan alıntıyla göster. Çıktının kaynağın epistemik düzeyini (gözlem, ölçüm, aktarım, çıkarım, öneri, "
        "karar) değiştirip değiştirmediğini özellikle denetle.\n\n"
        f"## Kaynak\n\n{section(case_text, 'Kaynak')}\n\n"
        f"## Talep\n\n{section(case_text, 'Talep')}\n\n"
        f"## Çıktı\n\n{output.strip()}\n\n"
        f"## Korunması gerekenler\n\n{section(case_text, 'Korunması gerekenler')}\n\n"
        f"## Kaçınılması gerekenler\n\n{section(case_text, 'Kaçınılması gerekenler')}\n\n"
        f"## Genel hakem ölçütleri\n\n{rubric}\n\n"
        "## İstenen cevap biçimi\n\n"
        "1. Korunması gerekenler: her madde için KORUNDU / İHLAL + kanıt\n"
        "2. Kaçınılması gerekenler: her madde için UYULDU / İHLAL + kanıt\n"
        "3. Genel ölçütler: yalnızca ihlal olanlar için kısa değerlendirme\n"
        "4. Son satır tam olarak şu biçimde olsun: SONUÇ: GEÇTİ  ya da  SONUÇ: BAŞARISIZ\n"
    )


def deterministic_checks(case_text: str, output: str) -> tuple[bool, list[str]]:
    problems: list[str] = []
    invariants = runner.evaluate(case_text, output)
    for item in invariants["missing"]:
        problems.append(f"eksik {item['category']}: {' | '.join(item['alternatives'])}")
    comparison = lint.compare(lint.analyse(section(case_text, "Kaynak")), lint.analyse(output))
    for item in comparison["introduced_hard"]:
        problems.append(f"yeni sert kalıp: {item['label']} «{item['example']}»")
    return not problems, problems


def call_text(client, model: str, system, user: str, max_tokens: int) -> tuple[str, dict[str, int]]:
    """One streamed request; returns the concatenated text and token usage."""
    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    ) as stream:
        message = stream.get_final_message()
    if message.stop_reason == "refusal":
        raise RuntimeError(f"{model} refused the request: {getattr(message, 'stop_details', None)}")
    text = "".join(block.text for block in message.content if block.type == "text")
    usage = {
        "input": message.usage.input_tokens,
        "output": message.usage.output_tokens,
        "cache_read": getattr(message.usage, "cache_read_input_tokens", 0) or 0,
        "cache_write": getattr(message.usage, "cache_creation_input_tokens", 0) or 0,
    }
    return text, usage


def run_case(client, case_path: Path, system, rubric: str, editor_model: str, judge_model: str) -> CaseResult:
    case_text = case_path.read_text(encoding="utf-8")
    output, usage_edit = call_text(client, editor_model, system, editor_prompt(case_text), max_tokens=16000)
    det_ok, det_problems = deterministic_checks(case_text, output)
    report, usage_judge = call_text(
        client, judge_model,
        "Sen titiz bir Türkçe editörlük hakemisin. Kaynakta olmayan hiçbir şeyi doğru varsayma.",
        judge_prompt(case_text, output, rubric), max_tokens=8000,
    )
    match = VERDICT_RE.search(report)
    verdict = match.group(1).upper().replace("GEÇTI", "GEÇTİ") if match else None
    usage = {k: usage_edit[k] + usage_judge[k] for k in usage_edit}
    return CaseResult(case_path.stem, det_ok, det_problems, verdict, report, output, usage)


def select_cases(args: argparse.Namespace) -> list[Path]:
    if args.cases:
        return [Path(c) if Path(c).is_file() else EVALS / f"{c}.md" for c in args.cases]
    if args.all:
        return sorted(p for p in EVALS.glob("*.md") if p.name != "README.md")
    names = (EVALS / "critical-cases.txt").read_text(encoding="utf-8").split()
    return [EVALS / f"{name}.md" for name in names]


def main() -> int:
    configure_stdio()
    parser = argparse.ArgumentParser(description="Gerçek model + gerçek skill ile davranışsal regresyon.")
    parser.add_argument("--cases", nargs="*", help="Vaka adları ya da evals/*.md yolları")
    parser.add_argument("--all", action="store_true", help="Bütün vakaları çalıştır (pahalı)")
    parser.add_argument("--editor-model", default=DEFAULT_EDITOR)
    parser.add_argument("--judge-model", default=DEFAULT_JUDGE)
    parser.add_argument("--no-references", action="store_true", help="Sistem istemine references/ dosyalarını ekleme")
    parser.add_argument("--dry-run", action="store_true", help="API çağrısı yapma; planı yazdır")
    parser.add_argument("--out", type=Path, default=BUILD, help="Çıktı klasörü")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    cases = select_cases(args)
    missing = [c for c in cases if not c.is_file()]
    if missing:
        print(f"Hata: vaka bulunamadı: {', '.join(str(m) for m in missing)}", file=sys.stderr)
        return 2
    rubric = section((EVALS / "README.md").read_text(encoding="utf-8"), "Hakem ölçütleri")
    system = skill_system_prompt(with_references=not args.no_references)
    system_bytes = sum(len(str(b["text"]).encode("utf-8")) for b in system)

    if args.dry_run:
        print(f"Kuru çalıştırma: {len(cases)} vaka, düzenleyici {args.editor_model}, hakem {args.judge_model}, "
              f"sistem istemi {system_bytes // 1024} KB ({len(system)} blok, sonuncusu önbellekli).")
        for case in cases:
            print(f"  - {case.stem}")
        return 0

    try:
        import anthropic
    except ImportError:
        print("Hata: `pip install anthropic` gerekli.", file=sys.stderr)
        return 2
    client = anthropic.Anthropic()

    args.out.mkdir(parents=True, exist_ok=True)
    results: list[CaseResult] = []
    for case in cases:
        started = time.time()
        try:
            result = run_case(client, case, system, rubric, args.editor_model, args.judge_model)
        except anthropic.RateLimitError as error:
            print(f"Hız sınırı ({case.stem}): {error}. 60 sn bekleniyor.", file=sys.stderr)
            time.sleep(60)
            result = run_case(client, case, system, rubric, args.editor_model, args.judge_model)
        except anthropic.APIStatusError as error:
            print(f"API hatası ({case.stem}): {error.status_code} {error.message}", file=sys.stderr)
            return 2
        except anthropic.APIConnectionError as error:
            print(f"Bağlantı hatası ({case.stem}): {error}", file=sys.stderr)
            return 2
        results.append(result)
        (args.out / f"{case.stem}.output.txt").write_text(result.output, encoding="utf-8", newline="\n")
        (args.out / f"{case.stem}.judge.md").write_text(result.judge_report, encoding="utf-8", newline="\n")
        state = "GEÇTİ" if result.passed else "BAŞARISIZ"
        print(f"{state}: {case.stem} ({time.time() - started:.0f} sn; hakem: {result.judge_verdict or 'karar yok'}; "
              f"deterministik: {'temiz' if result.deterministic_ok else 'sorunlu'})")
        for problem in result.deterministic_problems:
            print(f"  - {problem}")

    failed = [r for r in results if not r.passed]
    summary = {
        "editor_model": args.editor_model, "judge_model": args.judge_model,
        "with_references": not args.no_references, "system_prompt_bytes": system_bytes,
        "results": [{"case": r.case, "passed": r.passed, "judge": r.judge_verdict,
                     "deterministic": r.deterministic_problems, "usage": r.usage} for r in results],
    }
    (args.out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    total_in = sum(r.usage["input"] + r.usage["cache_read"] + r.usage["cache_write"] for r in results)
    total_out = sum(r.usage["output"] for r in results)
    print(f"\n{len(results) - len(failed)}/{len(results)} vaka geçti; girdi {total_in} token, çıktı {total_out} token; "
          f"rapor: {args.out}")
    print("Not: Hakem kararı model kararıdır; başarısız vakada önce hakem raporunu, sonra vaka ölçütlerini okuyun.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
