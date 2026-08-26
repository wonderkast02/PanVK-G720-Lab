# INV-2026-0003 — External 32-bit feature failure
Status: OPEN

Lord's 32-bit test reached PanVK, requested storageBuffer8BitAccess/storageBuffer16BitAccess/shaderFloat16/shaderInt8-related features, then `vkCreateDevice` returned `VK_ERROR_FEATURE_NOT_PRESENT (-8)`. Isolate the missing feature before concluding root cause.
