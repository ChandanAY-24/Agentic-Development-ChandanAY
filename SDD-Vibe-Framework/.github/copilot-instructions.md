# GitHub Copilot Adapter — SDD-Vibe (1-in-2 Single Workflow)

<!-- SDD-VIBE-3D-DIAGRAM -->
![SDD-Vibe 1-in-2 Single Workflow 3D Stack](../docs/diagrams/3d-sdd-vibe-pipeline.svg)

**MUST** follow root `AGENTS.md`, then `docs/INDEX.md` and the policies it lists. This file is an adapter, not an alternate authority.

- Frontend sensory discovery may iterate in `PROTOTYPE` / `DRAFT`; production backend, persistence, and auth **MUST** have `APPROVED` feature versions indexed in `docs/spec.md` with failing tests written before production code.
- **MUST** keep feature specifications in `docs/features/`; never create a `specs/` directory.
- **MUST** protect secrets, request approval for destructive or external actions and report real command output.
- Path-scoped rules: `.github/instructions/*.instructions.md`. Verify the installed Copilot version loads both files.