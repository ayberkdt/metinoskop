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
    ".github/workflows/validate.yml",
    "SKILL.md",
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    "agents/openai.yaml",
    "references/akicilik.md",
    "references/kavramsal-girisler.md",
    "references/rapor-yazimi.md",
    "references/retorik-yapilar.md",
    "references/turkce-oruntuler.md",
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
    "scripts/eval-runner.py",
    "scripts/style-lint.py",
    "scripts/validate-package.py",
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
if len(skill.splitlines()) > 500:
    fail("SKILL.md exceeds the 500-line portability budget")
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
    "**5. Yapay düzyazı ve yapı denetimi yap.**",
    "**E. Yapı:**",
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
    "[CHANGELOG.md](CHANGELOG.md)",
    "scripts/eval-runner.py",
    "scripts/style-lint.py",
    "retorik-yapilar.md",
    "yapisal-butunluk.md",
)
for requirement in readme_requirements:
    if requirement not in readme:
        fail(f"README.md is missing: {requirement}")
if f"v{CURRENT_VERSION}" not in readme:
    fail(f"README.md must mention the current version: v{CURRENT_VERSION}")

if not license_text.startswith("MIT License\n"):
    fail("LICENSE must contain the MIT License")
if "Copyright (c) 2026 Ayberk Demirkanat" not in license_text:
    fail("LICENSE copyright notice is missing")

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
for requirement in ("sıfır bilgi", "işlev tekrarı", "savunmacı", "paragraf", "style-lint.py", "başlık", "parçalanma", "yakınlık"):
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

for relative_path in ("scripts/eval-runner.py", "scripts/style-lint.py", "scripts/validate-package.py"):
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
