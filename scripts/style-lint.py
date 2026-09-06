#!/usr/bin/env python3
"""Flag AI-like rhetorical and structural patterns in Turkish prose for review.

The linter never rejects a text on its own. It reports where inspection is
needed: which sentences carry a suspicious rhetorical function, how dense those
functions are, and whether the document architecture is fragmented or
suspiciously uniform. Every family below is a trigger for inspection, not a
forbidden word list.

Usage:
    python scripts/style-lint.py output.txt
    python scripts/style-lint.py output.txt --source evals/case.md
    python scripts/style-lint.py output.txt --source source.txt --fail-on-introduced
    python scripts/style-lint.py output.txt --json
    python scripts/style-lint.py --self-test

With ``--source`` the report separates patterns the edit *introduced* (present in
the output more often than in the source, compared pattern by pattern) from
patterns that *remain* from the source. Introduced patterns are the only
deterministic failure signal, and only when ``--fail-on-introduced`` is given.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path


# --------------------------------------------------------------------------- #
# Pattern catalog, organised by rhetorical function.
# level "sert": hard-suppression families (almost always filler).
# level "bağlam": context-sensitive families (inspect, do not auto-delete).
# --------------------------------------------------------------------------- #

CATEGORIES: tuple[dict[str, object], ...] = (
    {
        "key": "onem",
        "label": "Üretilmiş önem",
        "level": "sert",
        "patterns": (
            r"açısından (?:son derece |oldukça |büyük |özellikle )?(?:önem|kritik)",
            r"(?:önemli|kritik|temel|belirleyici|merkezi) (?:bir )?rol (?:oyna|üstlen)",
            r"kritik (?:bir )?önem",
            r"belirleyici (?:bir )?(?:etken|faktör|unsur)|belirleyici olmaktadır|belirleyicidir",
            r"dikkat çekici (?:bir )?(?:sonuç|bulgu|gelişme)",
            r"kayda değer (?:bir )?(?:bulgu|sonuç|gelişme|iyileşme)",
            r"önemli (?:bir )?(?:çıkarım|bilgi|bulgu|gösterge|adım|aşama|iyileşme|katkı)",
            r"değerli (?:bir )?(?:içgörü|bilgi|kaynak)",
            r"içgörü(?:ler)? (?:sun|sağla)",
            r"anlayışımızı geliştir",
            r"daha iyi anlaşılmasını sağla",
            r"literatür(?:e|deki) (?:önemli )?(?:katkı|boşlu)",
            r"boşluğu doldur",
            r"yeni bir (?:perspektif|bakış açısı) (?:sun|kazandır|getir)",
            r"sağlam bir temel|temel oluştur|zemin hazırla",
            r"önemi(?:ni)? (?:bir kez daha )?(?:ortaya|göster|vurgula)",
            r"\bönem (?:taşı|arz)",
            r"göz ardı edilmemesi gereken",
            r"kritik (?:bir )?(?:etken|aşama|faktör)",
            r"açıkça (?:göster|ortaya koy)|güçlü biçimde destekle",
            r"önemli (?:bir )?(?:etki|katkı)",
        ),
    },
    {
        "key": "acimlama",
        "label": "Yeniden ifade",
        "level": "bağlam",
        "patterns": (
            r"^başka bir (?:ifadeyle|deyişle)|^bir başka (?:ifadeyle|deyişle)|^diğer bir deyişle",
            r"^yani\b",
            r"^bu da şu anlama gel|anlamına gelmektedir",
        ),
    },
    {
        "key": "savunma",
        "label": "Savunmacı açıklama",
        "level": "sert",
        "patterns": (
            r"burada (?:amaç|hedef|hedeflenen|kastedilen)",
            r"dikkat edilmesi gereken",
            r"vurgulamak (?:gerek|isterim|lazım|istiyorum)",
            r"belirtmek (?:gerek|isterim|istiyorum)",
            r"altını çiz",
            r"tesadüfi değil|tesadüf değil|keyfî değil|keyfi değil|rastgele değil",
            r"bilinçli (?:bir )?(?:seçim|tercih|karar)",
            r"eksiklik olarak (?:görül|değerlendiril)",
            r"zayıflığı değil|bir zayıflık değil",
            r"nedeni (?:oldukça |son derece |gayet )?(?:basit|açık)",
            r"buradaki temel fikir|temel fikir şudur",
            r"(?:asıl|bu noktada) önemli olan",
            r"bu ayrım (?:önemli|kritik)",
            r"bu açıdan bakıldığında|bu çerçevede değerlendir",
            r"yanlış anlaşılmama",
            r"şaşırtıcı değil|sürpriz değil",
            r"beklenen bir (?:sonuç|durum)",
            r"özellikle (?:belirtmek|vurgula)",
        ),
    },
    {
        "key": "duyuru",
        "label": "Yol haritası ve duyuru",
        "level": "sert",
        "patterns": (
            r"bu (?:bölümde|kısımda|yazıda|makalede|çalışmada|belgede|notta) .*(?:ele alın|incelen|açıklan|değinil|anlatıl|sunul|tartışıl|özetlen)",
            r"aşağıda .*(?:incelen|açıklan|sunul|ele alın|anlatıl)",
            r"(?:şimdi|önce|öncelikle) .*(?:bakalım|geçelim|ele alalım|inceleyelim)",
            r"öncelikle .*anlamak gerek|bunu anlamak için önce",
            r"buradan hareketle",
            r"(?:bir sonraki|ilerleyen|sonraki) (?:bölüm|kısım|adım)",
            r"(?:daha sonra|ileride) (?:yeniden |tekrar )?dön",
            r"sorulması gereken soru",
            r"^peki\b.*\?",
            r"bizi şu soruya",
            r"ne anlama geliyor\?",
        ),
    },
    {
        "key": "sarmalayici",
        "label": "Boş bölüm sarmalayıcısı",
        "level": "sert",
        "patterns": (
            r"önemli bileşenlerinden biri",
            r"birkaç noktaya değinmek gerek",
            r"önemi açıkça görülmektedir",
            r"(?:kritik|temel|önemli) rolünü (?:göster|ortaya koy)",
            r"temel önemini ortaya koy",
            r"bu bölüm,? .*(?:ortaya koy|göster)",
        ),
    },
    {
        "key": "gerilim",
        "label": "Yapay gerilim",
        "level": "sert",
        "patterns": (
            r"burada işler değiş",
            r"asıl sorun bundan sonra",
            r"^ilk bakışta",
            r"tam da bu noktada",
            r"beklenmedik bir (?:durum|sonuç)la",
            r"hikâye burada bitm|hikaye burada bitm|hikâye (?:burada |bununla )?bitmiyor",
            r"asıl şaşırtıcı olan",
            r"işin (?:ilginç|garip|tuhaf) (?:yanı|tarafı)",
            r"^daha da önemlisi",
            r"sorun tam olarak burada",
            r"görünüşte basit",
            r"tablo (?:değişmektedir|değişiyor|nettir)",
            r"kritik bir kırılma",
            r"asıl mesele (?:burada|bundan sonra)",
        ),
    },
    {
        "key": "aski",
        "label": "Paragraf sonu askısı",
        "level": "sert",
        "patterns": (
            r"yanıtı bir sonraki bölümde",
            r"bir sonraki bölümde (?:görül|ortaya çık|açıklan|ele alın)",
            r"^ancak burada önemli bir sorun",
            r"sonraki adıma geçmek gerek",
            r"daha temel bir soruya",
            r"asıl cevap ise",
        ),
    },
    {
        "key": "capraz",
        "label": "Çapraz gönderme",
        "level": "bağlam",
        "patterns": (
            r"yukarıda (?:belirtil|değinil|açıklan|anlatıl|görül|verilen|tanımlanan)",
            r"önceki bölümde|bir önceki (?:bölüm|başlık)",
            r"aşağıda görüleceği",
            r"ilerleyen bölüm",
            r"daha önce (?:değinil|belirtil|açıklan|tanımlan)",
            r"ileride (?:tekrar |yeniden )?dön",
            r"(?<![\d.])\d{1,2}\.\d'?(?:de|da|te|ta|deki|daki|teki|taki)\b|bölüm \d+(?:\.\d+)?'?(?:de|da|te|ta)\b",
        ),
    },
    {
        "key": "baglam_tekrari",
        "label": "Bağlam yeniden başlatma",
        "level": "bağlam",
        "patterns": (
            r"bu çalışmada kullanılan",
            r"^bu çalışmada\b",
            r"hatırlanacağı üzere|hatırlatmak gerekirse",
            r"daha önce de (?:belirtil|değinil|vurgulan)",
        ),
    },
    {
        "key": "giris",
        "label": "Kalıp giriş",
        "level": "bağlam",
        "patterns": (
            r"^günümüz",
            r"son yıllarda",
            r"hızla (?:değişen|gelişen|dönüşen)",
            r"teknolojinin hızla",
            r"her zamankinden daha",
            r"giderek (?:daha )?(?:artan|kritik|önemli)",
            r"beraberinde getir",
            r"bu gelişmeler ışığında|tüm bunların ışığında",
            r"her geçen gün",
            r"vazgeçilmez bir parça",
        ),
    },
    {
        "key": "sonuc",
        "label": "Kalıp sonuç ve gelecek çalışma",
        "level": "bağlam",
        "patterns": (
            r"^sonuç olarak|^özetle(?:mek gerekirse)?\b|^kısacası",
            r"genel olarak değerlendirildiğinde",
            r"birlikte (?:ele alındığında|değerlendirildiğinde)",
            r"bir bütün olarak",
            r"^nihayetinde|^netice(?:de| itibarıyla)",
            r"göstermektedir ki",
            r"bir kez daha (?:ortaya|göster|kanıtla|görül)",
            r"^dolayısıyla .*(?:önem|belirleyici|kritik|etken)",
            r"gelecek(?:te)? (?:yapılacak )?(?:çalışma|araştırma)",
            r"daha da geliştir",
            r"temel taşlar",
        ),
    },
    {
        "key": "karsitlik",
        "label": "Üretilmiş karşıtlık",
        "level": "bağlam",
        "patterns": (
            r"(?:yalnızca|sadece) .* değil,? aynı zamanda",
            r"^mesele .* değil|mesele (?:yalnızca|sadece) .* değil|asıl mesele",
            r"buradaki soru .* değil",
            r"(?:dan|den|tan|ten) ziyade",
            r"bir yandan .* (?:diğer|öte) yandan",
            r"her ne kadar .* olsa da",
            r"basitçe .* değil",
            r"ile sınırlı değil",
            r"ötesine geç",
            r"olmaktan öte",
            r"bir araçtan (?:fazla|öte)",
        ),
    },
    {
        "key": "denge",
        "label": "Zorlama denge",
        "level": "bağlam",
        "patterns": (
            r"^bununla birlikte|^öte yandan",
            r"avantajlarına rağmen|güçlü yönlerine rağmen",
            r"güçlü olmakla birlikte",
            r"bazı sınırl(?:ılık|ama)lar",
            r"her (?:çalışmada|yeniliğin|yöntemin|yaklaşımın) olduğu gibi",
            r"temkinli olmakta fayda|ihtiyatla (?:yaklaş|değerlendir)",
            r"dikkatle izlenmeli",
            r"denge meselesi",
        ),
    },
    {
        "key": "soyut_yuklem",
        "label": "Soyut yüklem",
        "level": "bağlam",
        "patterns": (
            r"ortaya koy",
            r"gözler önüne ser",
            r"işaret et",
            r"yansıt(?:makta|maktadır|ır|ıyor)",
            r"vurgula(?:makta|maktadır|r\b|ıyor)",
            r"öne çık(?:ar|makta|maktadır)",
            r"dikkat çek(?:mekte|mektedir|iyor|er)",
            r"rol oyna",
            r"katkı (?:sağla|sun)",
            r"olanak (?:sağla|tanı)|imkân (?:sağla|tanı)|imkan (?:sağla|tanı)",
            r"mümkün kıl",
            r"(?:çerçeve|perspektif|içgörü|bakış açısı) (?:sun|sağla)",
            r"kapı arala|ışık tut",
            r"şekillendir",
        ),
    },
    {
        "key": "uzun_ifade",
        "label": "Uzun çerçeve ifadesi",
        "level": "bağlam",
        "patterns": (
            r"ortaya çıkmasına neden ol",
            r"durumda bulunmaktadır",
            r"yapılması gerekmektedir",
            r"yapılmasına ihtiyaç",
            r"kullanılması durumunda",
            r"gerçekleştirilen .* sonucunda elde edilen",
            r"açısından değerlendirildiği",
            r"bakımından ele alındığında",
            r"husus olarak karşımıza",
            r"değerlendirilmesi mümkün olan",
            r"hususlardan biri",
            r"\bsöz konusu\b",
        ),
    },
    {
        "key": "bos_ozne",
        "label": "Boş soyut özne",
        "level": "bağlam",
        "patterns": (
            r"^(?:bu|söz konusu|ilgili) (?:durum|yaklaşım|yapı|süreç|çerçeve|bağlam|bulgu|sonuç|özellik|yöntem|perspektif|husus|nokta|veri|karar|gelişme)\b",
        ),
    },
    {
        "key": "sohbet",
        "label": "Sohbet botu kalıntısı",
        "level": "sert",
        "patterns": (
            r"^elbette|^tabii ki|^kesinlikle!",
            r"^harika (?:bir )?soru",
            r"umarım .*(?:faydalı|yardımcı)",
            r"^dilerseniz|dilerseniz .*(?:paylaşabilir|yapabilir|gönderebilir)",
            r"memnuniyetle",
        ),
    },
    {
        "key": "reklam",
        "label": "Reklam dili",
        "level": "bağlam",
        "patterns": (
            r"benzersiz|eşsiz|rakipsiz",
            r"çığır aç|devrim niteliğinde",
            r"kusursuz|sektör lideri",
            r"bir üst seviyeye|fark yarat|yeniden tanımla",
            r"dönüştürücü",
        ),
    },
    {
        "key": "klise_gecis",
        "label": "Klişe geçiş",
        "level": "bağlam",
        "patterns": (
            r"^bu (?:bağlamda|noktada|çerçevede|doğrultuda|kapsamda)\b",
            r"hiç şüphesiz|yadsınamaz|bilindiği üzere|önem arz",
        ),
    },
)

COMPILED: dict[str, tuple[re.Pattern[str], ...]] = {
    str(category["key"]): tuple(re.compile(p) for p in category["patterns"])  # type: ignore[union-attr]
    for category in CATEGORIES
}
LABELS: dict[str, str] = {str(c["key"]): str(c["label"]) for c in CATEGORIES}
LEVELS: dict[str, str] = {str(c["key"]): str(c["level"]) for c in CATEGORIES}

MAKTADIR_RE = re.compile(r"m[ae]kt[ae]d[ıi]r[.!?]*$")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-ZÇĞİÖŞÜ0-9\"'«(`])")
STRUCTURE_SKIP_PREFIXES = ("#", "|", "```", "- ", "* ", "+ ")
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
LIST_CHAIN_OPENERS = (
    "bu nedenle", "sonuç olarak", "dolayısıyla", "böylece", "bu yüzden", "bu da",
    "ancak", "fakat", "buna karşılık", "daha sonra", "ardından",
)
CONNECTOR_OPENERS = (
    "bununla birlikte", "öte yandan", "bu doğrultuda", "bu bağlamda", "bu noktada",
    "buna ek olarak", "ayrıca", "dolayısıyla", "ancak", "bu nedenle", "diğer yandan",
)


# --------------------------------------------------------------------------- #
# Text handling
# --------------------------------------------------------------------------- #


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="backslashreplace")


def tr_lower(text: str) -> str:
    """Turkish-aware lowercase: İ→i and I→ı before the generic lowercase."""
    return text.replace("İ", "i").replace("I", "ı").lower()


def normalize(text: str) -> str:
    return unicodedata.normalize("NFC", text).replace("\r\n", "\n")


@dataclass
class Sentence:
    paragraph: int
    index: int
    text: str
    lowered: str = ""

    def __post_init__(self) -> None:
        self.lowered = tr_lower(self.text.strip())


@dataclass
class Paragraph:
    number: int
    sentences: list[Sentence] = field(default_factory=list)
    prose: bool = True
    heading_index: int | None = None


@dataclass
class Heading:
    index: int
    level: int
    text: str
    paragraphs: int = 0
    first_sentence: str = ""


@dataclass
class Document:
    paragraphs: list[Paragraph] = field(default_factory=list)
    headings: list[Heading] = field(default_factory=list)
    list_items: int = 0
    list_item_texts: list[str] = field(default_factory=list)


def strip_markup(block: str) -> str:
    lines = []
    for line in block.split("\n"):
        stripped = line.strip()
        if stripped.startswith(">"):
            stripped = stripped.lstrip(">").strip()
        stripped = LIST_ITEM_RE.sub("", stripped)
        lines.append(stripped)
    return " ".join(line for line in lines if line)


def split_sentences(text: str) -> list[str]:
    parts = SENTENCE_SPLIT_RE.split(text.strip())
    return [part.strip() for part in parts if part.strip()]


def parse(text: str) -> Document:
    text = normalize(text)
    doc = Document()
    in_code = False
    number = 0
    current_heading: Heading | None = None
    for block in re.split(r"\n\s*\n", text):
        block = block.strip("\n")
        if not block.strip():
            continue
        if block.strip().startswith("```"):
            in_code = not in_code if block.count("```") % 2 else in_code
            continue
        if in_code:
            continue
        first = block.lstrip()
        heading_match = HEADING_RE.match(first.split("\n", 1)[0])
        if heading_match:
            current_heading = Heading(len(doc.headings), len(heading_match.group(1)), heading_match.group(2))
            doc.headings.append(current_heading)
            rest = first.split("\n", 1)[1] if "\n" in first else ""
            if not rest.strip():
                continue
            block = rest
            first = block.lstrip()
        if first.startswith("|"):
            continue
        for line in block.split("\n"):
            if LIST_ITEM_RE.match(line):
                doc.list_items += 1
                doc.list_item_texts.append(tr_lower(LIST_ITEM_RE.sub("", line).strip()))
        prose = not first.startswith(STRUCTURE_SKIP_PREFIXES) and not LIST_ITEM_RE.match(first)
        number += 1
        paragraph = Paragraph(number=number, prose=prose,
                              heading_index=current_heading.index if current_heading else None)
        for index, sentence in enumerate(split_sentences(strip_markup(block)), start=1):
            paragraph.sentences.append(Sentence(number, index, sentence))
        if paragraph.sentences:
            doc.paragraphs.append(paragraph)
            if current_heading is not None and prose:
                current_heading.paragraphs += 1
                if not current_heading.first_sentence:
                    current_heading.first_sentence = paragraph.sentences[0].lowered
    return doc


# --------------------------------------------------------------------------- #
# Analysis
# --------------------------------------------------------------------------- #


def find_hits(paragraphs: list[Paragraph]) -> list[dict[str, object]]:
    hits: list[dict[str, object]] = []
    for paragraph in paragraphs:
        for sentence in paragraph.sentences:
            for key, patterns in COMPILED.items():
                for pattern in patterns:
                    match = pattern.search(sentence.lowered)
                    if match:
                        hits.append(
                            {
                                "category": key,
                                "label": LABELS[key],
                                "level": LEVELS[key],
                                "pattern": pattern.pattern,
                                "paragraph": paragraph.number,
                                "sentence": sentence.index,
                                "text": sentence.text,
                                "match": match.group(0),
                            }
                        )
                        break  # one hit per category per sentence
    return hits


def sentence_matches_any(sentence: Sentence, keys: tuple[str, ...]) -> bool:
    return any(p.search(sentence.lowered) for key in keys for p in COMPILED[key])


def lowered_matches_any(lowered: str, keys: tuple[str, ...]) -> bool:
    return any(p.search(lowered) for key in keys for p in COMPILED[key])


def heading_stems(text: str) -> set[str]:
    return {w[:5] for w in re.findall(r"\w+", tr_lower(text)) if len(w) >= 5}


def structure_summary(doc: Document, hits: list[dict[str, object]]) -> dict[str, object]:
    prose = [p for p in doc.paragraphs if p.prose]
    headings = doc.headings
    short = sum(1 for p in prose if len(p.sentences) <= 2)
    return {
        "headings": len(headings),
        "max_depth": max((h.level for h in headings), default=0),
        "paragraphs_per_heading": round(len(prose) / len(headings), 2) if headings else None,
        "one_paragraph_sections": sum(1 for h in headings if h.paragraphs <= 1),
        "short_paragraphs": short,
        "prose_paragraphs": len(prose),
        "list_items": doc.list_items,
        "cross_references": sum(1 for h in hits if h["category"] == "capraz"),
        "announcements": sum(1 for h in hits if h["category"] in ("duyuru", "sarmalayici")),
        "mini_conclusions": sum(1 for h in hits if h["category"] in ("onem", "sonuc")),
    }


def structural_checks(doc: Document, hits: list[dict[str, object]]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    paragraphs = doc.paragraphs
    prose = [p for p in paragraphs if p.prose]
    all_sentences = [s for p in paragraphs for s in p.sentences]
    headings = doc.headings

    # --- uniformity -----------------------------------------------------------
    counts = [len(p.sentences) for p in prose]
    if len(counts) >= 4:
        if len(set(counts)) == 1 and counts[0] >= 3:
            findings.append({"check": "paragraf_uzunlugu",
                             "text": f"{len(counts)} paragrafın tamamı {counts[0]} cümle: tek biçimli paragraf mimarisi."})
        elif len(counts) >= 5 and max(counts) - min(counts) <= 1 and statistics.pstdev(counts) < 0.5 and max(counts) >= 3:
            findings.append({"check": "paragraf_uzunlugu",
                             "text": f"Paragraf uzunlukları neredeyse eşit ({', '.join(map(str, counts))} cümle)."})

    closers = [p for p in prose if len(p.sentences) >= 2]
    if len(closers) >= 3:
        closing = [p for p in closers
                   if sentence_matches_any(p.sentences[-1], ("onem", "sonuc", "soyut_yuklem", "bos_ozne", "sarmalayici"))]
        if len(closing) / len(closers) >= 0.6:
            findings.append({"check": "onem_ile_kapanis",
                             "text": f"{len(closers)} paragrafın {len(closing)}'i önem, sonuç veya soyut yüklem cümlesiyle bitiyor."})

    openers = [p for p in prose if p.sentences]
    if len(openers) >= 3:
        opening = [p for p in openers if sentence_matches_any(p.sentences[0], ("bos_ozne", "klise_gecis", "giris"))]
        if len(opening) / len(openers) >= 0.5:
            findings.append({"check": "bos_ozne_ile_acilis",
                             "text": f"{len(openers)} paragrafın {len(opening)}'i boş özne, klişe geçiş veya kalıp girişle açılıyor."})

    if len(all_sentences) >= 4:
        maktadir = [s for s in all_sentences if MAKTADIR_RE.search(s.lowered)]
        if len(maktadir) / len(all_sentences) >= 0.5:
            findings.append({"check": "maktadir_zinciri",
                             "text": f"{len(all_sentences)} cümlenin {len(maktadir)}'i -maktadır/-mektedir ile bitiyor."})

    for paragraph in prose:
        lengths = [len(s.text.split()) for s in paragraph.sentences]
        if len(lengths) >= 8:
            diffs = [b - a for a, b in zip(lengths, lengths[1:]) if b != a]
            if len(diffs) >= 7:
                alternations = sum(1 for a, b in zip(diffs, diffs[1:]) if (a > 0) != (b > 0))
                if alternations / (len(diffs) - 1) >= 0.85:
                    findings.append({"check": "cumle_uzunlugu_nobetlesmesi",
                                     "text": f"Paragraf {paragraph.number}: cümle uzunlukları düzenli olarak kısa-uzun nöbetleşiyor."})

    for paragraph in prose:
        if len(paragraph.sentences) >= 3:
            starts = [s.lowered.split()[0] for s in paragraph.sentences if s.lowered.split()]
            for word in set(starts):
                if starts.count(word) >= 3 and len(word) > 1:
                    findings.append({"check": "ayni_cumle_baslangici",
                                     "text": f"Paragraf {paragraph.number}: {starts.count(word)} cümle \"{word}\" ile başlıyor."})

    significance = [s for s in all_sentences if sentence_matches_any(s, ("onem",))]
    if len(significance) >= 3:
        findings.append({"check": "islev_tekrari",
                         "text": f"Önem bildirme işlevi {len(significance)} cümlede tekrarlanıyor (sözcükler farklı olsa da işlev aynı)."})

    # --- fragmentation --------------------------------------------------------
    if len(headings) >= 3:
        ratio = len(prose) / len(headings)
        if ratio < 1.5:
            findings.append({"check": "baslik_yogunlugu",
                             "text": f"{len(headings)} başlık, {len(prose)} paragraf: başlık başına {ratio:.1f} paragraf. Başlıklar içerikten sık."})
        single = [h for h in headings if h.paragraphs <= 1]
        if len(single) >= 3 and len(single) / len(headings) >= 0.5:
            findings.append({"check": "tek_paragraf_bolum",
                             "text": f"{len(headings)} başlığın {len(single)}'i altında en fazla bir paragraf var: bölme testini uygula."})

    deep = [h for h in headings if h.level >= 4]
    if deep:
        findings.append({"check": "derin_baslik",
                         "text": f"{len(deep)} dördüncü veya daha derin düzey başlık: derinlik testini uygula."})
    level3 = [h for h in headings if h.level == 3]
    if len(level3) >= 3 and all(h.paragraphs <= 1 for h in level3):
        findings.append({"check": "derin_baslik",
                         "text": f"{len(level3)} üçüncü düzey başlığın hepsi tek paragraflık: hiyerarşi içeriği aşıyor."})

    if len(prose) >= 5:
        short = [p for p in prose if len(p.sentences) <= 2]
        if len(short) / len(prose) >= 0.6:
            findings.append({"check": "kisa_paragraf",
                             "text": f"{len(prose)} paragrafın {len(short)}'i en fazla iki cümle: paragraflar erken bölünmüş olabilir."})

    prose_sentences = sum(len(p.sentences) for p in prose)
    chained = [item for item in doc.list_item_texts if item.startswith(LIST_CHAIN_OPENERS)]
    if len(chained) >= 2:
        findings.append({"check": "liste_yogunlugu",
                         "text": f"{len(chained)} liste ögesi bağlaçla başlıyor (\"{chained[0][:40]}...\"): nedensel akıl yürütme listeye çevrilmiş olabilir."})
    elif doc.list_items >= 6 and doc.list_items >= prose_sentences:
        findings.append({"check": "liste_yogunlugu",
                         "text": f"{doc.list_items} liste ögesi, {prose_sentences} düzyazı cümlesi: metnin çoğu listeye çevrilmiş olabilir."})

    for heading in headings:
        if not heading.first_sentence or heading.level == 1:
            continue
        if lowered_matches_any(heading.first_sentence, ("duyuru", "sarmalayici")):
            findings.append({"check": "baslik_tekrari",
                             "text": f"\"{heading.text}\" başlığının ilk cümlesi duyuru veya sarmalayıcı: doğrudan içerikle başla."})
            continue
        stems = heading_stems(heading.text)
        shared = {s for s in stems if s in heading.first_sentence}
        if stems and len(shared) >= 2:
            findings.append({"check": "baslik_tekrari",
                             "text": f"\"{heading.text}\" başlığı ilk cümlede yineleniyor ({', '.join(sorted(shared))})."})

    if len(prose) >= 4:
        connector = [p for p in prose if any(p.sentences[0].lowered.startswith(c) for c in CONNECTOR_OPENERS)]
        if len(connector) / len(prose) >= 0.5:
            findings.append({"check": "baglac_ile_acilis",
                             "text": f"{len(prose)} paragrafın {len(connector)}'i bağlaçla açılıyor: zorlama geçiş olabilir."})

    cross = [h for h in hits if h["category"] == "capraz"]
    if len(cross) >= 3:
        findings.append({"check": "capraz_gonderme_sikligi",
                         "text": f"{len(cross)} çapraz gönderme: birleştirme veya yeniden sıralama göndermeleri gereksiz kılabilir."})

    restarts = [h for h in hits if h["category"] == "baglam_tekrari"]
    if len(restarts) >= 2:
        findings.append({"check": "baglam_tekrari",
                         "text": f"{len(restarts)} bağlam hatırlatması: aynı düzenek veya amaç yeniden tanıtılıyor."})

    return findings


def analyse(text: str) -> dict[str, object]:
    doc = parse(text)
    hits = find_hits(doc.paragraphs)
    sentences = sum(len(p.sentences) for p in doc.paragraphs)
    per_category: dict[str, int] = {}
    for hit in hits:
        per_category[str(hit["category"])] = per_category.get(str(hit["category"]), 0) + 1
    density = round(100 * len(hits) / sentences, 1) if sentences else 0.0
    return {
        "sentences": sentences,
        "paragraphs": len(doc.paragraphs),
        "hits": hits,
        "per_category": per_category,
        "hard_hits": sum(1 for h in hits if h["level"] == "sert"),
        "density_per_100": density,
        "structure_summary": structure_summary(doc, hits),
        "structure": structural_checks(doc, hits),
    }


def pattern_counts(report: dict[str, object]) -> dict[tuple[str, str], int]:
    counts: dict[tuple[str, str], int] = {}
    for hit in report["hits"]:  # type: ignore[union-attr]
        key = (str(hit["category"]), str(hit["pattern"]))
        counts[key] = counts.get(key, 0) + 1
    return counts


def compare(source_report: dict[str, object], output_report: dict[str, object]) -> dict[str, object]:
    """Compare at pattern level so a filler phrase swapped for a sibling phrase
    in the same family still counts as newly introduced."""
    src = pattern_counts(source_report)
    out = pattern_counts(output_report)
    examples: dict[tuple[str, str], str] = {}
    for hit in output_report["hits"]:  # type: ignore[union-attr]
        examples.setdefault((str(hit["category"]), str(hit["pattern"])), str(hit["match"]))

    introduced: list[dict[str, object]] = []
    for key, count in out.items():
        extra = count - src.get(key, 0)
        if extra > 0:
            introduced.append({"category": key[0], "label": LABELS[key[0]], "count": extra, "example": examples[key]})

    src_cat = source_report["per_category"]
    out_cat = output_report["per_category"]
    remaining = {k: min(out_cat[k], src_cat[k]) for k in out_cat if k in src_cat}  # type: ignore[index]
    removed = {k: src_cat[k] - out_cat.get(k, 0) for k in src_cat if src_cat[k] > out_cat.get(k, 0)}  # type: ignore[index]

    src_struct = source_report["structure_summary"]
    out_struct = output_report["structure_summary"]
    structure_delta = {
        key: {"kaynak": src_struct[key], "çıktı": out_struct[key]}  # type: ignore[index]
        for key in ("headings", "max_depth", "one_paragraph_sections", "short_paragraphs",
                    "prose_paragraphs", "list_items", "cross_references", "announcements")
        if src_struct[key] != out_struct[key]  # type: ignore[index]
    }
    source_checks = {s["check"] for s in source_report["structure"]}  # type: ignore[union-attr]
    new_structure = [f["text"] for f in output_report["structure"]  # type: ignore[union-attr]
                     if f["check"] not in source_checks]
    return {"introduced": introduced, "remaining": remaining, "removed": removed,
            "structure_delta": structure_delta, "introduced_structure": new_structure}


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #

SUMMARY_LABELS = {
    "headings": "başlık", "max_depth": "en derin düzey", "paragraphs_per_heading": "paragraf/başlık",
    "one_paragraph_sections": "tek paragraflık bölüm", "short_paragraphs": "≤2 cümlelik paragraf",
    "prose_paragraphs": "düzyazı paragrafı", "list_items": "liste ögesi",
    "cross_references": "çapraz gönderme", "announcements": "duyuru/sarmalayıcı",
    "mini_conclusions": "önem/sonuç cümlesi",
}


def print_report(path: str, report: dict[str, object], comparison: dict[str, object] | None,
                 source_path: str | None) -> None:
    print(f"Stil denetimi: {path}")
    print(f"Cümle: {report['sentences']} | Paragraf: {report['paragraphs']} | "
          f"İşaret: {len(report['hits'])} ({report['density_per_100']} / 100 cümle) | "
          f"Sert bastırma ailesi: {report['hard_hits']}")
    summary: dict[str, object] = report["structure_summary"]  # type: ignore[assignment]
    print("Parçalanma yoğunluğu: " + " | ".join(
        f"{SUMMARY_LABELS[k]}: {v}" for k, v in summary.items() if v is not None))

    hits: list[dict[str, object]] = report["hits"]  # type: ignore[assignment]
    by_category: dict[str, list[dict[str, object]]] = {}
    for hit in hits:
        by_category.setdefault(str(hit["category"]), []).append(hit)
    for key, items in sorted(by_category.items(), key=lambda kv: (LEVELS[kv[0]] != "sert", kv[0])):
        print(f"\n[{LABELS[key]} · {LEVELS[key]}] {len(items)} işaret")
        for hit in items:
            text = str(hit["text"])
            excerpt = text if len(text) <= 140 else text[:137] + "..."
            print(f"  - P{hit['paragraph']}C{hit['sentence']} «{hit['match']}»: {excerpt}")

    structure: list[dict[str, object]] = report["structure"]  # type: ignore[assignment]
    if structure:
        print("\n[Yapı]")
        for finding in structure:
            print(f"  - {finding['text']}")

    if comparison is not None:
        print(f"\nKaynakla karşılaştırma ({source_path}):")
        introduced = comparison["introduced"]
        remaining = comparison["remaining"]
        removed = comparison["removed"]
        if introduced:
            print("  Kaynakta olmayıp çıktıda beliren kalıplar (dolgu başka dolguya çevrilmiş olabilir):")
            for item in introduced:  # type: ignore[union-attr]
                print(f"    - {item['label']}: +{item['count']} «{item['example']}»")
        else:
            print("  Çıktı kaynakta bulunmayan bir kalıp eklememiş.")
        if comparison["introduced_structure"]:
            print("  Kaynakta olmayıp çıktıda beliren yapı bulguları:")
            for text in comparison["introduced_structure"]:  # type: ignore[union-attr]
                print(f"    - {text}")
        if comparison["structure_delta"]:
            print("  Yapı ölçülerindeki değişim:")
            for key, pair in comparison["structure_delta"].items():  # type: ignore[union-attr]
                print(f"    - {SUMMARY_LABELS[key]}: {pair['kaynak']} → {pair['çıktı']}")
        if remaining:
            print("  Kaynakta olup çıktıda kalan aileler (işlevini incele; sert aileler için silme testini uygula):")
            for key, count in remaining.items():  # type: ignore[union-attr]
                print(f"    - {LABELS[key]} · {LEVELS[key]}: {count}")
        if removed:
            print("  Kaynakta olup çıktıda azalan:")
            for key, count in removed.items():  # type: ignore[union-attr]
                print(f"    - {LABELS[key]}: -{count}")

    print("\nNot: İşaretler inceleme içindir; tek bir işaret metni yapay yapmaz. "
          "Sert bastırma ailesindeki cümleler için \"bunu silersem hangi bilgi kaybolur?\", "
          "yapı bulguları için \"bu sınır kavramsal mı?\" sorusunu sor.")


# --------------------------------------------------------------------------- #
# Self-test
# --------------------------------------------------------------------------- #

SYNTHETIC_AI_TEXT = """Günümüzde teknolojinin hızla gelişmesiyle birlikte veri analizi her zamankinden daha önemli hale gelmiştir. Kurumlar giderek artan veri hacmiyle karşı karşıya kalmaktadır. Bu durum, analiz yöntemlerinin gözden geçirilmesini kritik bir konu haline getirmektedir.

