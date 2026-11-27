---
name: ml-evaluation
description: "Evaluate ML/AI components against dataset lineage, evaluation thresholds and drift checks defined in docs/domains."
---

# Skill: ml-evaluation

**Purpose:** Validate ML, Deep Learning, Computer Vision, and LLM/RAG pipelines for dataset lineage, leakage-free splits, metric thresholds, bias/drift monitoring, and reproducibility.

## Trigger

- **MUST** invoke when building, fine-tuning, evaluating, or deploying ML/DL/CV models, RAG pipelines, or prompt/agent evaluation harnesses.

## Inputs

- **MUST** read `AGENTS.md`, relevant `docs/domains/*.md`, `docs/performance.md`, and the `APPROVED` feature spec.

## Workflow

1. **Dataset Lineage & Split Integrity:**
   - Verify dataset provenance, license/PII compliance, and strict train/validation/test isolation (zero data or temporal leakage).
2. **Reproducibility Audit:**
   - Confirm fixed random seeds, pinned model/library versions, immutable dataset hashes, and logged hyperparameters.
3. **Evaluation Thresholds & Bias Check:**
   - Measure task metrics (e.g., F1, AUROC, RMSE, mAP, RAG faithfulness/groundedness) against `APPROVED` baselines; evaluate performance across demographic/edge-case slices.
4. **Latency, Cost & Drift Readiness:**
   - Benchmark p95 inference latency, memory/VRAM footprint, and token/compute cost; verify drift detection alerts and fallback/human-in-the-loop gates.

## Restrictions

- **MUST NOT** report synthetic or cherry-picked evaluation metrics; all metrics must come from held-out test sets.
- **MUST NOT** deploy models failing minimum accuracy, fairness, or latency gates.
- **MUST NOT** alter controlled guidelines without recorded approved revision.
