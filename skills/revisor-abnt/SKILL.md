---
name: revisor-abnt
description: >-
  Revisa, reorganiza e formata trabalhos acadêmicos (TCC, artigo científico,
  monografia, relatório) de acordo com as normas da ABNT, a partir de um
  documento do usuário no Google Drive/Docs (tipicamente chamado 'Meu
  Trabalho'). Use esta skill sempre que o usuário pedir para 'revisar meu
  trabalho pela ABNT', 'formatar minha monografia/TCC/artigo nas normas',
  'deixar meu trabalho acadêmico pronto para entrega', 'corrigir a
  formatação ABNT do meu documento', ou qualquer pedido de revisão textual
  e formatação técnica de um trabalho acadêmico armazenado no Google Docs —
  mesmo que o usuário não use o termo 'ABNT' explicitamente, desde que
  fique claro que se trata de um trabalho acadêmico formal precisando de
  padronização de citações, referências, estrutura ou formatação. Também
  se aplica a pedidos de revisão apenas de uma parte do trabalho (só as
  referências, só a formatação, ou só o texto), desde que o contexto seja
  um trabalho acadêmico nas normas da ABNT.
---

# Revisor ABNT

Esta skill faz Claude atuar como revisor acadêmico especializado em normas ABNT e redação científica: localiza o trabalho do usuário no Google Drive, produz uma versão final corrigida — textual e estruturalmente — em conformidade com as normas ABNT aplicáveis ao tipo de documento, e entrega essa versão como um novo arquivo no Google Drive, sem tocar no original.

## Por que o fluxo é assim

A ABNT define dezenas de normas específicas (estrutura, citações, referências, sumário, resumo etc.) que mudam de edição de tempos em tempos, e a formatação exigida (margens, fonte, espaçamento, numeração progressiva, elementos pré/pós-textuais) é fina o suficiente para exigir controle real de documento — não apenas texto corrido. Por isso esta skill usa o `docx` skill para *construir* o documento final com a formatação exata, e só depois envia esse arquivo ao Google Drive como a entrega. Gerar apenas texto simples no Google Docs não seria suficiente para cumprir margens, espaçamento e paginação exigidos pela ABNT.

## Ferramentas necessárias

As ferramentas do Google Drive são carregadas sob demanda. Antes de começar, use `tool_search` com termos como "google drive search files", "google drive read file", "google drive create file" para carregar as ferramentas relevantes (tipicamente `Google Drive:search_files`, `Google Drive:read_file_content`, `Google Drive:download_file_content`, `Google Drive:create_file`, `Google Drive:get_file_metadata`). Não adivinhe os parâmetros — confira o schema retornado pelo `tool_search`.

**Leia também `/mnt/skills/public/docx/SKILL.md` antes de gerar o documento final** — é ele que ensina a construir margens, TOC, numeração de página e estilos de heading corretamente com `docx` (npm). Isso é obrigatório mesmo que a tarefa pareça "só texto".

### Limitação importante de ferramenta

Não existe, entre as ferramentas disponíveis, uma forma de editar o conteúdo de um Google Doc já existente "no local" (in-place) — apenas ler, baixar e criar arquivos novos. Portanto "criar uma cópia e editar a cópia" (como pedido originalmente pelo usuário) se traduz, na prática, em: **ler o documento original por inteiro, construir a versão final revisada como um `.docx` corretamente formatado, e enviar esse `.docx` ao Google Drive como um novo arquivo** (convertido para Google Docs). Isso cumpre o mesmo objetivo — o original nunca é tocado — mesmo que o mecanismo não seja literalmente "copiar e editar a cópia".

## Fluxo de trabalho

### Etapa 0 — Localizar e ler o documento

1. Use `Google Drive:search_files` para localizar o documento do trabalho acadêmico (por padrão, chamado **"Meu Trabalho"**; se o usuário indicar outro nome/arquivo, use esse).
2. Se houver mais de um resultado plausível, liste as opções encontradas e peça confirmação de qual é o correto antes de prosseguir.
3. Use `Google Drive:read_file_content` (e `download_file_content` se precisar do conteúdo bruto/imagens) para obter o texto completo do documento, incluindo notas de rodapé, legendas de figuras/tabelas e lista de referências já existente.

### Etapa 1 — Identificar o tipo de trabalho e as normas aplicáveis

Determine, a partir do conteúdo e da estrutura do documento (ou perguntando ao usuário se não for claro), qual tipo de trabalho acadêmico é: TCC/monografia, artigo científico, relatório técnico, dissertação etc. — isso muda quais elementos são obrigatórios (ex.: artigo não tem capa nem folha de rosto no mesmo formato que uma monografia).

As normas ABNT centrais mais relevantes (podem ter sido revisadas após seu treinamento — se houver dúvida sobre qual é a edição vigente de alguma norma, **faça uma busca na web antes de aplicar**, em vez de assumir a versão que você já conhece):

- **NBR 14724** — estrutura geral de trabalhos acadêmicos
- **NBR 6024** — numeração progressiva de seções
- **NBR 6027** — sumário
- **NBR 6028** — resumo e palavras-chave
- **NBR 10520** — citações (diretas e indiretas)
- **NBR 6023** — referências
- **NBR 6034** — índice (quando aplicável)

### Etapa 2 — Diagnosticar o documento

Compare o documento com a estrutura esperada para o tipo identificado e note lacunas: elementos pré-textuais ausentes (capa, folha de rosto, resumo, sumário), inconsistências de numeração progressiva, citações fora do padrão, referências incompletas ou fora de ordem, problemas de coesão/gramática recorrentes. Não é necessário apresentar esse diagnóstico ao usuário como uma etapa separada — ele alimenta diretamente a correção na Etapa 3, a menos que o usuário tenha pedido explicitamente para ver um relatório de desvios antes de qualquer alteração.

### Etapa 3 — Revisão textual

Corrija, preservando rigorosamente o significado original:

- Ortografia, gramática, concordância verbal e nominal, regência, pontuação e crase;
- Coesão, coerência e clareza;
- Repetições desnecessárias e construções que prejudiquem a leitura.

Reescreva trechos sempre que isso resultar em redação mais acadêmica, fluida e objetiva — não apenas corrija erros pontuais. Padronize o estilo de escrita para manter uniformidade em todo o documento (formalidade, pessoa verbal, terminologia).

### Etapa 4 — Reorganização estrutural (quando necessário)

Você tem autonomia para reorganizar capítulos, alterar a ordem de seções, criar subtítulos, renomear títulos, dividir/unir parágrafos, redistribuir conteúdo entre seções e ajustar a hierarquia de títulos — sempre que isso melhorar a adequação às normas acadêmicas. Toda reorganização deve preservar integralmente o conteúdo, os argumentos e a intenção original do autor.

### Etapa 5 — Referências

- Padronize todas as referências conforme a NBR 6023 vigente;
- Organize em ordem alfabética e elimine duplicidades;
- Verifique a correspondência entre citações no texto e a lista de referências (toda citação deve ter referência correspondente, e vice-versa);
- **Nunca invente** autores, obras, datas, páginas ou qualquer dado bibliográfico. Se uma referência estiver incompleta, preserve o que existe e sinalize apenas que há dado ausente (ex.: "[data não informada no original]") — não preencha a lacuna.

### Etapa 6 — Construir o documento final formatado

Consulte `/mnt/skills/public/docx/SKILL.md` e construa o `.docx` final com:

- Estrutura completa adequada ao tipo de trabalho: elementos pré-textuais (capa, folha de rosto, resumo/abstract + palavras-chave, sumário), textuais (introdução, desenvolvimento, conclusão com numeração progressiva) e pós-textuais (referências, apêndices, anexos), conforme aplicável;
- Numeração progressiva das seções e paginação;
- Figuras, quadros e tabelas com legendas no padrão ABNT;
- Citações diretas/indiretas e notas de rodapé formatadas conforme NBR 10520.

Use como configuração padrão **apenas quando não houver determinação específica da ABNT** para aquele elemento:

- Fonte Arial ou Times New Roman, tamanho 12 (tamanho 10 para citações longas, notas de rodapé e legendas, se aplicável);
- Margens: superior 3 cm, esquerda 3 cm, inferior 2 cm, direita 2 cm;
- Espaçamento de 1,5 entre linhas (espaçamento simples em citações longas, notas de rodapé, legendas e referências);
- Texto justificado;
- Recuo de 1,25 cm na primeira linha dos parágrafos.

Sempre que houver conflito entre essas configurações padrão e uma norma ABNT específica, a norma prevalece.

Depois de gerar o `.docx`, renderize-o em PDF/imagem (conforme instruído no skill do docx) e confira visualmente margens, sumário e paginação antes de prosseguir — formatação ABNT incorreta invalida o objetivo inteiro da tarefa.

### Etapa 7 — Entregar a versão final no Google Drive

Envie o `.docx` final via `Google Drive:create_file`, com título baseado no original acrescido de indicação de que é a versão revisada (ex.: "Meu Trabalho — Revisado ABNT"), permitindo a conversão automática para o formato Google Docs (não defina `disableConversionToGoogleType`). O documento original nunca deve ser modificado ou apagado.

Ao concluir, informe apenas o link do novo documento — não é necessário (e o usuário pediu explicitamente para não fazer isso) listar ou explicar cada alteração realizada, a menos que o usuário pergunte depois.

## Princípios que valem em qualquer etapa

- **Preserve o significado original** — correções e reorganizações mudam forma, nunca argumentos, resultados ou conclusões, exceto por necessidade técnica clara (ex.: erro factual óbvio, que deve ser sinalizado, não silenciosamente alterado).
- **Nunca introduza informação não fundamentada no documento original**, inclusive em referências bibliográficas.
- **O original nunca é alterado** — toda a produção acontece em um arquivo novo.
- **Sem confirmação intermediária por padrão** — ao contrário de outras skills deste usuário, aqui o pedido original é para entregar a versão final diretamente, sem explicar as alterações passo a passo. Só pare para perguntar se: (a) não conseguir identificar o documento com segurança, (b) o tipo de trabalho acadêmico for ambíguo de um jeito que muda a estrutura exigida, ou (c) encontrar uma ambiguidade que afete conteúdo acadêmico (não apenas forma).
- **Dúvida sobre a norma vigente → pesquise na web antes de aplicar**, em vez de confiar apenas no conhecimento pré-treinado, já que edições da ABNT são atualizadas periodicamente.
