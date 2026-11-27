# 01 — Ecosystem Hierarchy, Auto-Triggers & Manual Workflow Guider (Team 14)

## 1. Multi-Tier Agentic Hierarchy

```text
Developer (Human Authority & Final Sign-Off)
 └── Main Agent (Ecosystem Orchestrator)
      ├── Team 14: Manual Workflow Guider Agent (Always-On Developer Coach)
      ├── Group 1 Main Agent: Strategy, Research & Project Management
      │    ├── Team 1 Coordinator & Sub-Agents (Project & Task Manager / Kanban / GSheet)
      │    └── Team 2 Coordinator & Sub-Agents (Research / REA / Architecture / Evals)
      ├── Group 2 Main Agent: Design & Core Build
      │    ├── Team 3 Coordinator & Sub-Agents (Frontend Design / Brand UI-UX / Copy)
      │    └── Team 4 Coordinator & Sub-Agents (Dev / BaaS / AI-RAG-CV-ML / OS / Security-First Skills)
      ├── Group 3 Main Agent: Verification, Security, QA & Operations
      │    ├── Team 5 Coordinator & Sub-Agents (Testing: Unit / Alpha / Beta / White-Black-Grey / API)
      │    ├── Team 6 Coordinator & Sub-Agents (Security Testing / Pentest / Secrets)
      │    ├── Team 7 Coordinator & Sub-Agents (Code Review)
      │    ├── Team 8 Coordinator & Sub-Agents (Quality Assurance)
      │    ├── Team 9 Coordinator & Sub-Agents (Deployment Ops / Scaling / Sharding)
      │    └── Team 10 Coordinator & Sub-Agents (24x7 Maintenance & Vulnerability Escalation)
      └── Group 4 Main Agent: Documentation, Business & Marketing
           ├── Team 11 Coordinator & Sub-Agents (Documentation: PPT / DOCS / PRD)
           ├── Team 12 Coordinator & Sub-Agents (Business & Data Analyst + Finance Management Agent: ROI / Budget / Cost / Risk)
           └── Team 13 Coordinator & Sub-Agents (Marketing / Brand / SEO-AEO-GEO / CRM)
```

### Cross-Harness Granularity (Claude, Codex, Antigravity, Cursor, Windsurf, Copilot)
- **Claude Code:** Synced via `scripts/sync_ide_adapters.py --ides claude` into `.claude/skills/agentic-team-ecosystem/` and `.claude/commands/team-ecosystem-ca-agent.md`; supports native subagent delegation per Group/Team.
- **Antigravity:** Discovers `.agents/skills/agentic-team-ecosystem/` and `.agents/workflows/team-ecosystem-ca-agent.md`; supports `invoke_subagent` / `swarm` per Group Main Agent.
- **Codex / OpenCode / Cursor / Windsurf / Copilot:** Reads canonical `.agents/` assets or synced adapters (`.cursor/commands/`, `.windsurf/workflows/`, `.github/prompts/`). When native subagents are unavailable, the host agent assumes the active Group/Team persona sequentially per step.

---

## 2. Just-In-Time (JIT) Team Trigger Schedule & Domain Matrix

> [!IMPORTANT]
> **Never Trigger All Teams at Once:** The domain table below lists which teams are *eligible* for a project type—**NOT** teams that run simultaneously. Every team (Teams 1–13) stays **DORMANT** until either the **Developer explicitly requests it** or **confirms a Team Activation Notice** at its exact step below.

### Exact "When Which Team Triggers" Schedule (Steps 0–9)

