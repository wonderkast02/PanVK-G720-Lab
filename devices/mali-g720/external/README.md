# External Mali-G720 targets

Store one directory per external device.

Do not assume that MC7/MC8/MC10 devices share the same kbase, UK interface, firmware, shader mask, WSI behavior or Android linker environment.

Minimum intake:
- device/SoC/GPU core configuration;
- Android/kernel;
- GPU ID and shader-present mask when available;
- kbase/UK/CSF identity;
- PanVK commit/build hash;
- capability dump;
- test/log evidence.
