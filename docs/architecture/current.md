# Architecture
`Vulkan app → loader/Android integration → PanVK → ARM kbase/CSF → Mali-G720`.

Target phone is direct kbase/CSF, not panthor/DRM. Historical wrapper PoC is not current architecture. Do not restore the obsolete fixed-4GiB VA diagnosis, hardcode shader mask `0xff`, or enable tessellation just to unlock a game.
