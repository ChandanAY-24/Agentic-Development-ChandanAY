# TaskFlow SaaS — Reference Implementation

> **Built end-to-end with the SDD-Vibe 1-in-2 Single Workflow**  
> **Stack:** Next.js 15 (App Router) · React 19 · TypeScript · Tailwind CSS v4 · Zod · SQLite (`node:sqlite`) · Vitest

## Why This Exists

`examples/taskflow-saas/` is a runnable, production-styled SaaS reference implementation proving how **SDD-Vibe** takes a project from **Phase 1 (Architecture & Vibe Discovery)** through **Phase 2 (Frontend Sensory Demo)**, **Phase 3 (Spec Lock & Red-Green-Refactor TDD)**, and **Phase 4 (Audit & Ship)**.

## Phase 1 → Phase 4 Artifact Trail

| Phase | SDD-Vibe Artifact | Purpose |
|---|---|---|
| **Phase 1** | [`docs/product.md`](docs/product.md), [`docs/prd.md`](docs/prd.md), [`docs/system-architecture.md`](docs/system-architecture.md) | Capabilities (`CAP-*`), requirements (`REQ-*`), HLD/LLD |
| **Phase 2** | [`src/app/page.tsx`](src/app/page.tsx) | Frontend-first interactive task board sensory demo (`:3000`) |
| **Phase 3** | [`docs/features/001-task-board.md`](docs/features/001-task-board.md), [`docs/features/002-auth-session/`](docs/features/002-auth-session/feature.md), [`docs/approvals/APR-001.md`](docs/approvals/APR-001.md) | `APPROVED` Flat & Modular specs + Zod/SQLite/Auth + Vitest TDD |
| **Phase 4** | [`docs/task.md`](docs/task.md), [`docs/error-tracker.md`](docs/error-tracker.md), [`tests/`](tests/unit/task-contracts.test.ts) | Completed tasks, resolved regression defect, green test suite |

## Quick Start

```bash
cd examples/taskflow-saas
npm install
npm test          # Run Vitest unit & integration suites (AC-* -> TEST-*)
npm run typecheck # TypeScript strict check
npm run dev       # Launch Next.js app on http://localhost:3000
```

## Inspect in Project-Manager-Dashboard (`:4200`)

You can point the SDD-Vibe `Project-Manager-Dashboard` at this directory to view live tasks (`TASK-001..004`), `APPROVED` specs (`FEAT-001`, `FEAT-002`), and defect history (`ERR-001`).
