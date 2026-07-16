# _template

Modelo padrão para criar uma nova skill neste repositório. Copie esta pasta,
renomeie para o nome descritivo da nova skill (kebab-case, ex.: `revisor-abnt`,
`karpathy-guidelines`) e preencha `SKILL.md`.

## Como usar

1. Copie `skills/_template/` para `skills/<nome-da-skill>/`.
2. Preencha o front-matter de `SKILL.md`:
   - `name`: mesmo nome da pasta, em kebab-case.
   - `description`: 1-2 frases descrevendo o que a skill faz **e** quando
     Claude deve usá-la. É o único texto que Claude lê para decidir se a
     skill se aplica a um pedido — seja específico com gatilhos, palavras-chave
     e contextos (veja `docs/style-guides/naming.md` e
     `context/project/conventions.md` para os padrões já usados no repositório).
3. Escreva o corpo do `SKILL.md`: objetivo, quando usar, passo a passo,
   regras/restrições e pelo menos um exemplo de entrada → saída.
4. Use `examples/` para pares completos de entrada/saída que não caibam
   diretamente no `SKILL.md`.
5. Use `resources/` para arquivos de apoio que a skill precise carregar sob
   demanda (referências grandes, templates, listas de padrões) — siga o
   modelo de "arquivos de referência" usado em `skills/prompt-master/references/`:
   não carregue tudo de uma vez, só o que a tarefa exigir.

## Por que esse padrão

Manter todas as skills na mesma forma (mesmos arquivos, mesma ordem de seções)
é o que permite revisar, comparar e evoluir a biblioteca inteira de forma
consistente — e é o padrão que o relatório de configuração do repositório
(`relatorio-setup-repositorio-ia(2026-07-13).md`, arquivado no histórico do
projeto) já registrava como convenção adotada desde a criação da pasta `skills/`.
