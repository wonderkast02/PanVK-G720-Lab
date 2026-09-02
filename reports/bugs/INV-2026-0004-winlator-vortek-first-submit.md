# INV-2026-0004 — Winlator/Vortek first-submit boundary

Status: `OPEN_CAUSAL_GATE`

## Fronteira conhecida

No caminho live Winlator/Vortek da linha Public Beta, a execução chega ao primeiro `vkQueueSubmit`.

O retorno observado é não-zero e ocorre antes de `vkAcquireNextImageKHR` / `vkQueuePresentKHR` entrarem no ciclo esperado.

Um `_wassert` downstream registra o erro retornado, mas não é evidência suficiente para classificar o evento como GPU fatal.

## Próximo critério

Fechar causalmente:

1. `VkResult` exato do primeiro submit;
2. fence/semaphore state associado;
3. validation/debug messages disponíveis;
4. kernel/Kbase/GPU fault evidence no mesmo intervalo;
5. somente depois repetir Gate A e WSI.

Não mascarar assert, não alterar feature advertisement e não reconstruir Mesa sem uma causa demonstrada.
