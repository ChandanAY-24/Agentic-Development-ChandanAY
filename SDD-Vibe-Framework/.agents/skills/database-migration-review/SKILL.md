---
name: database-migration-review
description: "Review schema and migration changes against docs/database.md for safety, reversibility and data retention."
---

# Skill: database-migration-review

**Purpose:** Audit database schema changes and migrations against `docs/database.md` for backward compatibility, reversibility, data integrity, and zero-downtime safety.

## Trigger

- **MUST** invoke before creating, modifying, or applying any database migration, schema DDL, index, or RLS policy.

## Inputs

- **MUST** read `AGENTS.md`, `docs/database.md`, `docs/system-architecture.md`, and the `APPROVED` feature spec requiring the schema change.

## Workflow

1. **Schema Diff & Contract Alignment:**
   - Compare proposed DDL/migration against `docs/database.md` naming conventions, types, nullability, and tenant/RLS isolation rules.
2. **Reversibility & Rollback Check:**
   - Verify a deterministic `down` / rollback migration exists and restores prior schema state without unintended data loss.
3. **Zero-Downtime & Locking Audit:**
   - Flag destructive or table-locking operations (`DROP COLUMN`, `ALTER TYPE`, non-concurrent `CREATE INDEX` on large tables); require expand-and-contract pattern for breaking changes.
4. **Data Preservation, FKs & Indexes:**
   - Audit foreign key `ON DELETE` / `ON UPDATE` cascades, backfill scripts for newly non-null columns, and index coverage for new query predicates.
5. **Backup & Verification Gate:**
   - Confirm pre-migration backup/snapshot requirement and test migration up + down against a local/staging database.

## Restrictions

- **MUST NOT** approve destructive migrations without an explicit `CR-###` / `DEC-###` and verified data backup plan.
- **MUST NOT** bypass Row-Level Security (RLS) or multi-tenant isolation constraints.
- **MUST NOT** alter controlled guidelines without recorded approved revision.
