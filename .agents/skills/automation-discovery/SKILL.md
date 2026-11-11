---
name: automation-discovery
description: >-
  Identify and prioritize automation opportunities in recurring business processes using frequency, error rate, data readiness, integration effort and operational risk. Use before choosing tools or designing detailed workflows; do not assume AI is necessary.
---

# Automation Discovery

## Purpose
Decide **whether a process should be automated, and which part first**. A useful outcome may be simplification or a simple rule rather than an AI-powered workflow.

## Discovery
1. Describe the process in plain language: trigger, actor, input, steps, output, cadence and current failure modes. Ask only for a decision-critical missing fact; otherwise mark assumptions.
2. Identify repetitive decisions and handoffs. Separate deterministic steps, judgment-heavy steps, sensitive approvals and exceptions. Include the no-automation option where appropriate.
3. Estimate candidate value from **known** time spent, volume, error incidence, urgency and business cost. Do not turn anecdotes into fake ROI. If volumes are unknown use low/medium/high qualitative scores.
4. Check readiness: input quality and permissions, available APIs, existing systems, user identity, ownership of credentials, auditability and exceptions. Explicitly flag personal or confidential data.
5. Rank up to three candidates by value, feasibility, reversibility and risk. Prefer a short pilot-sized slice with clear human review rather than cross-system replatforming.
6. For the chosen candidate, outline trigger → input → rule/AI decision (only if needed) → output → failure handling → approval. Recommend `workflow-architect` for detailed implementation design.

## Output
Process map (text), automation candidates ranked with evidence/confidence, recommended first slice, success and failure metrics, needed access/integrations and unresolved risks.

## Boundaries
No claim that a connector/API exists without checking. No assumption that LLMs are appropriate for deterministic work. No credential collection, production edits, outbound communication, file deletion or scheduling without explicit authorization. Never run a workflow against customer data during discovery.
