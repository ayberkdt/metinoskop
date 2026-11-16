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


def tokens(path: Path):
    """(sent_id, text, rows) for each sentence; rows are the ten CoNLL-U columns of word lines."""
    sent_id, text, rows = "", "", []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip("\n")
            if match := SENT_ID_RE.match(line):
                sent_id = match.group(1).strip()
            elif match := TEXT_RE.match(line):
                text = match.group(1).strip()
            elif not line:
                if rows:
                    yield sent_id, text, rows
                sent_id, text, rows = "", "", []
            elif not line.startswith("#"):
                cols = line.split("\t")
                if len(cols) == 10 and cols[0].isdigit():
                    rows.append(cols)
    if rows:
        yield sent_id, text, rows


def feats(row: list[str]) -> dict[str, str]:
    return dict(item.split("=", 1) for item in row[5].split("|") if "=" in item)


def gold_tense(row: list[str]) -> str:
    """Kaba zaman sınıfı, yalnızca UD biçim özelliklerinden."""
    f = feats(row)
    if f.get("Evident") == "Nfh":
        return "dolaylı geçmiş"
    # BOUN `-yor`'u çoğunlukla Aspect=Imp|Tense=Pres, bazen Aspect=Prog ile işaretler.
    if f.get("Aspect") == "Prog" or (f.get("Aspect") == "Imp" and f.get("Tense") == "Pres"):
        return "sürerlik"
    if f.get("Tense") == "Fut":
        return "gelecek"
    if f.get("Tense") == "Past":
        return "yalın geçmiş"
    if f.get("Aspect") == "Hab" and f.get("Tense") == "Pres":
        return "geniş zaman"
    return "diğer"


LINT_TO_GOLD = {"dı": "yalın geçmiş", "miştir": "dolaylı geçmiş", "mıştı": "dolaylı geçmiş", "yor": "sürerlik",
                "yordu": "sürerlik", "mektedir": "sürerlik", "r": "geniş zaman", None: "sınıflanmadı"}


def morphology_check(paths: list[Path]) -> None:
    """`style-lint.py` tense_class ve `eval-runner.py` kanıtsallık örüntüsünü UD işaretlemesine karşı ölçer."""
    lint = load_lint()
    spec = importlib.util.spec_from_file_location("eval_runner", ROOT / "scripts/eval-runner.py")
    runner = importlib.util.module_from_spec(spec)
    sys.modules["eval_runner"] = runner
    spec.loader.exec_module(runner)  # type: ignore[union-attr]
    confusion: Counter[tuple[str, str]] = Counter()
    ev_hit = Counter()
    for path in paths:
        for _sid, text, rows in tokens(path):
            words = [r for r in rows if r[3] != "PUNCT"]
            if words and words[-1][7] == "root" and words[-1][3] == "VERB" and "VerbForm" not in feats(words[-1]):
                doc = lint.parse(text)
                sentence = doc.paragraphs[-1].sentences[-1] if doc.paragraphs and doc.paragraphs[-1].sentences else None
                predicted = lint.tense_class(sentence) if sentence else None
                confusion[(gold_tense(words[-1]), LINT_TO_GOLD[predicted])] += 1
            # Kanıtsallık örüntüsü: noktalama önündeki çekimli -mIş.
            folded = runner.tr_fold(text)
            forms = {runner.tr_fold(r[1]): r for r in rows}
            for match in runner.EVIDENTIAL_MIS_RE.finditer(folded):
                row = forms.get(match.group(0))
                if row is None:
                    ev_hit["eşlenemedi"] += 1
                elif row[3] in ("VERB", "AUX") and feats(row).get("Evident") == "Nfh" and "VerbForm" not in feats(row):
                    ev_hit["çekimli dolaylı fiil"] += 1
                else:
                    ev_hit[f"başka: {row[3]} {feats(row).get('VerbForm', '')}".strip()] += 1
            for row in rows:
                f = feats(row)
                form = runner.tr_fold(row[1])
                if (row[3] == "VERB" and f.get("Evident") == "Nfh" and "VerbForm" not in f
                        and re.search(r"m[ıiuü]ş(?:l[ae]r)?$", form)):
                    ev_hit["tüm çekimli yalın -mIş"] += 1
    golds = sorted({g for g, _ in confusion})
    preds = sorted({p for _, p in confusion})
    print("Zaman sınıfı (satır: UD işaretlemesi, sütun: tense_class), yalnız cümle sonundaki çekimli fiil kökü:")
    print("UD \\ lint | " + " | ".join(preds))
    for gold in golds:
        print(f"{gold} | " + " | ".join(str(confusion[(gold, p)]) for p in preds))
    for label in preds:
        if label == "sınıflanmadı":
            continue
        tp = confusion[(label, label)]
        predicted = sum(confusion[(g, label)] for g in golds)
        actual = sum(confusion[(label, p)] for p in preds)
        print(f"{label}: kesinlik {tp}/{predicted} = {tp / max(1, predicted):.3f}, duyarlılık {tp}/{actual} = {tp / max(1, actual):.3f}")
    print("Kanıtsallık örüntüsü (EVIDENTIAL_MIS_RE) isabetleri:", dict(ev_hit))


