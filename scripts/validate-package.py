#!/usr/bin/env python3
"""Validate the portable Metinoskop package without external dependencies."""

from __future__ import annotations

import ast
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CURRENT_VERSION = "0.4.1"
REQUIRED_FILES = (
    ".gitattributes",
    ".gitignore",
    ".github/workflows/validate.yml",
    "SKILL.md",
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    "NOTICE",
    "agents/openai.yaml",
    "references/akicilik.md",
    "references/kavramsal-girisler.md",
    "references/rapor-yazimi.md",
    "references/retorik-yapilar.md",
    "references/turkce-oruntuler.md",
    "references/turkce-ritim-ve-ceviri-kokusu.md",
    "references/kanit-ve-kesinlik.md",
    "references/sozcuk-birlesimleri.md",
    "references/metinsel-tutarlilik.md",
    "references/zamansal-ankraj-ve-rapor-kipi.md",
    "references/yapisal-butunluk.md",
    "evals/README.md",
    "evals/akademik.md",
    "evals/belirsizlik.md",
    "evals/bicim-koruma.md",
    "evals/hukuki.md",
    "evals/kapsam-ve-kosul.md",
    "evals/kurumsal.md",
    "evals/kisisel.md",
    "evals/kaynak-sadakati.md",
    "evals/kavramsal-giris.md",
    "evals/degisiklik-butcesi.md",
    "evals/rapor-bulgu-yorum-oneri.md",
    "evals/rapor-yapisal-butunluk.md",
    "evals/teknik.md",
    "evals/uslup-eslestirme.md",
    "evals/yonetici-ozeti.md",
    "evals/savunmaci-akademik.md",
    "evals/iddia-tekrar-dongusu.md",
    "evals/yol-haritasi.md",
    "evals/yapay-denge.md",
    "evals/giris-hunisi.md",
    "evals/sonuc-ve-gelecek-calisma.md",
    "evals/soyut-yuklem.md",
    "evals/paragraf-simetrisi.md",
    "evals/gerekli-ifade.md",
    "evals/iyi-metin.md",
    "evals/egitsel-aciklama.md",
    "evals/asiri-bolumleme.md",
    "evals/derin-baslik.md",
    "evals/tek-paragraf-bolumler.md",
    "evals/kisa-paragraf-yigini.md",
    "evals/yapay-gerilim.md",
    "evals/tekrarlanan-bolum-girisleri.md",
    "evals/tekrarlanan-bolum-sonuclari.md",
    "evals/asiri-capraz-gonderme.md",
    "evals/uzun-cerceve-ifadeleri.md",
    "evals/ayrilmis-kanit.md",
    "evals/gereksiz-listeleme.md",
    "evals/korunacak-basliklar.md",
    "evals/yontem-ayrimi.md",
    "evals/uzun-paragraf-korunur.md",
    "evals/kisa-paragraf-korunur.md",
    "evals/yapisal-iyi-metin.md",
    "evals/tekrarlanan-acik-ozne.md",
    "evals/bu-sonuc-ritmi.md",
    "evals/asiri-bir.md",
    "evals/sahip-olmak-kalkisi.md",
    "evals/bulunmaktadir-kalkisi.md",
    "evals/ve-zinciri.md",
    "evals/dogal-ve-korunur.md",
    "evals/yararli-ip-yapisi.md",
    "evals/asiri-ip-zinciri.md",
    "evals/art-niteleme.md",
    "evals/gerekli-olan.md",
    "evals/gereksiz-olan.md",
    "evals/cerceve-yigini.md",
    "evals/gerekli-acisindan.md",
    "evals/soyut-ad-yuklemi.md",
    "evals/teknik-adlastirma-korunur.md",
    "evals/ozne-dusurme-akisi.md",
    "evals/belirsizlik-icin-acik-ozne.md",
    "evals/dogal-uzun-cumle-korunur.md",
    "evals/asiri-yuklu-cumle.md",
    "evals/ingilizce-soylem-belirtecleri.md",
    "evals/hukuki-kalip-korunur.md",
    "evals/teknik-ozne-tekrari-korunur.md",
    "evals/yerli-turkce-metin.md",
    "evals/edilgen-korunur.md",
    "evals/edilgen-etkene.md",
    "evals/bilinmeyen-aktor.md",
    "evals/aktarim-olgu-olmaz.md",
    "evals/olcum-ile-cikarim.md",
    "evals/cekince-korunur.md",
    "evals/kiplik-yigini.md",
    "evals/dayanaksiz-pekistirici.md",
    "evals/mesru-guclu-iddia.md",
    "evals/gerekceli-kip-degisimi.md",
    "evals/uslup-kip-nobetlesmesi.md",
    "evals/oneri-karar-degil.md",
    "evals/karar-uygulama-degil.md",
    "evals/gozlenmedi-yoktur-degil.md",
    "evals/atif-kapsami.md",
    "evals/kapsam-isareti-baglanmasi.md",
    "evals/sonuc-sonuclardan-guclu.md",
    "evals/iyi-akademik-paragraf.md",
    "evals/tuhaf-esdizim.md",
    "evals/teknik-esdizim-korunur.md",
    "evals/yanlis-hal-cercevesi.md",
    "evals/dogru-alisilmadik-hal.md",
    "evals/edat-aktarimi.md",
    "evals/hafif-fiil-sismesi.md",
    "evals/surec-adi-korunur.md",
    "evals/genel-fiil-kesin-iliski.md",
    "evals/epistemik-guvensiz-fiil.md",
    "evals/esanlam-kaymasi-teknik.md",
    "evals/kanonik-terim-tekrari.md",
    "evals/varlik-yeniden-adlandirma.md",
    "evals/hukuki-formul-korunur.md",
    "evals/dogal-is-epostasi.md",
    "evals/odunc-terim-korunur.md",
    "evals/olgu-yigini.md",
    "evals/sabit-konu-korunur.md",
    "evals/dogrusal-ilerleyis-korunur.md",
    "evals/desteksiz-bu-nedenle.md",
    "evals/gecerli-nedensel-baglac.md",
    "evals/esanlam-donusu.md",
    "evals/gerekli-ad-tekrari.md",
    "evals/uzak-bu.md",
    "evals/kisa-mesafe-eksilti.md",
    "evals/bolum-basi-sifirlama.md",
    "evals/temiz-devir.md",
    "evals/islev-kaymasi.md",
    "evals/kronoloji-nedensellik.md",
    "evals/kapsam-isareti-tasinmasi.md",
    "evals/olumsuzluk-kapsami.md",
    "evals/kayit-kaymasi.md",
    "evals/bilincli-kayit-degisimi.md",
    "evals/ingilizce-noktalama.md",
    "evals/teknik-noktalama-korunur.md",
    "evals/uzak-sinirlilik.md",
    "evals/ayni-iddia-yeni-rol.md",
    "evals/ayni-iddia-hacim.md",
    "evals/tutarli-metin-korunur.md",
    "evals/raporda-genis-zaman-yigini.md",
    "evals/bu-calisma-inceler.md",
    "evals/sonuclarda-genis-zaman.md",
    "evals/tarihli-olay-genis-zaman.md",
    "evals/metot-uygulamasi-gecmis.md",
    "evals/algoritma-genel-davranis-korunur.md",
    "evals/bilimsel-genelleme-korunur.md",
    "evals/prosedur-kilavuz-korunur.md",
    "evals/teknik-sistem-davranisi-korunur.md",
    "evals/metot-ve-uygulama-ayrimi.md",
    "evals/sonuc-ve-yorum-kip-ayrimi.md",
    "evals/tablo-sekil-zaman-korunur.md",
    "evals/durum-raporu-uc-zaman.md",
    "evals/gecmise-zorlama-yok.md",
    "evals/her-seyi-edildi-yapma.md",
    "evals/mistir-yigini-yapma.md",
    "evals/gecmis-genel-yasa-bozmasin.md",
    "evals/tetikleyici-iceren-sozcuk-korunur.md",
    "evals/periyodik-takvim-genis-zaman-korunur.md",
    "evals/gecmiste-surme-korunur.md",
    "evals/once-tamamlanmis-olay-korunur.md",
    "evals/gecmis-aliskanlik-korunur.md",
    "evals/sirali-olayda-misti-yigini.md",
    "evals/repo-guncel-davranis-yor.md",
    "evals/sonuc-guncel-yorum-yor.md",
    "evals/genel-gereklilik-genis-zaman-korunur.md",
    "evals/tablo-sekil-guncel-islev-yor.md",
    "evals/bulgu-guncel-yorum-yor.md",
    "evals/mevcut-durum-yor.md",
    "evals/burokratik-simdiki-zaman.md",
    "evals/normatif-yasak-genis-zaman-korunur.md",
    "evals/karisik-zaman-readme.md",
    "evals/yerel-hata-genel-kural-ayrimi.md",
    "evals/framework-kalkisi.md",
    "evals/campaign-kalkisi.md",
    "evals/capture-kalkisi.md",
    "evals/drive-kalkisi.md",
    "evals/enable-kalkisi.md",
    "evals/address-kalkisi.md",
    "evals/provide-kalkisi.md",
    "evals/deneyimlemek-kalkisi.md",
    "evals/ortaya-koymak-yigini.md",
    "evals/elde-etmek-olcum.md",
    "evals/referans-cercevesi-korunur.md",
    "evals/kuramsal-cerceve-korunur.md",
    "evals/yazilim-cercevesi-korunur.md",
    "evals/reklam-kampanyasi-korunur.md",
    "evals/yardim-kampanyasi-korunur.md",
    "evals/test-kampanyasi-alan-terimi.md",
    "evals/bellek-adresleme-korunur.md",
    "evals/hipotezi-desteklemek-korunur.md",
    "evals/davranisi-yakalamak-alan-terimi-korunur.md",
    "evals/erisim-saglamak-korunur.md",
    "scripts/eval-runner.py",
    "scripts/eval-suite.py",
    "scripts/style-lint.py",
    "scripts/validate-package.py",
    "scripts/behavioral-regression.py",
    ".github/workflows/behavioral.yml",
    "evals/critical-cases.txt",
)
EVAL_FILES = (
    "evals/akademik.md",
    "evals/belirsizlik.md",
    "evals/bicim-koruma.md",
    "evals/hukuki.md",
    "evals/kapsam-ve-kosul.md",
    "evals/kurumsal.md",
    "evals/kisisel.md",
    "evals/kaynak-sadakati.md",
    "evals/kavramsal-giris.md",
    "evals/degisiklik-butcesi.md",
    "evals/rapor-bulgu-yorum-oneri.md",
    "evals/rapor-yapisal-butunluk.md",
    "evals/teknik.md",
    "evals/uslup-eslestirme.md",
    "evals/yonetici-ozeti.md",
    "evals/savunmaci-akademik.md",
    "evals/iddia-tekrar-dongusu.md",
    "evals/yol-haritasi.md",
    "evals/yapay-denge.md",
    "evals/giris-hunisi.md",
    "evals/sonuc-ve-gelecek-calisma.md",
    "evals/soyut-yuklem.md",
    "evals/paragraf-simetrisi.md",
    "evals/gerekli-ifade.md",
    "evals/iyi-metin.md",
    "evals/egitsel-aciklama.md",
    "evals/asiri-bolumleme.md",
    "evals/derin-baslik.md",
    "evals/tek-paragraf-bolumler.md",
    "evals/kisa-paragraf-yigini.md",
    "evals/yapay-gerilim.md",
    "evals/tekrarlanan-bolum-girisleri.md",
    "evals/tekrarlanan-bolum-sonuclari.md",
    "evals/asiri-capraz-gonderme.md",
    "evals/uzun-cerceve-ifadeleri.md",
    "evals/ayrilmis-kanit.md",
    "evals/gereksiz-listeleme.md",
    "evals/korunacak-basliklar.md",
    "evals/yontem-ayrimi.md",
    "evals/uzun-paragraf-korunur.md",
    "evals/kisa-paragraf-korunur.md",
    "evals/yapisal-iyi-metin.md",
    "evals/tekrarlanan-acik-ozne.md",
    "evals/bu-sonuc-ritmi.md",
    "evals/asiri-bir.md",
    "evals/sahip-olmak-kalkisi.md",
    "evals/bulunmaktadir-kalkisi.md",
    "evals/ve-zinciri.md",
    "evals/dogal-ve-korunur.md",
    "evals/yararli-ip-yapisi.md",
    "evals/asiri-ip-zinciri.md",
    "evals/art-niteleme.md",
    "evals/gerekli-olan.md",
    "evals/gereksiz-olan.md",
    "evals/cerceve-yigini.md",
    "evals/gerekli-acisindan.md",
    "evals/soyut-ad-yuklemi.md",
    "evals/teknik-adlastirma-korunur.md",
    "evals/ozne-dusurme-akisi.md",
    "evals/belirsizlik-icin-acik-ozne.md",
    "evals/dogal-uzun-cumle-korunur.md",
    "evals/asiri-yuklu-cumle.md",
    "evals/ingilizce-soylem-belirtecleri.md",
    "evals/hukuki-kalip-korunur.md",
    "evals/teknik-ozne-tekrari-korunur.md",
    "evals/yerli-turkce-metin.md",
    "evals/edilgen-korunur.md",
    "evals/edilgen-etkene.md",
    "evals/bilinmeyen-aktor.md",
    "evals/aktarim-olgu-olmaz.md",
    "evals/olcum-ile-cikarim.md",
    "evals/cekince-korunur.md",
    "evals/kiplik-yigini.md",
    "evals/dayanaksiz-pekistirici.md",
    "evals/mesru-guclu-iddia.md",
    "evals/gerekceli-kip-degisimi.md",
    "evals/uslup-kip-nobetlesmesi.md",
    "evals/oneri-karar-degil.md",
    "evals/karar-uygulama-degil.md",
    "evals/gozlenmedi-yoktur-degil.md",
    "evals/atif-kapsami.md",
    "evals/kapsam-isareti-baglanmasi.md",
    "evals/sonuc-sonuclardan-guclu.md",
    "evals/iyi-akademik-paragraf.md",
    "evals/tuhaf-esdizim.md",
    "evals/teknik-esdizim-korunur.md",
    "evals/yanlis-hal-cercevesi.md",
    "evals/dogru-alisilmadik-hal.md",
    "evals/edat-aktarimi.md",
    "evals/hafif-fiil-sismesi.md",
    "evals/surec-adi-korunur.md",
    "evals/genel-fiil-kesin-iliski.md",
    "evals/epistemik-guvensiz-fiil.md",
    "evals/esanlam-kaymasi-teknik.md",
    "evals/kanonik-terim-tekrari.md",
    "evals/varlik-yeniden-adlandirma.md",
    "evals/hukuki-formul-korunur.md",
    "evals/dogal-is-epostasi.md",
    "evals/odunc-terim-korunur.md",
    "evals/olgu-yigini.md",
    "evals/sabit-konu-korunur.md",
    "evals/dogrusal-ilerleyis-korunur.md",
    "evals/desteksiz-bu-nedenle.md",
    "evals/gecerli-nedensel-baglac.md",
    "evals/esanlam-donusu.md",
    "evals/gerekli-ad-tekrari.md",
    "evals/uzak-bu.md",
    "evals/kisa-mesafe-eksilti.md",
    "evals/bolum-basi-sifirlama.md",
    "evals/temiz-devir.md",
    "evals/islev-kaymasi.md",
    "evals/kronoloji-nedensellik.md",
    "evals/kapsam-isareti-tasinmasi.md",
    "evals/olumsuzluk-kapsami.md",
    "evals/kayit-kaymasi.md",
    "evals/bilincli-kayit-degisimi.md",
    "evals/ingilizce-noktalama.md",
    "evals/teknik-noktalama-korunur.md",
    "evals/uzak-sinirlilik.md",
    "evals/ayni-iddia-yeni-rol.md",
    "evals/ayni-iddia-hacim.md",
    "evals/tutarli-metin-korunur.md",
    "evals/raporda-genis-zaman-yigini.md",
    "evals/bu-calisma-inceler.md",
    "evals/sonuclarda-genis-zaman.md",
    "evals/tarihli-olay-genis-zaman.md",
    "evals/metot-uygulamasi-gecmis.md",
    "evals/algoritma-genel-davranis-korunur.md",
    "evals/bilimsel-genelleme-korunur.md",
    "evals/prosedur-kilavuz-korunur.md",
    "evals/teknik-sistem-davranisi-korunur.md",
    "evals/metot-ve-uygulama-ayrimi.md",
    "evals/sonuc-ve-yorum-kip-ayrimi.md",
    "evals/tablo-sekil-zaman-korunur.md",
    "evals/durum-raporu-uc-zaman.md",
    "evals/gecmise-zorlama-yok.md",
    "evals/her-seyi-edildi-yapma.md",
    "evals/mistir-yigini-yapma.md",
    "evals/gecmis-genel-yasa-bozmasin.md",
    "evals/tetikleyici-iceren-sozcuk-korunur.md",
    "evals/periyodik-takvim-genis-zaman-korunur.md",
    "evals/gecmiste-surme-korunur.md",
    "evals/once-tamamlanmis-olay-korunur.md",
    "evals/gecmis-aliskanlik-korunur.md",
    "evals/sirali-olayda-misti-yigini.md",
    "evals/repo-guncel-davranis-yor.md",
    "evals/sonuc-guncel-yorum-yor.md",
    "evals/genel-gereklilik-genis-zaman-korunur.md",
    "evals/tablo-sekil-guncel-islev-yor.md",
    "evals/bulgu-guncel-yorum-yor.md",
    "evals/mevcut-durum-yor.md",
    "evals/burokratik-simdiki-zaman.md",
    "evals/normatif-yasak-genis-zaman-korunur.md",
    "evals/karisik-zaman-readme.md",
    "evals/yerel-hata-genel-kural-ayrimi.md",
    "evals/framework-kalkisi.md",
    "evals/campaign-kalkisi.md",
    "evals/capture-kalkisi.md",
    "evals/drive-kalkisi.md",
    "evals/enable-kalkisi.md",
    "evals/address-kalkisi.md",
    "evals/provide-kalkisi.md",
    "evals/deneyimlemek-kalkisi.md",
    "evals/ortaya-koymak-yigini.md",
    "evals/elde-etmek-olcum.md",
    "evals/referans-cercevesi-korunur.md",
    "evals/kuramsal-cerceve-korunur.md",
    "evals/yazilim-cercevesi-korunur.md",
    "evals/reklam-kampanyasi-korunur.md",
    "evals/yardim-kampanyasi-korunur.md",
    "evals/test-kampanyasi-alan-terimi.md",
    "evals/bellek-adresleme-korunur.md",
    "evals/hipotezi-desteklemek-korunur.md",
    "evals/davranisi-yakalamak-alan-terimi-korunur.md",
    "evals/erisim-saglamak-korunur.md",
)
TEXT_SUFFIXES = (".md", ".yaml", ".yml")


