# Guia de Estilo — Nomenclatura

Convenções de nomes de pastas e arquivos usadas neste repositório.

## Regra geral

- **kebab-case** para todas as pastas e a maioria dos arquivos:
  `karpathy-guidelines`, `revisor-abnt`, `organizador-de-anotacoes`,
  `prompt-master`.
- **Nome descritivo da função, não da origem/autor.** Quando uma skill de
  terceiros é importada para este repositório, ela é renomeada para
  descrever o que faz, não de onde veio.

## Caso de referência: `andrej-karpathy-skills` → `karpathy-guidelines`

Ao importar a skill de terceiros hoje em `skills/karpathy-guidelines/`, o
nome original do repositório clonado (`andrej-karpathy-skills`) foi trocado
por `karpathy-guidelines`, para alinhar com o padrão descritivo já usado
pelas demais skills do repositório (`organizador-de-anotacoes`,
`revisor-abnt`). O nome do autor original (Karpathy) foi mantido como
referência de origem/crédito, mas a segunda parte do nome descreve a função
("guidelines"), não o formato do repositório de origem ("skills").

## Caso de referência: `prompt-mestre-main` → `prompt-master`

De forma semelhante, a pasta baixada como `prompt-mestre-main` (sufixo
`-main` típico de download de ZIP do GitHub) foi renomeada para
`prompt-master` nesta reorganização, para coincidir com o `name:` já
declarado no front-matter do próprio `SKILL.md` da skill — o nome da pasta
deve sempre corresponder ao `name:` da skill que ela contém.

## Front-matter de skill

- `name:` no `SKILL.md` deve ser idêntico ao nome da pasta.
- `description:` deve conter tanto o que a skill faz quanto quando usá-la
  (gatilhos, palavras-chave, contextos) — é o único texto que Claude lê
  para decidir se aplica a skill a um pedido.

## Arquivos de contexto e prompts

- Arquivos em `context/` são nomeados pelo tópico que descrevem, em
  kebab-case (`academic-style.md`, `clean-code.md`), nunca pelo destino
  onde o conteúdo "morava antes" (evite nomes como `notion-sync.md` para
  conteúdo que não depende mais do Notion).
- Arquivos em `prompts/` não têm convenção de nome fixa além de kebab-case
  descritivo — o front-matter (`titulo`, `tags`) é o que torna o prompt
  localizável, não o nome do arquivo.

## Ver também

- `context/project/conventions.md` — versão em formato de contexto para IA
  destas mesmas convenções.
