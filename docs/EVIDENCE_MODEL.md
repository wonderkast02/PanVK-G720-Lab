# Evidence model

Every important result should record, when applicable:

`EVIDENCE_ID`, date/time, device, SoC, GPU, GPU ID, Kbase UAPI, Android,
driver/source ref, executed SO/ELF SHA-256, test name/version, executor SHA-256,
run count, expected result, actual result, first real failure, raw-log
references, artifact hashes, limitations, claim boundary and status.

## Status vocabulary

- **VERIFIED-HW** — confirmed on real hardware.
- **VERIFIED-STATIC** — confirmed by source/build/ELF/static inspection only.
- **REPRODUCED** — reproduced in repeated controlled runs.
- **PARTIAL-PASS** — part of the contract passed; remainder is explicit.
- **BLOCKED-TRANSPORT** — blocked before the driver by transport/serializer/runtime.
- **BLOCKED-TOOLING** — instrumentation/tool failure, not a driver failure.
- **SEMANTIC-FAIL** — execution happened, expected semantics were not produced.
- **SUPERSEDED** — historically valid evidence replaced by newer authority.
- **HISTORICAL** — retained for history; not current state.
- **INVALIDATED** — later evidence demonstrated the record was incorrect.

Operational ordering:

`RAW_EVIDENCE > CLASSIFIER`
`RUNTIME > GREP`
`COMPILE > STATIC_GUESS`
`FIRST_REAL_FAIL > LATER_NOISE`
