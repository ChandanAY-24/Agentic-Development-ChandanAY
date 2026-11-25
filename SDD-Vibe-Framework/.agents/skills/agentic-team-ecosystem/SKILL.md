---
name: agentic-team-ecosystem
description: "Optional default-installed 14-team Agentic AI Development Ecosystem for SaaS, E-commerce, Brand, Software, App, ML/DL/Data Science, Computer Vision, and OS projects across Claude, Codex, Antigravity, Cursor, Windsurf, and Copilot."
---

# Skill: agentic-team-ecosystem

**Purpose:** Provide a complete, **optional (developer-choice)**, cross-IDE 14-team Agentic AI Development Ecosystem bundled by default in `SDD-Vibe-Framework`. It auto-triggers only the required Group Main Agents, Team Coordinators, and Sub-Agents step by step based on project type and SDD-Vibe phase.

> **Developer Choice & Cross-Harness Portability:** Installed by default in `.agents/skills/agentic-team-ecosystem/` so every developer using `SDD-Vibe-Framework` across **Claude Code, Codex, Antigravity, Cursor, Windsurf, OpenCode, Trae, or VS Code** can invoke it on demand—or ignore it and use standard SDD-Vibe commands.

---

## Trigger & Auto-Activation

- **Explicit Trigger:** Invoke via `/team-ecosystem-ca-agent` or by referencing `agentic-team-ecosystem`.
- **Automatic Context Trigger:** When active on a project, the **Main Agent (Orchestrator)** inspects the project domain and current SDD-Vibe phase, then activates only the relevant **Group Main Agent(s)** and **Team Sub-Agents**—never loading all 14 teams into context at once.
- **Intuition, Frequency & Ranking Rule:** Never load references, skills, or external plugins randomly. Activate **at most 1–3 curated tools per step** based on project frequency and bottleneck intuition, picking **Rank #1** per category from trusted sources only (see [07-curated-external-skills-registry.md](references/07-curated-external-skills-registry.md)).

### Supported Domain Tracks (Auto-Detected)

| Domain Track | Auto-Activated Focus |
|---|---|
| **SaaS & Web Apps** | Multi-tenant architecture, BaaS/API gateway, auth/RBAC, billing/payments, UI/UX sensory demo, CI/CD |
| **E-commerce & Brand/Product/Service** | Brand discovery & identity, customer psychology, packaging, SEO/AEO/GEO, CRM/lead outreach, payment proposals |
| **Software & App Development (Mobile/Desktop)** | Cross-platform/native architecture, offline/sync, store packaging, device/E2E testing |
| **ML / Deep Learning / Data Science** | Dataset curation, feature engineering, model training/fine-tuning, RAG/LangGraph/LangSmith, model evals & drift |
| **Computer Vision (CV)** | Vision datasets, annotation quality, inference latency/throughput, edge/GPU deployment, visual evals |
| **Operating System (OS) & Systems** | Kernel/scheduler/memory/driver LLD, HAL, QEMU/VM test harness, memory-safety & privilege-boundary audits |

---

## Command Hierarchy

1. **Developer (Human Authority)** — Sets vision, answers discovery/grill questions, approves gates & specs.
2. **Main Agent (Ecosystem Orchestrator)** — Classifies domain, enforces step-by-step gates, switches models/context windows, reports to Developer.
3. **Team 14: Manual Workflow Guider Agent** — Runs alongside the Main Agent to give the Developer clear step-by-step "what to do next" guidance.
4. **4 Group-Wise Main Agents** — Coordinate **14 Specialized Teams** (see [references/01-hierarchy-and-auto-triggers.md](references/01-hierarchy-and-auto-triggers.md)).

---

## Step-by-Step Gated Pipeline (Mandatory)

Never skip steps. Each step ends with a **Developer Report & Gate Check**:

