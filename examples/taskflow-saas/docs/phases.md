# Phases — TaskFlow SaaS

> **Document class:** Living feature/specification  
> **Framework:** SDD-Vibe  
> **Guideline baseline:** 2.0.0  
> **Status:** Active

## Purpose

Release milestones for TaskFlow SaaS across all 4 SDD-Vibe phases.

## Agent read trigger

**MUST** read or consult this file: During phase transitions.

## Phase 1: Architecture & Vibe Discovery [DONE]

| Field | Value |
|---|---|
| Goal | Product vision, PRD, and system architecture |
| Features in scope | FEAT-001 (1.0.0), FEAT-002 (1.0.0) |
| Exit gate | Architecture signed off |
| Exit approval | APR-001 |

## Phase 2: Frontend-First Sensory Demo [DONE]

| Field | Value |
|---|---|
| Goal | Interactive Kanban UI on :3000 |
| Features in scope | FEAT-001 (1.0.0) |
| Exit gate | Visual demo approved |
| Exit approval | APR-001 |

## Phase 3: Formal Spec Lock & TDD [DONE]

| Field | Value |
|---|---|
| Goal | SQLite persistence, Zod contracts, HMAC auth, Vitest TDD |
| Features in scope | FEAT-001 (1.0.0), FEAT-002 (1.0.0) |
| Exit gate | 100% green Vitest suite |
| Exit approval | APR-001 |

## Phase 4: Audit & Ship [DONE]

| Field | Value |
|---|---|
| Goal | Typecheck, lint, build, and CI verification |
| Features in scope | FEAT-001 (1.0.0), FEAT-002 (1.0.0) |
| Exit gate | Zero errors across all gates |
| Exit approval | APR-001 |

## Evidence and change control

- **MUST** record exit approvals before advancing phases.

## SDD-Vibe enforcement

- **MUST** list exact `FEAT-###` versions in scope.
