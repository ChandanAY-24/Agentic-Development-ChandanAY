# AI-Powered Project Development — Universal Custom Slash Commands for 1-in-2 Single Workflow (`SDD-Vibe`)
### Operational Reference for `.agents/commands/` Across All 4 Hybrid Pipeline Phases

**Framework:** SDD-Vibe (1-in-2 Single Workflow)  
**Author / Engineering Lead:** Chandan Adhikary  
**Version:** 2.0.0 (Production-Grade Universal Release)  
**Applies to:** Claude Code, Cursor, Windsurf, Antigravity, GitHub Copilot, Codex, Trae, VS Code with AI Agents  

---

## 1. Command Pipeline Overview

All 17 custom slash commands carry the `-ca-agent` suffix to prevent collisions with IDE-native commands and map cleanly across the 4-phase **SDD-Vibe** pipeline:

```text
+---------------------------------------------------------------------------------+
|                    1-IN-2 SINGLE WORKFLOW COMMAND PIPELINE                      |
+---------------------------------------------------------------------------------+
|  PHASE 1 (Discovery) : /plan-ca-agent --> /task-ca-agent                        |
|  PHASE 2 (Vibe UI)   : /implement-ca-agent (UI) --> /run-ca-agent (:3000 Demo)  |
|  PHASE 3 (Spec+TDD)  : /spec-check-ca-agent --> /testing-ca-agent (RED)         |
|                        --> /tdd-ca-agent (GREEN/REFACTOR)                       |
|  PHASE 4 (Audit)     : /review-ca-agent --> /verify-ca-agent                    |
|                        --> /security-audit-ca-agent --> /release-check-ca-agent |
|  CONTINUOUS TOOLS    : /dashboard-ca-agent | /change-request-ca-agent           |
|                        /errorlogs-ca-agent | /gitlogs-ca-agent | /handoff-ca-agent
|                        /team-ecosystem-ca-agent (Optional 14-Team Orchestrator) |
+---------------------------------------------------------------------------------+
```

---

## 2. Complete 17-Command Operational Reference

| Slash Command | Phase | Operational Purpose & Contract |
|---|---|---|
| `/plan-ca-agent` | Phase 1 | Read-only research, domain & HLD/LLD synthesis, `docs/plan.md` & plan artifact generation. |
| `/task-ca-agent` | Phase 1 | Initializes atomic task entries in `docs/task.md` and `docs/phases.md`. |
| `/run-ca-agent` | Phase 2 & 3 | Starts local dev/backend server, verifies live UI sensory demo (`:3000`) and runtime health. |
| `/spec-check-ca-agent` | Phase 3 | Validates `docs/features/` (Flat/Modular), `AC-*` Given/When/Then, and `docs/spec.md` indexing. |
| `/change-request-ca-agent` | Phase 3 | Impact assessment (`CR-###`) and spec revision before altering `APPROVED` contracts. |
| `/testing-ca-agent` | Phase 3 | Runs targeted test suites; confirms expected `RED` failures before backend implementation. |
| `/tdd-ca-agent` | Phase 3 | Executes Red-Green-Refactor cycle against approved `AC-*` contracts. |
| `/implement-ca-agent` | Phase 2 & 3 | Scope-restricted implementation (UI shell in Phase 2; spec-locked code in Phase 3). |
| `/review-ca-agent` | Phase 4 | Pre-commit diff, lint, and traceability review. |
| `/verify-ca-agent` | Phase 4 | Objective verification scorecard against `AC-*` and `TEST-*` evidence. |
| `/security-audit-ca-agent` | Phase 4 | SAST scan, secret leak detection, and auth/RLS audit. |
| `/release-check-ca-agent` | Phase 4 | Final ship/no-ship gate (`docs/release-checklist.md`, `check_docs.py`, `manifest.py`). |
| `/dashboard-ca-agent` | Continuous | Launches the In-IDE Project-Manager-Dashboard on `http://127.0.0.1:4200`. |
| `/errorlogs-ca-agent` | Continuous | Analyzes `logs/error.log` and `docs/error-tracker.md` for root-cause triage. |
| `/gitlogs-ca-agent` | Continuous | Audits git commits against authorized task IDs and spec references. |
| `/handoff-ca-agent` | Continuous | Generates verifiable engineering handoff dossier (`docs/handoff.md`). |
| `/team-ecosystem-ca-agent` | Continuous (First Choice) | Activates the **first-choice** 14-team `agentic-team-ecosystem` skill step by step across SaaS, E-commerce, Brand, Software, App, ML/DL/DS, CV, and OS builds, triggering SDD-Vibe commands at each gate. |

---

## 3. Invoking `/team-ecosystem-ca-agent` (First Choice & Custom Features)

- **New Project / Full Feature Build:** `/team-ecosystem-ca-agent saas` (or `ecommerce`, `brand`, `software`, `app`, `ml`, `cv`, `os`) — starts Step 0 with Team 14 guiding Steps 0–9 and triggering `/plan-ca-agent`, `/task-ca-agent`, `/run-ca-agent`, `/dashboard-ca-agent`, `/spec-check-ca-agent`, `/testing-ca-agent`, `/tdd-ca-agent`, `/review-ca-agent`, `/security-audit-ca-agent`, and `/release-check-ca-agent` at their exact gates.
- **Jump to a Specific Step:** `/team-ecosystem-ca-agent step-3` (Frontend Sensory Demo) or `/team-ecosystem-ca-agent ml step-5` (TDD & ML Evals).
- **Adding a Custom Feature Mid-Project or Post-Launch:** Run `/change-request-ca-agent` (if altering an `APPROVED` spec), then `/team-ecosystem-ca-agent <feature-or-domain>` so the new feature follows the complete SDD-Vibe + external-skill workflow.
