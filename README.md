<div align="center">

# PanVK G720 Lab
### Research & Evidence Archive

**Vulkan → Mesa/PanVK → Kbase/CSF → Mali-G720**

Hardware real • Evidência reproduzível • Depuração causal

</div>

> **Source authority / Autoridade de código**
>
> This repository is the public research and evidence archive for Drive G720.
> The authoritative driver source, branches, tags and releases remain in
> **`wonderkast02/panvk-g720-kbase-csf`**.
>
> Este repositório é o arquivo público de pesquisa e evidência do Drive G720.
> O código, branches, tags e releases autoritativos permanecem em
> **`wonderkast02/panvk-g720-kbase-csf`**.

## Current state

| Area | Current authority |
|---|---|
| Reference hardware | Mali-G720 MC8 / MediaTek MT6899 / Kbase-CSF |
| Post-GS development | `g720-development @ 77832026e87fc39a48d691dd5a46e9908726b0bf` |
| Development qualification | `PPA6: PASS` |
| Geometry Shader | Functionally closed on the qualified reference-hardware scope |
| Public driver release | `0.1.0-beta.1.9.4` remains frozen/immutable |
| Source set | 22-path audited post-GS development delta |

The Lab is **not** a second source repository. Historical evidence may describe
older states; current authority always comes from the latest qualified source
reference plus the evidence boundary documented here.

## What belongs here

- hardware-backed evidence and manifests;
- validation and investigation reports;
- bring-up history and superseded hypotheses;
- capability snapshots and comparisons;
- runtime / Winlator / Vortek / DXVK diagnostics;
- reproducibility metadata, hashes and causal checkpoints;
- small auditable diagnostic tools.

Full builds, toolchains, caches, APKs and duplicate Mesa trees do not belong in
normal Git history.

## Evidence model

New evidence uses these states:

`VERIFIED-HW` · `VERIFIED-STATIC` · `REPRODUCED` · `PARTIAL-PASS` ·
`BLOCKED-TRANSPORT` · `BLOCKED-TOOLING` · `SEMANTIC-FAIL` ·
`SUPERSEDED` · `HISTORICAL` · `INVALIDATED`

See [`docs/EVIDENCE_MODEL.md`](docs/EVIDENCE_MODEL.md).

## Reproducibility

Important results should bind device identity, source ref, executed ELF hash
when cryptographically proven, test/executor version, run count, expected vs.
actual result, first real failure and artifact hashes.

See [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

## Claim boundary

This project does **not** claim Vulkan conformance or universal compatibility
across every Mali-G720, SoC, Winlator build or game. Results are scoped to the
hardware/runtime explicitly named by their evidence.

See [`docs/CLAIMS_POLICY.md`](docs/CLAIMS_POLICY.md).

## Navigation

- [`docs/STATUS.md`](docs/STATUS.md) — current qualified state
- [`docs/PURPOSE.md`](docs/PURPOSE.md) — repository role and authority boundary
- [`docs/EVIDENCE_MODEL.md`](docs/EVIDENCE_MODEL.md) — evidence taxonomy
- [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) — reproducibility contract
- [`docs/PUBLICATION_POLICY.md`](docs/PUBLICATION_POLICY.md) — publication gates
- [`history/`](history/) — causal and historical records
- [`reports/`](reports/) — investigations and validation reports
- [`devices/`](devices/) — hardware identity / community results
- [`capabilities/`](capabilities/) — capability evidence
- [`SECURITY.md`](SECURITY.md) — responsible disclosure
- [`LICENSING.md`](LICENSING.md) — licensing and third-party material

## Credits

Drive G720 builds on the work of Mesa, Panfrost, PanVK/Panfork, ARM Kbase
interfaces and the wider Vulkan/Linux graphics community. Upstream notices and
licenses remain authoritative for upstream-derived material.
