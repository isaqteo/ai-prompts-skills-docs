# Guia de Estilo — Markdown

Como escrever arquivos `.md` neste repositório, e por quê.

## Regras

- **Um único `#` (H1) por arquivo**, usado como título do documento. Isso
  mantém a hierarquia de headings previsível e evita que ferramentas de
  geração de índice (ex.: `scripts/generate-index.py`) se confundam sobre
  qual é o título "de verdade" do arquivo.
- **Não pule níveis de heading** (não vá de `##` direto para `####`) — um
  leitor navegando pela tabela de conteúdo espera uma progressão contínua.
- **Listas em vez de parágrafos longos** para qualquer sequência de 3+ itens
  paralelos — mais fácil de escanear, e mais fácil de uma IA processar
  quando o arquivo é usado como contexto.
- **Tabelas para comparações** ("antes/depois", "opção A vs. B") em vez de
  descrever a comparação em prosa corrida.
- **Blocos de código sempre com a linguagem declarada** (` ```python `,
  ` ```bash `, ` ```json `) — isso habilita highlighting correto e deixa
  claro para quem lê (humano ou IA) que tipo de conteúdo está ali.
- **Links internos relativos**, nunca URL absoluta do GitHub
  (`[texto](../pasta/arquivo.md)`, não
  `https://github.com/isaqteo/ai-prompts-skills-docs/blob/main/...`) — links
  relativos continuam funcionando em qualquer clone, fork ou renderização
  local.
- **Front-matter YAML obrigatório** em `prompts/`, `context/` e `templates/`
  (metadados estruturados de que essas pastas precisam para serem
  processadas por scripts/ferramentas); opcional em `docs/`.
- **Frases curtas.** Um parágrafo raramente precisa de mais de 3-4 frases.

## Por que existe também `context/writing-style/markdown-style.md`

Este documento explica o "porquê" para quem está lendo como humano. O
arquivo irmão em `context/writing-style/markdown-style.md` traz o mesmo
conjunto de regras em formato direto/imperativo, pensado para ser colado em
um prompt sem o "porquê" — apenas a regra. Mantenha os dois sincronizados.