def fail(message: str) -> None:
    raise SystemExit(message)


for relative_path in REQUIRED_FILES:
    path = ROOT / relative_path
    if not path.is_file():
        fail(f"Missing required file: {relative_path}")

text_files = [
    path
    for path in ROOT.rglob("*")
    if path.is_file()
    and path.suffix.lower() in TEXT_SUFFIXES
    and ".git" not in path.parts
]
texts: dict[Path, str] = {}
for path in text_files:
    try:
        texts[path] = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        fail(f"Package text files must be UTF-8 ({path.relative_to(ROOT)}): {error}")

if "__pycache__" not in (ROOT / ".gitignore").read_text(encoding="utf-8"):
    fail(".gitignore must exclude __pycache__")
for path, content in texts.items():
    for stale_name in ("name: insaniyet", "$insaniyet", "$hikayeci"):
        if stale_name in content:
            fail(
                f"Stale or external skill name found in "
                f"{path.relative_to(ROOT)}: {stale_name}"
            )

skill_path = ROOT / "SKILL.md"
skill = texts[skill_path]
readme = texts[ROOT / "README.md"]
openai_yaml = texts[ROOT / "agents/openai.yaml"]
license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")

frontmatter_match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", skill, re.DOTALL)
if frontmatter_match is None:
    fail("SKILL.md must start with YAML frontmatter")

