#!/usr/bin/env python3
"""Validate the portable Metinoskop skill package without dependencies."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "AGENTS.md",
    "agents/openai.yaml",
    "references/akicilik.md",
    "references/turkce-oruntuler.md",
)


def fail(message: str) -> None:
    raise SystemExit(message)


for relative_path in REQUIRED_FILES:
    path = ROOT / relative_path
    if not path.is_file():
        fail(f"Missing required file: {relative_path}")

try:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    openai_yaml = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
except UnicodeDecodeError as error:
    fail(f"Package text files must be UTF-8: {error}")

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
if "# Metinoskop" not in skill:
    fail("SKILL.md must use the Metinoskop heading")
if len(skill.splitlines()) > 500:
    fail("SKILL.md exceeds the 500-line portability budget")

for stale_name in ("name: insaniyet", "$insaniyet"):
    if stale_name in skill or stale_name in openai_yaml:
        fail(f"Stale skill name found: {stale_name}")

for relative_path in re.findall(r"\]\((references/[^)]+)\)", skill):
    if not (ROOT / relative_path).is_file():
        fail(f"Broken SKILL.md reference: {relative_path}")

metadata_requirements = (
    'display_name: "Metinoskop"',
    'short_description: "',
    "$metinoskop",
)
for requirement in metadata_requirements:
    if requirement not in openai_yaml:
        fail(f"agents/openai.yaml is missing: {requirement}")

readme_requirements = (
    "# Metinoskop",
    "## Kurulum",
    "## Kullanım",
    "## Kapsam ve sınırlar",
    "## Depo yapısı",
    "## Geliştirme ve doğrulama",
    "npx skills add ayberkdt/metinoskop --global",
)
for requirement in readme_requirements:
    if requirement not in readme:
        fail(f"README.md is missing: {requirement}")

print(
    "Metinoskop package is valid "
    f"({len(skill.splitlines())} SKILL.md lines, "
    f"{len(REQUIRED_FILES)} required files)"
)
