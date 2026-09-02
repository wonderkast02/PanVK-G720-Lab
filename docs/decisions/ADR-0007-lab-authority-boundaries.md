# ADR-0007 — Separação entre autoridade pública e Lab privado

Status: accepted — 2026-09-02

## Decisão

`wonderkast02/panvk-g720-kbase-csf` é a autoridade pública para:

- source lineage;
- tags/releases;
- documentação pública;
- provenance da Public Beta.

`wonderkast02/PanVK-G720-Lab` é uma memória técnica privada para:

- checkpoints;
- evidências e comparações;
- investigações;
- hipóteses;
- external/community validation;
- decisões e roadmap experimental.

## Consequências

O Lab não pode:

- substituir source provenance;
- modificar claims da Release;
- transformar evidência externa em validação autoritativa;
- promover hipótese a fato;
- relicenciar código upstream;
- ser usado para substituir bytes de uma Release imutável.

Quando houver conflito, a autoridade deve ser resolvida usando source/tag/release e evidência física mais recente.
