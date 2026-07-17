#!/usr/bin/env python3
"""Valida a estrutura basica dos arquivos deste repositorio.

Verifica:
- Toda pasta em skills/ (exceto _template) tem um SKILL.md com front-matter
  YAML contendo 'name' e 'description'.
- Todo arquivo .md em prompts/ (fora de _template) tem front-matter YAML
  contendo 'titulo' e 'ferramenta'.

Uso: python3 scripts/validate.py
Sai com codigo 1 se encontrar algum problema.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def read_front_matter(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    return match.group(1) if match else ""


def check_skills(errors: list[str]) -> None:
    skills_dir = ROOT / "skills"
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name == "_template":
            continue
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"skills/{skill_dir.name}/ nao tem SKILL.md")
            continue
        fm = read_front_matter(skill_file)
        for field in ("name", "description"):
            if f"{field}:" not in fm:
                errors.append(
                    f"skills/{skill_dir.name}/SKILL.md sem campo '{field}' no front-matter"
                )


def check_prompts(errors: list[str]) -> None:
    prompts_dir = ROOT / "prompts"
    for md_file in sorted(prompts_dir.rglob("*.md")):
        if "_template" in md_file.parts:
            continue
        fm = read_front_matter(md_file)
        for field in ("titulo", "ferramenta"):
            if f"{field}:" not in fm:
                errors.append(
                    f"{md_file.relative_to(ROOT)} sem campo '{field}' no front-matter"
                )


def main() -> int:
    errors: list[str] = []
    check_skills(errors)
    check_prompts(errors)

    if errors:
        print(f"{len(errors)} problema(s) encontrado(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Validacao concluida sem problemas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