Bu bölümde yöntemin temel bileşenleri ele alınacaktır. Model 120. derecede en düşük hatayı vermektedir. Başka bir ifadeyle bu derece diğer seçeneklerden daha başarılı olmaktadır. Bu sonuç, derece seçiminin kritik önemini açıkça ortaya koymaktadır.

Bu tercih tesadüfi değildir. Şunu vurgulamak gerekir ki bu seçim bilinçli bir seçimdir. Bu durum bir eksiklik olarak görülmemelidir. Bu yaklaşım, sürecin daha iyi anlaşılmasını sağlamaktadır.

Bir yandan hata azalmakta, öte yandan hesaplama süresi artmaktadır. Her ne kadar sonuçlar olumlu olsa da temkinli olmakta fayda bulunmaktadır. Bu bulgu, yöntemin sağlamlığı açısından önemli çıkarımlar sunmaktadır. Bu da yöntemin önemini bir kez daha ortaya koymaktadır.

Sonuç olarak elde edilen bulgular yöntemin etkinliğini açıkça göstermektedir. Tüm bu bulgular birlikte ele alındığında yöntemin literatürdeki önemli bir boşluğu doldurduğu görülmektedir. Gelecekte yapılacak çalışmalar bu yaklaşımı daha da geliştirebilir. Umarım bu açıklama faydalı olmuştur.
"""

FRAGMENTED_TEXT = """## 3. Yöntem

