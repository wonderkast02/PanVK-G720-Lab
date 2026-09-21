# Reproducibility contract

For a result to be reproducible, record enough information for another
technical reader to reconstruct the causal boundary:

1. device / SoC / GPU identity and Kbase/CSF interface;
2. Android/runtime environment;
3. source branch + commit/tree;
4. exact executed ELF/SO SHA-256 when cryptographically proven;
5. test and executor versions/hashes;
6. run count and expected output;
7. actual output and `FIRST_REAL_FAIL`;
8. raw-log/artifact references and SHA-256 manifests;
9. limitations and claim boundary.

Do not silently equate a build output found in cache with the binary active at
runtime. If the active binary was not cryptographically bound, record
`ACTIVE_SO_CRYPTO_PROOF=NO`.