frontmatter = frontmatter_match.group(1)
frontmatter_keys = re.findall(r"(?m)^([a-zA-Z0-9_-]+):", frontmatter)
if frontmatter_keys != ["name", "description"]:
    fail(
        "SKILL.md frontmatter must contain only name and description "
        f"(found: {frontmatter_keys})"
    )

if not re.search(r"(?m)^name:\s*metinoskop\s*$", frontmatter):
    fail("SKILL.md frontmatter name must be metinoskop")
if not re.search(r"(?m)^description:\s*\S", frontmatter):
    fail("SKILL.md frontmatter description is missing")
if "Türkçeye çevrilmiş metin" not in frontmatter:
    fail("SKILL.md must limit translation scope to existing Turkish translations")
if "# Metinoskop" not in skill:
    fail("SKILL.md must use the Metinoskop heading")
if len(skill.splitlines()) > 400:
    fail("SKILL.md exceeds the 400-line portability budget")
if len(skill.encode("utf-8")) > 60_000:
    fail("SKILL.md exceeds the 60 KB attention budget; move detail to references/")
if len(frontmatter_match.group(1)) > 1_200:
    fail("SKILL.md description must stay a trigger description, not a catalog (max 1200 bytes)")
for heading in (
    "## Belirsizlik ve yorum seçimi",
    "## Terim ve gösterim tutarlılığı",
    "## Rapor bütünlüğünü koru",
    "## Dört düzeyde yapay düzyazı",
    "### Cümle düzeyi",
    "### Paragraf düzeyi",
    "### Belge düzeyi",
    "**Sıfır bilgi cümlesi.**",
    "**Dolguyu başka dolguya çevirme.**",
    "**İşlev tekrarı.**",
    "**Savunmacı düzyazı.**",
    "**Üretilmiş önem.**",
    "**Üretilmiş karşıtlık.**",
    "**Soyut yüklem sisi.**",
    "**Açık olanı açıklama.**",
    "**Paragraf simetrisi.**",
    "**Zorlama denge.**",
    "**Yol haritası ve okur yönlendirmesi.**",
    "**Kalıp giriş ve kalıp sonuç.**",
    "## Yapı ve okur yorgunluğu",
    "Yapı, kavramsal sınırları izler",
    "### Bölme kararı",
    "### Okuru yoran alışkanlıklar",
    "### Cümle ekonomisi",
    "### Yapısal koruma",
    "**Önce süreklilik.**",
    "**Başlık hakkını kazanmalıdır.**",
    "**Derinlik testi.**",
    "**Başlık sıkıştırma.**",
    "**Paragraf görsel parça değil kavramsal birimdir.**",
    "**Zihinsel model sürekliliği.**",
    "**Yakınlık kuralı.**",
    "**Açıklama, metin ilerlemeden bitmelidir.**",
    "**Slayt değil belge.**",
    "**Yapay gerilim.**",
    "**Paragraf sonu askısı.**",
    "**Bağlam yeniden başlatma ve çapraz gönderme.**",
    "**Başlık tekrarı ve boş sarmalayıcılar.**",
    "**Zorlama geçişler.**",
    "**Yinelenme haritası.**",
    "**Gereksiz uzun ifadeler.**",
    "**Yığılmış çerçeve.**",
    "**Okur emeği.**",
    "Görsel parçalanmayı açıklık sanma",
    "## Sertlik düzeyleri",
    "## Akademik ve teknik metin",
    "**5. Yapay düzyazı, yapı, çeviri kokusu, kanıt, sözcük ve tutarlılık denetimi yap.**",
    "**E. Yapı:**",
    "**F. Çeviri kokusu:**",
    "## Çeviri kokusu ve Türkçe ritim",
    "**Kokuyu sözcükte değil ilişkide ara.**",
    "**Bilgi yapısı ve Türkçenin kendi kaynaklarıyla yeniden kur.**",
    "**Kesinliği bozma, aşırı Türkçeleştirme.**",
    "## Kanıt ve kesinlik",
    "**Bilginin kaynağını düzenleyip yok etme.**",
    "**Aktörlüğü koru; edilgeni epistemik seçim olarak değerlendir.**",
    "**Çekince kanıttır, pekiştirici değildir.**",
    "**Kip ve statü zincirini ilerletme.**",
    "## Sözcük birleşimleri",
    "**Eşdizim ve istem denetimi.**",
    "**Sözcük kimliğini koru.**",
    "## Metinsel tutarlılık ve konu ilerleyişi",
    "**Her cümle öncekinden büyür.**",
    "Edilgenliği yalnızca aktör belli diye etkene çevirme",
    "**Bağlaç ilişki kuramaz.**",
    "**Gönderge, kapsam ve olumsuzluk yerinde kalır.**",
    "**G. Kanıt ve kesinlik:**",
    "**H. Sözcük uyumu:**",
    "**I. Metinsel tutarlılık:**",
    "**J. Zamansal ankraj:**",
    "**Zamansal ankrajı koru.**",
    "**Şimdiki zamanı eksik bırakma.**",
    "**Sözcüksel kalkıyı denetle.**",
):
    if heading not in skill:
        fail(f"SKILL.md is missing: {heading}")

