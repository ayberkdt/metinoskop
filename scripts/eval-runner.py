#!/usr/bin/env python3
"""Run deterministic preservation checks against a Metinoskop eval output."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path


SECTION_PATTERN = r"(?ms)^## {heading}\s*\r?\n(.*?)(?=^## |\Z)"
URL_RE = re.compile(r"https?://[^\s)>\]]+")
INLINE_CODE_RE = re.compile(r"(?<!`)`([^`\r\n]+)`(?!`)")
CODE_BLOCK_RE = re.compile(r"(?ms)^```[^\r\n]*\r?\n.*?^```[ \t]*$")
FOOTNOTE_RE = re.compile(r"\[\^[^\]]+\]")
FOOTNOTE_DEFINITION_RE = re.compile(r"(?m)^\[\^[^\]]+\]:[^\r\n]*$")
EQUATION_NUMBER_RE = re.compile(r"\(\d+\)")
DATE_RE = re.compile(
    r"\b\d{1,2}\s+"
    r"(?:Ocak|Şubat|Mart|Nisan|Mayıs|Haziran|Temmuz|Ağustos|Eylül|Ekim|Kasım|Aralık)"
    r"\s+\d{4}\b",
    re.IGNORECASE,
)
NUMBER_RE = re.compile(
    r"(?<![\w])(?:%\s*)?\d+(?:[.,]\d+)*(?:[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)?(?![\w])"
)
TECH_IDENTIFIER_RE = re.compile(
    r"\b(?=[A-ZÇĞİÖŞÜ0-9_-]*[A-ZÇĞİÖŞÜ])"
    r"(?=[A-ZÇĞİÖŞÜ0-9_-]*\d)[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜ0-9_-]+\b"
)
GREEK_SYMBOL_RE = re.compile(r"[Α-Ωα-ω][A-Za-z0-9_]*")
MEASUREMENT_RE = re.compile(
    r"(?<![\w])\d+(?:[.,]\d+)?\s*(?:km/s|m/s|km|mm|cm|ms|kg|Hz|kHz|MHz|GHz|°C)\b"
)

MARKER_GROUPS = (
    ("kapsam", "yalnızca", ("yalnızca", "sadece")),
    ("kapsam", "en az", ("en az",)),
    ("kapsam", "en fazla", ("en fazla",)),
    ("kapsam", "bazı", ("bazı", "bir kısm")),
    ("kapsam", "çoğu", ("çoğu", "büyük bölümü")),
    ("kapsam", "tümü", ("tümü", "tamamı")),
    ("kapsam", "hariç", ("hariç", "dışında")),
    ("kapsam", "henüz", ("henüz",)),
    ("kapsam", "artık", ("artık",)),
    ("kapsam", "genellikle", ("genellikle", "çoğunlukla")),
    ("kapsam", "kural olarak", ("kural olarak",)),
    ("kapsam", "zorunlu değildir", ("zorunlu değildir", "zorunlu değil", "gerekmez")),
    ("kesinlik", "gözlen", ("gözlen", "tespit edil", "görüld")),
    ("kesinlik", "amaç", ("amaç", "hedefle")),
    ("kesinlik", "plan", ("plan", "öngör")),
    ("kesinlik", "ilişki", ("ilişki", "korelasyon", "bağlantı")),
    ("kesinlik", "değerlendir", ("değerlendir", "görüş")),
    ("kesinlik", "belirtil", ("belirtil", "aktar", "ifade edil")),
    ("kesinlik", "savun", ("savun",)),
    ("kesinlik", "olabilir", ("olabilir", "mümkün", "ihtimal")),
)


@dataclass(frozen=True)
class Invariant:
    category: str
    value: str
    alternatives: tuple[str, ...]
    case_sensitive: bool = True


def normalize(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="backslashreplace")


def section(markdown: str, heading: str) -> str:
    match = re.search(SECTION_PATTERN.format(heading=re.escape(heading)), markdown)
    if match is None:
        raise ValueError(f"Eksik bölüm: ## {heading}")
    return match.group(1).strip()


def invariant(category: str, value: str, *, case_sensitive: bool = True) -> Invariant:
    return Invariant(category, value, (value,), case_sensitive)


def extract_invariants(source: str) -> list[Invariant]:
    source = normalize(source)
    items: list[Invariant] = []

    for value in URL_RE.findall(source):
        items.append(invariant("url", value))
    for value in INLINE_CODE_RE.findall(source):
        items.append(invariant("satır içi kod", f"`{value}`"))
    for value in CODE_BLOCK_RE.findall(source):
        items.append(invariant("kod bloğu", value))
    for value in FOOTNOTE_RE.findall(source):
        items.append(invariant("dipnot işareti", value))
    for value in FOOTNOTE_DEFINITION_RE.findall(source):
        items.append(invariant("dipnot tanımı", value))
    for value in EQUATION_NUMBER_RE.findall(source):
        items.append(invariant("denklem numarası", value))
    for value in DATE_RE.findall(source):
        items.append(invariant("tarih", value, case_sensitive=False))
    for value in NUMBER_RE.findall(source):
        items.append(invariant("sayı", value))
    for value in TECH_IDENTIFIER_RE.findall(source):
        items.append(invariant("teknik ad", value))
    for value in GREEK_SYMBOL_RE.findall(source):
        items.append(invariant("sembol", value))
    for value in MEASUREMENT_RE.findall(source):
        items.append(invariant("ölçüm", value))
    if "±" in source:
        items.append(invariant("işaret", "±"))

    folded_source = source.casefold()
    for category, trigger, alternatives in MARKER_GROUPS:
        if trigger.casefold() in folded_source:
            items.append(
                Invariant(category, trigger, tuple(alternatives), case_sensitive=False)
            )

    unique: dict[tuple[str, str, tuple[str, ...], bool], Invariant] = {}
    for item in items:
        key = (item.category, item.value, item.alternatives, item.case_sensitive)
        unique[key] = item
    return list(unique.values())


def evaluate(case_text: str, output_text: str) -> dict[str, object]:
    source = section(case_text, "Kaynak")
    output = normalize(output_text)
    folded_output = output.casefold()
    invariants = extract_invariants(source)
    missing: list[dict[str, object]] = []

    for item in invariants:
        haystack = output if item.case_sensitive else folded_output
        alternatives = (
            item.alternatives
            if item.case_sensitive
            else tuple(value.casefold() for value in item.alternatives)
        )
        if not any(value in haystack for value in alternatives):
            missing.append(asdict(item))

    return {
        "passed": not missing,
        "checked": len(invariants),
        "missing": missing,
    }


def print_report(case_path: Path, output_path: Path, report: dict[str, object]) -> None:
    state = "GEÇTİ" if report["passed"] else "BAŞARISIZ"
    print(f"{state}: {case_path.name} → {output_path.name}")
    print(f"Denetlenen değişmez: {report['checked']}")
    for item in report["missing"]:
        alternatives = " | ".join(item["alternatives"])
        print(f"- Eksik {item['category']}: {alternatives}")
    print("Not: Akıcılık, ton ve genel anlam uyumu insan veya model hakemi gerektirir.")


def self_test() -> None:
    root = Path(__file__).resolve().parent.parent
    scenarios = (
        (
            root / "evals/teknik.md",
            "GRGM1200 modeli 1200 derece ve 1190 mertebeye kadar kullanıldı. "
            "Denklem (3), Δv değerini km/s cinsinden verir. DOP853 çözücüsünde "
            "bağıl tolerans 10⁻⁶ olarak ayarlandı; sonuç 2,40 ± 0,03 km/s bulundu.",
            "Model kullanıldı. Sonuç 2,40 km/s bulundu.",
        ),
        (
            root / "evals/kapsam-ve-kosul.md",
            "İyileşme yalnızca sistemi en az üç ay kullanan bazı katılımcılarda "
            "gözlendi. Sonuçlar 18 yaş altındaki katılımcıları kapsamamaktadır.",
            "Sistemi üç ay kullanan tüm katılımcılar iyileşti.",
        ),
        (
            root / "evals/bicim-koruma.md",
            section((root / "evals/bicim-koruma.md").read_text(encoding="utf-8"), "Kaynak"),
            "Sonuçlar raporda yer alıyor.",
        ),
    )

    for case_path, passing_output, failing_output in scenarios:
        case_text = case_path.read_text(encoding="utf-8")
        if not evaluate(case_text, passing_output)["passed"]:
            raise SystemExit(f"Öz sınama geçerli çıktıyı reddetti: {case_path.name}")
        if evaluate(case_text, failing_output)["passed"]:
            raise SystemExit(f"Öz sınama bozuk çıktıyı kabul etti: {case_path.name}")

    print(f"Eval runner öz sınaması geçti ({len(scenarios)} vaka).")


def main() -> int:
    configure_stdio()
    parser = argparse.ArgumentParser(
        description="Metinoskop çıktısında kaynak değişmezlerini denetler."
    )
    parser.add_argument("case", nargs="?", type=Path, help="evals/*.md vaka dosyası")
    parser.add_argument("output", nargs="?", type=Path, help="Model çıktısı dosyası")
    parser.add_argument("--json", action="store_true", help="Raporu JSON olarak yazdır")
    parser.add_argument("--self-test", action="store_true", help="Yerleşik öz sınamayı çalıştır")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0
    if args.case is None or args.output is None:
        parser.error("case ve output dosyaları birlikte verilmelidir")

    try:
        case_text = args.case.read_text(encoding="utf-8")
        output_text = args.output.read_text(encoding="utf-8")
        report = evaluate(case_text, output_text)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Hata: {error}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(args.case, args.output, report)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
