#!/usr/bin/env python3
"""Score blind A/B skill outputs with the repo's deterministic checks.

Each skill version is given, with nothing else, to independent model samples
together with ``scripts/ab-gorevler.md``. Every sample writes one file with
``=== T1 ===`` ... ``=== T5 ===`` blocks; the file name ends in the arm letter
and a sample number (``hk_D3.md`` is arm D, sample 3). The script reports, per
arm, what the eval suite cannot see without fresh model output: epistemic
markers the output added, lost invariants, sentence-final tails, conversation
leakage, list conversion and the known misreadings.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


lint = load("style_lint", "style-lint.py")
runner = load("eval_runner", "eval-runner.py")

POSITIVE = re.compile(r"fırsat|potansiyel|altını çiz|değerli|önemli ölçüde")


def task_sources(tasks_text: str) -> dict[str, str]:
    sources: dict[str, str] = {}
    for match in re.finditer(r"(?ms)^## (T\d)\s*$(.*?)(?=^## T\d|\Z)", tasks_text):
        for key in ("Metin:", "Notlar:", "İstek:"):
            if key in match.group(2):
                sources[match.group(1)] = match.group(2).split(key, 1)[1]
                break
    return sources


def parse_output(path: Path) -> dict[str, str]:
    parts = re.split(r"(?m)^=== (T\d) ===\s*$", path.read_text(encoding="utf-8"))
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def misreadings(task: str, body: str, full: str) -> list[str]:
    """Misreadings seen in the 2026-10 A/B rounds; content checks read the body,
    the note check reads what follows the `---` separator."""
    found = []
    note = re.split(r"(?m)^---\s*$", full)
    if len(note) > 1 and re.search(r"çıkarıldı|silindi|kaldırıldı|korundu|eklenmedi", note[1]):
        found.append("degisiklik_notu")
    if task == "T1":
        if re.search(r"değerlendiril(?:e)?m(?:iyor|ez|emiyor)|ölçülemiyor|bilinmiyor|yorumlanamıyor"
                     r"|yayın\w* (?:bekleniyor|olacak|girecek)|24 ekim", body):
            found.append("cikarim_dolgusu")
        if re.search(r"düşünülüyor|düşünülmektedir|tahmin ediliyor|değerlendiriliyor|öngörülüyor"
                     # "görüşüm var", "kanaatim var" birinci şahıstır, kişiyi korur.
                     r"|\b(?:tahmin|kanaat|görüş|varsayım)(?![ıiuü]m\b)\w* (?:var|bulunuyor)", body):
            found.append("kisi_kaymasi")
    if task == "T3":
        if "fırsat" in body:
            found.append("olumluya_cekme")
        if re.search(r"güvenilirli\w*.{0,40}düşündür|düşündür\w*.{0,40}güvenilirli", body):
            found.append("yumusatilmis_iddia")
        if re.search(r"(?m)^sonuç olarak|\. sonuç olarak", body):
            found.append("kalip_kapanis")
    return found


def score(task: str, output: str, source: str) -> dict[str, object]:
    body = re.split(r"(?m)^---\s*$", output)[0].strip()
    report = lint.analyse(body)
    evaluation = runner.evaluate(f"## Kaynak\n\n{source}\n\n## Talep\n\nx\n", body)
    return {
        "kuyruk": report["kuyruk"],
        "sizinti": report["sizinti"],
        "sert": report["hard_hits"],
        "liste": report["structure_summary"]["list_items"],
        "eklenen": sum(int(item["count"]) for item in evaluation["added"]),
        "eklenen_ornek": [e for item in evaluation["added"] for e in item["examples"]],
        "kayip": [item["value"] for item in evaluation["missing"]],
        "olumluya_cekme": len(POSITIVE.findall(lint.tr_lower(body))),
        "yanilgi": misreadings(task, lint.tr_lower(body), lint.tr_lower(output)),
    }


def fisher_one_sided(err_a: int, n_a: int, err_b: int, n_b: int) -> float:
    """P(arm A has at least err_a erroneous outputs) under the hypergeometric null
    that errors are spread over both arms at random (one-sided Fisher exact test)."""
    from math import comb
    total_err, total = err_a + err_b, n_a + n_b
    denominator = comb(total, n_a)
    return sum(comb(total_err, k) * comb(total - total_err, n_a - k)
               for k in range(err_a, min(total_err, n_a) + 1)) / denominator


def main() -> int:
    lint.configure_stdio()
    parser = argparse.ArgumentParser(description="Kör A/B skill çıktılarını deterministik denetimle puanlar.")
    parser.add_argument("outputs", type=Path, help="Örnek çıktılarının klasörü")
    parser.add_argument("--tasks", type=Path, default=ROOT / "scripts" / "ab-gorevler.md")
    parser.add_argument("--glob", default="*.md", help="Çıktı dosyası deseni (son harf + sayı kolu ve örneği verir)")
    parser.add_argument("--detail", action="store_true", help="Her görevin ölçümünü de yazdır")
    parser.add_argument("--compare", nargs=2, metavar=("ESKI", "YENI"),
                        help="İki kolun hatalı görev çıktısı oranını tek yönlü Fisher kesin testiyle karşılaştır")
    args = parser.parse_args()

    sources = task_sources(args.tasks.read_text(encoding="utf-8"))
    arms: dict[str, dict[str, float]] = {}
    for path in sorted(args.outputs.glob(args.glob)):
        arm_match = re.search(r"([A-Z])\d+$", path.stem)
        if not arm_match:
            continue
        arm = arms.setdefault(arm_match.group(1), {"örnek": 0})
        arm["örnek"] += 1
        for task, output in parse_output(path).items():
            if task not in sources:
                continue
            result = score(task, output, sources[task])
            if args.detail:
                print(f"{path.stem} {task}: {result}")
            for key in ("kuyruk", "sizinti", "sert", "liste", "eklenen", "olumluya_cekme"):
                arm[key] = arm.get(key, 0) + int(result[key])  # type: ignore[arg-type]
            arm["kayip"] = arm.get("kayip", 0) + len(result["kayip"])  # type: ignore[arg-type]
            arm["yanilgi"] = arm.get("yanilgi", 0) + len(result["yanilgi"])  # type: ignore[arg-type]
            faulty = bool(result["eklenen"] or result["kayip"] or result["yanilgi"] or result["kuyruk"] or result["sizinti"])
            arm["cikti"] = arm.get("cikti", 0) + 1
            arm["hatali"] = arm.get("hatali", 0) + int(faulty)

    print("Kol | örnek | eklenen/örnek | kayıp/örnek | yanılgı/örnek | olumluya çekme | liste | kuyruk | sızıntı | sert")
    for name, arm in sorted(arms.items()):
        n = arm["örnek"] or 1
        print(f"{name} | {arm['örnek']} | {arm.get('eklenen', 0) / n:.2f} | {arm.get('kayip', 0) / n:.2f} | "
              f"{arm.get('yanilgi', 0) / n:.2f} | {arm.get('olumluya_cekme', 0)} | {arm.get('liste', 0)} | "
              f"{arm.get('kuyruk', 0)} | {arm.get('sizinti', 0)} | {arm.get('sert', 0)}")
    if args.compare:
        old, new = (arms[name] for name in args.compare)
        p = fisher_one_sided(int(old.get("hatali", 0)), int(old["cikti"]), int(new.get("hatali", 0)), int(new["cikti"]))
        print(f"\nHatalı görev çıktısı: {args.compare[0]} {old.get('hatali', 0)}/{old['cikti']}, "
              f"{args.compare[1]} {new.get('hatali', 0)}/{new['cikti']}; tek yönlü Fisher p = {p:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
