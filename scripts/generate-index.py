#!/usr/bin/env python3
"""Gera um INDEX.md com a lista de skills e prompts deste repositorio.

Reaproveita a logica de export.py para ler front-matter, e escreve um
arquivo Markdown legivel por humanos na raiz do repositorio.

Uso: python3 scripts/generate-index.py
Escreve/sobrescreve INDEX.md na raiz do repositorio.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from export import export_prompts, export_skills  # noqa: E402


def build_index() -> str:
    skills = export_skills()
    prompts = export_prompts()

    lines = ["# Indice", "", "Gerado por `scripts/generate-index.py`. Nao edite manualmente.", ""]

    lines.append("## Skills")
    lines.append("")
    lines.append("| Pasta | Nome | Descricao |")
    lines.append("|-------|------|-----------|")
    for skill in skills:
        desc = skill["description"].replace("|", "\\|")
        lines.append(f"| `{skill['folder']}` | {skill['name']} | {desc} |")
    lines.append("")

    lines.append("## Prompts")
    lines.append("")
    lines.append("| Caminho | Titulo | Ferramenta |")
    lines.append("|---------|--------|------------|")
    for prompt in prompts:
        lines.append(
            f"| `{prompt['path']}` | {prompt['titulo']} | {prompt['ferramenta']} |"
        )
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    content = build_index()
    (ROOT / "INDEX.md").write_text(content, encoding="utf-8")
    print("INDEX.md atualizado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
