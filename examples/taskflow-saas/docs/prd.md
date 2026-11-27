# Product Requirements Document (PRD) — TaskFlow SaaS

> **Document class:** Living feature/specification  
> **Framework:** SDD-Vibe  
> **Guideline baseline:** 2.0.0  
> **Status:** Active

## Purpose

Measurable functional (`REQ-###`) and non-functional (`NFR-###`) requirements derived from `docs/product.md`.

## Agent read trigger

**MUST** read or consult this file: Before decomposing features into `docs/features/`.

## Requirements

| ID | Parent | Requirement |
|---|---|---|
| `REQ-001` | `CAP-001` (`PER-01`, `PER-02`) | Users can list, create, and update task status (`BACKLOG`, `IN_PROGRESS`, `DONE`) and priority (`P0`–`P3`). |
| `REQ-002` | `CAP-002` (`PER-01`, `PER-02`) | All task payloads are validated with Zod schemas and persisted in SQLite. |
| `REQ-003` | `CAP-003` (`PER-02`) | Task mutations (`POST`, `PATCH`, `DELETE`) require a valid HMAC-signed session cookie. |
| `NFR-001` | `CAP-002` | API validation rejects malformed payloads with HTTP `400` and structured JSON errors. |
| `NFR-002` | `CAP-003` | Unauthenticated mutations return HTTP `401` without modifying database state. |

## Evidence and change control

- **MUST** trace every `REQ-###` to `FEAT-###` in `docs/spec.md`.

## SDD-Vibe enforcement

- **MUST** maintain 100% traceability from `CAP-###` → `REQ-###` → `FEAT-###`.
