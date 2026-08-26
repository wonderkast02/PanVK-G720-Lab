# Continuity — Dev → Dev 2 → current
Consolidated project memory from the earlier **Dev** and **Dev 2** threads through this chat. Raw local reports are imported+hashed when present; unavailable originals are not fabricated.

## Reference target — PROVEN
POCO X8 Pro/klee; MT6899; Mali-G720 MC8; `/dev/mali0`; kbase r49p1/CSF; UK 1.30; GPU ID `0xc8700010`; vendor `0x13b5`; CSF `0x03060000`; 8 groups/64 streams; instruction features `0x71`.

## Source
Main repo `wonderkast02/panvk-g720-kbase-csf`, branch `ci`, published SHA `0521a3257628e811cfead6b5a9753e9f705e2f31`. Direct PanVK→kbase/CSF is current architecture.

## Proven milestones
Real G720 MC8 GPU execution. Direct libpoly tessellation completed SW-VS→TCS→COUNT→PREFIX→WITH_COUNTS→TES/IDVS→raster. SW-VS padded WG64 OOB fixed by predication, not local_size=1. TES point-mode IO bases recomputed after lowering. Oracles: triangle 1352/1352 zero mismatch; tesscoord 12/12; varying 12/12; even 19/19; odd 29/29; quad 21/21; isoline 28/28.

`tessellationShader` remains false in published checkpoint. OPEN: indirect; simultaneous-use/poly_heap; multiple/dirty draws; queries/XFB; winding/discard/limits/invariance; focused CTS.

## Preserved decisions
Old fixed 4GiB VA diagnosis is obsolete. `shader_present` is a mask; never hardcode `0xff`. Need real MMU evidence before VA changes. Sky1 40-bit VA/WLS work is prior art, not blind patch material.

DISCARDED: generic cache/coherency as old TCS root cause; FAU16B primary cause; TP-only corruption; `INDEX_BUFFER=tp->index_buffer` general fix; local_size=1 permanent SW-VS fix; blind Sky1 40-bit cherry-pick.

## Bionic/Winlator
Clean NDK r29 target path with native host mesa_clc/vtn_bindgen2/panfrost_compile; target LLVM disabled. kbase-only compile-time backend dispatch fixed unresolved panthor refs. Final clean SO SHA256 `4d1bf7958b7ddc899122bd382bc77eca7aca799d8bd74360e714ea63b9cc2263`; TZST SHA256 `670dd902f663983c7bdbcab64ddd33460ed2339a12a5b465e3f0ad1bfc67d785`. Winlator enumerated PanVK and returned 163 extensions.

## External Lord/MC7
64-bit DXVK evidence reached PanVK device/queue, AHB/dma-buf and swapchain; max D3D FL10_1 observed. Separate 32-bit feature-not-present remains OPEN.

## Current continuation
Before Lab bootstrap, local source restored the previously validated direct tess path by removing three temporary gates from `panvk_vX_cmd_draw.c`; feature advertisement remains false; both known Linux builds passed. Treat this as local development state until hardware revalidation/review.
