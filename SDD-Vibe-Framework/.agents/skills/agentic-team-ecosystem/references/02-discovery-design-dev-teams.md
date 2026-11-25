# 02 — Group 1 & Group 2 Teams (PM, Research, Frontend Design, Dev)

## Team 1 — Project & Task Manager Team

**Scope:** End-to-end orchestration, developer Q&A, recommendations, and Kanban task governance.

- **Orchestration & Recommendations:** Coordinate handoffs across Groups 1–4; proactively ask clarifying questions and suggest scope/priority optimizations to the Developer.
- **Post-Frontend Design Kanban & Google Sheet Trigger:** Immediately after **Step 3 (Frontend Design / Sensory Demo)** is verified, initialize the Kanban board and Google Sheet export schema (see [06-kanban-gsheet-and-token-ops.md](06-kanban-gsheet-and-token-ops.md)).
- **Task Tracker Fields (Mandatory):**
  - `task_id` (e.g., `TASK-001`), `group`, `team`, `title`, `spec_ref` (`FEAT-###`), `start_date` (`DD-MM-YYYY`), `stop_date` (`DD-MM-YYYY`), `status` (`PENDING`, `IN_PROGRESS`, `IN_REVIEW`, `COMPLETE`, `SIGNED_OFF`), `sign_off` (Developer/QA approval).
- **Sync:** Keep `docs/task.md` and `Project-Manager-Dashboard` synchronized at every state transition.

---

## Team 2 — Research & Architecture Team

**Scope:** 100% domain confidence, critical thinking, developer grilling, system design, and evaluation planning.

### Sub-Agent Capabilities
1. **Domain & Market Intelligence:** Multi-source web research, competitor/reference gathering, target user/customer personas, lead finding/generation, problem statements, pain points, and **unique differentiators** (why this product beats existing alternatives).
2. **Developer Grilling Protocol:** Challenge every assumption (scale, budget, latency, compliance, edge cases, failure modes) until requirements are unambiguous.
3. **Engineering Modes:**
   - **Forward Engineering:** Problem → Requirements (FRs & NFRs) → Architecture → Spec.
   - **Reverse Engineering (REA Agent):** Existing codebase/product/binary → Dependency & API extraction → Architecture & Gap recovery.
4. **Architecture & Diagrams (Mermaid/Markdown in `docs/system-architecture.md`):**
   - HLD (High-Level Design) & LLD (Low-Level Design)
   - DFD (Data Flow Diagram), Use Case Diagram, Workflow Diagram, UML (Class/Sequence), Control Flow Diagram
   - Coupling & Cohesion analysis, Anti-Hardcoding rules, Risk Management register
5. **Technical Deep-Dive:** Tech stack selection, Algorithms & Data Structures, Mathematical/logical problem solving, Database design (schema, indexing, storage), Resource Gathering (vetted skills, MCPs, plugins).
6. **AI/Agent Governance & Evals:** Token optimization planning, context window switching, model switching, agent guidelines, **Model Evals** & **Project Evals** (accuracy, latency, cost, hallucination rate).
7. **Domain-Specific Research Extensions:**
   - *ML / DL / Data Science / CV:* Dataset licensing, class balance, baseline metrics (mAP, F1, ROC-AUC, BLEU), compute/GPU budget.
   - *Operating Systems / Systems:* Bootloader/kernel/scheduler/memory/filesystem/driver boundaries, ISA target, interrupt & privilege rings.

---

## Team 3 — Frontend Design Team

**Scope:** Research-backed UI/UX, brand-aligned visual systems, copywriting, and interactive sensory demos.

- **Design Motivation & UI/UX Research:** User flows, wireframes, information architecture, accessibility (WCAG).
- **Visual System:** Logo, typography, font pairing, color palette (semantic tokens), spacing scale, alignment, grid, restraint & white space, visual hierarchy, texture, imagery, illustrations, graphic language, motion/animations, data visualizations.
- **Conversion & Layout Principles:** Hero sections, social proof, clear CTAs, responsive breakpoints (mobile → 4K), reusable component patterns, design templates, and UX copywriting.
- **Domain Adaptation:**
  - *SaaS / E-commerce / Brand:* Landing/storefront, pricing, checkout, brand mockups.
  - *ML / CV / Data Science:* Interactive inference/analytics dashboards, dataset/metric visualizers.
  - *OS / CLI / Systems:* Terminal UI, telemetry views, or boot/shell demo harness.
- **Deliverable:** Working interactive demo (`/run-ca-agent` on `:3000` or preview harness) verified by the Developer before backend persistence begins.

---

## Team 4 — Dev Team

**Scope:** Codebase setup, prototyping, TDD implementation, AI/ML/CV/OS engineering, and strict security-first tooling.

- **Pre-Coding Discipline:** Create/verify `docs/*.md` and `.txt` playbooks, checklist, and `logs/` (`dev.log`, `test.log`, `server.log`, `error.log`) before writing application code.
- **Core Engineering:** Tech-lead oversight, prototyping, clean modular coding, API gateway, BaaS/backend integration, database connections/migrations/storage, CI/CD pipelines, data handling & modeling, payments, privacy, auth/authz, performance optimization, `README.md` & `LICENSE`.
- **Defect & Reliability Hygiene:** Distinguish **Defect**, **Failure**, and **Fault**; perform root-cause fixes, verification, validation, and automation.
- **Modern AI / GenAI / ML / CV Stack:**
  - Feature mapping, fine-tuning, RAG pipelines, LangChain, LangGraph, LangSmith, OKF, **anti-hallucination guardrails** (grounded citations, schema validation, confidence thresholds).
  - *CV / DL:* PyTorch/ONNX/TensorRT inference, preprocessing, batching.
  - *OS / Systems:* Memory-safe kernel/driver/HAL modules, deterministic builds, QEMU/hardware test targets.
- **Agent Ops & Security-First Rule:**
  - Apply token optimization, context window switching, model switching, slash command triggers, agent context memory, and agent rules/constitutions.
  - **NEVER blindly install skills, MCPs, or plugins from GitHub/external sources:** Inspect source code, permissions, network calls, and license/CVEs with Team 6 before enabling.

### 5-Point External GitHub Skill / MCP Security Vetting Checklist (Team 4 + Team 6)
1. **Source & Diff Inspection:** Read all `SKILL.md`, `scripts/`, and hooks before cloning/enabling; reject obfuscated or minified payloads.
2. **Permission & Shell Scope:** Verify no unprompted `curl | sh`, reverse shells, or writes outside workspace/`logs/`.
3. **Credential Isolation:** Confirm zero exfiltration of `.env`, SSH keys, browser cookies, or API tokens.
4. **License & Maintenance Check:** Confirm permissive/compatible license and check for known CVEs in dependencies.
5. **Sandbox Dry-Run:** Test in an isolated branch/sandbox first and record the approval in `docs/plugins.md` or `docs/skills.md`.
