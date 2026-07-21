---
titulo: inventory-control-spreadsheet
ferramenta: Claude
tags: []
versao: 1.0
data_criacao: 2026-07-20
ultima_revisao: 2026-07-20
---

# Inventory Control Spreadsheet

Você é um especialista em Google Sheets/Excel e gestão de estoque para o varejo de material de construção, com domínio de fórmulas, formatação condicional e validação de dados.

Instruções: Gere um arquivo .xlsx completo e pronto para uso de controle de estoque, com todas as colunas, fórmulas, menus suspensos e formatações já aplicados no arquivo — não apenas descritos em texto.

Etapas:

  1. Crie as colunas na ordem: Produto | Marca | Quantidade Atual em Estoque | Valor de Compra (R$) | Valor de Venda (R$) | Lucro (R$) | Margem de Lucro (%) | Curva ABC
  2. Na coluna "Marca", aplique validação de dados do tipo lista suspensa com 5 a 8 marcas comuns de material de construção como exemplo (ex: Votorantim, Tigre, Quartzolit, Vedacit, Suvinil, Eucatex), editável pelo usuário depois
  3. Na coluna "Lucro", insira a fórmula real da planilha (Valor de Venda - Valor de Compra) em todas as linhas de dados
  4. Na coluna "Margem de Lucro (%)", insira a fórmula real (Lucro / Valor de Compra) formatada como porcentagem em todas as linhas de dados
  5. Na coluna "Curva ABC", aplique validação de dados do tipo lista suspensa com as opções fixas: A, B, C
  6. Aplique formatação condicional na coluna "Curva ABC": verde para A, amarelo para B, vermelho para C
  7. Aplique formatação condicional na coluna "Quantidade Atual em Estoque": vermelho quando o valor for menor ou igual a 5
  8. Formate o cabeçalho com negrito, cor de fundo e congele a primeira linha
  9. Preencha 5 linhas de exemplo com dados fictícios de produtos de material de construção para demonstrar o funcionamento das fórmulas e formatações
  10. Ajuste a largura das colunas automaticamente para caber o conteúdo

Objetivo Final: Um arquivo .xlsx funcional, aberto e usável imediatamente no Google Sheets (via upload) ou no Excel, com fórmulas ativas e menus suspensos operacionais, sem necessidade de configuração manual adicional pelo usuário.

Delimitação: Não use Apps Script nem macros. Não invente marcas reais como se fossem parceiras da loja — deixe claro nos dados de exemplo que são apenas ilustrativos. As fórmulas devem ser nativas de planilha (não texto simulando fórmula).
