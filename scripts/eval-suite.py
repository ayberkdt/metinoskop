#!/usr/bin/env python3
"""Regression suite over recorded eval outputs.

For every ``evals/<case>.md`` that has a recorded output in
``evals/outputs/<case>.txt`` the suite runs three deterministic checks:

1. source invariants (numbers, dates, code, markers) via ``eval-runner.py``;
2. no *hard-suppression* pattern introduced relative to the source via
   ``style-lint.py`` (context-sensitive families only warn);
3. the structural expectations declared in the case's optional
   ``## Yapısal beklenti`` section (``- başlık: <= 1``, ``- liste ögesi: 0`` ...),
   including source-language-shadow metrics such as ``- sahip olmak: 0``,
   ``- çerçeve yığını: 0``, ``- tekrarlanan cümle başlangıcı: 0`` or ``- bir / 100 sözcük: <= 6``,
   and discourse metrics such as ``- kiplik yığını: 0``, ``- pekiştirici: 0``,
   ``- aktarım sonrası sonuç: 0``, ``- kip nöbetleşmesi: 0``, ``- hafif fiil: 0``,
   ``- ilgeç yoğunluğu: 0``, ``- eş anlamlı kayması: 0``, ``- konu sıfırlama: 0``,
   ``- parantez yükü: 0``, ``- kayıt kayması: 0``,
   ``- zamansal sürtünme: 0`` or ``- geniş zaman doygunluğu: 0``.

Recorded outputs are reference edits, not the only acceptable ones; they keep
the skill's documented behaviour from regressing silently. Human or model
judgement is still required for fluency, tone and meaning. ``--export-judge-prompts``
writes one prompt file per case so a model judge can score the recorded (or a
fresh) output against the case's preserve/avoid lists.

Usage:
    python scripts/eval-suite.py
    python scripts/eval-suite.py --json
    python scripts/eval-suite.py --export-judge-prompts build/judge
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
OUTPUTS = EVALS / "outputs"
SECTION_HEADINGS = ("Kaynak", "Talep", "Korunması gerekenler", "Kaçınılması gerekenler", "Yapısal beklenti", "Serbest değişmezler")
EXPECTATION_RE = re.compile(r"^-\s*(?P<key>[^:]+?)\s*:\s*(?P<op><=|>=|==|=|<|>)?\s*(?P<value>-?\d+(?:[.,]\d+)?)\s*$")
EXPECTATION_KEYS = {
    "başlık": ("structure_summary", "headings"),
    "en derin düzey": ("structure_summary", "max_depth"),
    "tek paragraflık bölüm": ("structure_summary", "one_paragraph_sections"),
    "düzyazı paragrafı": ("structure_summary", "prose_paragraphs"),
    "≤2 cümlelik paragraf": ("structure_summary", "short_paragraphs"),
    "kısa paragraf": ("structure_summary", "short_paragraphs"),
    "liste ögesi": ("structure_summary", "list_items"),
    "çapraz gönderme": ("structure_summary", "cross_references"),
    "duyuru/sarmalayıcı": ("structure_summary", "announcements"),
    "önem/sonuç cümlesi": ("structure_summary", "mini_conclusions"),
    "sert işaret": ("", "hard_hits"),
    "cümle": ("", "sentences"),
    "sahip olmak": ("ceviri_kokusu", "sahip_olmak"),
    "varlık kalıbı": ("ceviri_kokusu", "varlik_kalibi"),
    "çerçeve yığını": ("ceviri_kokusu", "cerceve_yigini"),
    "olan zinciri": ("ceviri_kokusu", "olan_zinciri"),
    "tekrarlanan cümle başlangıcı": ("ceviri_kokusu", "tekrarlanan_cumle_baslangici"),
    "ve zinciri": ("ceviri_kokusu", "ve_zinciri"),
    "fiilimsi yığını": ("ceviri_kokusu", "fiilimsi_yigini"),
    "iyelik zinciri": ("ceviri_kokusu", "iyelik_zinciri"),
    "bağlaçla başlayan cümle": ("ceviri_kokusu", "baglac_baslangici"),
    "bir / 100 sözcük": ("ceviri_kokusu", "bir_per_100"),
    "çekince işareti": ("soylem_olculeri", "kiplik"),
    "pekiştirici": ("soylem_olculeri", "pekistirici"),
    "hafif fiil": ("soylem_olculeri", "hafif_fiil"),
    "kiplik yığını": ("soylem_olculeri", "kiplik_yigini"),
    "pekiştirici çatışması": ("soylem_olculeri", "pekistirici_catismasi"),
    "kip nöbetleşmesi": ("soylem_olculeri", "kip_nobetlesmesi"),
    "edilgen adlaştırma": ("soylem_olculeri", "edilgen_adlastirma"),
    "aktarım sonrası sonuç": ("soylem_olculeri", "aktarim_sonrasi_sonuc"),
    "ilgeç yoğunluğu": ("soylem_olculeri", "ilgec_yogunlugu"),
    "eş anlamlı kayması": ("soylem_olculeri", "esanlam_kaymasi"),
    "konu sıfırlama": ("soylem_olculeri", "konu_sifirlama"),
    "parantez yükü": ("soylem_olculeri", "parantez_yuku"),
    "kayıt kayması": ("soylem_olculeri", "kayit_kaymasi"),
    "zamansal sürtünme": ("soylem_olculeri", "zamansal_surtunme"),
    "geniş zaman doygunluğu": ("soylem_olculeri", "genis_zaman_doygunlugu"),
}


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module  # dataclasses resolve annotations through sys.modules
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


def parse_expectations(block: str) -> list[tuple[str, str, float]]:
    expectations: list[tuple[str, str, float]] = []
    for line in block.splitlines():
        line = line.strip()
        if not line:
            continue
        match = EXPECTATION_RE.match(line)
        if match is None:
            raise ValueError(f"Yapısal beklenti satırı anlaşılamadı: {line!r}")
        key = match.group("key").strip().casefold()
        if key not in {k.casefold() for k in EXPECTATION_KEYS}:
            raise ValueError(f"Bilinmeyen yapısal ölçü: {match.group('key')!r}")
        op = match.group("op") or "="
        value = float(match.group("value").replace(",", "."))
        expectations.append((key, op, value))
    return expectations


def lookup(report: dict[str, object], key: str) -> float | None:
    for label, (container, field) in EXPECTATION_KEYS.items():
        if label.casefold() == key:
            source = report[container] if container else report  # type: ignore[index]
            value = source[field]  # type: ignore[index]
            return None if value is None else float(value)
    return None


def holds(actual: float, op: str, expected: float) -> bool:
    return {
        "=": actual == expected, "==": actual == expected,
        "<=": actual <= expected, ">=": actual >= expected,
        "<": actual < expected, ">": actual > expected,
    }[op]


def evaluate_case(case_path: Path, output_path: Path) -> dict[str, object]:
    case_text = case_path.read_text(encoding="utf-8")
    output_text = output_path.read_text(encoding="utf-8")
    source = section(case_text, "Kaynak")

    invariants = runner.evaluate(case_text, output_text)
    source_report = lint.analyse(source)
    output_report = lint.analyse(output_text)
    comparison = lint.compare(source_report, output_report)
    expectations = parse_expectations(section(case_text, "Yapısal beklenti", required=False))

    failed_expectations: list[str] = []
    for key, op, expected in expectations:
        actual = lookup(output_report, key)
        if actual is None or not holds(actual, op, expected):
            failed_expectations.append(f"{key}: beklenen {op} {expected:g}, bulunan {actual}")

    problems: list[str] = []
    for item in invariants["missing"]:
        problems.append(f"eksik {item['category']}: {' | '.join(item['alternatives'])}")
    for item in comparison["introduced_hard"]:
        problems.append(f"yeni sert kalıp: {item['label']} «{item['example']}»")
    problems.extend(failed_expectations)
    warnings = [f"yeni bağlamsal kalıp: {item['label']} «{item['example']}»" for item in comparison["introduced_context"]]
    warnings.extend(comparison["introduced_structure"])
    warnings.extend(f"yeni çeviri kokusu bulgusu: {text}" for text in comparison["introduced_translationese"])
    warnings.extend(f"yeni söylem bulgusu: {text}" for text in comparison["introduced_discourse"])

    return {
        "case": case_path.stem,
        "passed": not problems,
        "problems": problems,
        "warnings": warnings,
        "expectations": len(expectations),
        "invariants": invariants["checked"],
    }


def export_judge_prompts(target: Path) -> int:
    target.mkdir(parents=True, exist_ok=True)
    criteria = section((EVALS / "README.md").read_text(encoding="utf-8"), "Hakem ölçütleri")
    count = 0
    for case_path in sorted(EVALS.glob("*.md")):
        if case_path.name == "README.md":
            continue
        case_text = case_path.read_text(encoding="utf-8")
        output_path = OUTPUTS / f"{case_path.stem}.txt"
        output = output_path.read_text(encoding="utf-8") if output_path.exists() else "[buraya değerlendirilecek çıktıyı yapıştırın]"
        prompt = (
            "Sen bir Türkçe editörlük hakemisin. Aşağıdaki kaynak ve talep için üretilen çıktıyı, "
            "yalnızca verilen ölçütlere göre değerlendir. Tek bir doğru yeniden yazım yoktur; "
            "davranışı puanla. Her ihlali kaynaktan ve çıktıdan alıntıyla göster.\n\n"
            f"## Kaynak\n\n{section(case_text, 'Kaynak')}\n\n"
            f"## Talep\n\n{section(case_text, 'Talep')}\n\n"
            f"## Çıktı\n\n{output.strip()}\n\n"
            f"## Korunması gerekenler\n\n{section(case_text, 'Korunması gerekenler')}\n\n"
            f"## Kaçınılması gerekenler\n\n{section(case_text, 'Kaçınılması gerekenler')}\n\n"
            f"## Genel hakem ölçütleri\n\n{criteria}\n\n"
            "## İstenen cevap biçimi\n\n"
            "1. Korunması gerekenler: her madde için KORUNDU / İHLAL + kanıt\n"
            "2. Kaçınılması gerekenler: her madde için UYULDU / İHLAL + kanıt\n"
            "3. Genel ölçütler: her madde için kısa değerlendirme\n"
            "4. Sonuç: GEÇTİ / BAŞARISIZ ve tek cümlelik gerekçe\n"
        )
        (target / f"{case_path.stem}.md").write_text(prompt, encoding="utf-8", newline="\n")
        count += 1
    return count


def main() -> int:
    configure_stdio()
    parser = argparse.ArgumentParser(description="Kayıtlı eval çıktıları üzerinde deterministik regresyon denetimi.")
    parser.add_argument("--json", action="store_true", help="Raporu JSON olarak yazdır")
    parser.add_argument("--export-judge-prompts", type=Path, metavar="DIR",
                        help="Her vaka için model hakem istemini DIR altına yaz")
    parser.add_argument("--require-all", action="store_true", help="Kayıtlı çıktısı olmayan vaka varsa başarısız çık")
    args = parser.parse_args()

    if args.export_judge_prompts is not None:
        count = export_judge_prompts(args.export_judge_prompts)
        print(f"{count} hakem istemi yazıldı: {args.export_judge_prompts}")
        return 0

    results: list[dict[str, object]] = []
    missing: list[str] = []
    for case_path in sorted(EVALS.glob("*.md")):
        if case_path.name == "README.md":
            continue
        output_path = OUTPUTS / f"{case_path.stem}.txt"
        if not output_path.exists():
            missing.append(case_path.stem)
            continue
        results.append(evaluate_case(case_path, output_path))

    for output_path in sorted(OUTPUTS.glob("*.txt")):
        if not (EVALS / f"{output_path.stem}.md").exists():
            results.append({"case": output_path.stem, "passed": False,
                            "problems": ["kayıtlı çıktının eval vakası yok"], "warnings": [],
                            "expectations": 0, "invariants": 0})

    failed = [r for r in results if not r["passed"]]
    if args.json:
        print(json.dumps({"results": results, "missing": missing}, ensure_ascii=False, indent=2))
    else:
        for r in results:
            state = "GEÇTİ" if r["passed"] else "BAŞARISIZ"
            print(f"{state}: {r['case']} (değişmez {r['invariants']}, beklenti {r['expectations']})")
            for problem in r["problems"]:  # type: ignore[union-attr]
                print(f"  - {problem}")
            for warning in r["warnings"]:  # type: ignore[union-attr]
                print(f"  ~ uyarı: {warning}")
        print(f"\n{len(results) - len(failed)}/{len(results)} kayıtlı vaka geçti; "
              f"{len(missing)} vakanın kayıtlı çıktısı yok"
              + (f" ({', '.join(missing)})" if missing else "") + ".")
        print("Not: Bu denetim değişmezleri, sert kalıp eklenmesini ve yapısal beklentileri ölçer; "
              "akıcılık, ton ve anlam için insan veya model hakemi gerekir.")

    if failed or (args.require_all and missing):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