if re.search(r"(?m)^####", skill):
    fail("SKILL.md must not use fourth-level headings (its own structure rule)")
if len(re.findall(r"(?m)^### ", skill)) > 12:
    fail("SKILL.md has too many third-level headings for its own fragmentation rule")

for relative_path in re.findall(r"\]\((references/[^)]+)\)", skill):
    if not (ROOT / relative_path).is_file():
        fail(f"Broken SKILL.md reference: {relative_path}")

metadata_requirements = (
    'display_name: "Metinoskop"',
    'short_description: "Türkçe metindeki mekanik kalıpları ve yapay ritmi azaltır"',
    'default_prompt: "$metinoskop kullanarak',
)
for requirement in metadata_requirements:
    if requirement not in openai_yaml:
        fail(f"agents/openai.yaml is missing: {requirement}")

readme_requirements = (
    "# Metinoskop",
    "## Kurulum",
    "## Kullanım",
    "### İsteğe bağlı kavramsal giriş",
    "## Kapsam ve sınırlar",
    "## Depo yapısı",
    "## Geliştirme ve doğrulama",
    "## Sürümleme",
    "## Lisans",
    "npx skills add ayberkdt/metinoskop --global",
    "[LICENSE](LICENSE)",
    "[NOTICE](NOTICE)",
    "## Lisans ve atıf",
    "CC BY 4.0",
    "[CHANGELOG.md](CHANGELOG.md)",
    "scripts/eval-runner.py",
    "scripts/style-lint.py",
    "scripts/eval-suite.py",
    "retorik-yapilar.md",
    "yapisal-butunluk.md",
    "turkce-ritim-ve-ceviri-kokusu.md",
    "kanit-ve-kesinlik.md",
    "sozcuk-birlesimleri.md",
    "metinsel-tutarlilik.md",
    "zamansal-ankraj-ve-rapor-kipi.md",
)
for requirement in readme_requirements:
    if requirement not in readme:
        fail(f"README.md is missing: {requirement}")
if f"v{CURRENT_VERSION}" not in readme:
    fail(f"README.md must mention the current version: v{CURRENT_VERSION}")

if not license_text.startswith("Attribution 4.0 International\n"):
    fail("LICENSE must contain the Creative Commons Attribution 4.0 International legal code")
for clause in ("Section 3 -- License Conditions", "Attribution.", "Section 2 -- Scope"):
    if clause not in license_text:
        fail(f"LICENSE is missing a CC BY 4.0 clause: {clause}")
for foreign in ("ShareAlike", "NonCommercial", "NoDerivatives"):
    if foreign in license_text:
        fail(f"LICENSE must be plain CC BY 4.0, not a variant carrying {foreign}")
notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
if "Copyright (c) 2026 Ayberk Demirkanat" not in notice:
    fail("NOTICE copyright notice is missing")
for requirement in ("CC BY 4.0", "https://github.com/ayberkdt/metinoskop", "Ayberk Demirkanat"):
    if requirement not in notice:
        fail(f"NOTICE must carry the attribution detail: {requirement}")

changelog = texts[ROOT / "CHANGELOG.md"]
if "## [Unreleased]" not in changelog:
    fail("CHANGELOG.md must include an Unreleased section")
if f"## [{CURRENT_VERSION}] - 2026-07-31" not in changelog:
    fail(f"CHANGELOG.md must document version {CURRENT_VERSION}")
if "## [0.2.0] - 2026-07-31" not in changelog:
    fail("CHANGELOG.md must document version 0.2.0")
if "## [0.1.0] - 2026-07-31" not in changelog:
    fail("CHANGELOG.md must document version 0.1.0")

evals_readme = texts[ROOT / "evals/README.md"]
for requirement in ("sıfır bilgi", "işlev tekrarı", "savunmacı", "paragraf", "style-lint.py", "başlık", "parçalanma", "yakınlık", "eval-suite.py", "yapısal beklenti", "sentez", "çeviri kokusu", "açık özne", "sahip olmak", "epistemik", "eşdizim", "konu ilerleyişi", "aktarım", "olumsuzluk", "serbest değişmezler", "behavioral-regression.py", "gold", "zamansal ankraj"):
    if requirement not in evals_readme.casefold():
        fail(f"evals/README.md must mention review axis: {requirement}")

eval_headings = (
    "## Kaynak",
    "## Talep",
    "## Korunması gerekenler",
    "## Kaçınılması gerekenler",
)
for relative_path in EVAL_FILES:
    content = texts[ROOT / relative_path]
    for heading in eval_headings:
        if heading not in content:
            fail(f"{relative_path} is missing: {heading}")