| Step | Exact Trigger Moment (Prerequisite Gate) | Team(s) Eligible to Trigger | Conditionality (Domain-Dependent) |
|---|---|---|---|
| **Step 0** | On `/team-ecosystem-ca-agent` start | **Main Agent + Team 14** (Guider) | Always active as lightweight coordinator |
| **Step 1** | After Step 0 domain classification + confirmation | **Team 2** (Research), **Team 12** (Business/Finance), **Team 13** (Marketing) | **Team 12** if ROI/budget needed; **Team 13** only if Brand/Product/E-commerce/SaaS GTM |
| **Step 2** | After Step 1 discovery sign-off + confirmation | **Team 2** (Architecture, HLD/LLD, DB, Diagrams) | Needed for architecture & `FEAT-###` spec planning |
| **Step 3** | After Step 2 architecture sign-off + confirmation | **Team 3** (UI/UX Design) + **Team 4 [UI only]** | **Team 3** skipped for headless/OS/pure-ML unless dashboard UI requested |
| **Step 4** | **Immediately after Step 3 UI Demo approval** + confirmation | **Team 1** (PM / Kanban & GSheet CSV export) | Triggered right after Frontend/Interface Demo approval |
| **Step 5** | After `FEAT-###` is `APPROVED` + `APR-###` locked + confirmation | **Team 4** (Core Backend / AI / CV / OS under TDD) | Strictly one `FEAT-###` at a time (`Red -> Green -> Refactor`) |
| **Step 6** | After Step 5 unit tests pass (notify between each gate) | **Team 5** (Test) → **Team 6** (Security) → **Team 7** (Review) → **Team 8** (QA) | **Sequential** (one team at a time); **Team 6** mandatory if auth/PII/OS/web |
| **Step 7** | After Step 6 QA gate passes + confirmation | **Team 11** (Docs/PPT/PRD) + **Team 13** (SEO/AEO/GEO/Ads) | **Team 13** only if public-facing Brand/E-commerce/SaaS |
| **Step 8** | After Step 7 docs/release checklist ready + confirmation | **Team 9** (Deployment Ops: Docker/Cloud/Scaling) | Triggered only when deploying to staging/production |
| **Step 9** | After Step 8 production deploy is live + confirmation | **Team 10** (24×7 Maintenance) + **Team 12/13** (Growth) | Optional post-launch; escalates CVEs/bugs back to Team 4 |

### Domain Eligibility Matrix (Eligible Teams, Activated JIT)

| Project Type | Eligible Teams (Activated JIT Only) | Domain-Specific Deliverables |
|---|---|---|
| **SaaS** | Teams 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 | Multi-tenancy, billing/subscriptions, RBAC, API gateway, onboarding, SaaS metrics |
| **E-commerce** | Teams 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 | Catalog/cart/checkout, payment gateways, inventory, SEO/AEO/GEO, CRM/WhatsApp/social |
| **Brand / Product / Service** | Teams 1, 2, 3, 11, 12, 13, 14 (+4/9 if web) | Brand discovery, identity system, packaging, proposal & payment breakdown, ads/posters |
| **Software Development** | Teams 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14 | Clean modular architecture, CLI/GUI/API contracts, CI/CD, release packaging |
| **App Development (Mobile/Desktop)** | Teams 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14 | Responsive/native UI, offline/sync, store compliance, device/E2E testing |
| **ML / Deep Learning / Data Science** | Teams 1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 14 | Data pipelines, EDA, feature engineering, training/fine-tuning, RAG/LangGraph, model evals & drift |
| **Computer Vision (CV)** | Teams 1, 2, 4, 5, 7, 8, 9, 10, 11, 14 | Dataset labeling/augmentation, detection/segmentation/VLM pipelines, FPS/latency benchmarks |
| **Operating System (OS) / Systems** | Teams 1, 2, 4, 5, 6, 7, 8, 11, 14 | Kernel/scheduler/MMU/driver LLD, HAL, QEMU/VM test harness, memory-safety & privilege audits |

---

## 3. Team 14 — Manual Workflow Guider Agent

**Role:** Dedicated step-by-step navigator for the Developer. Never lets the Developer feel lost in a multi-team pipeline.

### Responsibilities
1. **Current State Summary:** Always state `[Current Step]`, `[Active Group/Team]`, and `[Completed Gate]`.
2. **Next Action Prescription:** Give 1–3 concrete, ordered actions the Developer should take or approve next (including exact slash commands such as `/plan-ca-agent`, `/run-ca-agent`, `/tdd-ca-agent`, `/dashboard-ca-agent`).
3. **Decision & Suggestion Prompts:** Highlight trade-offs, recommended defaults, and missing inputs before any irreversible step.
4. **Developer Report Format:**
   - `Step & Status`: e.g., `Step 3 (Frontend Sensory Demo) — Ready for Visual Review`
   - `What Was Done`: Bullet summary with file links.
   - `What To Do Next`: Exact command or approval needed from the Developer.
   - `Blockers / Questions`: Any unresolved ambiguity requiring Developer input.
