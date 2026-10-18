#!/usr/bin/env python3
"""Score blind A/B outputs for the repo's own eval cases with eval-suite checks.

Model samples receive only each case's ``## Kaynak`` and ``## Talep`` (the
expectations stay hidden) and write one file with ``=== <vaka> ===`` blocks.
The file name ends in the arm letter and a sample number (``vk_R3.md``). Each
block is checked exactly like a recorded gold output: invariants, added
epistemic markers, introduced hard patterns and structural expectations.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


suite = load("eval_suite", "eval-suite.py")
ab = load("ab_score", "ab-score.py")


def blocks(path: Path) -> dict[str, str]:
    parts = re.split(r"(?m)^=== ([\w-]+) ===\s*$", path.read_text(encoding="utf-8"))
    return {parts[i]: parts[i + 1].strip() + "\n" for i in range(1, len(parts) - 1, 2)}


def main() -> int:
    suite.configure_stdio()
    parser = argparse.ArgumentParser(description="Kör A/B vaka çıktılarını eval-suite denetimiyle puanlar.")
    parser.add_argument("outputs", type=Path)
    parser.add_argument("--glob", default="vk_*.md")
    parser.add_argument("--compare", nargs=2, metavar=("ESKI", "YENI"), action="append", default=[])
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()

    arms: dict[str, dict[str, list[bool]]] = {}
    with tempfile.TemporaryDirectory() as tmp:
        for path in sorted(args.outputs.glob(args.glob)):
            arm_match = re.search(r"([A-Z])\d+$", path.stem)
            if not arm_match:
                continue
            arm = arms.setdefault(arm_match.group(1), {})
            for case, text in blocks(path).items():
                case_path = ROOT / "evals" / f"{case}.md"
                if not case_path.exists():
                    continue
                out = Path(tmp) / f"{path.stem}-{case}.txt"
                out.write_text(text, encoding="utf-8")
                result = suite.evaluate_case(case_path, out)
                arm.setdefault(case, []).append(bool(result["passed"]))
                if args.detail and not result["passed"]:
                    print(f"{path.stem} {case}: {result['problems']}")

    cases = sorted({case for arm in arms.values() for case in arm})
    print("Vaka | " + " | ".join(sorted(arms)))
    for case in cases:
        cells = []
        for name in sorted(arms):
            runs = arms[name].get(case, [])
            cells.append(f"{sum(runs)}/{len(runs)}")
        print(f"{case} | " + " | ".join(cells))
    totals = {name: (sum(sum(r) for r in arm.values()), sum(len(r) for r in arm.values())) for name, arm in arms.items()}
    print("toplam geçen | " + " | ".join(f"{totals[n][0]}/{totals[n][1]}" for n in sorted(arms)))
    for old, new in args.compare:
        old_fail = totals[old][1] - totals[old][0]
        new_fail = totals[new][1] - totals[new][0]
        p = ab.fisher_one_sided(old_fail, totals[old][1], new_fail, totals[new][1])
        print(f"Başarısız vaka çıktısı: {old} {old_fail}/{totals[old][1]}, {new} {new_fail}/{totals[new][1]}; tek yönlü Fisher p = {p:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
