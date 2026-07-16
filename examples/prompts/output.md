# Exemplo — saída (prompt corrigido pelo prompt-master)

Versão corrigida do prompt em `input.md`, aplicando o Template A (RTF) e o
Padrão de Tarefa #1 de `skills/prompt-master/references/patterns.md`.

## Prompt gerado

```
Papel: Você é um engenheiro de back-end sênior especializado em Node.js.
Tarefa: Refatore a função `buscarUsuario()` em `src/services/usuarios.js`
para usar async/await no lugar de callbacks, e trate o caso em que a
consulta ao banco retorna nulo (lance um erro `UsuarioNaoEncontrado`
em vez de deixar o retorno como `undefined`).
Formato: Apenas o código da função alterada, em um bloco de código
JavaScript. Não altere nenhuma outra função do arquivo.
Concluído quando: a função usar async/await, tratar o caso de retorno
nulo, e os testes existentes em `src/services/usuarios.test.js`
continuarem passando.
```

**🎯 Alvo:** Claude Code · **💡 Estratégia:** o verbo vago "me ajuda" virou uma
operação precisa (refatorar uma função nomeada, em um arquivo nomeado), com
escopo de arquivo travado e critério de sucesso binário — seguindo o Template
G (Escopo de Arquivo) descrito em `skills/prompt-master/references/templates.md`.

## O que mudou em relação ao `input.md`

| Antes | Depois |
|-------|--------|
| Verbo de tarefa vago | Verbo preciso: "refatore", com função e arquivo nomeados |
| Sem critérios de sucesso | "Concluído quando" explícito e verificável |
| Sem escopo definido | "Não altere nenhuma outra função do arquivo" |
| Sem papel atribuído | Papel de especialista definido (Node.js sênior) |