### 3.1 Veri

#### 3.1.1 Kaynak

Bu bölümde veri kaynağı ele alınmaktadır. Analizde 2024 yılına ait 1.200 kayıt kullanılmıştır.

#### 3.1.2 Eksik değerler

Yukarıda belirtilen kayıtların %12'si eksik değer içermektedir.

### 3.2 Gruplar

Önceki bölümde açıklanan kayıtlar üç gruba ayrılmıştır. Bu ayrımın nedenine ileride tekrar dönülecektir.

### 3.3 Gerekçe

İlk bakışta bu ayrım keyfî görünmektedir. Ancak hikâye burada bitmez. Bu bağlamda, söz konusu grupların değerlendirilmesi gereken hususlardan biri hizmet düzeyi sınıflarıdır.

### 3.4 Sonuç

Bu değerlendirmeler grup ayrımının kritik rolünü göstermektedir. Asıl cevap ise bir sonraki bölümde ortaya çıkmaktadır.

Gruplar şu nedenlerle seçilmiştir:

- Hizmet sınıflarıyla örtüşmektedir.
- Bu nedenle karşılaştırma kolaylaşmaktadır.
- Sonuç olarak gruplar korunmuştur.
- Dolayısıyla analiz bu gruplarla yapılmıştır.
"""

CLEAN_TEXT = """Deney grubunda ortalama tepki süresi 310 milisaniye, kontrol grubunda 342 milisaniyeydi. Hata sayısı iki grupta da ortalama 1,2 olarak ölçüldü.

