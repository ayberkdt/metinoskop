#!/usr/bin/env python3
"""Measure eval sources and gold outputs on the AI-vs-human differences in
``references/insan-ve-yapay-metin.md``.

For every case the script counts, in the source and in the gold output, the
features the research ties to LLM text: sentence-final converb tails, style
verbs and adjectives, nominalization density, hard filler families, formulaic
``Sonuç olarak`` openers, positive spin, list conversion and the share of
sentences in the 10-30 token band (Turkish: 7-20 words). It prints corpus
totals for transformation cases and lists gold outputs that still carry a
feature the edit did not remove, so they can be revised.
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
validator_text = (ROOT / "scripts" / "validate-package.py").read_text(encoding="utf-8")
SHOULD_REMAIN = set(re.findall(r'"evals/([^"]+)\.md"', validator_text[validator_text.find("SHOULD_REMAIN_CASES"):validator_text.find("locked = []")]))

STYLE_WORDS = re.compile(
    r"\baltını çiz\w*|\bvurgula\w*|\bgözler önüne ser\w*|\bderinlemesine\b|\bkapsamlı\b|\bçok yönlü\b"
    r"|\bkayda değer\b|\bdinamik\b|\bzengin\b|\bkritik\b|\beşsiz\b|\bsağlam bir\b|\bpotansiyel\w*")
SPIN = re.compile(r"\bfırsat\w*|\bgelişime açık\b|\bpotansiyel\w*")
OPENER = re.compile(r"(?m)(?:^|[.!?]\s+)(?:sonuç olarak|özetle|kısacası)\b")


def source_of(case: str) -> str:
    match = re.search(r"(?ms)^## Kaynak\s*\n(.*?)(?=^## (?:Talep|Korunması gerekenler)\s*$)", case)
    return match.group(1) if match else ""


def profile(text: str) -> dict[str, float]:
    report = lint.analyse(text)
    low = lint.tr_lower(text)
    words = re.findall(r"\w+", low)
    lengths = [len(re.findall(r"\w+", s.text)) for p in lint.parse(text).paragraphs for s in p.sentences]
    return {
        "kuyruk": report["kuyruk"],
        "bicem": len(STYLE_WORDS.findall(low)),
        "adlastirma": sum(1 for w in words if lint.NOMINALIZATION_RE.match(w)),
        "sert": report["hard_hits"],
        "kalip_acilis": len(OPENER.findall(low)),
        "olumluya": len(SPIN.findall(low)),
        "liste": report["structure_summary"]["list_items"],
        "sozcuk": len(words),
        "cumle": len(lengths),
        "bant": sum(1 for n in lengths if 7 <= n <= 20),
    }


def main() -> int:
    lint.configure_stdio()
    parser = argparse.ArgumentParser(description="Eval kaynaklarını ve gold çıktılarını AI–insan metni farklarıyla ölçer.")
    parser.add_argument("--list", action="store_true", help="İz taşıyan gold çıktılarını listele")
    args = parser.parse_args()

    totals = {"kaynak": {}, "gold": {}}
    residual = []
    cases = 0
    for case_path in sorted((ROOT / "evals").glob("*.md")):
        if case_path.name == "README.md" or case_path.stem in SHOULD_REMAIN:
            continue
        output_path = ROOT / "evals" / "outputs" / f"{case_path.stem}.txt"
        source = profile(source_of(case_path.read_text(encoding="utf-8")))
        gold = profile(output_path.read_text(encoding="utf-8"))
        cases += 1
        for side, values in (("kaynak", source), ("gold", gold)):
            for key, value in values.items():
                totals[side][key] = totals[side].get(key, 0) + value
        kept = [key for key in ("kuyruk", "bicem", "sert", "kalip_acilis", "olumluya") if gold[key] and gold[key] >= source[key]]
        if kept:
            residual.append((case_path.stem, {k: (source[k], gold[k]) for k in kept}))

    print(f"Dönüşüm vakası: {cases} (korunur vakalar hariç)")
    print("Ölçü | kaynak | gold")
    for key, label in (("kuyruk", "cümle sonu kuyruğu"), ("bicem", "biçem fiili/sıfatı"), ("sert", "sert dolgu kalıbı"),
                       ("kalip_acilis", "kalıp açılış (Sonuç olarak …)"), ("olumluya", "olumluya çekme"), ("liste", "liste ögesi")):
        print(f"{label} | {totals['kaynak'][key]} | {totals['gold'][key]}")
    for side in ("kaynak", "gold"):
        t = totals[side]
        totals[side]["adl100"] = 100 * t["adlastirma"] / max(1, t["sozcuk"])
        totals[side]["bant%"] = 100 * t["bant"] / max(1, t["cumle"])
    print(f"adlaştırma / 100 sözcük | {totals['kaynak']['adl100']:.2f} | {totals['gold']['adl100']:.2f}")
    print(f"7–20 sözcük bandındaki cümle oranı | %{totals['kaynak']['bant%']:.0f} | %{totals['gold']['bant%']:.0f}")
    print(f"toplam sözcük | {totals['kaynak']['sozcuk']} | {totals['gold']['sozcuk']}")
    print(f"İz taşımaya devam eden gold: {len(residual)}")
    if args.list:
        for name, kept in residual:
            print(f"  {name}: {kept}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
