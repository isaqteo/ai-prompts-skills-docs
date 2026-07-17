---
titulo: Estilo de Markdown (contexto para IA)
categoria: writing-style
tags: [markdown, formatacao]
versao: 1.0
data_criacao: 2026-07-16
ultima_revisao: 2026-07-16
---

## O que este contexto descreve

Regras diretas de formatação Markdown a colar em prompts/system prompts
quando uma IA for gerar ou editar arquivos `.md` deste repositório. Para a
versão explicada para humanos (com o porquê de cada regra), veja
`docs/style-guides/markdown.md`.

## Conteúdo

- Use exatamente um `#` (H1) por arquivo, como título do documento.
- Não pule níveis de heading (não vá de `##` direto para `####`).
- Prefira listas (`-`) a parágrafos longos para qualquer sequência de 3 ou
  mais itens paralelos.
- Use tabelas Markdown para comparações estruturadas (ex.: "antes/depois",
  "opção A vs. opção B") em vez de descrever a comparação em prosa.
- Blocos de código sempre com a linguagem declarada após os três acentos
  graves (` ```python `, ` ```bash `, ` ```json ` etc.); use ` ```text ` ou
  ` ``` ` sem linguagem apenas para saída de terminal ou texto genérico.
- Links internos entre arquivos do repositório usam caminho relativo
  Markdown (`[texto](../pasta/arquivo.md)`), nunca URL absoluta do GitHub —
  isso mantém os links funcionando em qualquer clone/fork.
- Front-matter YAML (entre `---`) é obrigatório em `prompts/`, `context/` e
  `templates/`; opcional em `docs/`.
- Frases curtas. Um parágrafo raramente precisa de mais de 3-4 frases.

## Quando incluir este contexto

- Ao gerar qualquer novo arquivo `.md` neste repositório.
- Ao revisar Pull Requests que adicionam ou editam documentação.

## Notas de manutenção
- Mantenha sincronizado com `docs/style-guides/markdown.md` (mesma regra,
  registro diferente: este arquivo é para consumo por IA, o outro é para
  leitura humana).
