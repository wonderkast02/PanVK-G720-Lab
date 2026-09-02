# Public Beta 0.1.0-beta.1.9.4 — validation snapshot

Classificação: `LOCAL_AUTHORITATIVE_MC8`

## Identidade

- Release: `0.1.0-beta.1.9.4`
- source commit: `3549264275c9663ed73e01d652f4c0d16f21df22`
- package SHA-256: `01c6304206c6e348cb069e3d04fb1c7b693195b543b4134ad7c108a33906d1fa`
- hardware: Mali-G720 MC8 / MT6899
- Kbase: r49p1

## Evidência aceita

A linha MC8 provou execução nativa PanVK → Kbase/CSF, FullPlane e tessellation no escopo dirigido.

`tessellationShader=true` é aceito somente para a linha MC8 qualificada e não deve ser extrapolado para MC7, outros SoCs ou conformidade Vulkan.

## WSI / Winlator

A Release permanece experimental.

No caminho Winlator/Vortek registrado antes da publicação, o primeiro submit retornou erro antes de acquire/present. Esse limite continua sendo o gate live primário para a próxima rodada causal.

## Claims proibidos

Não registrar como provado:

- conformidade Vulkan;
- compatibilidade universal G720;
- suporte garantido a DXVK 3.x;
- geometry shader nativo;
- multiViewport nativo;
- BCn nativo.
