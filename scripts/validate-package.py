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
    "references/turkce-oruntuler.md",
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
    "scripts/eval-runner.py",
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
):
    if heading not in skill:
        fail(f"SKILL.md is missing: {heading}")

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

for relative_path in ("scripts/eval-runner.py", "scripts/validate-package.py"):
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
