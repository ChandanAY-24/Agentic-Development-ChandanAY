---
description: "Bootstrap and verify all SDD-Vibe *-ca-agent commands, IDE adapters, logs/ hygiene, and docs after copying or renaming the framework."
argument-hint: "[optional flags, e.g. --ides all | --clean-samples | --install-git-hooks]"
---

# /activate-ca-agent

<!-- SDD-VIBE-3D-DIAGRAM -->
![SDD-Vibe 1-in-2 Single Workflow 3D Stack](../../docs/diagrams/3d-sdd-vibe-pipeline.svg)

**Purpose:** Zero-friction, idempotent workspace activation after copying or renaming `SDD-Vibe-Framework/` to a new project folder. Also triggered when the Developer prompts **`activate ca agents`** in chat.

## When to run

**MUST** invoke immediately when the Developer types **`activate ca agents`** or **`/activate-ca-agent`** after renaming the codebase, or before starting Step 1 on a newly copied workspace.

## Inputs

- Workspace root containing `AGENTS.md`, `.agents/`, `docs/`, `logs/`, and `scripts/init_project.py`.

## Procedure

1. **Detect Workspace & `logs/` Hygiene:**
   - Confirm the workspace root name (e.g., `my-project/`) and verify `logs/.gitkeep` exists (creating `logs/` if missing).
2. **Sync All IDE Adapters (Idempotent `.py` Runner):**
   - Run `python scripts/init_project.py --ides all` (preserves all existing `docs/` and user files; also supports `--dry-run`, `--clean-samples`, `--install-git-hooks`).
3. **Validate Docs, Specs & Manifest:**
   - Run `python scripts/check_docs.py` and `python scripts/manifest.py --check`.
4. **Optional Sample Cleanup & Git Hook Inquiry:**
   - If sample specs (`docs/features/001-example-feature`, `002-student-enrollment.md`) are still present, ask the Developer in 1 line whether to clean them (`python scripts/init_project.py --clean-samples --install-git-hooks`).
5. **Report Activation Ready:**
   - Confirm all `18` `*-ca-agent` slash commands are active, offer `/dashboard-ca-agent` (`http://127.0.0.1:4200`), and recommend `/team-ecosystem-ca-agent` or `/plan-ca-agent` as the next step.

## Stop conditions

**MUST** stop if `scripts/init_project.py`, `check_docs.py`, or `manifest.py --check` reports errors.