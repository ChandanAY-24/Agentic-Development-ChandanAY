# GEMINI.md — SDD-Vibe 1-in-2 Single Workflow Agent Instructions
### Hybrid Sensory Prototyping + Spec-Driven Development (SDD) & TDD Engineering Protocol

> **Canonical System Instruction:** This document defines the operational directives for Google Antigravity, Gemini CLI, and autonomous coding agents operating within this **1-in-2 Single Workflow (`SDD-Vibe`)** project.

---

## 1. Prime Directives for SDD-Vibe (1-in-2 Single Workflow)

1. **Unified 4-Phase Hybrid Staged Pipeline:**
   - **Phase 1 — Architecture & Vibe Discovery:** Establish domain knowledge, HLD/LLD (`docs/system-architecture.md`), product/aesthetic tokens (`docs/product.md`, `docs/design.md`, `docs/plan.md`), and living prompts (`docs/prompts.md`) before writing code.
   - **Phase 2 — Frontend-First Sensory Demo & Living Spec:** For web/UI applications, build the frontend first (UI components, layout, responsiveness, mock/client state) with `PROTOTYPE` → `DRAFT` living specs in `docs/features/`. Launch a live demo (`/run-ca-agent` at `:3000`) and iterate via conversational vibe-tuning until visually approved.
   - **Phase 3 — Formal Spec Lock & TDD Red-Green-Refactor:** Lock feature specs (`IN REVIEW` → `APPROVED`, indexed in `docs/spec.md`, approved in `docs/approvals/`), verify traceability (`/spec-check-ca-agent`), write failing tests first (`RED` via `/testing-ca-agent`), implement minimal backend/persistence/auth/logic (`GREEN` via `/tdd-ca-agent` and `/implement-ca-agent`), and refactor cleanly.
   - **Phase 4 — Quality Audit & Production Ship:** Execute `/review-ca-agent`, `/verify-ca-agent`, `/security-audit-ca-agent`, and `/release-check-ca-agent` before shipping.

2. **Step-by-Step Spec Development Pacing:**
   - **Never develop all core features at once.**
   - Implement strictly one feature specification at a time (`FEAT-###`).
   - Complete the full cycle, pass all automated tests, update documentation (`docs/task.md`, `docs/error-tracker.md`), and only then proceed to the next spec.

3. **Mandatory Spec Inquiry (Flat vs. Modular):**
   - When initiating a new feature specification, the agent **MUST ALWAYS ask the developer first**:
     > *"Would you prefer this specification in **Flat format** (`docs/features/NNN-name.md`) or **Modular format** (`docs/features/NNN-name/{feature,acceptance,test-plan}.md`)?"*
   - If the developer does not specify, default by complexity tier:
     - Tier 1 (Easy, 1–2 files): Flat format.
     - Tier 2 (Intermediate, 3–6 files): Flat format.
     - Tier 3 (Hard / Complex, 7+ files): Modular format.

4. **Strict TDD Implementation Cycle (Red → Green → Refactor):**
   - **Red (`/testing-ca-agent`):** Write failing tests mapped to each `AC-FEAT###-##` and confirm they fail with expected error messages.
   - **Green (`/tdd-ca-agent` / `/implement-ca-agent`):** Write the minimal production code necessary to turn all tests green.
   - **Refactor:** Clean architecture, remove duplication, and guarantee 100% passing tests.

5. **System Design & Technical Architecture:**
   - Consult `docs/system-architecture.md` for High-Level Design (HLD), Low-Level Design (LLD), scalability, caching hierarchy, data consistency (ACID vs. BASE), and asynchronous message queuing before modifying services or database schemas.
   - Consult Section 5 of `docs/prd.md` for technical requirements guidelines.

6. **Mandatory Development Logging (`logs/` Folder):**
   - **Always maintain proper log files (`*.log`) during development** inside a separate, dedicated `logs/` directory at the project root (`logs/dev.log`, `logs/test.log`, `logs/server.log`, `logs/error.log`).
   - Never write loose log files into source code or root folders.
   - Sanitize all credentials, tokens, and PII prior to logging. Keep directory tracked via `logs/.gitkeep` and git-ignore `logs/*.log`.

7. **Pre-Step 5 Domain Knowledge & System Design Synthesis:**
   - Before executing Step 5 (Prompt 1: Master Architecture), developers and agents must synthesize comprehensive domain knowledge (business rules, regulatory constraints) and system design (HLD/LLD, data models, entity relationships).
   - If not manually provided, the developer **MUST ask the AI agent** about the overall system design during the planning phase, and integrate this synthesized design directly into the first prompt.

---

## 2. Mandatory Verification Gate: Step 0 Activation

Before creating or altering codebase files:
- **Chat Dropdown:** Verify all 17 `*-ca-agent` commands appear when typing `/` (including `/team-ecosystem-ca-agent` for `agentic-team-ecosystem`).
- **Terminal CLI:** Verify command contracts: `ls .agents/commands/*-ca-agent.md`.

---

## 3. In-IDE Project-Manager-Dashboard

- Launch via `/dashboard-ca-agent` (Port `4200`).
- Styled with Shadcn UI Zinc dark theme design tokens, Radix-style Sheet dialogs, and subtle spring physics.
- The dashboard is 100% fluid across all monitor resolutions.
- Current running task (`Task 1`, `Task 2`, `IN_PROGRESS`) and latest HEAD git commit are pinned to the top.
- Dates strictly formatted in `DD-MM-YYYY` across live header clock, Task Start/Stop date chips, and git commits.
- Interactive AC Contract engine: Given/When/Then scenario inspection, test traceability, and live status cycling.

---

## 4. Documentation Conformance & Quality Checks

Run the verification suite before any commit:
```bash
python scripts/check_docs.py
python scripts/manifest.py --check
```
Both checks must report **0 errors** before any release.

---

## 5. Strict Terminology Privacy Directive

- **Never disclose, use, or write the term "Antigravity" paired with "Engineering" anywhere** across documentation, codebase, commits, responses, artifacts, or metadata.
