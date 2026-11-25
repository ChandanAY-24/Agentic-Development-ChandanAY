# AI-Powered Project Development — 1-in-2 Custom Slash Commands Demo: EduSphere SMS

**Framework:** SDD-Vibe (1-in-2 Single Workflow)  
**Reference Project:** EduSphere Multi-Tenant School Management System (SMS)  

---

## End-to-End Command Walkthrough

1. **Launch Mission Control:** Run `/dashboard-ca-agent` → open `http://127.0.0.1:4200` in IDE Simple Browser.
2. **Phase 1 — Architecture & Vibe Discovery:**
   - Run `/plan-ca-agent` to synthesize EduSphere's multi-tenant RLS architecture, FERPA boundaries, and Shadcn UI design tokens.
   - Run `/task-ca-agent` to register `TASK-001` (Enrollment UI Demo) and `TASK-002` (Enrollment API & RLS) in `docs/task.md`.
3. **Phase 2 — Frontend Sensory Demo:**
   - Run `/implement-ca-agent` scoped to `FEAT-002` (`PROTOTYPE` → `DRAFT`) frontend components and mock student state.
   - Run `/run-ca-agent` to inspect EduSphere at `http://localhost:3000` and iterate until visually approved.
4. **Phase 3 — Formal Spec Lock & TDD:**
   - Lock `docs/features/002-student-enrollment.md` as `APPROVED` and run `/spec-check-ca-agent`.
   - Run `/testing-ca-agent` to confirm `RED` failures for `TEST-FEAT002-01`..`03` (logged to `logs/test.log`).
   - Run `/tdd-ca-agent` to implement PostgreSQL RLS, Zod schemas, and enrollment endpoints until all tests turn `GREEN`.
5. **Phase 4 — Audit & Release:**
   - Run `/review-ca-agent`, `/verify-ca-agent`, `/security-audit-ca-agent`, and `/release-check-ca-agent`.
   - Use `/errorlogs-ca-agent`, `/gitlogs-ca-agent`, or `/handoff-ca-agent` as needed during triage and team transfer.
