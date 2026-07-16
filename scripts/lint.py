#!/usr/bin/env python3
"""Lint basico de Markdown para este repositorio.

Verifica, em todo arquivo .md do repositorio (fora de blocos de codigo):
- Exatamente um heading H1 (#) por arquivo — a menos que o front-matter YAML
  do arquivo tenha um campo 'titulo:', caso em que o titulo cumpre esse papel
  (convencao usada em prompts/, context/ e templates/), ou o arquivo esteja
  em .github/ (templates de issue/PR nao costumam ter H1).
- Nenhum heading pula de nivel (ex.: ## seguido direto de ####).
- Sem espacos em branco no fim da linha (trailing whitespace).
- Arquivo termina com uma unica quebra de linha.

Arquivos importados verbatim de terceiros (ver ARQUIVOS_IMPORTADOS_VERBATIM)
sao ignorados: preservar o conteudo original tem prioridade sobre reformatar
um arquivo que nao foi escrito para este repositorio.

Uso: python3 scripts/lint.py
Sai com codigo 1 se encontrar algum problema.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules"}

# Arquivos trazidos de repositorios de terceiros e preservados verbatim
# (ver docs/style-guides/naming.md e o historico em CHANGELOG.md) — nao
# foram escritos seguindo as convencoes deste repositorio, entao nao faz
# sentido aplicar o lint local a eles.
ARQUIVOS_IMPORTADOS_VERBATIM = {
    "skills/karpathy-guidelines/EXAMPLES.md",
    "skills/karpathy-guidelines/README.md",
    "skills/karpathy-guidelines/README.zh.md",
    "skills/prompt-master/SKILL.md",
    "skills/prompt-master/README.md",
    "skills/prompt-master/references/patterns.md",
    "skills/prompt-master/references/templates.md",
    "templates/prompt-template.md",
}

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
FENCE_RE = re.compile(r"^```")


def strip_front_matter(text: str) -> tuple[str, bool]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return text, False
    has_titulo = bool(re.search(r"^titulo:", match.group(1), re.MULTILINE))
    return text[match.end():], has_titulo


def iter_markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in ARQUIVOS_IMPORTADOS_VERBATIM:
            continue
        yield path


def lines_outside_code_fences(lines: list[str]):
    """Gera (indice, linha) para linhas fora de blocos ```...```."""
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield i, line


def lint_file(path: pathlib.Path, errors: list[str]) -> None:
    raw = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    body, has_titulo = strip_front_matter(raw)
    lines = body.split("\n")

    requires_h1 = not has_titulo and ".github" not in path.parts
    if requires_h1:
        h1_count = sum(
            1 for _, line in lines_outside_code_fences(lines) if line.startswith("# ")
        )
        if h1_count != 1:
            errors.append(f"{rel}: esperado exatamente 1 heading H1, encontrado {h1_count}")

    last_level = 0
    for _, line in lines_outside_code_fences(lines):
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            if last_level and level > last_level + 1:
                errors.append(f"{rel}: heading pula de nivel ({line.strip()!r})")
            last_level = level

    for i, line in enumerate(raw.split("\n"), start=1):
        if line != line.rstrip():
            errors.append(f"{rel}:{i}: espaco em branco no fim da linha")

    if raw and not raw.endswith("\n"):
        errors.append(f"{rel}: arquivo nao termina com quebra de linha")


def main() -> int:
    errors: list[str] = []
    for md_file in iter_markdown_files():
        lint_file(md_file, errors)

    if errors:
        print(f"{len(errors)} problema(s) encontrado(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Lint concluido sem problemas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
