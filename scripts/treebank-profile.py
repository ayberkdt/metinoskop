#!/usr/bin/env python3
"""Measure style-lint families on Universal Dependencies Turkish treebanks.

The treebanks are not part of this repository (BOUN, Penn and PUD are CC BY-SA 4.0, IMST
CC BY-NC-SA 3.0); download the CoNLL-U files yourself and pass their paths:

    B=https://raw.githubusercontent.com/UniversalDependencies
    curl -sSO $B/UD_Turkish-BOUN/master/tr_boun-ud-test.conllu
    curl -sSO $B/UD_Turkish-Penn/master/tr_penn-ud-test.conllu
    python scripts/treebank-profile.py tr_boun-ud-test.conllu tr_penn-ud-test.conllu
    python scripts/treebank-profile.py --by-genre tr_boun-ud-*.conllu      # BOUN sent_id öneki: tür
    python scripts/treebank-profile.py --examples yazim tr_boun-ud-*.conllu  # elle inceleme için

Each sentence is analysed on its own, so only sentence-level families are meaningful; paragraph
and document measures (döngüsel tekrar, kip nöbetleşmesi, bölüm yapısı) are not reported.
A hit on edited, published Turkish is a candidate false positive, not a verdict: read the examples.
Original (BOUN, IMST) and translated (Penn, PUD) treebanks differ in genre and sentence length
too, so a rate gap is not by itself a translation effect.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_RE = re.compile(r"^# text = (.*)$")
SENT_ID_RE = re.compile(r"^# sent_id = (.*)$")
WORD_RE = re.compile(r"\w+")


def load_lint():
    spec = importlib.util.spec_from_file_location("style_lint", ROOT / "scripts/style-lint.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["style_lint"] = module
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


def sentences(path: Path) -> list[tuple[str, str]]:
    """(sent_id, text) pairs from a CoNLL-U file."""
    found: list[tuple[str, str]] = []
    sent_id = ""
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if match := SENT_ID_RE.match(line):
                sent_id = match.group(1).strip()
            elif match := TEXT_RE.match(line):
                found.append((sent_id, match.group(1).strip()))
    return found


def group_name(path: Path, sent_id: str, by_genre: bool) -> str:
    corpus = path.name.split("-ud-")[0]
    if by_genre and "_" in sent_id and sent_id.split("_")[0].isalpha():
        return f"{corpus}:{sent_id.split('_')[0]}"
    return corpus


def profile(paths: list[Path], by_genre: bool, examples: str | None, limit: int, max_words: int = 0):
    lint = load_lint()
    stats: dict[str, dict[str, object]] = defaultdict(lambda: {"cumle": 0, "sozcuk": 0, "aile": Counter(), "bir": 0})
    shown: list[str] = []
    for path in paths:
        for sent_id, text in sentences(path):
            words = WORD_RE.findall(text)
            if max_words and len(words) > max_words:
                continue
            group = group_name(path, sent_id, by_genre)
            entry = stats[group]
            entry["cumle"] += 1  # type: ignore[operator]
            entry["sozcuk"] += len(words)  # type: ignore[operator]
            entry["bir"] += sum(1 for w in words if w.casefold() == "bir")  # type: ignore[operator]
            # Derlem Markdown değildir: satır başındaki `- ` diyalog çizgisidir, liste değil.
            report = lint.analyse("– " + text[2:] if text.startswith("- ") else text)
            for hit in report["hits"]:
                entry["aile"][hit["category"]] += 1  # type: ignore[index]
                if examples and hit["category"] == examples and len(shown) < limit:
                    shown.append(f"{group} {sent_id}: «{hit.get('match', '')}» {text}")
    return lint, stats, shown


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="+", type=Path, help="CoNLL-U dosyaları")
    parser.add_argument("--by-genre", action="store_true", help="BOUN sent_id önekine göre türlere ayır")
    parser.add_argument("--examples", metavar="AILE", help="bu ailenin isabet ettiği cümleleri yazdır")
    parser.add_argument("--limit", type=int, default=40, help="yazdırılacak örnek sayısı")
    parser.add_argument("--max-words", type=int, default=0,
                        help="yalnızca en çok N sözcüklü cümleler (Penn ≤15 belirteçle kuruldu; uzunluğu eşlemek için)")
    parser.add_argument("--per-words", action="store_true", help="oranı bin cümle yerine on bin sözcükte ver")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    lint, stats, shown = profile(args.files, args.by_genre, args.examples, args.limit, args.max_words)
    families = sorted({f for entry in stats.values() for f in entry["aile"]},  # type: ignore[union-attr]
                      key=lambda f: (lint.LEVELS.get(f) != "sert", f))
    if args.json:
        print(json.dumps({g: {"cumle": e["cumle"], "sozcuk": e["sozcuk"], "bir": e["bir"], "aile": dict(e["aile"])}
                          for g, e in stats.items()}, ensure_ascii=False, indent=2))
        return 0
    groups = sorted(stats)
    unit, base = ("on bin sözcükte", "sozcuk") if args.per_words else ("bin cümlede", "cumle")
    scale = 10000 if args.per_words else 1000
    print(f"{unit.capitalize()} isabet (sert aileler önce). Tek cümle tek metin olarak denetlendi.")
    print("aile | düzey | " + " | ".join(groups))
    print("cümle | | " + " | ".join(str(stats[g]["cumle"]) for g in groups))
    print("sözcük/cümle | | " + " | ".join(f"{stats[g]['sozcuk'] / max(1, stats[g]['cumle']):.1f}" for g in groups))  # type: ignore[operator]
    print("bir/100 sözcük | | " + " | ".join(f"{100 * stats[g]['bir'] / max(1, stats[g]['sozcuk']):.2f}" for g in groups))  # type: ignore[operator]
    for family in families:
        cells = [f"{scale * stats[g]['aile'][family] / max(1, stats[g][base]):.1f}" for g in groups]  # type: ignore[index,operator]
        print(f"{family} | {lint.LEVELS.get(family, '?')} | " + " | ".join(cells))
    for line in shown:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
