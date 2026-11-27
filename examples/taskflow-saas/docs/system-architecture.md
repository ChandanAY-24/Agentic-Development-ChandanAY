# System Architecture — TaskFlow SaaS

> **Document class:** Living feature/specification  
> **Framework:** SDD-Vibe  
> **Guideline baseline:** 2.0.0  
> **Status:** Active

## Purpose

High-Level Design (HLD) and Low-Level Design (LLD) boundaries for TaskFlow SaaS.

## Agent read trigger

**MUST** read or consult this file: Before modifying routes, database schemas, or auth boundaries.

## Architecture Overview

- **Presentation Layer (`src/app/page.tsx`):** Next.js App Router + React 19 + Tailwind CSS v4 interactive board.
- **API Layer (`src/app/api/`):** Next.js Route Handlers enforcing Zod contract validation (`src/lib/contracts.ts`) and HMAC session guards (`src/lib/auth.ts`).
- **Persistence Layer (`src/db/`):** Node.js built-in `node:sqlite` (`DatabaseSync`) with parameterized SQL queries and WAL mode.

## Evidence and change control

- **MUST** record architectural changes via ADRs or `docs/system-architecture.md` revisions.

## SDD-Vibe enforcement

- **MUST** keep validation and auth logic decoupled from React UI components.
