# Feature Specifications (`docs/features/`)
### Canonical Living Contracts & Acceptance Criteria Architecture

<div align="center">

[![Specifications](https://img.shields.io/badge/Contracts-Living_Feature_Specs-blue?style=for-the-badge&logo=gitbook)](.)
[![Formats](https://img.shields.io/badge/Formats-Flat_|_Modular-indigo?style=for-the-badge)](.)
[![Lifecycle](https://img.shields.io/badge/Lifecycle-Formal_Quality_Gates-teal?style=for-the-badge)](.)
[![Traceability](https://img.shields.io/badge/Traceability-CAP_|_REQ_|_AC_|_TEST-green?style=for-the-badge)](../requirements-traceability.md)

[🌟 Purpose](#-purpose) • [🏛️ Format Decision Tree](#️-flat-vs-modular-decision-tree) • [📊 Complexity Tiers](#-feature-complexity-breakdown-tiers) • [🔄 Lifecycle State Machine](#-specification-lifecycle-state-machine) • [📋 Traceability](#-identifier-traceability-scheme)

</div>

---

## 🌟 Purpose

`docs/features/` is the **only** canonical location for versioned feature contracts within the repository. A root-level `specs/` directory is not permitted. `docs/spec.md` indexes the current approved version of every feature; it never overrides an individual feature file.

### Traceability Hierarchy:
`docs/product.md` (Capabilities `CAP-###`) → `docs/prd.md` (Requirements `REQ-###`) → `docs/features/` (Contracts `FEAT-###`) → Automated Tests (`TEST-*`) → Production Code.

---

## 🏛️ Flat vs. Modular Decision Tree

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 40}}}%%
flowchart LR
    classDef start fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef gate fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#fffbeb;
    classDef flat fill:#172554,stroke:#60a5fa,stroke-width:1.5px,color:#eff6ff;
    classDef modular fill:#2e1065,stroke:#c084fc,stroke-width:2px,color:#faf5ff;

    Start(["`**🚀 Initiate New Feature Spec**
/plan-ca-agent or /spec-check-ca-agent`"]):::start --> DevAsk{"Format Choice?"}:::gate
    
    DevAsk -->|"User Defined"| UserChoice["`**🎯 Follow Explicit User Choice**
Adhere strictly to chosen format`"]:::start
    DevAsk -->|"Auto Detect"| AutoTier{"Evaluate Tier?"}:::gate
    
    AutoTier -->|"Tier 1 / Tier 2"| FlatFormat["`**📄 Scaffold Flat Format**
docs/features/NNN-name.md`"]:::flat
    AutoTier -->|"Tier 3"| ModularFormat["`**📁 Scaffold Modular Format**
docs/features/NNN-name/`"]:::modular
```

---

## 📊 Feature Complexity Breakdown Tiers

Every feature must be categorized into one of three complexity tiers to drive sizing, test strategies, and implementation pacing:

| Tier | Complexity Category | Characteristics & Scope | Verification Strategy |
|---|---|---|---|
| **Tier 1** | **Easy (Low Complexity)** | Self-contained, static or simple CRUD, single table/model, minimal dependencies, read-only views, health check endpoints (1–2 files). | Unit tests only; rapid Red-Green cycle. |
| **Tier 2** | **Intermediate (Medium Complexity)** | Multi-table relational logic, form validation, role-based auth guards, API endpoints, state management, UI component interactions (3–6 files). | Unit + API integration tests; component state testing. |
| **Tier 3** | **Hard / Complex (High Complexity)** | Multi-tenant row-level security (RLS), distributed transactions, WebSocket live streams, external payment webhooks, background worker queues, forecasting/ML pipelines (7+ files). | Unit + Integration + Contract tests + E2E failure recovery scenarios. |

---

## 🔄 Step-by-Step Spec Development Protocol

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 44}}}%%
flowchart TB
    classDef step fill:#082f49,stroke:#38bdf8,stroke-width:1.5px,color:#f0f9ff;
    classDef red fill:#4c0519,stroke:#fb7185,stroke-width:2px,color:#fff1f2;
    classDef green fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ecfdf5;
    classDef gate fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#fffbeb;

    subgraph ForwardTier ["🧪 SPEC IMPLEMENTATION STAGE"]
        direction LR
        SelectSpec["`**1. 📑 Select Spec**
Approved FEAT-###`"]:::step
        WriteTests["`**2. 🔴 Write Tests**
Verify AC (Red Phase)`"]:::red
        ImplementCode["`**3. 🟢 Minimal Code**
Pass Tests (Green Phase)`"]:::green
    end

    subgraph ReviewTier ["🔍 VERIFICATION & REVIEW STAGE"]
        direction LR
        RefactorCode["`**4. ✨ Refactor**
Clean Architecture`"]:::green
        UpdateDocs["`**5. 📝 Update Docs**
Living Trackers Synced`"]:::step
        NextSpec{"Next Spec?"}:::gate
        ReleaseAudit(["`**6. 🚀 Release Audit**
/release-check-ca-agent`"]):::green
    end

    SelectSpec -->|"Contract"| WriteTests
    WriteTests -->|"Failing"| ImplementCode
    ImplementCode ==>|"Pass All"| RefactorCode

    RefactorCode -->|"Polish"| UpdateDocs
    UpdateDocs -->|"Evaluate"| NextSpec
    NextSpec -.->|"Yes: Next"| SelectSpec
    NextSpec -->|"No: Done"| ReleaseAudit

    style ForwardTier fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
    style ReviewTier fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
```

> [!CRITICAL]
> **MUST NOT** begin work on a subsequent feature until the current feature's acceptance criteria are fully met, verified green by automated tests, and all relevant documentation files are updated.

---

## 🔄 Specification Lifecycle State Machine

```mermaid
stateDiagram-v2
    [*] --> PROTOTYPE: 🎨 Frontend Sensory Demo
    PROTOTYPE --> DRAFT: 📝 Formalize Spec
    [*] --> DRAFT: 📝 Author Specification
    DRAFT --> IN_REVIEW: 🔍 Submit for Review
    IN_REVIEW --> DRAFT: 🔄 Revisions Requested
    IN_REVIEW --> APPROVED: 👤 Human Approval (docs/approvals/)
    
    APPROVED --> SUPERSEDED: 📑 Replaced by Newer Approved Spec
    APPROVED --> DEPRECATED: 📦 Capability Retired / Decommissioned
    
    SUPERSEDED --> [*]
    DEPRECATED --> [*]
```

| Status | Meaning | Implementation Permitted? |
| :--- | :--- | :--- |
| **`PROTOTYPE`** | Frontend-first sensory UI discovery & mock-state demo. | **UI / Mock State Only** (no production DB/auth) |
| **`DRAFT`** | Initial specification draft being written. | **UI Polish Only** |
| **`IN REVIEW`** | Submitted for developer/lead review. | **No** (tests may be drafted) |
| **`APPROVED`** | Formally signed off; record exists in `docs/approvals/`. | **YES** — strictly this approved version |
| **`SUPERSEDED`** | Replaced by a newer approved version. | **No** (new work forbidden) |
| **`DEPRECATED`** | Capability retired or decommissioned. | Removal work only |

---

## 📋 Identifier Traceability Scheme

Defined canonically in `docs/requirements-traceability.md`:

| Artifact | Pattern | Concrete Example |
| :--- | :--- | :--- |
| **Feature Contract** | `FEAT-###` | `FEAT-002` |
| **Functional Requirement** | `FR-FEAT###-##` | `FR-FEAT002-01` |
| **Non-Functional Requirement** | `NFR-FEAT###-##` | `NFR-FEAT002-01` |
| **Acceptance Criterion** | `AC-FEAT###-##` | `AC-FEAT002-03` |
| **Test Case Identifier** | `TEST-FEAT###-##` | `TEST-FEAT002-03` |

- **MUST** reference the AC ID (`AC-FEAT###-##`) in the title and description of every unit/integration test.
- **MUST** trace each feature to at least one `CAP-###` in `docs/product.md` and one `REQ-###` in `docs/prd.md`.
