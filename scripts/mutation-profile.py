#!/usr/bin/env python3
"""Gold çıktılarına bilinen hatalar ekleyip ``eval-runner.py``'nin yakalama oranını ölçer.

Her geçen gold'a sırayla bir mutasyon uygulanır: kapsam sözcüğünü silmek, ilk sayıyı
silmek, ikinci cümleye pekiştirici, nedensellik bağı ya da çekince eklemek, çekimli
``-mIş``ı ``-DI``ya çevirmek. Çıktı mutasyon türü başına uygulanan ve yakalanan vaka
sayısıdır; kaçan vakalar ``--examples`` ile listelenir.

Bilinen sınırlar: denetim sayının çıktıda en az bir kez geçmesine bakar, iki kez geçen
sayıdan birinin silinmesini yakalamaz. Kaynak aynı aileden işaret taşıyorsa ekleme aile
içi dönüşüm sayılır. ``-mIş,`` ile kurulan ek ortaklığı (``uygulanmış, ... -tır``)
kanıtsal değildir; bu mutasyonun orada kaçması denetim hatası değildir.
"""
from __future__ import annotations

import argparse
import collections
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("eval_runner", ROOT / "scripts/eval-runner.py")
runner = importlib.util.module_from_spec(spec)
sys.modules["eval_runner"] = runner
spec.loader.exec_module(runner)

SCOPE = re.compile(r"\b(yalnızca|sadece|en az|en fazla|bazı|çoğu|henüz|genellikle|yaklaşık|ortalama|hariç|dışında)\s+", re.I)
NUMBER = re.compile(r"(?<![\w.,])\d+(?:[.,]\d+)?\s*")
SECOND = re.compile(r"(\. )([A-ZÇĞİÖŞÜ])")
PAST = re.compile(r"\b(\w+?)(dı|di|du|dü|tı|ti|tu|tü)\.")
EVID = re.compile(r"\b(\w+?)(mış|miş|muş|müş)([.,])")
EVID_MAP = {"mış": "dı", "miş": "di", "muş": "du", "müş": "dü"}


def mutations():
    return {
        "kapsam-sil": lambda t: SCOPE.sub("", t, count=1) if SCOPE.search(t) else None,
        "sayi-sil": lambda t: NUMBER.sub("", t, count=1) if NUMBER.search(t) else None,
        "pekistirici": lambda t: SECOND.sub(r"\1Açıkça \2", t, count=1) if SECOND.search(t) else None,
        "nedensellik": lambda t: SECOND.sub(r"\1Bu nedenle \2", t, count=1) if SECOND.search(t) else None,
        "cekince": lambda t: PAST.sub(r"\1\2 ve bu durum değişebilir.", t, count=1) if PAST.search(t) else None,
        "mis-di": lambda t: EVID.sub(lambda m: m.group(1) + EVID_MAP[m.group(2)] + m.group(3), t, count=1)
        if EVID.search(t) else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--examples", type=int, default=0, help="her tür için listelenecek kaçan vaka sayısı")
    args = parser.parse_args()
    stats = collections.defaultdict(lambda: [0, 0])
    missed = collections.defaultdict(list)
    for path in sorted((ROOT / "evals").glob("*.md")):
        if path.name == "README.md":
            continue
        gold_path = ROOT / "evals/outputs" / f"{path.stem}.txt"
        if not gold_path.exists():
            continue
        case = path.read_text(encoding="utf-8")
        gold = gold_path.read_text(encoding="utf-8")
        if not runner.evaluate(case, gold)["passed"]:
            continue
        for name, mutate in mutations().items():
            mutated = mutate(gold)
            if not mutated or mutated == gold:
                continue
            stats[name][0] += 1
            if runner.evaluate(case, mutated)["passed"]:
                missed[name].append(path.stem)
            else:
                stats[name][1] += 1
    for name, (applied, caught) in stats.items():
        print(f"{name:12} uygulandı {applied:3}  yakalandı {caught:3}  (%{100 * caught / applied:.0f})")
        if args.examples:
            print("   kaçan:", ", ".join(missed[name][: args.examples]) or "—")


if __name__ == "__main__":
    main()
