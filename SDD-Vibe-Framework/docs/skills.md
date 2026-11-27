# Skills Registry & Developer Choice Policy

> **Document class:** Controlled process guideline  
> **Framework:** SDD-Vibe  
> **Guideline baseline:** 2.0.0  
> **Status:** Active Standard

<!-- SDD-VIBE-3D-DIAGRAM -->
![SDD-Vibe 1-in-2 Single Workflow 3D Stack](diagrams/3d-sdd-vibe-pipeline.svg)

## Purpose

Registry of portable agent skills and third-party skills installation policy.

## Agent read trigger

**MUST** read or consult this file: Before skill creation, invocation, or importing external capabilities.

---

## 1. Developer Choice Policy for External Skills

- **External Skills are Developer Choice:** Pre-bundling arbitrary third-party guidelines (e.g., `andrej-karpathy-skill` or unverified GitHub skills) is strictly avoided. The repository template contains only core deterministic engineering skills.
- **GitHub Installation on Demand:** Developers may freely install external skills directly from GitHub repositories or their personal IDE plugin manager if desired.
- **No Direct Hardcoded Dependencies:** Agents must never require or mandate third-party external skills unless explicitly configured and installed by the project developer.

---

## 2. Core Repository Skills Matrix (18 Portable Skills)

| Skill Name | Location | Primary Operational Scope |
|---|---|---|
| `requirements-analysis` | `.agents/skills/requirements-analysis/` | Pre-start pin-point developer grilling, domain research, and ambiguity elimination (`0` blockers gate). |
| `prd-writer` | `.agents/skills/prd-writer/` | Authors/updates `docs/prd.md` with measurable outcomes and technical requirements. |
| `architecture-review` | `.agents/skills/architecture-review/` | Reviews HLD/LLD, service boundaries, data consistency, and `docs/system-architecture.md`. |
| `task-planner` | `.agents/skills/task-planner/` | Generates granular, atomic tasks mapped to approved specifications in `docs/task.md`. |
| `spec-validator` | `.agents/skills/spec-validator/` | Validates `docs/features/` against canonical AC IDs and Given/When/Then contracts. |
| `api-contract-review` | `.agents/skills/api-contract-review/` | Validates API schemas, versioning, error envelopes, and `docs/apis.md` conformance. |
| `database-migration-review` | `.agents/skills/database-migration-review/` | Audits schema changes, rollbacks, indexing, and `docs/database.md` safety. |
| `ui-fidelity-review` | `.agents/skills/ui-fidelity-review/` | Verifies Phase 2 sensory demo layout, responsiveness, and `docs/design.md` fidelity. |
| `accessibility-auditor` | `.agents/skills/accessibility-auditor/` | Audits WCAG compliance, keyboard navigation, contrast, and `docs/accessibility.md`. |
| `tdd-enforcer` | `.agents/skills/tdd-enforcer/` | Enforces the Red-Green-Refactor cycle and verifies failing tests before implementation. |
| `debugging-analyst` | `.agents/skills/debugging-analyst/` | Performs root-cause analysis on runtime failures, `logs/`, and `docs/error-tracker.md`. |
| `performance-profiler` | `.agents/skills/performance-profiler/` | Profiles latency, Core Web Vitals, query/bundle budgets, and `docs/performance.md`. |
| `code-reviewer` | `.agents/skills/code-reviewer/` | Reviews code changes for security, architectural integrity, and style conformance. |
| `security-auditor` | `.agents/skills/security-auditor/` | Audits code for hardcoded secrets, injection vectors, and dependency CVEs. |
| `ml-evaluation` | `.agents/skills/ml-evaluation/` | Evaluates ML/LLM/CV model accuracy, drift, hallucination thresholds, and dataset lineage. |
| `documentation-sync` | `.agents/skills/documentation-sync/` | Keeps living `docs/`, `CHANGELOG.md`, and traceability matrices synchronized. |
| `release-validator` | `.agents/skills/release-validator/` | Verifies all quality gates before production deployments (`docs/release-checklist.md`). |
| `agentic-team-ecosystem` | `.agents/skills/agentic-team-ecosystem/` | Optional default-installed 14-team Agentic AI Development Ecosystem (auto-triggers across SaaS, E-commerce, Brand, Software, App, ML/DL/DS, CV, and OS builds). |

---

## 3. Zero-Confusion Universal Skill Activation Policy (Core, Antigravity, Vercel, Claude & GitHub)

To guarantee **0 confusion** about which skill to use at a particular time vs. when to wait for explicit developer instruction, all agents **MUST** follow the **3 Activation Modes** and **Ecosystem Precedence Rule**:

### Ecosystem Precedence (0-Overlap)
1. **Built-in Core (`.agents/skills/` + `*-ca-agent` commands):** Always used first for SDD-Vibe process, grilling, spec validation, TDD, review, and release gates.
2. **Platform-Native (Antigravity / Vercel / Claude Official):** Used next only when the workspace stack matches (e.g., `vercel-labs/agent-skills` for React/Next.js/Vercel; Antigravity native skills for Firebase/Flutter/Gemini/BigQuery/Chrome DevTools; `anthropics/skills` for Claude baseline workflows).
3. **GitHub / OSS Tier 2–3:** Used only when neither Core nor Platform-Native covers the specialized need (see `.agents/skills/agentic-team-ecosystem/references/07-curated-external-skills-registry.md`).

### 3 Strict Activation Modes
- **Mode 1 — Auto-Active Core / Stack-Native:** Core `.agents/skills/*` and active IDE-native platform skills matching the current phase/stack. Still disclose activation transparently.
- **Mode 2 — Phase-Gate Auto-Suggest (Consent Required):** At a matching phase gate, the agent **MAY suggest at most 1 Rank #1** external skill (Claude, Vercel, or GitHub) using the **Transparent Skill Disclosure** format and **MUST** wait for developer `"yes"` before using it.
- **Mode 3 — Developer-Instructed Only (Never Auto-Suggested):** Niche, high-privilege, or aesthetic-opinionated external tools (e.g., `obscura`, `OpenWA`, `OpenBot`, `SecLists`, `glass-ui`, `react-spline`, `REA`, `postiz-app`) **MUST NOT** be suggested or triggered unless the developer explicitly asks for that capability.

### Mandatory Transparent Skill Disclosure
Whenever activating or suggesting any skill, disclose:
`Skill: <name> | Ecosystem: <Core / Antigravity / Vercel / Claude / GitHub> | Why Now: <exact phase & feature> | Mode: <Mode 1 / Mode 2 (awaiting "yes") / Mode 3 (developer-instructed)>`

---

## 4. Normative Rules

- **MUST** evaluate security and privileges before running any third-party skill installed from GitHub.
- **MUST NOT** allow a skill to alter an `APPROVED` specification without formal human review.

## Evidence and change control

- **MUST** record owner, revision/date, relevant approval reference, and traceable evidence in the applicable project instantiation.
- **MUST** route changes to process rules through `docs/guideline-CHANGELOG.md` and formal baseline revision; route feature behavior through approved versioned specs and `docs/CHANGELOG.md`.
- **SHOULD** keep links to canonical artifacts instead of duplicating definitions.

## SDD-Vibe enforcement

- **MUST** verify the latest approved feature spec version before changing implementation.
- **MUST** stop if this document conflicts with approved guidelines; pursue a guideline revision rather than an implicit exception.