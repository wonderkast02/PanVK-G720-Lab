# Tessellation
**PROVEN direct path:** `SW-VS → TCS → COUNT → PREFIX → WITH_COUNTS → generated indexed indirect draw → TES/IDVS → raster`.

Historical evidence: 64×64 triangle 1352 covered / 2744 clear / 0 mismatches; tesscoord 12/12; varying 12/12; fractional-even 19/19; fractional-odd 29/29; quad 21/21; isoline 28/28; padded WG64 3×1/3×2/66×1 pass.

Fixes kept: predicate padded SW-VS lanes; recompute TES output bases after `poly_nir_lower_tes` when needed.

**OPEN before advertisement:** app indirect tessellation; simultaneous-use/poly_heap lifetime; sequential/multiple draws/dirty state; queries/XFB; discard/winding/limits/invariance; focused CTS/regression.