eval_markers = {
    "evals/belirsizlik.md": ("Bu durum", "birden fazla makul yorum"),
    "evals/kapsam-ve-kosul.md": ("Yalnızca en az üç ay", "18 yaş altındaki"),
    "evals/uslup-eslestirme.md": ("### Üslup örneği", "### Düzenlenecek metin"),
    "evals/bicim-koruma.md": ("| Model | Hata |", "[^1]", "`max_iter=500`"),
    "evals/teknik.md": ("GRGM1200", "DOP853", "bağıl tolerans", "Δv", "10⁻⁶", "±", "(3)"),
    "evals/rapor-bulgu-yorum-oneri.md": ("%6,2", "%3,1", "üç aylık", "henüz"),
    "evals/rapor-yapisal-butunluk.md": (
        "## 2. Bulgular",
        "## 3. Sınırlılıklar",
        "(Tablo 2)",
        "**Tablo 2. Çalışma biçimine göre eğitim süresi değerlendirmesi**",
        "Ek A",
    ),
    "evals/yonetici-ozeti.md": ("1 Ocak–31 Mart 2026", "480", "%14", "altı haftalık", "henüz"),
    "evals/savunmaci-akademik.md": ("0,001", "0,01", "0,0001", "200 dönem", "tesadüfi değildir", "bilinçli bir seçimdir"),
    "evals/iddia-tekrar-dongusu.md": ("120. derece", "%2,1", "%6,8", "Başka bir ifadeyle", "Dolayısıyla"),
    "evals/yol-haritasi.md": ("## Yapılandırma", "`config/settings.yaml`", "`timeout`", "`retries`", "Bu bölümde", "Şimdi"),
    "evals/yapay-denge.md": ("4,5", "3,1", "soğuk zincir", "her yeniliğin olduğu gibi", "öte yandan"),
    "evals/giris-hunisi.md": ("Günümüzde", "Mart 2026", "14 saat", "haftada bir", "her gece"),
    "evals/sonuc-ve-gelecek-calisma.md": ("## Sonuç", "20 °C", "40 °C", "60 °C", "Sonuç olarak", "Gelecekte yapılacak", "tek bir sensör"),
    "evals/soyut-yuklem.md": ("0,8 dB", "4,1 dB", "100 MHz", "rol oynadığını", "ışık tutmaktadır", "30 metre"),
    "evals/paragraf-simetrisi.md": ("Nisan 2025", "180 bin", "yüzde 62", "yüzde 70", "2026 planında", "henüz"),
    "evals/gerekli-ifade.md": ("`retries`", "`timeout`", "4xx", "429", "Bu ayrım önemlidir", "Sonuç olarak"),
    "evals/iyi-metin.md": ("Merhaba Selin", "yalnızca", "henüz", "geçen ay konuştuğumuz gibi", "bayi bazında değil"),
    "evals/egitsel-aciklama.md": ("doğrulama kümesi", "cevap anahtarını", "1.000", "800", "200"),
    "evals/asiri-bolumleme.md": ("### Veri kümesinin seçimi", "### Sınırlılık", "48.000", "%12", "%2", "10 dakika"),
    "evals/derin-baslik.md": ("#### 3.1.1", "#### 3.2.1", "`timeout`", "`retries`", "`log_level`"),
    "evals/tek-paragraf-bolumler.md": ("### Teslim süresi", "### Soğuk zincirin sonucu", "4,5", "3,1"),
    "evals/kisa-paragraf-yigini.md": ("214", "%61", "%48", "%35", "gönüllü katılım"),
    "evals/yapay-gerilim.md": ("İlk bakışta", "hikâye burada bitmez", "%12", "%8", "yalnızca", "henüz"),
    "evals/tekrarlanan-bolum-girisleri.md": ("### 4.1", "### 4.3", "Bu bölümde", "tek sensörlü", "20 °C", "%19"),
    "evals/tekrarlanan-bolum-sonuclari.md": ("%6,2", "%3,1", "%2,9", "gözden geçirilmesi", "Sonuç olarak"),
    "evals/asiri-capraz-gonderme.md": ("### 2.1 Veri", "### 2.4 Gerekçe", "Önceki bölümde", "aşağıda görüleceği üzere", "ileride tekrar dönülecektir", "1.200"),
    "evals/uzun-cerceve-ifadeleri.md": ("Bu bağlamda, söz konusu", "karşımıza çıkmasıdır", "en az 500", "%70"),
    "evals/ayrilmis-kanit.md": ("### 3.1 Doğruluk", "### 3.3 Sınırlılıklar", "%91", "yalnızca 2024"),
    "evals/gereksiz-listeleme.md": ("- Sorgular arasında", "%2", "4 GB", "yanıt süresi değişmedi"),
    "evals/korunacak-basliklar.md": ("# Kurulum kılavuzu", "## 1. Gereksinimler", "## 4. Sorun giderme", "üçüncü bölüme", "en az 8 GB", "`config/settings.yaml`"),
    "evals/yontem-ayrimi.md": ("### Deney 1", "### Deney 3", "25 °C", "5 °C", "yalnızca deney başında", "30 dakika"),
    "evals/uzun-paragraf-korunur.md": ("yüzde 9", "yüzde 14", "gösteriyor olabilir", "ayrıştırılamıyor", "yalnızca"),
    "evals/kisa-paragraf-korunur.md": ("`--purge`", "geri alınamaz", "02.00", "%90"),
    "evals/yapisal-iyi-metin.md": ("## Sorun", "## Yapılan işlem ve sonraki adım", "2.140", "120", "henüz", "en olası açıklama"),
    "evals/tekrarlanan-acik-ozne.md": ("Model ilk koşulda", "%4", "1.500", "henüz", "tekrarlanan cümle başlangıcı: 0"),
    "evals/bu-sonuc-ritmi.md": ("Bu sonuç", "Bu bulgu", "Bu durum", "0,2", "0,5", "40 saniyeden 18 saniyeye", "iki katına"),
    "evals/asiri-bir.md": ("bir sensörden gelen bir veri", "tek bir sensörle", "birden fazla", "henüz", "bir / 100 sözcük"),
    "evals/sahip-olmak-kalkisi.md": ("hesaplama maliyetine sahiptir", "üç katmana sahiptir", "IP67", "64", "iki fabrikaya sahiptir", "yönetici yetkisine sahip olmalıdır", "sahip olmak: <= 2"),
    "evals/bulunmaktadir-kalkisi.md": ("bulunmaktadır", "yer almaktadır", "mevcuttur", "içermektedir", "doldurmak zorundadır", "varlık kalıbı"),
    "evals/ve-zinciri.md": ("okur ve veriyi", "100 Hz", "10 ms", "uygular ve uygulama sonucunu", "ve zinciri: 0"),
    "evals/dogal-ve-korunur.md": ("%12 düşürdü ve hesaplama süresini %30", "200", "henüz", "düşürüp artırdı"),
    "evals/yararli-ip-yapisi.md": ("Daha sonra", "Ardından", "Bunun ardından", "12 istasyondan", "0 ile 1", "3 saat", "fiilimsi yığını: 0"),
    "evals/asiri-ip-zinciri.md": ("toplayıp", "temizleyip", "ölçekleyip", "bölüp", "eğitip", "doğrulayıp", "%91", "Tablo 2"),
    "evals/art-niteleme.md": ("eğitilmiş olan bir modeldir", "2024", "2023", "0,01", "olan zinciri: 0"),
    "evals/gerekli-olan.md": ("40 °C'nin üzerinde olan", "18", "belirtilmedi"),
    "evals/gereksiz-olan.md": ("sahip olan ve", "uygun olan bir seçenektir", "5 ms", "%98", "20 ms", "olan zinciri: 0", "sahip olmak: 0"),
    "evals/cerceve-yigini.md": ("Bu bağlamda, performans açısından", "kapsamında", "noktasında", "perspektifinden", "çerçevesinde", "%35", "8 GB", "henüz", "çerçeve yığını: 0"),
    "evals/gerekli-acisindan.md": ("maliyet açısından ucuz, süre açısından pahalıdır", "4.000", "12.000", "altı hafta", "iki hafta", "henüz"),
    "evals/soyut-ad-yuklemi.md": ("bir değerlendirme yapmıştır", "bir analiz gerçekleştirilmiştir", "olumlu bir etkiye sahiptir", "belirleyici bir rol oynamaktadır", "karar alma sürecine", "240", "%7", "%4", "ölçülmemiştir"),
    "evals/teknik-adlastirma-korunur.md": ("Kalman kazancının hesaplanması", "yenilik kovaryansının tersinin alınmasını", "Tablo 3", "50", "0,12", "yalnızca"),
    "evals/ozne-dusurme-akisi.md": ("Yeni sürüm", "3 Eylül", "4,2", "1,9", "henüz", "kademeli", "tekrarlanan cümle başlangıcı: 0"),
    "evals/belirsizlik-icin-acik-ozne.md": ("Filtre", "Gözlemci", "50 Hz", "hiçbir veri iletmez"),
    "evals/dogal-uzun-cumle-korunur.md": ("ıraksamadığını fakat", "60 °C", "40 saniyeden 210 saniyeye", "yalnızca", "henüz", "cümle: 2"),
    "evals/asiri-yuklu-cumle.md": ("Bu kapsamda, söz konusu", "değerlendirilmesinin gerçekleştirilmesi", "20 °C", "40 °C", "60 °C", "%3", "%11", "bakımından", "çerçeve yığını: 0"),
    "evals/ingilizce-soylem-belirtecleri.md": ("Bununla birlikte", "Buna ek olarak", "Öte yandan", "Bu nedenle", "Sonuç olarak", "7 günlük", "%40", "yalnızca", "bağlaçla başlayan cümle"),
    "evals/hukuki-kalip-korunur.md": ("İşbu", "aksi kararlaştırılmadıkça", "söz konusu", "takdirde", "7.2", "on iş günü", "yalnızca", "cümle: 4"),
    "evals/teknik-ozne-tekrari-korunur.md": ("Denetleyici komutu doğrular", "Denetleyici komutu uygular", "`E-41`", "ayrı ayrı kaydedilir", "cümle: 4"),
    "evals/yerli-turkce-metin.md": ("yedi buçukta", "Kışın bu bekleme çekilmez, yazın umursamıyorum", "üç gün", "henüz", "cümle: 4"),
    "evals/edilgen-korunur.md": ("4 °C", "48 saat", "iki kez", "0,1 gram", "cümle: 3",),
    "evals/edilgen-etkene.md": ("yönetim kurulu tarafından", "12 Mart 2026", "iki proje", "bildirilmiştir",),
    "evals/bilinmeyen-aktor.md": ("karar verildi", "belirtilmedi", "henüz",),
    "evals/aktarim-olgu-olmaz.md": ("bildirdi", "belirtti", "10 iş günü", "18 gün", "ölçüldü",),
    "evals/olcum-ile-cikarim.md": ("düşünülmektedir", "ölçülmemiştir", "%11", "%3",),
    "evals/cekince-korunur.md": ("olabilir", "yalnızca 2024 verisiyle sınırlı olarak", "henüz", "0,6", "0,2",),
    "evals/kiplik-yigini.md": ("muhtemelen", "düşünülebilir", "Görünüşe göre", "40", "öne sürmektedir", "kiplik yığını: 0",),
    "evals/dayanaksiz-pekistirici.md": ("açıkça kanıtlamaktadır", "yalnızca iki gürültü düzeyi", "%5", "henüz", "pekiştirici: 0",),
    "evals/mesru-guclu-iddia.md": ("belirlendi", "72 saat", "6 saatte", "0,3 bar",),
    "evals/gerekceli-kip-degisimi.md": ("214", "Şekil 2", "yapılacaktır", "cümle: 4",),
    "evals/uslup-kip-nobetlesmesi.md": ("temizlenmiştir", "eğitilmektedir", "verilmiş bulunmaktadır", "18 dakika", "Tablo 1", "kip nöbetleşmesi: 0",),
    "evals/oneri-karar-degil.md": ("önermektedir", "beklenmektedir", "henüz", "üç ay",),
    "evals/karar-uygulama-degil.md": ("5 Mayıs 2026", "1 Eylül 2026", "uygulanacaktır", "planlanmaktadır",),
    "evals/gozlenmedi-yoktur-degil.md": ("gözlenmedi", "test yapılmamıştır", "çözümsüzdür", "önerilmektedir",),
    "evals/atif-kapsami.md": ("belirtildi", "Bu nedenle", "%6,2", "henüz", "aktarım sonrası sonuç: 0",),
    "evals/kapsam-isareti-baglanmasi.md": ("yalnızca 30 °C'nin üzerinde", "12", "40 örnekte", "görülmedi",),
    "evals/sonuc-sonuclardan-guclu.md": ("## Sonuçlar", "## Tartışma", "## Sonuç", "r = 0,18", "açıklamaktadır", "ortaya konmuştur",),
    "evals/iyi-akademik-paragraf.md": ("74", "68", "p < 0,05", "gözlemsel", "yalnızca %40", "cümle: 3",),
    "evals/tuhaf-esdizim.md": ("cevap sağlamaktadır", "karar gerçekleştirmiştir", "risk sergilemekte", "güçlü iyileşme", "6 saatten 4 saate",),
    "evals/teknik-esdizim-korunur.md": ("kazanç matrisini", "durum kovaryansını", "Yenilik kovaryansı", "6×6",),
    "evals/yanlis-hal-cercevesi.md": ("hakkında hassas", "üzerine odaklanan", "üzerinde tartışmış", "ilgeç yoğunluğu: 0",),
    "evals/dogru-alisilmadik-hal.md": ("hatadan etkilenmez", "gecikmeye duyarlıdır", "20 ms", "2 kat",),
    "evals/edat-aktarimi.md": ("hakkında ilişkin", "üzerinde dair", "yönelik olarak", "120 bin", "2025 fiyatları üzerinden",),
    "evals/hafif-fiil-sismesi.md": ("değerlendirme gerçekleştirmiştir", "analiz gerçekleştirilmiş", "işlemi yapılmıştır", "iyileştirme sağlanmış", "%9", "%6", "Yük testi", "hafif fiil: 0",),
    "evals/surec-adi-korunur.md": ("risk değerlendirmesi yapar", "14 risk", "3'ü", "sınıflandırılmıştır",),
    "evals/genel-fiil-kesin-iliski.md": ("Tablo 2", "Şekil 4", "Ek B", "göstermektedir",),
    "evals/epistemik-guvensiz-fiil.md": ("olumlu bir etkiye sahiptir", "30 koşuda", "%4", "%7", "rastgele atanmamıştır",),
    "evals/esanlam-kaymasi-teknik.md": ("0,4 mm", "sapma", "Bu hata", "bulgu", "Gözlem", "düşündürüyor", "eş anlamlı kayması: 0",),
    "evals/kanonik-terim-tekrari.md": ("Ayırıcı her istekte", "Ayırıcı uygun blok", "Ayırıcı sayfayı", "64 baytlık",),
    "evals/varlik-yeniden-adlandirma.md": ("Bu yaklaşım", "Yapı 20 ms", "Sistem düşük güç", "Çözüm gömülü", "eş anlamlı kayması: 0",),
    "evals/hukuki-formul-korunur.md": ("kabul ve taahhüt eder", "kiralananı", "15 Ocak 2027", "zorunludur",),
    "evals/dogal-is-epostasi.md": ("14.00", "salon değişmedi", "henüz", "haber ver",),
    "evals/odunc-terim-korunur.md": ("baseline", "pipeline", "benchmark", "en fazla 2 puan",),
    "evals/olgu-yigini.md": ("%91", "üç kaynaktan", "4.000", "üç katmanlıdır", "18 dakika",),
    "evals/sabit-konu-korunur.md": ("50 Hz", "tahminle karşılaştırır", "kazançla çarpar", "cümle: 4",),
    "evals/dogrusal-ilerleyis-korunur.md": ("yüzde 9", "çoğu", "yüzde 11", "düşündürüyor",),
    "evals/desteksiz-bu-nedenle.md": ("%5", "%3", "Bu nedenle", "sınanmamıştır",),
    "evals/gecerli-nedensel-baglac.md": ("50 bağlantı", "bu nedenle", "30 saniye", "2.140",),
    "evals/esanlam-donusu.md": ("Bulgular", "Çıktılar", "Gözlemler", "özellikle 30 yaş", "iki bölgede",),
    "evals/gerekli-ad-tekrari.md": ("Deney grubu 24", "kontrol grubu 22", "310", "342", "Deney grubundaki iki",),
    "evals/uzak-bu.md": ("0,5", "50 Hz", "40 °C", "10 ms", "18 saniye", "Bu, yakınsama",),
    "evals/kisa-mesafe-eksilti.md": ("perşembe", "Cuma sabahı", "çoğu", "ikinci bölümle",),
    "evals/bolum-basi-sifirlama.md": ("## 3.1", "## 3.3", "Bu çalışmada önerilen", "2024", "%12", "%8", "yalnızca", "konu sıfırlama: 0",),
    "evals/temiz-devir.md": ("%12", "%8", "yalnızca", "henüz", "düzyazı paragrafı: 2",),
    "evals/islev-kaymasi.md": ("%8", "düşük irtifada", "Bu nedenle", "henüz",),
    "evals/kronoloji-nedensellik.md": ("Bu nedenle", "yüzde 8", "Ayrıca", "mayısta",),
    "evals/kapsam-isareti-tasinmasi.md": ("Yalnızca yüksek irtifadaki", "48", "hiçbiri çıkarılmadı",),
    "evals/olumsuzluk-kapsami.md": ("azaltmadı", "yalnızca varyansı", "0,9", "0,4",),
    "evals/kayit-kaymasi.md": ("İşin ilginç yanı", "Bu kapsamda söz konusu", "kritik önem arz", "0,01", "kayıt kayması: 0",),
    "evals/bilincli-kayit-degisimi.md": ("**Uyarı:**", "`--purge`", "geri alınamaz", "yaklaşık 40 saniye",),
    "evals/ingilizce-noktalama.md": ("Model — üç katmanlı", "(ki bu koşul", "beklenen bir sonuçtur", "2024", "parantez yükü: 0",),
    "evals/teknik-noktalama-korunur.md": ("0,2; 0,5 ve 0,8", "(bkz. Tablo 3)", "2025",),
    "evals/uzak-sinirlilik.md": ("%12", "12 istasyondan", "3 saatte", "yalnızca 30 °C",),
    "evals/ayni-iddia-yeni-rol.md": ("## Sonuçlar", "## Tartışma", "## Sonuç", "40 °C", "%11", "düşündürüyor", "önerilmektedir",),
    "evals/ayni-iddia-hacim.md": ("Yani 40 °C", "göstermektedir", "üç kez", "cümle: <= 1",),
    "evals/tutarli-metin-korunur.md": ("3 Eylül", "14.10", "14.35", "50 bağlantı", "120", "cümle: 3",),
    "evals/raporda-genis-zaman-yigini.md": ("12 Ağustos", "1.200", "%4", "%6", "Yalnızca", "geniş zaman doygunluğu: 0",),
    "evals/bu-calisma-inceler.md": ("Bu çalışma üç farklı modeli karşılaştırır", "2025", "800", "zamansal sürtünme: 0",),
    "evals/sonuclarda-genis-zaman.md": ("120. derecede", "üç koşuda", "artırır", "geniş zaman doygunluğu: 0",),
    "evals/tarihli-olay-genis-zaman.md": ("12 Ağustos'ta", "14 Ağustos'taki", "gözlenmez", "eylülde", "yapılacaktır",),
    "evals/metot-uygulamasi-gecmis.md": ("4 °C", "iki kez", "40 dönem", "18 dakika",),
    "evals/algoritma-genel-davranis-korunur.md": ("RK4 her adımda türevi dört kez değerlendirir", "yenilik kovaryansından", "cümle: 4",),
    "evals/bilimsel-genelleme-korunur.md": ("yerçekimi gradyanı artar", "20 °C", "80 °C", "100 °C",),
    "evals/prosedur-kilavuz-korunur.md": ("şalter kapatılır", "yalnızca kuru bezle", "çözücü kullanılmaz", "5 dakika",),
    "evals/teknik-sistem-davranisi-korunur.md": ("`E-41`", "20 ms", "IP67", "en eski kaydı siler",),
    "evals/metot-ve-uygulama-ayrimi.md": ("RK4 her adımda", "10 saniyede", "12 istasyondan", "durumu günceller",),
    "evals/sonuc-ve-yorum-kip-ayrimi.md": ("120. derecede minimuma", "40 °C", "%11", "çözünürlüğünü artırır",),
    "evals/tablo-sekil-zaman-korunur.md": ("Şekil 4", "Tablo 2'de", "Bölüm 3", "(7)",),
    "evals/durum-raporu-uc-zaman.md": ("1.400", "15 Ekim'de", "hâlen", "önerir",),
    "evals/gecmise-zorlama-yok.md": ("100 örnek", "Şekil 3'te", "gelecek ay", "0,2 mm", "cümle: 4",),
    "evals/her-seyi-edildi-yapma.md": ("%4'tür", "toplanır", "kaydedilir", "fiilimsi yığını: 0",),
    "evals/mistir-yigini-yapma.md": ("üç senaryo", "%7", "ikinci senaryoda", "karşılaştırılmıştır",),
    "evals/gecmis-genel-yasa-bozmasin.md": ("60 °C", "%3", "%11", "direnç artar", "malzemeden bağımsızdır",),
    "evals/tetikleyici-iceren-sozcuk-korunur.md": ("Güneşsiz", "eşsizlik teoremiyle", "Analog-dijital dönüştürücü", "dönüştürücüsünün", "40 W", "12 bit", "%78",),
    "evals/periyodik-takvim-genis-zaman-korunur.md": ("15 Ekim", "her ayın ilk pazartesi", "02.00", "1 Ocak", "kendiliğinden yenilenir",),
    "evals/gecmiste-surme-korunur.md": ("14 Mayıs", "03.12", "çalışıyordu", "henüz belirlenmedi",),
    "evals/once-tamamlanmis-olay-korunur.md": ("kalibre edilmişti", "12 Ağustos", "0,3", "zaten",),
    "evals/gecmis-aliskanlik-korunur.md": ("yapardı", "yalnızca başlangıçta", "belirtilmedi",),
    "evals/sirali-olayda-misti-yigini.md": ("8 Ekim", "incelemişti", "raporlamıştı", "iki öneri", "cümle: <= 2",),
    "evals/repo-guncel-davranis-yor.md": ("Repo bunu yasaklar", "eksik kayıtlı çıktıyı reddeder", "mevcut sürümde", "geniş zaman katılığı: 0",),
    "evals/sonuc-guncel-yorum-yor.md": ("Üçüncü koşunun sonucu", "dikkatli incelenmesini gerektirir", "ikinci açıklamaya işaret eder",),
    "evals/genel-gereklilik-genis-zaman-korunur.md": ("Bu tür sonuçlar", "ikinci bir doğrulama ister", "cümle: 2",),
    "evals/tablo-sekil-guncel-islev-yor.md": ("Şekil 4", "Tablo 3", "maliyet dağılımını özetler",),
    "evals/bulgu-guncel-yorum-yor.md": ("120. derecede minimuma indi", "düşündürür", "yetersiz kaldığını",),
    "evals/mevcut-durum-yor.md": ("iki bölgede kullanılır", "devam eder", "Üç ekip",),
    "evals/burokratik-simdiki-zaman.md": ("hâlen", "kullanılmaktadır", "devam etmektedir", "izlenmektedir",),
    "evals/normatif-yasak-genis-zaman-korunur.md": ("Yönetmelik", "yalnızca ilgilinin açık rızasıyla", "idari para cezası", "cümle: 3",),
    "evals/karisik-zaman-readme.md": ("145 eval içerir", "en az dört bölüm gerektirir", "v0.4.1'de eklendi",),
    "evals/yerel-hata-genel-kural-ayrimi.md": ("Günlükteki bu hata", "Bu tür hatalar", "her zaman", "zaman aşımı",),
    "evals/framework-kalkisi.md": ("bir çerçeve önerilmektedir", "Çerçeve kapsamında", "üç ölçütü", "çerçeve yığını: 0",),
    "evals/campaign-kalkisi.md": ("doğrulama kampanyası başlattı", "240 test senaryosu", "12 hata kaydı",),
    "evals/capture-kalkisi.md": ("yakalamaktadır", "doğrusal olmayan etkiyi", "Şekil 3",),
    "evals/drive-kalkisi.md": ("yönlendirmektedir", "0,62 korelasyon", "Sıcaklık değişimi",),
    "evals/enable-kalkisi.md": ("mümkün kılmaktadır", "olanak sağlamaktadır", "iki sensörün",),
    "evals/address-kalkisi.md": ("problemini adreslemektedir", "gecikme riskini", "adreslemek gerekmektedir",),
    "evals/provide-kalkisi.md": ("görünürlük sağlamaktadır", "iyileşme sağlamıştır", "6 saatten 4 saate", "hafif fiil: 0",),
    "evals/deneyimlemek-kalkisi.md": ("performans kaybı deneyimlemiştir", "gecikme deneyimlemiştir", "%12",),
    "evals/ortaya-koymak-yigini.md": ("ortaya koymaktadır", "Tablo 2", "düşük sıcaklıkta",),
    "evals/elde-etmek-olcum.md": ("iyileşme elde edilmiştir", "512 MB", "410 MB", "%20",),
    "evals/referans-cercevesi-korunur.md": ("eylemsiz referans çerçevesinde", "J2000", "cümle: 2",),
    "evals/kuramsal-cerceve-korunur.md": ("kuramsal çerçevesi", "Kavramsal çerçeve", "planlı davranış kuramına",),
    "evals/yazilim-cercevesi-korunur.md": ("Django framework", "ORM katmanı", "önbelleğe",),
    "evals/reklam-kampanyasi-korunur.md": ("yaz kampanyasını", "üç mecrada", "%2,4", "%3,1",),
    "evals/yardim-kampanyasi-korunur.md": ("Bağış kampanyası", "aşı kampanyasına", "1,2 milyon", "40 bin",),
    "evals/test-kampanyasi-alan-terimi.md": ("Uçuş test kampanyası", "14 sortiden", "38 saat",),
    "evals/bellek-adresleme-korunur.md": ("sayfalar hâlinde adresler", "Adresleme birimi", "16 bitlik",),
    "evals/hipotezi-desteklemek-korunur.md": ("ikinci hipotezi destekliyor", "yeterli kanıt bulunamadı", "40 katılımcıyla",),
    "evals/davranisi-yakalamak-alan-terimi-korunur.md": ("davranışı iyi yakalıyor", "surrogate", "0,4 mm",),
    "evals/erisim-saglamak-korunur.md": ("erişim sağlıyor", "bağlantı sağlıyor", "güvenliği sağlamayı", "yetkili kullanıcılara",),
}
for relative_path, markers in eval_markers.items():
    content = texts[ROOT / relative_path]
    for marker in markers:
        if marker not in content:
            fail(f"{relative_path} is missing coverage marker: {marker}")

