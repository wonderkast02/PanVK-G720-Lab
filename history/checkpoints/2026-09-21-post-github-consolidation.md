# Checkpoint 2026-09-21 — post-GitHub consolidation / Lab reconciliation

This checkpoint records the state after the audited G720 post-GS source was consolidated publicly and before Termux cleanup.

## Public source authority

Repository: `wonderkast02/panvk-g720-kbase-csf`

- `main`: `35e06e5c64c494c817e5d3e5b0c68ef8bb3a08d4`
- `ci`: `0521a3257628e811cfead6b5a9753e9f705e2f31`
- `android-candidate-beta-1.9.4`: `3549264275c9663ed73e01d652f4c0d16f21df22`
- `g720-development`: `77832026e87fc39a48d691dd5a46e9908726b0bf`
- development tree: `03b9282039bc82c9eeed7a4914e6cf93a020e17d`
- frozen public tag: `0.1.0-beta.1.9.4` -> `3549264275c9663ed73e01d652f4c0d16f21df22`

No new beta, tag, or public release was created by the post-GS consolidation.

## Qualified development state

- Premium source audit: PASS (PPA6 closure).
- RAW95 physical ELF byte identity: PASS.
- source22 final set: frozen, 22 paths.
- source22 manifest SHA-256: `196f4aabbbe2707d0e5131eb1d02a208b152acd4e4296acab5d8ac2e52e4c998`.
- cumulative patch SHA-256: `0dc403a40a353a2fac73bb8b1dc2d8c105e0fea5d2e9ef51a1a7b1d76373194d`.
- RAW95 physical ELF SHA-256: `44fca977ae86d88c9b43b674f14a54bf2611f84801510662be7731427073d526`.
- portable shallow public-development checkpoint SHA-256: `d69713f77e3c1cc4198aa0c8d8355a71e8fea114ceb571b577983426a142b561`.

These facts describe the audited G720/Kbase-CSF development line; they do not create a Vulkan-conformance or cross-GPU claim.

## Lab reconciliation lineage

The private Lab remained an evidence/history registry, not public source authority.

- pre-reconciliation local Lab head: `82c091d5729105e3bdded87deddda6752cf10248`
- reviewed remote Lab head: `6805ff40b981f85abf11660e655e4bfd6b3499e5`
- relationship: remote ahead of local by exactly one commit
- LAB-A1 RETURN SHA-256: `c61eaf0b34ef8e1410647d4273fc63d00a01d4d295ba6d81ad19a4a9ac3c57ee`
- LAB-A2 RETURN SHA-256: `f6269ecf508715090ed220d5d7fbe66995955c6c44a0796e1e271363e1c4d453`
- preserved local-state bundle SHA-256: `6c388ded738c289c9dc2d26b63544f9bb0bcbed9e9c461d48f0b42f0d3da375c`
- preserved remote-state bundle SHA-256: `24076cf0daf4849ea7f8438902a368c9f8d4d34e2378186f59c6f6130ef61a73`

The 2026-09-02 records remain historical snapshots and are intentionally not rewritten.

## Cleanup boundary

Termux cleanup remains blocked until Lab remote verification, essential-artifact preservation, and cleanup inventory gates are independently closed.
