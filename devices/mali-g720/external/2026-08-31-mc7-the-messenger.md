# External community validation — Mali-G720 MC7 — The Messenger

Classificação: `EXTERNAL_COMMUNITY_MC7`

Esta evidência é externa e não substitui a qualificação autoritativa MC8.

## Stack observado

Sessão PanVK:

- GPU: Mali-G720 MC7
- PanVK driver view: 26.2.99
- Vulkan: 1.4.354
- wrapper: Leegao
- DXVK: 1.7.2
- API: D3D11
- feature level usado: D3D_FEATURE_LEVEL_11_0
- workload: The Messenger

Foi observada renderização funcional do jogo no caminho PanVK.

O presenter iniciou em `VK_PRESENT_MODE_MAILBOX_KHR` e posteriormente recriou em `VK_PRESENT_MODE_FIFO_KHR`, com acquire/submit/present reais no trace.

## Limites

- resultado DXVK 1.7.2 não prova DXVK 3.x;
- a feature view do Leegao não equivale à feature view nativa do PanVK;
- sucesso externo MC7 não prova tessellation nativo no MC7;
- screenshots pontuais PanVK vs system não constituem benchmark formal;
- nenhuma alegação de conformidade Vulkan.

A identidade/hash byte-exata do driver externo deve ser registrada quando a autoridade correspondente estiver disponível.
