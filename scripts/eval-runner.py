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


SECTION_PATTERN = (
    r"(?ms)^## {heading}\s*\r?\n(.*?)"
    r"(?=^## (?:Kaynak|Talep|Korunması gerekenler|Kaçınılması gerekenler|Yapısal beklenti|Serbest değişmezler|Serbest eklemeler)\s*$|\Z)"
)
HEADING_LINE_RE = re.compile(r"(?m)^#{1,6}[ \t].*$")
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
    # "olabileceğini", "olabileceği" çekincenin çekimli biçimleridir; yalnızca "olabilir" aramak korunmuş çekinceyi kayıp sayar.
    ("kesinlik", "olabilir", ("olabil", "mümkün", "ihtimal")),
)

# Epistemic markers an edit must not ADD. Preservation checks above catch a
# number or a scope word that disappears; they pass an output that keeps every
# number but writes a new negative claim, hedge, causal verb or commitment
# into a deflated sentence. Families group interchangeable forms, so turning
# "Sonuç olarak" into "-dığından" or "Bu nedenle" is not an addition.
ADDED_MARKER_FAMILIES = (
    ("olumsuzluk", "olumsuz iddia",
     r"\bdeğil\w*|\byok(?:tur|tu|muş)?\b|\bhiç\w*|\b\w{2,}m[ae](?:d[ıi](?!r)\w*|m[ıi]ş\w*|z(?:lar|ler|dı|di)?\b"
     r"|makta\w*|mekte\w*|yacak\w*|yecek\w*|yabil\w*|yebil\w*)|\b\w{2,}m[ıiuü]yor\w*"),
    ("cekince", "çekince ya da olasılık",
     r"\bolabil\w*|\bolası\b|\bmuhtemel\w*|\bbelki\b|\bgörün(?:mektedir|üyor|ür)\b|\bdüşündür\w*|\bsanıl\w*"
     r"|\btahmin edil\w*|\bişaret e\w*|\bsanırım\b|\bgaliba\b|\b\w+[ae]bil(?:ir|ece[kğ]|mekte)\w*"),
    ("nedensellik", "nedensellik ya da sonuç bağı",
     r"\bneden ol\w*|\byol aç\w*|\betkile\w*|\bsayesinde|\bbu sayede|\byüzünden|\bdolayı\w*|\bnedeniyle"
     r"|\bbu nedenle|\bbu yüzden|\bsonuç olarak|\bsonucunda|\bkaynaklan\w*|\b\w+[dt][ıiuü]ğ[ıiuü]ndan\b"),
    ("pekistirici", "pekiştirici",
     # "kesin bir bilgim yok", "kesin değil" çekincedir, pekiştirici değil.
     r"\baçıkça\b|\bkesin(?:likle)?\b(?!(?:\s+\S+){0,3}?\s+(?:değil|yok))|\bkanıtla\w*|\btartışmasız|\bkuşkusuz|\bşüphesiz"),
    ("karsilastirma", "karşılaştırma ya da üstünlük",
     # "en son" sıra bildirir (`en son hata dağılımları değerlendirildi`), üstünlük değil.
     r"\bdaha\b|\ben\b(?!\s+son\b)|\bkıyasla|\boranla|\bzamankinden"),
    ("tumel", "tümel nicelik",
     r"\btüm\w*|\bbütün\w*|\bher\b|\bhepsi\w*|\btamamı\w*|\btamamen|\bdaima"),
    ("zorunluluk", "zorunluluk",
     r"\b\w+m[ae]l[ıi](?:d[ıi]r|y[ıi]z)?(?=\s*[.!?;:,]|\s*$)|\b\w+m[ae]l[ıi]d[ıi]r\w*|\bgerek\w*|\bzorunlu\w*"),
    ("gelecek", "gelecek ya da taahhüt",
     r"\b\w+[ae]c[ae]k(?:t[ıi]r|lar|ler)?(?=\s*[.!?;:,(]|\s*$)"),
)
ADDED_MARKER_RE = tuple((key, label, re.compile(pattern, re.MULTILINE)) for key, label, pattern in ADDED_MARKER_FAMILIES)
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")


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
    # Dotted numbers that appear in heading lines (2.3, 3.1.1) are section
    # numbers, not facts; a structural edit may legitimately drop them.
    heading_numbers = {
        value for line in HEADING_LINE_RE.findall(source) for value in NUMBER_RE.findall(line) if "." in value
    }
    for value in NUMBER_RE.findall(source):
        if value in heading_numbers:
            continue
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


