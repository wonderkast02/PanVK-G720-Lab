# Deferred gates — 2026-09-02

Itens registrados, mas não autorizados automaticamente.

## PAN_KMOD_REMAINING_GAP_AUDIT

Antes de abrir issue/MR upstream Mesa:

- comparar `panvk_vX_gpu_queue` local com o PanVK/pan_kmod upstream atual;
- listar dependências Panthor diretas restantes;
- demonstrar por que a API pan_kmod atual não representa cada caso;
- definir o menor gap de abstração;
- verificar se upstream master já resolveu o ponto.

Só abrir upstream se um gap residual concreto continuar existindo.

## DXVK G720 LAB provenance

A árvore `/root/dxvk-g720-lab-src` existiu e foi historicamente preservada durante o desenvolvimento.

Publicação de patch permanece bloqueada até revalidar a autoridade Git exata no ambiente Ubuntu/proot:

- upstream tag/commit;
- local delta exato;
- modified paths;
- licença;
- SHA-256 do patch regenerado.

Não reconstruir patch apenas a partir do README.

## External MC7

Pode permanecer como evidência privada com classificação externa.

Promoção para documentação pública requer provenance suficiente do stack e claims limitados ao que foi observado.
