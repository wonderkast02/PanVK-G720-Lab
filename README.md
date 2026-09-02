# PanVK-G720-Lab
Official long-term technical memory for Mali-G720/PanVK/CSF.

**Boundary:** code/patches/CTS build logic stay in `wonderkast02/panvk-g720-kbase-csf`; this repo stores evidence, logs, capability snapshots, tests, decisions, history and diagnostic tools.

Evidence: **PROVEN / STRONG / OPEN / DISCARDED**.
Capabilities: **Advertised → Implemented → Tested → Working/Broken/Partial/Unknown**.
Workflow: `Lab Issue → investigation → minimal test → main Issue → branch → tests → PR → CI → review → merge → hardware re-test → Lab VERIFIED`.

Anchor: branch `ci`, published SHA `0521a3257628e811cfead6b5a9753e9f705e2f31`. Tessellation stays unadvertised until remaining closure.
See `history/DEV-DEV2-CURRENT.md`.

<!-- PANVK-G720-LAB-CURRENT:BEGIN -->

## Estado atual — 2026-09-02

Este repositório é o **Lab privado de memória técnica/evidências** do PanVK G720.

A autoridade pública permanece em `wonderkast02/panvk-g720-kbase-csf`.

Estado público ancorado:

- Public Beta: `0.1.0-beta.1.9.4`
- source: `3549264275c9663ed73e01d652f4c0d16f21df22`
- package SHA-256: `01c6304206c6e348cb069e3d04fb1c7b693195b543b4134ad7c108a33906d1fa`
- release: pre-release + immutable
- MC8: tessellation validado no escopo dirigido
- FullPlane + Kbase/CSF: qualificados no escopo registrado
- Winlator/Vortek: Gate A ainda aberto no primeiro submit
- MC7: evidência comunitária externa mantida separada da autoridade MC8

Novos registros:

- `history/checkpoints/2026-09-02.md`
- `reports/validation/2026-09-02-public-beta-1.9.4.md`
- `devices/mali-g720/external/2026-08-31-mc7-the-messenger.md`
- `reports/bugs/INV-2026-0004-winlator-vortek-first-submit.md`
- `docs/decisions/ADR-0007-lab-authority-boundaries.md`
- `docs/roadmap/2026-09-02-deferred-gates.md`

<!-- PANVK-G720-LAB-CURRENT:END -->