if "RK4 çözücüsünde tolerans" in texts[ROOT / "evals/teknik.md"]:
    fail("evals/teknik.md contains the stale RK4 tolerance example")

workflow = texts[ROOT / ".github/workflows/validate.yml"]
if "python3 scripts/eval-runner.py --self-test" not in workflow:
    fail("CI must run the deterministic eval runner self-test")
if "python3 scripts/style-lint.py --self-test" not in workflow:
    fail("CI must run the style-lint self-test")
if "python3 scripts/eval-suite.py --require-all" not in workflow:
    fail("CI must run the recorded-output eval suite with --require-all")
behavioral = ROOT / ".github/workflows/behavioral.yml"
if not behavioral.is_file():
    fail("Missing .github/workflows/behavioral.yml (real-model behavioral regression)")
if "scripts/behavioral-regression.py" not in behavioral.read_text(encoding="utf-8"):
    fail("behavioral.yml must run scripts/behavioral-regression.py")
critical = (ROOT / "evals/critical-cases.txt").read_text(encoding="utf-8").split()
for name in critical:
    if not (ROOT / "evals" / f"{name}.md").is_file():
        fail(f"evals/critical-cases.txt names a missing case: {name}")
if not 15 <= len(critical) <= 36:
    fail("evals/critical-cases.txt must list 15-36 cases")