def free_invariants(case_text: str) -> set[str]:
    """Marker triggers the case declares as filler, listed under
    ``## Serbest değişmezler`` as ``- <trigger> — <reason>`` lines. A case must
    justify each exemption; the runner only reads the trigger before the dash."""
    try:
        block = section(case_text, "Serbest değişmezler")
    except ValueError:
        return set()
    freed: set[str] = set()
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        trigger = re.split(r"\s+[—–-]\s+", line[1:].strip(), maxsplit=1)[0].strip().strip("`")
        if trigger:
            freed.add(trigger.casefold())
    return freed


def tr_fold(text: str) -> str:
    return CODE_SPAN_RE.sub(" ", normalize(text).replace("I", "ı").replace("İ", "i").lower())


def marker_hits(text: str) -> dict[str, list[str]]:
    folded = tr_fold(text)
    return {key: pattern.findall(folded) for key, _, pattern in ADDED_MARKER_RE}


def free_additions(case_text: str) -> set[str]:
    """Families a case allows the output to add, listed under
    ``## Serbest eklemeler`` as ``- <aile> — <gerekçe>`` lines."""
    try:
        block = section(case_text, "Serbest eklemeler")
    except ValueError:
        return set()
    allowed: set[str] = set()
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("-"):
            family = re.split(r"\s+[—–-]\s+", line[1:].strip(), maxsplit=1)[0].strip().strip("`")
            if family:
                allowed.add(family.casefold())
    return allowed


def added_markers(source: str, output: str, allowed: set[str] = frozenset()) -> list[dict[str, object]]:
    # Soru cümlesi önerme kurmaz: kavramsal girişin `... verilebilir mi?` sorusu çekince eklemez.
    asserted = re.sub(r"[^.!?\n]*\?", "", output)
    before, after = marker_hits(source), marker_hits(asserted)
    added: list[dict[str, object]] = []
    for key, label, _ in ADDED_MARKER_RE:
        extra = len(after[key]) - len(before[key])
        # Kaynakta plan zaten varsa (yazma kipinde `bakımın amacı sürüm yükseltmesi` → `sürüm yükseltilecek`),
        # ek gelecek biçimi aynı planın dağılmasıdır; risk, kaynakta hiç plan yokken taahhüt yazmaktır.
        if key == "gelecek" and before[key]:
            continue
        if extra > 0 and key not in allowed:
            new_forms = [form for form in after[key] if form not in before[key]] or after[key]
            added.append({"family": key, "label": label, "count": extra,
                          "source": len(before[key]), "output": len(after[key]), "examples": new_forms[:3]})
    return added


def evaluate(case_text: str, output_text: str) -> dict[str, object]:
    source = section(case_text, "Kaynak")
    output = normalize(output_text)
    folded_output = output.casefold()
    freed = free_invariants(case_text)
    invariants = [
        item for item in extract_invariants(source)
        if not (item.category in ("kapsam", "kesinlik") and item.value.casefold() in freed)
    ]
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

    # Talepte verilen bilgi kaynağın parçasıdır (SKILL.md › Kural önceliği): "Kasım'da başlamayacak" diyen
    # kullanıcının olumsuzluğu metne eklenmiş sayılmaz. `---` sonrası not metin dışıdır; nottaki
    # "kapsam dışı olduğundan" metne yazılmış bir iddia değildir.
    try:
        request = section(case_text, "Talep")
    except ValueError:
        request = ""
    body = re.split(r"(?m)^---\s*$", output)[0]
    added = added_markers(source + "\n" + request, body, free_additions(case_text))

    return {
        "passed": not missing and not added,
        "checked": len(invariants),
        "missing": missing,
        "added": added,
    }


def print_report(case_path: Path, output_path: Path, report: dict[str, object]) -> None:
    state = "GEÇTİ" if report["passed"] else "BAŞARISIZ"
    print(f"{state}: {case_path.name} → {output_path.name}")
    print(f"Denetlenen değişmez: {report['checked']}")
    for item in report["missing"]:
        alternatives = " | ".join(item["alternatives"])
        print(f"- Eksik {item['category']}: {alternatives}")
    for item in report["added"]:
        print(f"- Eklenen {item['label']}: {item['source']} → {item['output']} «{', '.join(item['examples'])}»")
    if report["added"]:
        print("Eklenen işaretin kaynakta dayanağı yoksa kaldır; gerekçeliyse vakaya `## Serbest eklemeler` yaz.")
    print("Not: Akıcılık, ton ve genel anlam uyumu insan veya model hakemi gerektirir.")


