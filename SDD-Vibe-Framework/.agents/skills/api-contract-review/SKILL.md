---
name: api-contract-review
description: "Review API changes against docs/apis.md and the contracts cited by feature specs; use before approving or merging interface changes."
---

# Skill: api-contract-review

**Purpose:** Validate API endpoint additions and modifications against `docs/apis.md` and feature contracts for schema accuracy, backward compatibility, auth enforcement, and error consistency.

## Trigger

- **MUST** invoke whenever adding, modifying, or deprecating REST, GraphQL, RPC, or SSE/WebSocket endpoints.

## Inputs

- **MUST** read `AGENTS.md`, `docs/apis.md`, `docs/security.md`, and the `APPROVED` feature spec defining the endpoint behavior.

## Workflow

1. **Contract & Schema Diff:**
   - Compare route paths, HTTP methods, request/response payloads, and pagination/filtering against `docs/apis.md`.
2. **Breaking Change Detection:**
   - Flag removed fields, renamed keys, narrowed types, or changed status codes; require API versioning or deprecation notice if breaking.
3. **Status Codes & Error Schema Audit:**
   - Verify semantic HTTP status codes (`200`, `201`, `400`, `401`, `403`, `404`, `409`, `422`, `429`, `500`) and uniform structured error payloads (no raw stack traces in responses).
4. **Auth, Validation & Rate-Limit Check:**
   - Confirm authentication/RBAC middleware, strict input schema validation, idempotency keys (for mutations/webhooks), and rate-limit headers are enforced and documented.

## Restrictions

- **MUST NOT** approve undocumented endpoints or breaking contract changes without updating `docs/apis.md` and passing contract tests.
- **MUST NOT** expose internal stack traces, secrets, or cross-tenant records in API responses.
- **MUST NOT** alter controlled guidelines without recorded approved revision.
