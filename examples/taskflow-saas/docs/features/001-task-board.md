# FEAT-001: Sprint Task Board & Persistence

| Field | Value |
|---|---|
| Feature ID | FEAT-001 |
| Spec version | 1.0.0 |
| Status | APPROVED |
| Approval reference | APR-001 |
| Product capability | CAP-001, CAP-002 |
| PRD requirements | REQ-001, REQ-002, NFR-001 |

## Acceptance Criteria

### AC-FEAT001-01: Create and persist a valid task
- **Given** an authenticated user submits a valid task title and priority (`P0`–`P3`)
- **When** `createTask` is invoked
- **Then** the task is persisted in SQLite with status `BACKLOG` and returned with a generated ID

### AC-FEAT001-02: Reject invalid or whitespace-only task payloads
- **Given** a task payload with an empty or whitespace-only title or invalid priority
- **When** `CreateTaskSchema.safeParse` validates the input
- **Then** validation fails with a structured field error and nothing is written to SQLite

### AC-FEAT001-03: Transition task status across columns
- **Given** an existing task in `BACKLOG`
- **When** `updateTaskStatus` updates status to `IN_PROGRESS` or `DONE`
- **Then** the updated status is persisted and reflected in subsequent `listTasks` queries

## Verification Matrix

| AC ID | Test ID | Test File |
|---|---|---|
| AC-FEAT001-01 | TEST-FEAT001-01 | `tests/unit/task-contracts.test.ts` |
| AC-FEAT001-02 | TEST-FEAT001-02 | `tests/unit/task-contracts.test.ts` |
| AC-FEAT001-03 | TEST-FEAT001-03 | `tests/integration/auth-and-tasks.test.ts` |
