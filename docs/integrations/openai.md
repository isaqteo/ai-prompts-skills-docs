# Integração — OpenAI

Este repositório não usa a API da OpenAI diretamente para nenhuma skill ou
automação própria. A relação com a OpenAI, até o momento, é indireta: como
provedor de modelo por trás de testes feitos na plataforma Agenta.ai (ver
`docs/integrations/agenta.md`).

## Problema já encontrado

Ao testar um app de exemplo no Agenta, ocorreu um `RateLimitError`. A causa
raiz não foi um problema de configuração do Agenta em si, mas sim **falta de
crédito/billing configurado na conta OpenAI vinculada** a esse app de teste.

## O que isso significa

- Antes de testar qualquer app no Agenta que dependa de um modelo OpenAI,
  confirme que a conta OpenAI vinculada tem billing configurado e crédito
  disponível.
- Se billing pago não for desejado, considerar um provedor de modelo
  alternativo suportado pelo Agenta (não avaliado ainda neste repositório —
  ver "Possíveis Caminhos Futuros" no histórico de configuração original).
- Nenhum uso adicional da API da OpenAI está documentado ou planejado neste
  repositório além do que o Agenta usa internamente.