Ölçümler 24 katılımcıyla tek oturumda yapıldı; ikinci oturum planlanmadı.

Ekip, tepki süresi farkının kaynağını belirlemek için göz izleme verisini ayrıca inceleyecek. Bu inceleme için henüz tarih verilmedi.
"""

WELL_STRUCTURED_TEXT = """## Sorun

Ödeme servisi 3 Eylül'de 14.10 ile 14.35 arasında istek zaman aşımı verdi. Etkilenen istek sayısı 2.140'tı; bunların 310'u müşteri tarafından yeniden denendi ve başarılı oldu. Kesinti, veritabanı bağlantı havuzunun 50 bağlantı sınırına ulaşmasıyla başladı.

Havuz doluyken yeni istekler 30 saniye bekleyip zaman aşımına düştü. Aynı dakikalarda rapor işi uzun süreli bağlantılar açıyordu; bu işin havuzu doldurup doldurmadığı henüz doğrulanmadı.

## Yapılan işlem

Havuz sınırı 14.35'te 120'ye çıkarıldı ve zaman aşımları bu değişiklikten sonra durdu. Ekip, rapor işini ayrı bir havuza taşımayı önerdi; karar perşembe toplantısında verilecek. Değişiklik geri alınırsa aynı kesintinin yinelenmesi bekleniyor.