missing_outputs = [p.stem for p in (ROOT / "evals").glob("*.md")
                   if p.name != "README.md" and not (ROOT / "evals/outputs" / f"{p.stem}.txt").is_file()]
if missing_outputs:
    fail(f"Every eval case needs a recorded output: {', '.join(missing_outputs)}")

for output_path in sorted((ROOT / "evals/outputs").glob("*.txt")):
    if not (ROOT / "evals" / f"{output_path.stem}.md").is_file():
        fail(f"Recorded output without an eval case: evals/outputs/{output_path.name}")
if len(list((ROOT / "evals/outputs").glob("*.txt"))) < 175:
    fail("evals/outputs must keep at least one hundred and seventy-five recorded reference outputs")

SHOULD_REMAIN_CASES = (
    "evals/dogal-ve-korunur.md", "evals/gerekli-olan.md", "evals/gerekli-acisindan.md",
    "evals/teknik-adlastirma-korunur.md", "evals/belirsizlik-icin-acik-ozne.md", "evals/dogal-uzun-cumle-korunur.md",
    "evals/hukuki-kalip-korunur.md", "evals/teknik-ozne-tekrari-korunur.md", "evals/yerli-turkce-metin.md",
    "evals/edilgen-korunur.md",
    "evals/cekince-korunur.md",
    "evals/mesru-guclu-iddia.md",
    "evals/gerekceli-kip-degisimi.md",
    "evals/karar-uygulama-degil.md",
    "evals/kapsam-isareti-baglanmasi.md",
    "evals/iyi-akademik-paragraf.md",
    "evals/teknik-esdizim-korunur.md",
    "evals/dogru-alisilmadik-hal.md",
    "evals/surec-adi-korunur.md",
    "evals/kanonik-terim-tekrari.md",
    "evals/hukuki-formul-korunur.md",
    "evals/dogal-is-epostasi.md",
    "evals/odunc-terim-korunur.md",
    "evals/sabit-konu-korunur.md",
    "evals/dogrusal-ilerleyis-korunur.md",
    "evals/gecerli-nedensel-baglac.md",
    "evals/gerekli-ad-tekrari.md",
    "evals/uzak-bu.md",
    "evals/kisa-mesafe-eksilti.md",
    "evals/temiz-devir.md",
    "evals/kapsam-isareti-tasinmasi.md",
    "evals/bilincli-kayit-degisimi.md",
    "evals/teknik-noktalama-korunur.md",
    "evals/ayni-iddia-yeni-rol.md",
    "evals/tutarli-metin-korunur.md",
    "evals/algoritma-genel-davranis-korunur.md",
    "evals/bilimsel-genelleme-korunur.md",
    "evals/prosedur-kilavuz-korunur.md",
    "evals/teknik-sistem-davranisi-korunur.md",
    "evals/tablo-sekil-zaman-korunur.md",
    "evals/gecmise-zorlama-yok.md",
    "evals/tetikleyici-iceren-sozcuk-korunur.md",
    "evals/periyodik-takvim-genis-zaman-korunur.md",
    "evals/gecmiste-surme-korunur.md",
    "evals/once-tamamlanmis-olay-korunur.md",
    "evals/gecmis-aliskanlik-korunur.md",
    "evals/genel-gereklilik-genis-zaman-korunur.md",
    "evals/normatif-yasak-genis-zaman-korunur.md",
    "evals/referans-cercevesi-korunur.md",
    "evals/kuramsal-cerceve-korunur.md",
    "evals/yazilim-cercevesi-korunur.md",
    "evals/reklam-kampanyasi-korunur.md",
    "evals/yardim-kampanyasi-korunur.md",
    "evals/test-kampanyasi-alan-terimi.md",
    "evals/bellek-adresleme-korunur.md",
    "evals/hipotezi-desteklemek-korunur.md",
    "evals/davranisi-yakalamak-alan-terimi-korunur.md",
    "evals/erisim-saglamak-korunur.md",
)
locked = []
for relative_path in EVAL_FILES:
    if relative_path in SHOULD_REMAIN_CASES:
        continue  # korunur vakasında çıktı kaynağa eşittir; cümle sayısı sözleşmenin parçasıdır
    # "- cümle: N" bir varsayılan gibi yazılmıştır; "- cümle: = N" vakanın
    # kendi talebinin dayattığı bilinçli bir yapısal kısıttır ve serbesttir.
    if re.search(r"(?m)^- cümle: \d+\s*$", texts[ROOT / relative_path]):
        locked.append(relative_path)