def self_test() -> None:
    root = Path(__file__).resolve().parent.parent
    scenarios = (
        (
            root / "evals/teknik-gosterim-korunur.md",
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
            root / "evals/markdown-bicimi-korunur.md",
            section((root / "evals/markdown-bicimi-korunur.md").read_text(encoding="utf-8"), "Kaynak"),
            "Sonuçlar raporda yer alıyor.",
        ),
        (
            root / "evals/rapor-bulgu-yorum-oneri.md",
            "2025 yılında iade oranı kuzey depoda %6,2, diğer depolarda %3,1 olarak "
            "ölçüldü. Görüşmeler, manuel veri girişlerinin hatalara katkıda "
            "bulunabileceğine işaret ediyor. Yönetim üç aylık pilot öneriyor; pilot "
            "henüz başlamadı.",
            "Kuzey depodaki iade sorunu barkod sistemiyle çözülecek.",
        ),
        (
            root / "evals/iddia-tekrar-dongusu.md",
            "Polinom derecesi 20 ile 200 arasında değiştirildiğinde en düşük doğrulama "
            "hatası 120. derecede elde edildi (%2,1). 200. derecede hata %6,8'e yükseldi.",
            "En düşük hata 120. derecede elde edildi. Derece seçimi başarımı belirliyor.",
        ),
        (
            root / "evals/giris-hunisi.md",
            "Şirket, Mart 2026'da yaşanan 14 saatlik veri erişim kesintisinin ardından "
            "yedekleme politikasını yeniledi. Bu belge yeni politikayı açıklar. Tam yedek "
            "haftada bir, artımlı yedek her gece alınır.",
            "Veri güvenliği önemlidir. Bu belge yedekleme politikasını açıklar.",
        ),
        (
            root / "evals/yapay-gerilim.md",
            "Yeni denetleyici kuvvet hatasını %12 azaltmış, yedi günlük konum hatasını ise %8 "
            "artırmıştır; artış yalnızca yüksek eğimli yörüngelerde görülmüştür ve ekip bu "
            "ödünleşimi henüz açıklayamamaktadır.",
            "Yeni denetleyici kuvvet hatasını %12 azalttı.",
        ),
        (
            root / "evals/asiri-bolumleme.md",
            "Deneylerde 2022 yılına ait 48.000 kayıtlık trafik veri kümesi kullanılmıştır; "
            "kayıtların %12'si eksik hız değeri içermektedir. Eksik değerler aynı sensörün "
            "önceki ve sonraki ölçümlerinin ortalamasıyla doldurulmuştur; ön denemelerde bu "
            "yöntem medyanla doldurmaya göre doğrulama hatasını %2 azaltmıştır. Doldurma "
            "yalnızca 10 dakikadan kısa boşluklar için uygulanmış, daha uzun boşluklu kayıtlar "
            "çıkarılmıştır.",
            "48.000 kayıtlık veri kümesinde eksik değerler ortalamayla dolduruldu.",
        ),
        (
            root / "evals/sahip-olmak-kalkisi.md",
            "Önerilen yöntemin hesaplama maliyeti yüksektir. Model üç katmanlıdır; her katmanda "
            "64 birim bulunur. Cihazın koruma sınıfı IP67'dir. Sistem ayrıca hata günlüğü tutar. "
            "Cihaz, şirketin sahip olduğu iki fabrikada üretilmektedir. Kullanıcı bu ayarı "
            "değiştirmek için yönetici yetkisine sahip olmalıdır.",
            "Yöntem pahalıdır. Model üç katmanlıdır ve cihaz su geçirmez. Kullanıcı ayarı değiştirebilir.",
        ),
    )

    for case_path, passing_output, failing_output in scenarios:
        case_text = case_path.read_text(encoding="utf-8")
        if not evaluate(case_text, passing_output)["passed"]:
            raise SystemExit(f"Öz sınama geçerli çıktıyı reddetti: {case_path.name}")
        if evaluate(case_text, failing_output)["passed"]:
            raise SystemExit(f"Öz sınama bozuk çıktıyı kabul etti: {case_path.name}")


    drift = (
        # Historical gold errors that kept every number and passed the suite.
        ("Bu bulgu yöntemin davranışını açıklamaktadır.",
         "Davranış mekanizması bu çalışmada ortaya konmamıştır; olası bir açıklama önerilebilir.",
         {"olumsuzluk", "cekince"}),
        ("Yöntemi kullanan 30 koşuda ortalama hata %4, kullanmayan 30 koşuda %7 idi.",
         "Yöntem hatayı olumlu yönde etkilemektedir: kullanan 30 koşuda hata %4, kullanmayan 30 koşuda %7 idi.",
         {"nedensellik"}),
        ("Yönetim üç aylık pilot öneriyor.", "Pilot üç ay sürecek ve sorunu çözecek.", {"gelecek"}),
    )
    # Soru muafiyeti önermeyi kapsamaz: sorudan sonra gelen çekince yine sayılır.
    drift += (("Sonuç saklanır.", "Saklanabilir mi? Sonuç saklanabilir.", {"cekince"}),)
    for source, output, expected in drift:
        found = {item["family"] for item in added_markers(source, output)}
        if not expected <= found:
            raise SystemExit(f"Öz sınama: eklenen işaret yakalanmadı: beklenen {sorted(expected)}, bulunan {sorted(found)}")
    # Same family, different form: a connective conversion is not an addition.
    for source, output in (
        ("Sonuç olarak tek deneme yapılır.", "Dolayısıyla tek deneme yapılır."),
        ("Hata birikmektedir. Bu nedenle düzeltme gerekir.", "Hata biriktiğinden düzeltme gerekir."),
        ("Doğrulama kümesi yüksek doğruluğa sahip olan ve düşük gecikmeye sahip olan filtreyi seçti.",
         "Doğrulama kümesi yüksek doğruluklu, düşük gecikmeli filtreyi seçti."),
        ("Ölçüm `max_iter=500` ile yapılmadı mı?", "Ölçüm `max_iter=500` ile yapılmadı mı?"),
        ("Bu bir çalışmadır.", "Bu bir çalışmadır."),
        # Yazma kipi: kaynaktaki plan duyuru kipine geçer; paranteze bitişik gelecek kipi de sayılır.
        ("Bakım 4 saat sürecek (22.00–02.00). Panel kapalı olacak.", "Bakım 22.00–02.00 arasında yapılacak. Panel kapalı olacak."),
        ("İyileşme mevsimsel olabilir, emin değilim.", "İyileşme mevsimsel olabilir; bu konuda kesin bir bilgim yok."),
        ("İyileşme mevsimsel olabilir, emin değilim.", "İyileşme mevsimsel olabilir; kesin bir sonuca varmış değilim."),
        ("Son olarak hata dağılımlarını değerlendirir.", "En son hata dağılımları değerlendirildi."),
        ("Sistem aynı sorguları tekrar çalıştırıyor.", "Sistem aynı sorguları tekrar çalıştırıyor. Sonuç yeniden üretilmeden verilebilir mi?"),
    ):
        if added_markers(source, output):
            raise SystemExit(f"Öz sınama: aynı aile içi dönüşüm eklenen işaret sayıldı: {output!r} -> {added_markers(source, output)}")
    case = "\n\n".join(("## Kaynak", "Bulgular önermektedir.", "## Talep", "x",
                        "## Serbest eklemeler", "- cekince — kalkı düzeltmesi")) + "\n"
    if not evaluate(case, "Bulgular düşündürüyor.")["passed"]:
        raise SystemExit("Öz sınama: ## Serbest eklemeler muafiyeti uygulanmadı")
    request_case = "## Kaynak\n\nPilot Kasım'da başlayacak.\n\n## Talep\n\nPilot Kasım'da başlamayacak, düzelt.\n"
    if not evaluate(request_case, "Pilot Kasım'da başlamayacak.")["passed"]:
        raise SystemExit("Öz sınama: talepte verilen bilgi eklenen işaret sayıldı")
    if not evaluate(request_case.replace("başlamayacak, düzelt", "iptal edildi, düzelt"), "Pilot iptal edildi.\n\n---\nNot: kapsam dışı olduğundan değiştirilmedi.")["passed"]:
        raise SystemExit("Öz sınama: metin dışı nottaki ifade metne eklenmiş sayıldı")
    if evaluate(request_case.replace("başlamayacak, düzelt", "düzelt"), "Pilot Kasım'da başlamayacak.")["passed"]:
        raise SystemExit("Öz sınama: talepte olmayan olumsuzluk yakalanmadı")
    hedge_case = "## Kaynak\n\nİyileşme kısmen mevsimsel olabilir, emin değilim.\n\n## Talep\n\nx\n"
    if not evaluate(hedge_case, "İyileşmenin kısmen mevsimsel olabileceğini düşünüyorum, ancak emin değilim.")["passed"]:
        raise SystemExit("Öz sınama: çekimli çekince (`olabileceğini`) kayıp sayıldı")

    print(f"Eval runner öz sınaması geçti ({len(scenarios)} vaka, {len(drift)} eklenen işaret senaryosu).")


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
