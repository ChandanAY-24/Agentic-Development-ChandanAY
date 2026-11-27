# AGENTS.md

> **Canonical specification:** this file, `docs/constitution.md` and `docs/rules.md` govern every AI coding agent session across Claude Code, Cursor, Windsurf, Antigravity, OpenCode, Codex, Trae, and VS Code.

- Autonomous, non-interactive agents (e.g. CI, batch runs) **MUST NOT** make speculative changes without human approval.
- An interactive agent working on a task **MUST** stop and ask when an edit touches protected policy (`docs/constitution.md`, `docs/rules.md`, `AGENTS.md`) or when an ambiguity affects architecture, security or data isolation.

**SDD-Vibe 1-in-2 rule:** UI/UX discovery may iterate in `PROTOTYPE` / `DRAFT` (`docs/plan.md`, `docs/prompts.md`, frontend sensory demo via `/run-ca-agent`), but production backend, persistence, auth, and release behavior **MUST** be governed by an `APPROVED` feature contract version (indexed in `docs/spec.md`, approval in `docs/approvals/`) and verified via Red-Green-Refactor TDD.

Canonical `.agents/` contracts (`.agents/commands/`, `.agents/skills/`) serve as the universal cross-IDE source of truth; IDEs dynamically configure their own settings at runtime.

## Sovereign Agent Configuration & Commands

- **MUST** treat **`activate ca agents`** (natural-language prompt) or **`/activate-ca-agent`** as the collision-free workspace activation command: when invoked after copying/renaming the codebase, run `python scripts/init_project.py --ides all`, `python scripts/check_docs.py`, and `python scripts/manifest.py --check`, verify `logs/`, ask in 1 line whether to clean sample features (`--clean-samples`), and offer `/dashboard-ca-agent`.
- **MUST** verify custom slash commands (`.agents/commands/*-ca-agent.md`) in the chat dropdown and terminal CLI before creating or altering application code.
- **MUST** maintain proper development log files (`*.log`) during all development, test runs, and debugging inside a separate `logs/` directory.
- **MUST** establish complete domain knowledge and system design before Step 5 (First Prompting); if not manually prepared, ask the agent to formulate system design during planning and integrate it into Prompt 1.
- **MUST** enforce staged web development (Frontend-First): build frontend first, verify design and features completely via interactive demo run (`/run-ca-agent`), then lock formal specs and proceed to TDD backend persistence, security, and maintenance.
- **MUST** preserve canonical project guidelines, approved specifications, and repository standards.
- **MUST** rely on canonical `AGENTS.md` and `.agents/` as the single source of truth across all coding platforms.
- **MUST NOT** assume external tools or uninstalled third-party skills exist.
- **MUST** request approval before modifying process guidelines or enabling external integrations.
- **SHOULD** maintain portability across Claude Code, Cursor, Windsurf, Antigravity, OpenCode, Trae, Codex, and terminal agents.

## Agent–Developer Transparency Contract

- **MUST** tag every domain/technical claim as `[VERIFIED: <source/file>]` or `[ASSUMPTION — NEEDS CONFIRMATION]`; never present guesses as verified facts.
- **MUST** complete **Pre-Start Pin-Point Grilling & Domain Research** (`requirements-analysis` / `/plan-ca-agent`) until `0` `CRITICAL` ambiguities remain before generating PRDs, architecture, or feature specs.
- **MUST** follow the **Zero-Confusion Universal Skill Activation Policy** (`docs/skills.md` + `07-curated-external-skills-registry.md`): never silently load external skills; disclose `Skill | Ecosystem | Why Now | Mode` and wait for developer `"yes"` on Mode 2/3 skills.
- **MUST** surface blockers, failed checks, and architectural trade-offs immediately (no silent workarounds) and log decisions in `docs/decision-log.md`.

**Rule:** IDE switching must never silently change project specifications, engineering guidelines, testing policies, security controls, or repository structure.