if locked:
    fail("Transform eval cases must not pin a bare sentence count; use '<= N', "
         "or '= N' when the case's own request requires an exact structure: "
         + ", ".join(locked))

for relative_path in SHOULD_REMAIN_CASES:
    # "Should remain" translationese cases record the source itself as the reference output.
    case_source = re.search(r"(?ms)^## Kaynak\s*\n(.*?)(?=^## (?:Talep|Korunması gerekenler|Kaçınılması gerekenler|Yapısal beklenti)\s*$)", texts[ROOT / relative_path])
    recorded = (ROOT / "evals/outputs" / (Path(relative_path).stem + ".txt")).read_text(encoding="utf-8")
    if case_source is None or case_source.group(1).strip() != recorded.strip():
        fail(f"{relative_path}: recorded output must equal the source for a should-remain case")

for relative_path in ("scripts/eval-runner.py", "scripts/eval-suite.py", "scripts/style-lint.py", "scripts/validate-package.py", "scripts/behavioral-regression.py"):
    try:
        ast.parse((ROOT / relative_path).read_text(encoding="utf-8"))
    except SyntaxError as error:
        fail(f"Invalid Python syntax in {relative_path}: {error}")

print(
    "Metinoskop package is valid "
    f"({len(skill.splitlines())} SKILL.md lines, "
    f"{len(REQUIRED_FILES)} required files, "
    f"{len(EVAL_FILES)} behavioral evals)"
)
