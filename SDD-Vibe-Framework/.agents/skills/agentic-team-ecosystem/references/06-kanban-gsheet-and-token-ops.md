# 06 — Post-Design Kanban, Google Sheet Sync & Token/Model Ops

## 1. Post-Frontend Design Kanban & Google Sheet Tracker (Team 1)

**Activation Rule:** Triggered automatically immediately after **Step 3 (Frontend / Interface Design & Sensory Demo)** is verified by the Developer.

### Canonical Kanban Columns (Google Sheet & `docs/task.md` Sync)

| Column | Format / Allowed Values | Description |
|---|---|---|
| `task_id` | `TASK-001`, `TASK-002`, ... | Unique sequential task identifier |
| `group` | `Group 1` .. `Group 4` | Ecosystem Group Main Agent owning the task |
| `team` | `Team 1` .. `Team 14` | Specific Team Coordinator responsible |
| `title` | Short imperative phrase | Actionable unit of work |
| `status` | `PENDING`, `IN_PROGRESS`, `IN_REVIEW`, `COMPLETE`, `SIGNED_OFF` | Live Kanban lane |
| `start_date` | `DD-MM-YYYY` | Date task moved to `IN_PROGRESS` |
| `stop_date` | `DD-MM-YYYY` | Date task moved to `COMPLETE` / `SIGNED_OFF` |
| `sign_off` | `PENDING` / `APPROVED (<Owner>)` | Developer / QA final sign-off |
| `spec_ref` | `FEAT-### / AC-FEAT###-##` | Traceability link to `docs/features/` |

### Sync Workflow
1. **Local Dashboard Export:** Use `Project-Manager-Dashboard` → **Export Kanban CSV (Google Sheets)** (`GET /api/kanban-export`) to download `kanban-gsheet-export.csv`.
2. **Google Sheets Import:** Import or paste into your project's Google Sheet Kanban tab (or connect via your own optional Google Sheets MCP/Apps Script if configured by the Developer).
3. **Rule:** Never store Google OAuth tokens or service account JSON inside the repository or `logs/`.

### Quick Google Sheet Setup (1-Click Import)
1. Open Google Sheets → **File → Import → Upload** `kanban-gsheet-export.csv` (from `GET /api/kanban-export`).
2. Freeze Row 1 (**View → Freeze → 1 row**) and enable **Data → Create a filter**.
3. Apply Conditional Formatting on Column E (`status`): `PENDING` (Gray), `IN_PROGRESS` (Blue), `IN_REVIEW` (Amber), `COMPLETE` / `SIGNED_OFF` (Green).

---

## 2. Token Optimization, Context Window & Model Switching (Team 2 & Team 4)

### Progressive Disclosure & Context Budget
- Load only `SKILL.md` + the **1–2 reference files** needed for the current step. Never dump all 14 team playbooks into a single prompt.
- Summarize completed step outputs into concise handoff artifacts (`docs/plan.md`, `docs/task.md`, `.agents/templates/AGENT-COMPLETION-REPORT.md`) before switching context windows.

### Model Switching Strategy (Dual-Budget: Lean-Burn vs. Full-Potential)
- **Lean-Burn (Lightweight / Fast Models):** File discovery (`rg`), log tailing (`logs/*.log`), boilerplate generation, formatting, simple unit test scaffolding, and repetitive checks. Batch independent reads/edits in one turn and read 50–150 line slices instead of whole files.
- **Full-Potential (High-Reasoning / Pro Models):** System architecture (HLD/LLD/DFD/UML), deep domain research & developer grilling (`/plan-ca-agent`), complex computations/algorithms, security threat modeling (`/security-audit-ca-agent`), hard root-cause debugging (`/errorlogs-ca-agent`), and final release gates (`/verify-ca-agent`).
- **Context Window Switching:** When context approaches saturation, checkpoint state to `docs/task.md` + `docs/memory.md` (Memory Lanes) + `logs/dev.log`, run `/compact` or start a fresh session tab, and resume from the exact `TASK-###` and `Step` number.
- **Detailed Guide:** See `SDD-Vibe-Token-Optimization-Guide.md` at the repository root for prompt templates and the 7-pillar playbook.
