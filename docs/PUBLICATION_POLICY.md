# Publication policy

The Lab follows a fail-closed publication sequence.

- **P0 Freeze** — stop unrelated mutation during final audit.
- **P1 Inventory** — paths, types, sizes, branches/tags.
- **P2 Secret/PII** — working tree plus all reachable history.
- **P3 Licensing** — upstream/third-party provenance and redistribution boundary.
- **P4 Authority** — source duplication and conflicting claims.
- **P5 Evidence normalization** — current vs historical/superseded status.
- **P6 README/docs** — public landing and policies.
- **P7 Hash/provenance** — deterministic manifests and source refs.
- **P8 Git history** — secrets/PII must not survive in reachable public history.
- **P9 Public switch** — only after P1–P8 pass.
- **P10 External verification** — anonymous/read-only verification after publication.

Publication must fail closed on unresolved secrets, unnecessary PII or
licensing/redistribution blockers.
