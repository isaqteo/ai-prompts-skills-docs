# Guia de Estilo — Escrita de Prompts

Como estruturar e escrever prompts salvos em `prompts/` neste repositório.
Este guia é o resumo operacional para humanos; a engenharia de prompts em
si (roteamento por ferramenta, técnicas seguras, os 35 padrões que
desperdiçam tokens) é implementada em detalhe pela skill
`skills/prompt-master/`.

## Estrutura de um arquivo de prompt

Todo prompt salvo em `prompts/` segue `templates/prompt-template.md`:

```markdown
---
titulo:
ferramenta:
tags: []
versao: 1.0
data_criacao:
ultima_revisao:
---

## Objetivo do prompt


## Prompt

\`\`\`
(texto do prompt aqui)
\`\`\`

## Notas de uso
-
```

- **`ferramenta`** no front-matter deve corresponder à subpasta onde o
  arquivo está (`prompts/claude/`, `prompts/chatgpt/`, `prompts/gemini/`) —
  ou `shared` se o prompt funciona sem adaptação em qualquer ferramenta.
- **"Objetivo do prompt"** vem sempre antes do prompt em si: uma frase
  dizendo o que ele resolve, para quem for escanear a pasta sem abrir cada
  arquivo.
- **O prompt em si** fica isolado em um bloco de código, pronto para
  copiar/colar — nunca misturado com comentários ou instruções fora do
  bloco.
- **"Notas de uso"** é o lugar para pré-requisitos e observações — nunca
  dentro do texto do prompt.

## Princípios de escrita (resumo da skill `prompt-master`)

- Verbo de tarefa preciso, nunca vago.
- Critérios de sucesso explícitos ("concluído quando...") em qualquer
  tarefa não trivial.
- Escopo travado (arquivo, função, diretório) para prompts de edição de
  código.
- Papel/persona atribuído quando a tarefa é complexa ou especializada —
  reaproveite `context/personas/` quando fizer sentido, em vez de escrever
  a persona do zero dentro do próprio prompt.
- Nunca adicione instruções de "pense passo a passo" a modelos de
  raciocínio nativo (o3, DeepSeek-R1, Qwen3 em modo thinking) — isso
  degrada a saída.

Para o conjunto completo de técnicas, templates (RTF, CO-STAR, RISEN,
ReAct + Condições de Parada etc.) e os 35 padrões que desperdiçam tokens
com exemplos de antes/depois, use a skill `skills/prompt-master/` — este
guia é deliberadamente um resumo, não uma duplicata.

## Ver também

- `context/project/conventions.md` — nomenclatura e estrutura, em formato
  de contexto para IA.
- `skills/prompt-master/references/patterns.md` — os 35 padrões completos.
- `skills/prompt-master/references/templates.md` — os 12 templates
  completos.