# Yüzey biçimleri ham metinden sayılır: ağaç bankaları belirteçlemede ve biçim özelliği işaretlemesinde
# ayrışır (PUD'da ortaç ve zarf-fiil özelliği neredeyse yoktur), bu yüzden özellik sayımı kümeler arasında
# karşılaştırılmaz.
SURFACE_WORDS = {
    "olan": r"olan", "olarak": r"olarak", "ki (ayrı sözcük)": r"ki", "ve": r"ve", "açısından": r"açısından",
    "-mAktAdIr": r"\w+m[ae]kt[ae]d[ıi]r(?:l[ae]r)?", "-mAktA (tümü)": r"\w+m[ae]kt[ae]\w*",
    "gerçekleştir-": r"gerçekleştir\w*", "sağla-": r"sağla\w*",
    "ile ilgili": r"ile ilgili", "söz konusu": r"söz konusu", "yer al-": r"yer al\w*", "neden ol-": r"neden ol\w*",
}
SENTENCE_OPENERS = ("ancak", "fakat", "ama", "ayrıca", "bununla birlikte", "öte yandan", "buna ek olarak",
                    "bu nedenle", "bu yüzden", "dolayısıyla", "sonuç olarak", "bu bağlamda", "üstelik")


def surface_profile(paths: list[Path], by_genre: bool) -> None:
    """Çeviri kokusu sayılan yüzey biçimlerini ve cümle başı bağlayıcılarını kümelere göre sayar."""
    stats: dict[str, Counter] = defaultdict(Counter)
    word_res = {k: re.compile(rf"(?<!\w){v}(?!\w)") for k, v in SURFACE_WORDS.items()}
    for path in paths:
        for sent_id, text in sentences(path):
            group = group_name(path, sent_id, by_genre)
            low = text.replace("I", "ı").replace("İ", "i").lower()
            entry = stats[group]
            entry["cümle"] += 1
            entry["sözcük"] += len(WORD_RE.findall(low))
            for key, pattern in word_res.items():
                entry[key] += len(pattern.findall(low))
            opener = low.lstrip("-–—\"' ")
            for word in SENTENCE_OPENERS:
                if re.match(rf"{word}(?!\w)", opener):
                    entry[f"cümle başı: {word}"] += 1
    groups = sorted(stats)
    print("Yüzey biçimi | " + " | ".join(groups))
    print("cümle | " + " | ".join(str(stats[g]["cümle"]) for g in groups))
    print("sözcük | " + " | ".join(str(stats[g]["sözcük"]) for g in groups))
    for key in SURFACE_WORDS:
        print(f"{key} (10.000 sözcükte) | " + " | ".join(f"{1e4 * stats[g][key] / max(1, stats[g]['sözcük']):.1f}" for g in groups))
    for word in SENTENCE_OPENERS:
        key = f"cümle başı: {word}"
        print(f"{key} (1.000 cümlede) | " + " | ".join(f"{1e3 * stats[g][key] / max(1, stats[g]['cümle']):.1f}" for g in groups))


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
    parser.add_argument("--morph", action="store_true",
                        help="tense_class ve kanıtsallık örüntüsünü UD biçim işaretlemesine karşı ölç")
    parser.add_argument("--surface", action="store_true",
                        help="çeviri kokusu sayılan yüzey biçimlerini ve cümle başı bağlayıcıları say")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.surface:
        surface_profile(args.files, args.by_genre)
        return 0
    if args.morph:
        morphology_check(args.files)
        return 0
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
