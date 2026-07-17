#!/usr/bin/env python3
"""Exporta um indice de skills e prompts deste repositorio para JSON.

Le o front-matter YAML (formato simples 'chave: valor', sem listas
aninhadas) de cada SKILL.md em skills/ e de cada .md em prompts/, e escreve
um resumo estruturado em JSON.

Uso: python3 scripts/export.py [caminho-de-saida.json]
Sem argumento, escreve em stdout.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_front_matter(text: str) -> dict:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    data = {}
    for line in match.group(1).split("\n"):
        if ":" in line and not line.strip().startswith("#"):
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip()
    return data


def export_skills() -> list[dict]:
    skills = []
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if not skill_dir.is_dir() or skill_dir.name == "_template":
            continue
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue
        fm = parse_front_matter(skill_file.read_text(encoding="utf-8"))
        skills.append(
            {
                "folder": skill_dir.name,
                "name": fm.get("name", ""),
                "description": fm.get("description", ""),
            }
        )
    return skills


def export_prompts() -> list[dict]:
    prompts = []
    for md_file in sorted((ROOT / "prompts").rglob("*.md")):
        if "_template" in md_file.parts:
            continue
        fm = parse_front_matter(md_file.read_text(encoding="utf-8"))
        prompts.append(
            {
                "path": str(md_file.relative_to(ROOT)),
                "titulo": fm.get("titulo", ""),
                "ferramenta": fm.get("ferramenta", ""),
            }
        )
    return prompts


def main() -> int:
    index = {"skills": export_skills(), "prompts": export_prompts()}
    output = json.dumps(index, ensure_ascii=False, indent=2)

    if len(sys.argv) > 1:
        pathlib.Path(sys.argv[1]).write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
