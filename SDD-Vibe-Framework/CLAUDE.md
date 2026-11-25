# Claude Code Adapter

**MUST** obey `AGENTS.md`, then applicable `docs/` policies and feature specs. **MUST** verify CLI version before creating native skills/hooks/commands under `.claude/`. **MUST** follow the 1-in-2 Hybrid Staged Pipeline: plan & synthesize architecture, verify frontend sensory demo first, lock formal specs, write failing tests before production backend/auth implementation, run checks, and report actual evidence.

Recommended workflow: read `docs/INDEX.md` → inspect task and contract → Phase 1 plan → Phase 2 frontend sensory demo → Phase 3 spec lock & Red-Green-Refactor tests → Phase 4 CI-equivalent checks → report. No native Claude feature is assumed installed.
