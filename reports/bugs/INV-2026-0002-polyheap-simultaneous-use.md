# INV-2026-0002 — poly_heap simultaneous use
Status: OPEN

The command buffer owns a tessellation `poly_heap`; execution resets allocator bottom. Concurrent execution of the same command buffer can race. Atomic allocation alone does not solve the reset. Compare per-execution heap vs safe GPU serialization with evidence.