Bu arada havuz doluluğu dakikada bir izleniyor ve %80'i aştığında ekibe uyarı gidiyor. Uyarı eşiği geçici olarak düşük tutuldu; kalıcı değer toplantıda belirlenecek.
"""

FILLER_SOURCE = "Model 120. derecede en düşük hatayı verdi. Bu sonuç derece seçiminin kritik önemini ortaya koymaktadır."
FILLER_TRANSLATED = "Model 120. derecede en düşük hatayı verdi. Sonuç olarak derece seçimi önemli bir etkendir; bu bulgu derece seçimine ışık tutmaktadır."
FILLER_DELETED = "Model 120. derecede en düşük hatayı verdi."


def self_test() -> None:
    ai = analyse(SYNTHETIC_AI_TEXT)
    expected = {"onem", "acimlama", "savunma", "duyuru", "giris", "sonuc", "karsitlik", "denge",
                "soyut_yuklem", "bos_ozne", "sohbet"}
    missing = expected - set(ai["per_category"])  # type: ignore[arg-type]
    if missing:
        raise SystemExit(f"Öz sınama: yapay metinde beklenen aileler bulunamadı: {sorted(missing)}")
    checks = {f["check"] for f in ai["structure"]}  # type: ignore[union-attr]
    for check in ("paragraf_uzunlugu", "onem_ile_kapanis", "islev_tekrari", "maktadir_zinciri"):
        if check not in checks:
            raise SystemExit(f"Öz sınama: yapay metinde beklenen yapı bulgusu yok: {check}")

    fragmented = analyse(FRAGMENTED_TEXT)
    expected_frag = {"gerilim", "aski", "capraz", "uzun_ifade", "duyuru", "sarmalayici"}
    missing = expected_frag - set(fragmented["per_category"])  # type: ignore[arg-type]
    if missing:
        raise SystemExit(f"Öz sınama: parçalanmış metinde beklenen aileler bulunamadı: {sorted(missing)}")
    checks = {f["check"] for f in fragmented["structure"]}  # type: ignore[union-attr]
    for check in ("baslik_yogunlugu", "tek_paragraf_bolum", "derin_baslik", "kisa_paragraf",
                  "liste_yogunlugu", "baslik_tekrari", "capraz_gonderme_sikligi"):
        if check not in checks:
            raise SystemExit(f"Öz sınama: parçalanmış metinde beklenen yapı bulgusu yok: {check}")

    for label, text in (("temiz", CLEAN_TEXT), ("iyi yapılı", WELL_STRUCTURED_TEXT)):
        report = analyse(text)
        if report["hard_hits"] != 0:
            raise SystemExit(f"Öz sınama: {label} metinde sert bastırma işareti bulundu: {report['hits']}")
        if report["structure"]:
            raise SystemExit(f"Öz sınama: {label} metinde yapı bulgusu üretildi: {report['structure']}")
        if len(report["hits"]) > 1:  # type: ignore[arg-type]
            raise SystemExit(f"Öz sınama: {label} metinde fazla işaret: {report['hits']}")

    src = analyse(FILLER_SOURCE)
    translated = compare(src, analyse(FILLER_TRANSLATED))
    if not translated["introduced"]:
        raise SystemExit("Öz sınama: dolguyu dolguya çeviren çıktı 'yeni kalıp' olarak işaretlenmedi")
    deleted = compare(src, analyse(FILLER_DELETED))
    if deleted["introduced"]:
        raise SystemExit("Öz sınama: dolguyu silen çıktı yanlışlıkla 'yeni kalıp' olarak işaretlendi")
    if not deleted["removed"]:
        raise SystemExit("Öz sınama: dolguyu silen çıktıda azalma görülmedi")

    repaired = compare(fragmented, analyse(WELL_STRUCTURED_TEXT))
    if repaired["introduced_structure"]:
        raise SystemExit("Öz sınama: iyi yapılı çıktı yeni yapı bulgusu üretti")
    if repaired["structure_delta"].get("headings", {}).get("çıktı") != 2:  # type: ignore[union-attr]
        raise SystemExit("Öz sınama: yapı ölçüsü değişimi başlık sayısını yanlış raporladı")

    if tr_lower("İSTANBUL IŞIK") != "istanbul ışık":
        raise SystemExit("Öz sınama: Türkçe küçük harf dönüşümü hatalı")

    print("Stil denetimi öz sınaması geçti (yapay metin, parçalanmış belge, temiz metin, iyi yapılı belge, dolgu çevirisi, dolgu silme).")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def read_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".md":
        match = re.search(r"(?ms)^## Kaynak\s*\n(.*?)(?=^## (?:Talep|Korunması|Kaçınılması)|\Z)", text)
        if match:
            return match.group(1)
    return text


def main() -> int:
    configure_stdio()
    parser = argparse.ArgumentParser(
        description="Türkçe metinde yapay retorik ve yapısal örüntüleri inceleme için işaretler; tek başına reddetmez."
    )
    parser.add_argument("output", nargs="?", type=Path, help="Denetlenecek metin (model çıktısı)")
    parser.add_argument("--source", type=Path, help="Kaynak metin veya evals/*.md vakası; karşılaştırma için")
    parser.add_argument("--json", action="store_true", help="Raporu JSON olarak yazdır")
    parser.add_argument("--fail-on-introduced", action="store_true",
                        help="Çıktı kaynakta olmayan bir kalıp eklemişse 1 ile çık (yalnızca --source ile)")
    parser.add_argument("--self-test", action="store_true", help="Yerleşik öz sınamayı çalıştır")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0
    if args.output is None:
        parser.error("denetlenecek metin dosyası verilmelidir")

    try:
        report = analyse(read_text(args.output))
        comparison = None
        if args.source is not None:
            comparison = compare(analyse(read_text(args.source)), report)
    except (OSError, UnicodeError) as error:
        print(f"Hata: {error}", file=sys.stderr)
        return 2

    if args.json:
        payload = dict(report)
        if comparison is not None:
            payload["comparison"] = comparison
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_report(str(args.output), report, comparison, str(args.source) if args.source else None)

    if args.fail_on_introduced and comparison is not None and comparison["introduced"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
