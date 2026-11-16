#!/usr/bin/env python3
"""Query the Turkish grammar and usage literature database (references/turkce-dil-literaturu.csv).

Usage:
    python scripts/literatur.py                      # özet: kayıt, konu ve tür sayıları
    python scripts/literatur.py --konu tamlama       # konuya göre süz
    python scripts/literatur.py --kural yazim-ve-dil-bilgisi.md
    python scripts/literatur.py --ara "odak"         # başlıkta ya da bulguda geçen sözcük
    python scripts/literatur.py --id enc-1986 --tam  # tek kaydın bütün alanları
    python scripts/literatur.py --check              # şema denetimi (doğrulayıcı da çağırır)
    python scripts/literatur.py --bib > kaynaklar.bib  # BibTeX (süzgeçlerle birlikte de çalışır)

The database is a source register, not a rulebook: a finding becomes a Metinoskop rule only
after it is written into a reference file with its source and tested with an eval case.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATABASE = ROOT / "references/turkce-dil-literaturu.csv"
COLUMNS = ("id", "yazarlar", "yil", "baslik", "yayin", "tur", "konular", "bulgu", "metinoskop", "dogrulama", "url")
TYPES = frozenset({"dil-bilgisi-kitabi", "kitap", "kitap-bolumu", "makale", "bildiri", "tez", "derlem",
                   "agac-bankasi", "sozluk", "on-baski", "veri-kumesi", "kilavuz", "mevzuat"})
VERIFICATION = frozenset({"künye+içerik", "künye"})
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
YEAR_RE = re.compile(r"^(?:1[89]\d\d|20\d\d)(?:[/-]\d{2,4})?$")


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="backslashreplace")


def load(path: Path = DATABASE) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != COLUMNS:
            raise SystemExit(f"{path.name}: başlık satırı {COLUMNS} olmalı, bulunan {reader.fieldnames}")
        return [dict(row) for row in reader]


def problems(rows: list[dict[str, str]]) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for number, row in enumerate(rows, start=2):
        rid = row["id"]
        where = f"satır {number} ({rid or '?'})"
        for column in COLUMNS:
            if not (row.get(column) or "").strip():
                found.append(f"{where}: boş alan {column}")
        if rid in seen:
            found.append(f"{where}: yinelenen id")
        seen.add(rid)
        if rid and not ID_RE.match(rid):
            found.append(f"{where}: id küçük harf ASCII ve tire olmalı")
        if row["yil"] and not YEAR_RE.match(row["yil"]):
            found.append(f"{where}: yıl biçimi {row['yil']!r}")
        if row["tur"] and row["tur"] not in TYPES:
            found.append(f"{where}: bilinmeyen tür {row['tur']!r}")
        if row["dogrulama"] and row["dogrulama"].split(":")[0].strip() not in VERIFICATION:
            found.append(f"{where}: doğrulama 'künye+içerik: …' ya da 'künye: …' ile başlamalı")
        if row["url"] and not row["url"].startswith(("https://", "http://")):
            found.append(f"{where}: url http(s) ile başlamalı")
        if row["dogrulama"].startswith("künye:") and row["bulgu"] != "Künye doğrulandı; içerik özetlenmedi.":
            found.append(f"{where}: içeriği doğrulanmamış kayıt bulgu yazamaz")
        for target in (t.strip() for t in row["metinoskop"].split(";")):
            if target and target != "—" and not (ROOT / "references" / target).is_file():
                found.append(f"{where}: metinoskop alanı var olmayan dosyayı gösteriyor: {target}")
    return found


BIB_TYPES = {"makale": "article", "bildiri": "inproceedings", "tez": "phdthesis", "kitap-bolumu": "incollection",
             "dil-bilgisi-kitabi": "book", "kitap": "book", "sozluk": "book", "on-baski": "misc", "veri-kumesi": "misc",
             "derlem": "misc", "agac-bankasi": "misc", "kilavuz": "misc", "mevzuat": "misc"}


def bib_escape(value: str) -> str:
    return value.replace("\\", "\\textbackslash{}").replace("{", "\\{").replace("}", "\\}").replace("&", "\\&").replace("%", "\\%")


def to_bibtex(row: dict[str, str]) -> str:
    """Bir kaydı BibTeX girdisine çevir; doğrulama düzeyi ve bulgu `note` alanına yazılır."""
    kind = BIB_TYPES.get(row["tur"], "misc")
    venue_field = {"article": "journal", "inproceedings": "booktitle", "incollection": "booktitle",
                   "phdthesis": "school", "book": "publisher"}.get(kind, "howpublished")
    year = re.match(r"\d{4}", row["yil"])
    fields = [
        ("author", " and ".join(a.strip() for a in row["yazarlar"].split(";"))),
        ("title", "{" + row["baslik"] + "}"),
        (venue_field, row["yayin"]),
        ("year", year.group(0) if year else row["yil"]),
        ("url", row["url"]),
        ("keywords", ", ".join(t.strip() for t in row["konular"].split(";"))),
        ("note", f"Doğrulama: {row['dogrulama']}. {row['bulgu']}"),
    ]
    body = ",\n".join(f"  {name} = {{{value if name in ('title', 'url') else bib_escape(value)}}}" for name, value in fields)
    return f"@{kind}{{{row['id']},\n{body}\n}}\n"


def main() -> int:
    configure_stdio()
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--konu", help="konu etiketi (konular alanında)")
    parser.add_argument("--kural", help="Metinoskop referans dosyası (metinoskop alanında)")
    parser.add_argument("--ara", help="başlıkta, yazarda ya da bulguda geçen metin")
    parser.add_argument("--id", help="tek kayıt")
    parser.add_argument("--tam", action="store_true", help="bütün alanları yazdır")
    parser.add_argument("--check", action="store_true", help="şemayı denetle")
    parser.add_argument("--bib", action="store_true", help="seçilen kayıtları BibTeX olarak yazdır")
    args = parser.parse_args()

    rows = load()
    if args.check:
        found = problems(rows)
        for item in found:
            print(item)
        print(f"{len(rows)} kayıt; {len(found)} sorun.")
        return 1 if found else 0

    selected = rows
    if args.konu:
        selected = [r for r in selected if args.konu in (t.strip() for t in r["konular"].split(";"))]
    if args.kural:
        selected = [r for r in selected if args.kural in r["metinoskop"]]
    if args.ara:
        needle = args.ara.casefold()
        selected = [r for r in selected if needle in (r["baslik"] + r["bulgu"] + r["yazarlar"]).casefold()]
    if args.id:
        selected = [r for r in selected if r["id"] == args.id]

    if args.bib:
        for row in selected:
            print(to_bibtex(row))
        return 0

    if not any((args.konu, args.kural, args.ara, args.id)):
        topics = Counter(t.strip() for r in rows for t in r["konular"].split(";") if t.strip())
        types = Counter(r["tur"] for r in rows)
        levels = Counter(r["dogrulama"].split(":")[0] for r in rows)
        print(f"{len(rows)} kayıt")
        print("Doğrulama: " + ", ".join(f"{k} {v}" for k, v in levels.most_common()))
        print("Tür: " + ", ".join(f"{k} {v}" for k, v in types.most_common()))
        print("Konu: " + ", ".join(f"{k} {v}" for k, v in topics.most_common()))
        return 0

    for row in selected:
        if args.tam:
            for column in COLUMNS:
                print(f"{column}: {row[column]}")
            print()
        else:
            print(f"{row['id']} — {row['yazarlar']} ({row['yil']}). {row['baslik']}.")
            print(f"    {row['bulgu']}")
    print(f"{len(selected)} kayıt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