- **Step 0 — Intake & Domain Classification:** Main Agent + Team 14 classify domain track and select active teams.
- **Step 1 — Discovery, Grilling & Business Viability:** Team 2 (Research) + Team 12 (Business) + Team 13 (Marketing, if Brand/Product).
- **Step 2 — Architecture, Diagrams & Spec Planning:** Team 2 produces HLD, LLD, DFD, UML, Use-Case, Workflow, Control-Flow, DB schema, tech stack, and token/model plan.
- **Step 3 — Frontend / Interface Design & Sensory Demo:** Team 3 (Design) + Team 4 (Dev UI) build interactive demo (`:3000` or CLI/VM/app preview).
- **Step 4 — Post-Design Kanban & Google Sheet Sync:** Team 1 initializes Kanban board + Google Sheet export (`task_id`, `start_date`, `stop_date`, `status`, `sign_off`) synced with `docs/task.md`.
- **Step 5 — Formal Spec Lock & Core Engineering (TDD):** Team 4 implements core/backend/AI/CV/OS under Red-Green-Refactor TDD and `logs/`.
- **Step 6 — Testing, Security, Review & QA Gates:** Team 5 (Testing) → Team 6 (Security) → Team 7 (Review) → Team 8 (QA).
- **Step 7 — Documentation & Brand/Marketing Packaging:** Team 11 (Docs/PPT/PRD) + Team 13 (Brand guidelines, SEO/AEO/GEO, CRM/ads).
- **Step 8 — Deployment Operations:** Team 9 (Docker, Nginx, Redis, AWS/VPS/Vercel/Render, scaling, sharding, rate limiting).
- **Step 9 — 24×7 Maintenance & Growth:** Team 10 (24×7 monitoring & vulnerability escalation to Team 4) + Team 12 & Team 13.

---

## Progressive Disclosure Playbooks (Load Only What You Need)

- [01-hierarchy-and-auto-triggers.md](references/01-hierarchy-and-auto-triggers.md) — 4-tier hierarchy, auto-trigger matrix, cross-harness portability, and **Team 14 (Manual Workflow Guider)**.
- [02-discovery-design-dev-teams.md](references/02-discovery-design-dev-teams.md) — **Team 1** (PM/Kanban), **Team 2** (Research/REA/Architecture/Evals), **Team 3** (Frontend Design), **Team 4** (Dev/AI/RAG/Security-first skills).
- [03-testing-security-review-qa-ops-teams.md](references/03-testing-security-review-qa-ops-teams.md) — **Team 5** (Testing), **Team 6** (Security Testing), **Team 7** (Code Review), **Team 8** (QA), **Team 9** (Deployment Ops), **Team 10** (24×7 Maintenance).
- [04-docs-business-marketing-teams.md](references/04-docs-business-marketing-teams.md) — **Team 11** (Documentation), **Team 12** (Business & Data Analyst), **Team 13** (Marketing & Brand).
- [05-brand-marketing-proposals.md](references/05-brand-marketing-proposals.md) — Brand discovery prompts, 5-phase proposal, 5-stage payment breakdown, and brand research checklist.
- [06-kanban-gsheet-and-token-ops.md](references/06-kanban-gsheet-and-token-ops.md) — Google Sheet Kanban schema (post-Frontend Design), token optimization, context window switching, and model switching.
- [07-curated-external-skills-registry.md](references/07-curated-external-skills-registry.md) — Trust-tiered, category-ranked, intuition & frequency-driven external skills/tools registry (`grill-me`, `superpowers`, `claude-mem`, `playwright`, `semgrep`, `ui-ux-pro-max`, etc.).

---

## Restrictions

- **MUST NOT** alter `APPROVED` specs in `docs/features/` without formal change control (`/change-request-ca-agent`).
- **MUST NOT** blindly install external GitHub skills/plugins without Team 4 / Team 6 security vetting first.
- **MUST** maintain all runtime/test/error logs inside `logs/*.log` with PII/secrets redacted.
- **MUST** report real command/test evidence (never fabricated) to the Developer at every gate.
