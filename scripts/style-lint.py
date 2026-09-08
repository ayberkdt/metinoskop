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
patterns that *remain* from the source. Only introduced *hard-suppression*
patterns are a deterministic failure signal (``--fail-on-introduced-hard``);
context-sensitive families such as ``yani``, ``öte yandan`` or ``işaret etmek``
only warn, because the skill itself forbids deleting them automatically.
``--fail-on-introduced-any`` is the strict mode.

Source-language-shadow (translationese) signals are reported as review
findings only: frame-noun stacks (``açısından / kapsamında / noktasında``),
``bir`` density, ``olan`` chains, runs of sentences opening with the same
subject, ``ve`` clause chains, converb pile-ups, genitive stacks and
connector-initial sentence density. None of them is a deterministic failure;
a single ``bir``, ``olan``, ``ve`` or ``açısından`` is never flagged.

Discourse signals (epistemic architecture, lexical fit, textual coherence) are
likewise review-only: hedge stacks, booster/hedge conflicts, attribution
followed by an unattributed "bu nedenle", unmotivated tense alternation,
passive + nominalization clusters, light-verb density, postposition clusters,
synonym drift among generic nouns, per-section topic resets, parenthetical
load and register clashes. No regex decides epistemic correctness.
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
    {
        "key": "sahip",
        "label": "Sahip olmak kalkısı",
        "level": "bağlam",
        "patterns": (
            r"\bsahip(?!lik|len|siz)",
        ),
    },
    {
        "key": "varlik",
        "label": "Varlık kalıbı",
        "level": "bağlam",
        "patterns": (
            r"\bbulunma(?:kta|makta)dır|\byer almaktadır|\bmevcuttur|\bmevcut (?:bulun|değildir)|\biçermektedir",
        ),
    },
    {
        "key": "kalki",
        "label": "Çeviri kalkısı",
        "level": "bağlam",
        "patterns": (
            r"olarak hizmet (?:et|ver|gör)",
            r"hakkında konuş",
            r"günün sonunda",
            r"\bbir (?:değerlendirme|analiz|inceleme|ölçüm|kontrol|uygulama|iyileştirme) (?:yap|gerçekleştir|yürüt)",
            r"karar alma süreci",
            r"(?:etki|rol)y?e sahip|özelli(?:ğ|g)ine sahip",
        ),
    },
    {
        "key": "kiplik",
        "label": "Çekince işareti",
        "level": "bağlam",
        "patterns": (
            r"\bolabilir\b|\bolabileceğ|\bolmayabilir|\bdüşünülebilir|\bdüşünülmektedir|\bdüşünülüyor|\bdüşündür",
            r"\bgörünmektedir|\bgörünüyor|\bgörünüşe göre|\bmuhtemel|\bolası\b|\bolasıdır|\bbelki\b|\bsanılmaktadır|\btahmin edil",
        ),
    },
    {
        "key": "pekistirici",
        "label": "Pekiştirici",
        "level": "bağlam",
        "patterns": (
            r"\baçıkça\b|\bkesin olarak|\bkesinlikle\b|\bgüçlü biçimde|\btartışmasız|\bkuşkusuz|\bşüphesiz|\bnet biçimde",
            r"\bkanıtla(?:maktadır|mıştır|r\b|ıyor)|\bdoğrudan göster",
        ),
    },
    {
        "key": "aktarim",
        "label": "Aktarım işareti",
        "level": "bağlam",
        "patterns": (
            r"(?:rapor|çalışma|araştırma|yazar|üretici|ekip|kurum|görüşme|katılımcı|kaynak|belge|tutanak|yönetim|müşteri)\w* göre",
            r"\bbildir(?:di|miştir|mektedir|ilmiştir|ildi|iyor|mişlerdir)|\bbelirt(?:ti|miştir|mektedir|ilmiştir|ildi|iyor|mişlerdir)",
            r"\böne sür|\bifade et(?:ti|miştir|mektedir|ilmiştir)|\baktar(?:dı|mıştır|maktadır|ıldı|ıyor)|\bsavun(?:du|maktadır|muştur|uyor)|\biddia et",
        ),
    },
    {
        "key": "hafif_fiil",
        "label": "Hafif fiil",
        "level": "bağlam",
        "patterns": (
            r"\bgerçekleştir|\bmeydana getir",
            r"(?:iyileştirme|artış|azalma|gelişme|katkı|fayda|yarar|cevap|yanıt|çözüm|sonuç) (?:sağla|üret)",
            r"işlemi (?:yap|gerçekleştir)|(?:değerlendirme|analiz|inceleme|ölçüm|kontrol|karşılaştırma|uygulama) (?:yap|gerçekleştir|yürüt)",
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
SENTENCE_CONNECTORS = CONNECTOR_OPENERS + ("sonuç olarak", "buna karşılık", "bu yüzden", "üstelik")

# Source-language-shadow (translationese) signals. All review-only.
FRAME_RE = re.compile(
    r"\b(?:açısından|bakımından|kapsamında|bağlamında|çerçevesinde|doğrultusunda|"
    r"noktasında|üzerinden|temelinde|perspektifinden|ekseninde)\b"
)
OLAN_RE = re.compile(r"\bolan\b")
BIR_RE = re.compile(r"\bbir\b")
VE_RE = re.compile(r"\bve\b")
WORD_RE = re.compile(r"\w+")
CONVERB_RE = re.compile(r"\w+(?:[ıiuü]p|[ae]r[ae]k)$")
CONVERB_STOP = {"ekip", "prensip", "kulüp", "grup", "tip", "yaprak", "toprak", "bayrak", "mübarek", "merak", "gerek", "direk", "börek", "kürek"}
GENITIVE_RE = re.compile(r"\w{3,}(?:[ıiuü]n|n[ıiuü]n)$")
GENITIVE_STOP = {"için", "bütün", "zaten", "metin", "zemin", "yetkin", "uzun", "derin", "yakın", "bugün", "yarın", "dün", "kalın", "bin", "on", "gün", "esin"}
# Discourse (epistemic / lexical / coherence) signals. All review-only.
HEDGE_RE = re.compile(
    r"\b(?:olabilir|olabileceğ\w*|olmayabilir|düşünülebilir|düşünülmektedir|düşünülüyor|düşündür\w*|"
    r"görünmektedir|görünüyor|görünüşe göre|muhtemel\w*|olası\w*|belki|sanılmaktadır|tahmin edil\w*)"
)
BOOSTER_RE = re.compile(
    r"\b(?:açıkça|kesin olarak|kesinlikle|güçlü biçimde|tartışmasız|kuşkusuz|şüphesiz|net biçimde|"
    r"kanıtla(?:maktadır|mıştır|r|ıyor)|doğrudan göster\w*)\b"
)
CONCLUSION_OPENERS = ("bu nedenle", "dolayısıyla", "bu yüzden", "sonuç olarak", "demek ki", "öyleyse")
NOMINALIZATION_RE = re.compile(r"\w+(?:l|n)m[ae]s[ıi]\w*$")
PASSIVE_FINITE_RE = re.compile(r"\w+(?:[ıiuü]l|n)(?:m[ıiuü]şt[ıi]r|m[ıiuü]ş|m[ae]kt[ae]d[ıi]r|d[ıi]|[ae]c[ae]kt[ıi]r)$")
POSTPOSITION_RE = re.compile(r"\b(?:hakkında|ilişkin|yönelik|dair|üzerine)\b")
GENERIC_NOUN_SETS = (
    ("yöntem/yaklaşım/yapı/çözüm", (r"\byöntem\w*", r"\byaklaşım\w*", r"\byapı(?:s[ıi]n?|y[ıi]|ya|da|dan|n[ıi]n|lar\w*|d[ıi]r)?\b", r"\bçözüm\w*", r"\bstrateji\w*", r"\bmekanizma\w*")),
    ("sonuç/bulgu/çıktı/gözlem", (r"\bsonuç\w*", r"\bbulgu\w*", r"\bçıktılar\w*|\bçıktı(?:s[ıi]|y[ıi]|ya|n[ıi]n|da|dan)\b", r"\bgözlem(?!ci|le)\w*")),
)
GENERIC_NOUN_COMPILED = tuple((label, tuple(re.compile(p) for p in patterns)) for label, patterns in GENERIC_NOUN_SETS)
TOPIC_RESET_RE = re.compile(r"^bu (?:çalışmada|çalışma\b|raporda|belgede|bölümde|araştırmada|makalede)")
DASH_RE = re.compile(r"[—–]")
TENSE_CLASSES = (
    ("mektedir", re.compile(r"m[ae]kt[ae](?:d[ıi]r)?$")),
    ("miştir", re.compile(r"m[ıiuü]ş(?:t[ıi]r|lerdir|lardır)?$")),
    ("yor", re.compile(r"yor(?:lar|du|um|uz|sunuz)?$")),
    ("dı", re.compile(r"[dt][ıiuü](?:m|k|n|lar|ler|nız|niz)?$")),
    ("r", re.compile(r"(?<![dt])[ıiuüae]r$")),
)
FRAME_STACK_MIN = 2
OLAN_CHAIN_MIN = 2
BIR_SENTENCE_MIN = 3
BIR_PER_100_MAX = 6.0
VE_CHAIN_MIN = 3
CONVERB_MIN = 4
GENITIVE_RUN_MIN = 3
SUBJECT_RUN_MIN = 3


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
    direct: int = 0      # paragraphs directly under this heading
    subtree: int = 0     # paragraphs under this heading and all its sub-headings
    parent: int | None = None
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
    stack: list[Heading] = []
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
            level = len(heading_match.group(1))
            while stack and stack[-1].level >= level:
                stack.pop()
            heading = Heading(len(doc.headings), level, heading_match.group(2),
                              parent=stack[-1].index if stack else None)
            doc.headings.append(heading)
            stack.append(heading)
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
                              heading_index=stack[-1].index if stack else None)
        for index, sentence in enumerate(split_sentences(strip_markup(block)), start=1):
            paragraph.sentences.append(Sentence(number, index, sentence))
        if paragraph.sentences:
            doc.paragraphs.append(paragraph)
            if stack and prose:
                stack[-1].direct += 1
                for open_heading in stack:
                    open_heading.subtree += 1
                if not stack[-1].first_sentence:
                    stack[-1].first_sentence = paragraph.sentences[0].lowered
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


def sentence_words(sentence: Sentence) -> list[str]:
    return WORD_RE.findall(sentence.lowered)


def converb_count(words: list[str]) -> int:
    return sum(
        1 for w in words
        if len(w) >= 5 and w not in CONVERB_STOP and CONVERB_RE.match(w)
        and not (w.endswith(("rak", "rek")) and len(w) < 6)
    )


def frame_stacked(frames: list[str]) -> bool:
    """Two *different* frame nouns, or three of any kind, in one sentence.
    A parallel pair such as "maliyet açısından ucuz, süre açısından pahalı" is
    a comparison axis, not a stack."""
    return len(set(frames)) >= FRAME_STACK_MIN or len(frames) >= FRAME_STACK_MIN + 1


def longest_genitive_run(words: list[str]) -> int:
    best = run = 0
    for w in words:
        if len(w) >= 5 and w not in GENITIVE_STOP and GENITIVE_RE.match(w):
            run += 1
            best = max(best, run)
        else:
            run = 0
    return best


def subject_runs(paragraph: Paragraph) -> list[tuple[str, int]]:
    """Runs of consecutive sentences that open with the same one or two tokens.
    This is a *sentence-opening* heuristic, not subject detection: "İlk deney ...
    İlk sonuç ..." also matches. The judge decides whether it is subject repetition."""
    runs: list[tuple[str, int]] = []
    keys: list[tuple[str, str]] = []
    for sentence in paragraph.sentences:
        words = sentence_words(sentence)
        if not words:
            keys.append(("", ""))
            continue
        first = words[0]
        two = " ".join(words[:2]) if len(words) >= 2 else first
        keys.append((first if len(first) > 1 else "", two))
    index = 0
    while index < len(keys):
        first, two = keys[index]
        end = index + 1
        while end < len(keys) and keys[end][0] and (keys[end][0] == first or keys[end][1] == two):
            end += 1
        length = end - index
        if first and length >= SUBJECT_RUN_MIN:
            label = two if all(keys[j][1] == two for j in range(index, end)) else first
            runs.append((label, length))
        index = end if length > 1 else index + 1
    return runs


def translationese_summary(doc: Document, hits: list[dict[str, object]]) -> dict[str, object]:
    prose = [p for p in doc.paragraphs if p.prose]
    sentences = [s for p in prose for s in p.sentences]
    words_total = sum(len(sentence_words(s)) for s in sentences)
    bir_total = sum(len(BIR_RE.findall(s.lowered)) for s in sentences)
    return {
        "sahip_olmak": sum(1 for h in hits if h["category"] == "sahip"),
        "varlik_kalibi": sum(1 for h in hits if h["category"] == "varlik"),
        "cerceve_yigini": sum(1 for s in sentences if frame_stacked(FRAME_RE.findall(s.lowered))),
        "olan_zinciri": sum(1 for s in sentences if len(OLAN_RE.findall(s.lowered)) >= OLAN_CHAIN_MIN),
        "tekrarlanan_cumle_baslangici": sum(len(subject_runs(p)) for p in prose),
        "ve_zinciri": sum(1 for s in sentences if len(VE_RE.findall(s.lowered)) >= VE_CHAIN_MIN),
        "fiilimsi_yigini": sum(1 for s in sentences if converb_count(sentence_words(s)) >= CONVERB_MIN),
        "iyelik_zinciri": sum(1 for s in sentences if longest_genitive_run(sentence_words(s)) >= GENITIVE_RUN_MIN),
        "baglac_baslangici": sum(1 for s in sentences if s.lowered.startswith(SENTENCE_CONNECTORS)),
        "bir_per_100": round(100 * bir_total / words_total, 1) if words_total else 0.0,
    }


def translationese_checks(doc: Document, hits: list[dict[str, object]]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    prose = [p for p in doc.paragraphs if p.prose]
    sentences = [s for p in prose for s in p.sentences]

    def excerpt(sentence: Sentence) -> str:
        text = sentence.text
        return text if len(text) <= 90 else text[:87] + "..."

    for s in sentences:
        frames = FRAME_RE.findall(s.lowered)
        if frame_stacked(frames):
            findings.append({"check": "cerceve_yigini",
                             "text": f"P{s.paragraph}C{s.index}: {len(frames)} çerçeve adı ({', '.join(frames)}) tek cümlede: ilişkiyi hâl eki, iyelik veya fiil kodlayabilir mi?"})
        olan = len(OLAN_RE.findall(s.lowered))
        if olan >= OLAN_CHAIN_MIN:
            findings.append({"check": "olan_zinciri",
                             "text": f"P{s.paragraph}C{s.index}: {olan} \"olan\" tek cümlede: niteleme adın önüne alınabilir mi? «{excerpt(s)}»"})
        bir = len(BIR_RE.findall(s.lowered))
        if bir >= BIR_SENTENCE_MIN:
            findings.append({"check": "bir_yogunlugu",
                             "text": f"P{s.paragraph}C{s.index}: {bir} \"bir\" tek cümlede: tanımlık kalkısı mı, sayı mı? «{excerpt(s)}»"})
        ve = len(VE_RE.findall(s.lowered))
        if ve >= VE_CHAIN_MIN:
            findings.append({"check": "ve_zinciri",
                             "text": f"P{s.paragraph}C{s.index}: {ve} \"ve\" tek cümlede: çekimli cümle zinciri mi; -ip, -erek, -ince ilişkiyi daha açık kurar mı?"})
        words = sentence_words(s)
        converbs = converb_count(words)
        if converbs >= CONVERB_MIN:
            findings.append({"check": "fiilimsi_yigini",
                             "text": f"P{s.paragraph}C{s.index}: {converbs} -ip/-erek fiilimsisi tek yükleme asılı: kavramsal sınırda bölünebilir mi?"})
        genitive = longest_genitive_run(words)
        if genitive >= GENITIVE_RUN_MIN:
            findings.append({"check": "iyelik_zinciri",
                             "text": f"P{s.paragraph}C{s.index}: {genitive} ardışık iyelik eki: ilişki zinciri fiil veya yan cümleyle açılabilir mi?"})

    words_total = sum(len(sentence_words(s)) for s in sentences)
    bir_total = sum(len(BIR_RE.findall(s.lowered)) for s in sentences)
    if words_total >= 40 and bir_total >= 4 and 100 * bir_total / words_total > BIR_PER_100_MAX:
        findings.append({"check": "bir_yogunlugu",
                         "text": f"{words_total} sözcükte {bir_total} \"bir\" ({100 * bir_total / words_total:.1f} / 100 sözcük): tanımlık kalkısı yoğun olabilir."})

    for paragraph in prose:
        for label, length in subject_runs(paragraph):
            findings.append({"check": "tekrarlanan_cumle_baslangici",
                             "text": f"Paragraf {paragraph.number}: {length} ardışık cümle \"{label}\" ile başlıyor. Bu gerçekten özne tekrarı mı (hakem karar verir)? Öyleyse özne düşürme, birleştirme veya yeni bilgi etrafında yeniden sıralama mümkün mü?"})

    # Connector and demonstrative density are judged per paragraph (a run of
    # labelled transitions inside one paragraph) and across the document.
    scopes: list[tuple[str, list[Sentence]]] = [
        (f"Paragraf {p.number}", p.sentences) for p in prose if len(p.sentences) >= 4
    ]
    if len(sentences) >= 4 and len(prose) > 1:
        scopes.append(("Belge", sentences))
    seen: set[str] = set()
    for scope, group in scopes:
        threshold = 0.5 if scope != "Belge" else 0.4
        connector = [s for s in group if s.lowered.startswith(SENTENCE_CONNECTORS)]
        if len(connector) / len(group) >= threshold and "baglac" not in seen:
            seen.add("baglac")
            findings.append({"check": "baglac_yogunlugu",
                             "text": f"{scope}: {len(group)} cümlenin {len(connector)}'i söylem belirteciyle başlıyor: ilişki yapıdan çıkıyorsa etiket gereksiz olabilir."})
        demonstrative = [s for s in group if sentence_matches_any(s, ("bos_ozne",))]
        if len(demonstrative) / len(group) >= threshold and "gosterme" not in seen:
            seen.add("gosterme")
            findings.append({"check": "gosterme_ritmi",
                             "text": f"{scope}: {len(group)} cümlenin {len(demonstrative)}'i \"bu + söylem adı\" ile başlıyor: önceki önerme her seferinde yeniden paketleniyor."})
    return findings


def tense_class(sentence: Sentence) -> str | None:
    words = sentence_words(sentence)
    if not words:
        return None
    last = words[-1]
    if last.endswith(("lar", "ler")) and not last.endswith("yorlar"):
        # "kalırlar", "gelirler" are aorist plurals; "sensörler", "örnekler" are nouns.
        return "r" if re.search(r"[ıiuüae]rl[ae]r$", last) else None
    for label, pattern in TENSE_CLASSES:
        if pattern.search(last):
            return label
    return None


def tense_alternation(paragraph: Paragraph) -> tuple[int, int]:
    classes = [c for c in (tense_class(s) for s in paragraph.sentences) if c]
    if len(classes) < 4:
        return 0, 0
    switches = sum(1 for a, b in zip(classes, classes[1:]) if a != b)
    return len(set(classes)), switches


def parenthetical_load(sentence: Sentence) -> bool:
    text = sentence.text
    parens = text.count("(")
    dashes = len(DASH_RE.findall(text))
    return parens >= 2 or dashes >= 2 or (parens >= 1 and dashes >= 1) or text.count(";") >= 3


def discourse_summary(doc: Document, hits: list[dict[str, object]]) -> dict[str, object]:
    findings = discourse_checks(doc, hits)
    counts = {key: 0 for key in DISCOURSE_LABELS}
    for finding in findings:
        counts[str(finding["check"])] = counts.get(str(finding["check"]), 0) + 1
    counts["kiplik"] = sum(1 for h in hits if h["category"] == "kiplik")
    counts["pekistirici"] = sum(1 for h in hits if h["category"] == "pekistirici")
    counts["hafif_fiil"] = sum(1 for h in hits if h["category"] == "hafif_fiil")
    return counts


def discourse_checks(doc: Document, hits: list[dict[str, object]]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    prose = [p for p in doc.paragraphs if p.prose]
    sentences = [s for p in prose for s in p.sentences]

    def excerpt(sentence: Sentence) -> str:
        text = sentence.text
        return text if len(text) <= 90 else text[:87] + "..."

    for s in sentences:
        hedges = HEDGE_RE.findall(s.lowered)
        boosters = BOOSTER_RE.findall(s.lowered)
        if len(hedges) >= 2:
            findings.append({"check": "kiplik_yigini",
                             "text": f"P{s.paragraph}C{s.index}: {len(hedges)} çekince işareti ({', '.join(hedges)}) tek cümlede: hangisi olasılık, hangisi atıf, hangisi gereksiz?"})
        if hedges and boosters:
            findings.append({"check": "pekistirici_catismasi",
                             "text": f"P{s.paragraph}C{s.index}: pekiştirici ({', '.join(boosters)}) ile çekince ({', '.join(hedges)}) aynı önermede çekişiyor: kaynağın gerçek kanıt düzeyi hangisi?"})
        words = sentence_words(s)
        nominal = [w for w in words if NOMINALIZATION_RE.match(w)]
        passive = [w for w in words if PASSIVE_FINITE_RE.match(w)]
        if len(nominal) >= 2 and passive:
            findings.append({"check": "edilgen_adlastirma",
                             "text": f"P{s.paragraph}C{s.index}: {len(nominal)} adlaştırma ve edilgen yüklem bir arada: aktör biliniyor mu, doğrudan yüklem mümkün mü? «{excerpt(s)}»"})
        posts = POSTPOSITION_RE.findall(s.lowered)
        if len(posts) >= 2:
            findings.append({"check": "ilgec_yogunlugu",
                             "text": f"P{s.paragraph}C{s.index}: {len(posts)} ilgeç ({', '.join(posts)}) tek cümlede: ilişki konu mu, hedef mi, referans mı; hâl eki yeterli mi?"})
        if parenthetical_load(s):
            findings.append({"check": "parantez_yuku",
                             "text": f"P{s.paragraph}C{s.index}: ara söz yükü (parantez, uzun çizgi veya noktalı virgül yığını): ara söz ana cümleye mi ait, ayrı cümle mi olmalı?"})

    for paragraph in prose:
        for index, s in enumerate(paragraph.sentences):
            if sentence_matches_any(s, ("aktarim",)):
                for later in paragraph.sentences[index + 1:]:
                    if later.lowered.startswith(CONCLUSION_OPENERS):
                        findings.append({"check": "aktarim_sonrasi_sonuc",
                                         "text": f"Paragraf {paragraph.number}: atıflı cümleden (C{s.index}) sonra C{later.index} sonuç bağlacıyla başlıyor: atıflı yorum yazar olgusuna dönüşüyor olabilir."})
                        break
                break
        distinct, switches = tense_alternation(paragraph)
        if distinct >= 3 and switches >= 3:
            findings.append({"check": "kip_nobetlesmesi",
                             "text": f"Paragraf {paragraph.number}: {distinct} farklı kip, {switches} geçiş: her kip değişimi gerçek bir bakış açısı değişimine mi karşılık geliyor?"})
        joined = " ".join(s.lowered for s in paragraph.sentences)
        for label, patterns in GENERIC_NOUN_COMPILED:
            present = [p.pattern for p in patterns if p.search(joined)]
            if len(present) >= 3:
                findings.append({"check": "esanlam_kaymasi",
                                 "text": f"Paragraf {paragraph.number}: {label} ailesinden {len(present)} farklı ad: aynı nesneye mi gönderiyorlar?"})
        if any(sentence_matches_any(s, ("gerilim", "sohbet")) for s in paragraph.sentences) and any(
                MAKTADIR_RE.search(s.lowered) or sentence_matches_any(s, ("uzun_ifade", "klise_gecis"))
                for s in paragraph.sentences):
            findings.append({"check": "kayit_kaymasi",
                             "text": f"Paragraf {paragraph.number}: sohbet gerilimi ile bürokratik ya da akademik kayıt aynı paragrafta: kayıt profili tek mi?"})

    resets = [p for p in prose if p.sentences and TOPIC_RESET_RE.search(p.sentences[0].lowered)]
    if len(resets) >= 2:
        findings.append({"check": "konu_sifirlama",
                         "text": f"{len(resets)} paragraf \"bu çalışmada / bu bölümde\" ile açılıyor: amaç, yöntem veya veri kümesi her bölümde yeniden mi tanıtılıyor?"})
    return findings


def structure_summary(doc: Document, hits: list[dict[str, object]]) -> dict[str, object]:
    prose = [p for p in doc.paragraphs if p.prose]
    headings = doc.headings
    short = sum(1 for p in prose if len(p.sentences) <= 2)
    return {
        "headings": len(headings),
        "max_depth": max((h.level for h in headings), default=0),
        "paragraphs_per_heading": round(len(prose) / len(headings), 2) if headings else None,
        "one_paragraph_sections": sum(1 for h in headings if h.subtree <= 1),
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
        single = [h for h in headings if h.subtree <= 1]
        if len(single) >= 3 and len(single) / len(headings) >= 0.5:
            findings.append({"check": "tek_paragraf_bolum",
                             "text": f"{len(headings)} başlığın {len(single)}'i altında en fazla bir paragraf var: bölme testini uygula."})

    deep = [h for h in headings if h.level >= 4]
    if deep:
        findings.append({"check": "derin_baslik",
                         "text": f"{len(deep)} dördüncü veya daha derin düzey başlık: derinlik testini uygula."})
    level3 = [h for h in headings if h.level == 3]
    if len(level3) >= 3 and all(h.subtree <= 1 for h in level3):
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
        first = heading.first_sentence
        # A first sentence that reuses the heading's words but delivers a number,
        # or is long enough to carry content, is using the concept, not restating it.
        restates = (
            stems and len(shared) >= 2 and not re.search(r"\d", first)
            and (len(first.split()) <= 8 or lowered_matches_any(first, ("onem", "savunma")))
        )
        if restates:
            findings.append({"check": "baslik_tekrari",
                             "text": f"\"{heading.text}\" başlığı ilk cümlede yalnızca yineleniyor olabilir ({', '.join(sorted(shared))}); cümle yeni bilgi taşıyor mu?"})

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
        "ceviri_golgesi": translationese_summary(doc, hits),
        "ceviri": translationese_checks(doc, hits),
        "soylem_olculeri": discourse_summary(doc, hits),
        "soylem": discourse_checks(doc, hits),
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
            introduced.append({"category": key[0], "label": LABELS[key[0]], "level": LEVELS[key[0]],
                               "count": extra, "example": examples[key]})
    introduced_hard = [item for item in introduced if item["level"] == "sert"]
    introduced_context = [item for item in introduced if item["level"] != "sert"]

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
    src_tr = source_report["ceviri_golgesi"]
    out_tr = output_report["ceviri_golgesi"]
    translationese_delta = {
        key: {"kaynak": src_tr[key], "çıktı": out_tr[key]}  # type: ignore[index]
        for key in TRANSLATIONESE_LABELS
        if src_tr[key] != out_tr[key]  # type: ignore[index]
    }
    source_tr_checks = {s["check"] for s in source_report["ceviri"]}  # type: ignore[union-attr]
    new_translationese = [f["text"] for f in output_report["ceviri"]  # type: ignore[union-attr]
                          if f["check"] not in source_tr_checks]
    source_ds_checks = {s["check"] for s in source_report["soylem"]}  # type: ignore[union-attr]
    new_discourse = [f["text"] for f in output_report["soylem"]  # type: ignore[union-attr]
                     if f["check"] not in source_ds_checks]
    src_ds = source_report["soylem_olculeri"]
    out_ds = output_report["soylem_olculeri"]
    discourse_delta = {
        key: {"kaynak": src_ds[key], "çıktı": out_ds[key]}  # type: ignore[index]
        for key in DISCOURSE_LABELS
        if src_ds[key] != out_ds[key]  # type: ignore[index]
    }
    return {"introduced": introduced, "introduced_hard": introduced_hard,
            "introduced_context": introduced_context, "remaining": remaining, "removed": removed,
            "structure_delta": structure_delta, "introduced_structure": new_structure,
            "translationese_delta": translationese_delta, "introduced_translationese": new_translationese,
            "discourse_delta": discourse_delta, "introduced_discourse": new_discourse}


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
TRANSLATIONESE_LABELS = {
    "sahip_olmak": "sahip olmak", "varlik_kalibi": "varlık kalıbı", "cerceve_yigini": "çerçeve yığını",
    "olan_zinciri": "olan zinciri", "tekrarlanan_cumle_baslangici": "tekrarlanan cümle başlangıcı", "ve_zinciri": "ve zinciri",
    "fiilimsi_yigini": "fiilimsi yığını", "iyelik_zinciri": "iyelik zinciri",
    "baglac_baslangici": "bağlaçla başlayan cümle", "bir_per_100": "bir / 100 sözcük",
}
DISCOURSE_LABELS = {
    "kiplik": "çekince işareti", "pekistirici": "pekiştirici", "hafif_fiil": "hafif fiil",
    "kiplik_yigini": "kiplik yığını", "pekistirici_catismasi": "pekiştirici çatışması",
    "kip_nobetlesmesi": "kip nöbetleşmesi", "edilgen_adlastirma": "edilgen adlaştırma",
    "aktarim_sonrasi_sonuc": "aktarım sonrası sonuç", "ilgec_yogunlugu": "ilgeç yoğunluğu",
    "esanlam_kaymasi": "eş anlamlı kayması", "konu_sifirlama": "konu sıfırlama",
    "parantez_yuku": "parantez yükü", "kayit_kaymasi": "kayıt kayması",
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

    translationese: dict[str, object] = report["ceviri_golgesi"]  # type: ignore[assignment]
    print("\nÇeviri gölgesi ölçüleri: " + " | ".join(
        f"{TRANSLATIONESE_LABELS[k]}: {v}" for k, v in translationese.items()))
    ceviri: list[dict[str, object]] = report["ceviri"]  # type: ignore[assignment]
    if ceviri:
        print("[Çeviri gölgesi · inceleme]")
        for finding in ceviri:
            print(f"  - {finding['text']}")

    discourse: dict[str, object] = report["soylem_olculeri"]  # type: ignore[assignment]
    print("\nSöylem ölçüleri (kanıt, sözcük uyumu, tutarlılık): " + " | ".join(
        f"{DISCOURSE_LABELS[k]}: {v}" for k, v in discourse.items() if v))
    soylem: list[dict[str, object]] = report["soylem"]  # type: ignore[assignment]
    if soylem:
        print("[Söylem · inceleme]")
        for finding in soylem:
            print(f"  - {finding['text']}")

    if comparison is not None:
        print(f"\nKaynakla karşılaştırma ({source_path}):")
        introduced = comparison["introduced"]
        remaining = comparison["remaining"]
        removed = comparison["removed"]
        if comparison["introduced_hard"]:
            print("  Kaynakta olmayıp çıktıda beliren SERT kalıplar (deterministik hata adayı; dolgu başka dolguya çevrilmiş olabilir):")
            for item in comparison["introduced_hard"]:  # type: ignore[union-attr]
                print(f"    - {item['label']}: +{item['count']} «{item['example']}»")
        if comparison["introduced_context"]:
            print("  Kaynakta olmayıp çıktıda beliren bağlamsal kalıplar (uyarı; işlevini incele):")
            for item in comparison["introduced_context"]:  # type: ignore[union-attr]
                print(f"    - {item['label']}: +{item['count']} «{item['example']}»")
        if not introduced:
            print("  Çıktı kaynakta bulunmayan bir kalıp eklememiş.")
        if comparison["introduced_structure"]:
            print("  Kaynakta olmayıp çıktıda beliren yapı bulguları:")
            for text in comparison["introduced_structure"]:  # type: ignore[union-attr]
                print(f"    - {text}")
        if comparison["structure_delta"]:
            print("  Yapı ölçülerindeki değişim:")
            for key, pair in comparison["structure_delta"].items():  # type: ignore[union-attr]
                print(f"    - {SUMMARY_LABELS[key]}: {pair['kaynak']} → {pair['çıktı']}")
        if comparison["introduced_translationese"]:
            print("  Kaynakta olmayıp çıktıda beliren çeviri gölgesi bulguları (uyarı; aşırı düzeltme veya yeni kalkı olabilir):")
            for text in comparison["introduced_translationese"]:  # type: ignore[union-attr]
                print(f"    - {text}")
        if comparison["translationese_delta"]:
            print("  Çeviri gölgesi ölçülerindeki değişim:")
            for key, pair in comparison["translationese_delta"].items():  # type: ignore[union-attr]
                print(f"    - {TRANSLATIONESE_LABELS[key]}: {pair['kaynak']} → {pair['çıktı']}")
        if comparison["introduced_discourse"]:
            print("  Kaynakta olmayıp çıktıda beliren söylem bulguları (uyarı; kanıt düzeyi, sözcük uyumu veya tutarlılık değişmiş olabilir):")
            for text in comparison["introduced_discourse"]:  # type: ignore[union-attr]
                print(f"    - {text}")
        if comparison["discourse_delta"]:
            print("  Söylem ölçülerindeki değişim:")
            for key, pair in comparison["discourse_delta"].items():  # type: ignore[union-attr]
                print(f"    - {DISCOURSE_LABELS[key]}: {pair['kaynak']} → {pair['çıktı']}")
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
          "yapı bulguları için \"bu sınır kavramsal mı?\", çeviri gölgesi bulguları için "
          "\"bu yapı Türkçede bağımsız olarak doğal mı, yoksa gizli İngilizce cümle mi dayatıyor?\", "
          "söylem bulguları için \"kim biliyor, nasıl biliyor, ne kadar kesin; sözcükler doğal mı birleşiyor; "
          "cümle öncekinden mi büyüyor?\" sorusunu sor.")


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

NESTED_TEXT = """## Yöntem

### Veri

Analizde 2024 yılına ait 1.200 kayıt kullanılmıştır. Kayıtların %12'si eksik değer içermektedir ve bunlar komşu ölçümlerin ortalamasıyla doldurulmuştur. Ön denemelerde bu yöntem medyanla doldurmaya göre doğrulama hatasını %2 azaltmıştır.

Doldurma yalnızca 10 dakikadan kısa boşluklara uygulanmıştır; daha uzun boşluklu kayıtlar çıkarılmıştır. Çıkarılan kayıtların dağılımı Ek A'da verilmiştir.

### Gruplar

Kayıtlar teslim süresine göre üç gruba ayrılmıştır: 2 günden kısa, 2 ile 5 gün arası ve 5 günden uzun teslimatlar. Gruplar şirketin hizmet düzeyi sınıflarıyla örtüştüğü için seçilmiştir. Eşikler analiz boyunca sabit tutulmuştur. Eşik değişikliğinin sonuçlara etkisi ayrıca sınanmamıştır.

Grup büyüklükleri sırasıyla 410, 520 ve 270 kayıttır. En küçük grup bile ayrı raporlama için yeterli sayılmıştır. Gruplar arasında kayıt geçişi yoktur.

### Doğrulama sonuçları

Doğrulama sonuçlarında ortalama hata %3'tür. En yüksek hata 5 günden uzun teslimat grubunda görülmüştür; bu grupta hata %5'e çıkmaktadır. Diğer iki grupta hata %3'ün altında kalmıştır.

Hata dağılımı üç grupta da tek tepeli olduğundan medyan ve ortalama birbirine yakındır. Aykırı değer temizliği yapılmamıştır.
"""

TRANSLATED_TEXT = """Bu, bir sensörden gelen bir veri akışını bir filtreden geçiren bir yöntemdir. Bu yöntem yüksek bir hesaplama maliyetine sahiptir. Bu yöntem üç katmana sahip olan bir model kullanmaktadır. Bu yöntem ayrıca bir hata günlüğüne sahiptir. Tabloda üç farklı hata türü bulunmaktadır.

Bu bağlamda, performans açısından, yöntem kapsamında değerlendirilmesi gereken temel husus bellek kullanımı noktasında ortaya çıkan artıştır. Yüksek doğruluğa sahip olan ve düşük gecikmeye sahip olan filtre, gerçek zamanlı sistemler için uygun olan bir seçenektir. Yöntemin performansının değerlendirilmesinin yapılmasının gerekliliği ortaya çıkmaktadır.

Sensör veriyi okur ve veriyi filtreler ve filtrelenmiş veriyi denetleyiciye gönderir ve denetleyici komut üretir. Ekip veriyi toplayıp temizleyip ölçekleyip bölüp modeli eğitip doğrulayıp raporlamıştır. Bununla birlikte, hata birikmektedir. Buna ek olarak, süre artmaktadır. Bu nedenle, düzeltme gerekmektedir. Bu yöntem, bir temel olarak hizmet etmektedir.
"""

NATIVE_TEXT = """Yöntem maliyet açısından ucuz, süre açısından pahalıdır: lisans yıllık 4.000 lira, kurulum altı haftadır. Sıcaklığı 40 °C'nin üzerinde olan sensörler devre dışı bırakıldı; kalan 18 sensörün verisi analize alındı. Yeni yöntem konum hatasını %12 düşürdü ve hesaplama süresini %30 artırdı. Şirket üç fabrikaya sahiptir ve bu fabrikaların ikisi Bursa'dadır.

Filtre ölçümü alır. Gözlemci durumu günceller. Filtre kazancı yeniden hesaplar. Ekip veriyi toplayıp temizledikten sonra modeli eğitti; eğitim 3 saat sürdü. Bir sonraki sürüm için tarih verilmedi.
"""

DISCOURSE_TEXT = """Bu farkın muhtemelen örneklem büyüklüğünden kaynaklanıyor olabileceği düşünülebilir. Sonuçlar, etkinin açıkça var olabileceğini güçlü biçimde düşündürmektedir. Çalışan görüşmelerinde manuel girişin hataları artırdığı belirtildi. İade oranı %6,2 idi. Bu nedenle manuel giriş hataları artırmaktadır.

Örnekler üç kaynaktan toplandı. Ardından aykırı değerlerden temizlenmiştir. Model bu veriyle eğitilmektedir. Eğitim 18 dakika sürüyor. Sonuçlar tabloda verilir. Kontrollerin düzenli biçimde gerçekleştirilmesinin sağlanması planlanmaktadır.

Bu çalışmada önerilen yöntem üç sensörü birleştirir. Bu yaklaşım kalibrasyon gerektirmez; yapı 20 ms gecikmeyle çalışır ve çözüm gömülü platformlara uygundur. Rapor, gecikmeler hakkında ilişkin bulguları tedarikçilere yönelik olarak sunmaktadır. Ekip bir değerlendirme gerçekleştirmiş ve analiz gerçekleştirilmiştir.

Bu çalışmada model — üç katmanlı olan — ilk koşulda (ki en zor olanıdır) kararlı davranır. İşin ilginç yanı sonuçların beklenen eğilimden ayrılmasıdır. Bu kapsamda söz konusu parametrenin kritik önem arz ettiği görülmektedir.
"""

FILLER_SOURCE = "Model 120. derecede en düşük hatayı verdi. Bu sonuç derece seçiminin kritik önemini ortaya koymaktadır."
FILLER_TRANSLATED = "Model 120. derecede en düşük hatayı verdi. Sonuç olarak derece seçimi önemli bir etkendir; bu bulgu derece seçiminin önemini bir kez daha ortaya koymaktadır."
CONTEXT_ONLY = "Yani model 120. derecede en düşük hatayı verdi; öte yandan derece seçimi kritik önemini korumaktadır."
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
    if not translated["introduced_hard"]:
        raise SystemExit("Öz sınama: dolguyu dolguya çeviren çıktı 'yeni sert kalıp' olarak işaretlenmedi")
    context_only = compare(src, analyse(CONTEXT_ONLY))
    if context_only["introduced_hard"] or not context_only["introduced_context"]:
        raise SystemExit("Öz sınama: yalnızca bağlamsal kalıp ekleyen çıktı sert/bağlam ayrımında yanlış sınıflandı")
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

    nested = analyse(NESTED_TEXT)
    summary = nested["structure_summary"]
    if summary["one_paragraph_sections"] != 0:  # type: ignore[index]
        raise SystemExit(f"Öz sınama: alt bölümleri dolu üst başlık tek paragraflık bölüm sayıldı: {summary}")
    if nested["structure"]:
        raise SystemExit(f"Öz sınama: iç içe başlıklı sağlıklı belgede yapı bulgusu üretildi: {nested['structure']}")
    doc = parse(NESTED_TEXT)
    if doc.headings[0].direct != 0 or doc.headings[0].subtree != 6 or doc.headings[1].parent != 0:
        raise SystemExit("Öz sınama: başlık ağacı sayımı hatalı")

    if tr_lower("İSTANBUL IŞIK") != "istanbul ışık":
        raise SystemExit("Öz sınama: Türkçe küçük harf dönüşümü hatalı")

    translated = analyse(TRANSLATED_TEXT)
    expected_tr = {"sahip", "varlik", "kalki", "bos_ozne"}
    missing = expected_tr - set(translated["per_category"])  # type: ignore[arg-type]
    if missing:
        raise SystemExit(f"Öz sınama: çeviri metninde beklenen aileler bulunamadı: {sorted(missing)}")
    if translated["hard_hits"] != 0:
        raise SystemExit(f"Öz sınama: çeviri gölgesi aileleri sert bastırma sayıldı: {translated['hits']}")
    checks = {f["check"] for f in translated["ceviri"]}  # type: ignore[union-attr]
    for check in ("cerceve_yigini", "olan_zinciri", "bir_yogunlugu", "ve_zinciri", "fiilimsi_yigini",
                  "iyelik_zinciri", "tekrarlanan_cumle_baslangici", "baglac_yogunlugu", "gosterme_ritmi"):
        if check not in checks:
            raise SystemExit(f"Öz sınama: çeviri metninde beklenen çeviri gölgesi bulgusu yok: {check}")
    summary = translated["ceviri_golgesi"]
    if summary["bir_per_100"] <= BIR_PER_100_MAX or summary["fiilimsi_yigini"] != 1 or summary["ve_zinciri"] != 1:  # type: ignore[index]
        raise SystemExit(f"Öz sınama: çeviri gölgesi ölçüleri hatalı: {summary}")

    for label, text in (("yerli", NATIVE_TEXT), ("temiz", CLEAN_TEXT), ("iyi yapılı", WELL_STRUCTURED_TEXT), ("iç içe", NESTED_TEXT)):
        report = analyse(text)
        if report["ceviri"]:
            raise SystemExit(f"Öz sınama: {label} metinde çeviri gölgesi bulgusu üretildi (yanlış pozitif): {report['ceviri']}")
    native = analyse(NATIVE_TEXT)
    if native["ceviri_golgesi"]["sahip_olmak"] != 1:  # type: ignore[index]
        raise SystemExit("Öz sınama: gerçek mülkiyet bildiren tek 'sahip' bir kez işaretlenmeli, reddedilmemeli")
    if native["ceviri_golgesi"]["tekrarlanan_cumle_baslangici"] != 0:  # type: ignore[index]
        raise SystemExit("Öz sınama: dönüşümlü özneler tekrarlanan cümle başlangıcı sayıldı")
    if native["structure"]:
        raise SystemExit(f"Öz sınama: yerli metinde yapı bulgusu üretildi: {native['structure']}")

    repaired_tr = compare(translated, native)
    if repaired_tr["introduced_translationese"]:
        raise SystemExit("Öz sınama: yerli çıktı yeni çeviri gölgesi bulgusu üretti")
    if repaired_tr["translationese_delta"].get("cerceve_yigini", {}).get("çıktı") != 0:  # type: ignore[union-attr]
        raise SystemExit("Öz sınama: çeviri gölgesi ölçü değişimi çerçeve yığınını yanlış raporladı")
    if converb_count(["ekip", "toplayıp", "yaprak", "okuyarak", "gerek"]) != 2:
        raise SystemExit("Öz sınama: fiilimsi sayımı durak listesini yanlış uyguladı")
    if longest_genitive_run(["yöntemin", "performansının", "değerlendirilmesinin", "yapılmasının"]) != 4:
        raise SystemExit("Öz sınama: iyelik zinciri sayımı hatalı")
    if longest_genitive_run(["bunun", "için", "metin", "uzun"]) != 1:
        raise SystemExit("Öz sınama: iyelik zinciri durak listesi hatalı")

    discourse = analyse(DISCOURSE_TEXT)
    expected_ds = {"kiplik", "pekistirici", "aktarim", "hafif_fiil"}
    missing = expected_ds - set(discourse["per_category"])  # type: ignore[arg-type]
    if missing:
        raise SystemExit(f"Öz sınama: söylem metninde beklenen aileler bulunamadı: {sorted(missing)}")
    checks = {f["check"] for f in discourse["soylem"]}  # type: ignore[union-attr]
    for check in ("kiplik_yigini", "pekistirici_catismasi", "aktarim_sonrasi_sonuc", "kip_nobetlesmesi",
                  "edilgen_adlastirma", "esanlam_kaymasi", "ilgec_yogunlugu", "konu_sifirlama",
                  "parantez_yuku", "kayit_kaymasi"):
        if check not in checks:
            raise SystemExit(f"Öz sınama: söylem metninde beklenen bulgu yok: {check}")
    for label, text in (("yerli", NATIVE_TEXT), ("temiz", CLEAN_TEXT), ("iyi yapılı", WELL_STRUCTURED_TEXT), ("iç içe", NESTED_TEXT)):
        report = analyse(text)
        if report["soylem"]:
            raise SystemExit(f"Öz sınama: {label} metinde söylem bulgusu üretildi (yanlış pozitif): {report['soylem']}")
    if tense_class(Sentence(1, 1, "Deney 100 örnek üzerinde yürütüldü.")) != "dı":
        raise SystemExit("Öz sınama: kip sınıfı -dı tanınmadı")
    if tense_class(Sentence(1, 1, "Sonuç önemlidir.")) is not None or tense_class(Sentence(1, 1, "Üç sensörler.")) is not None:
        raise SystemExit("Öz sınama: koşaç ya da çoğul ad kip sınıfı sayıldı")
    if tense_class(Sentence(1, 1, "Model kararsız davranır.")) != "r":
        raise SystemExit("Öz sınama: geniş zaman tanınmadı")
    repaired_ds = compare(discourse, analyse(WELL_STRUCTURED_TEXT))
    if repaired_ds["introduced_discourse"]:
        raise SystemExit("Öz sınama: iyi yapılı çıktı yeni söylem bulgusu üretti")

    print("Stil denetimi öz sınaması geçti (yapay metin, parçalanmış belge, temiz metin, iyi yapılı belge, iç içe başlıklar, sert/bağlam ayrımı, dolgu silme, çeviri gölgesi, yerli metin, söylem sinyalleri).")


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
    parser.add_argument("--fail-on-introduced-hard", "--fail-on-introduced", dest="fail_on_introduced_hard",
                        action="store_true",
                        help="Çıktı kaynakta olmayan bir SERT bastırma kalıbı eklemişse 1 ile çık; bağlamsal aileler yalnızca uyarır (yalnızca --source ile)")
    parser.add_argument("--fail-on-introduced-any", action="store_true",
                        help="Bağlamsal aileler dahil, kaynakta olmayan herhangi bir kalıp eklenmişse 1 ile çık (katı mod)")
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

    if comparison is not None:
        if args.fail_on_introduced_any and comparison["introduced"]:
            return 1
        if args.fail_on_introduced_hard and comparison["introduced_hard"]:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
