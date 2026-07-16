# Exemplo — entrada (prompt ruim)

Este é um exemplo de entrada real que a skill `prompt-master` corrige,
ilustrando o **Padrão de Tarefa #1** documentado em
`skills/prompt-master/references/patterns.md` ("Verbo de tarefa vago").

## Prompt original enviado por um usuário

```
me ajuda com meu código
```

## Por que esse prompt desperdiça tokens

- Nenhum verbo de tarefa preciso (o que fazer: corrigir? refatorar? explicar?).
- Nenhum arquivo, função ou trecho de código referenciado.
- Nenhum critério de sucesso — a IA não sabe quando parar.
- Nenhuma ferramenta-alvo identificada.

Ver `output.md` para a versão corrigida pelo `prompt-master`.
