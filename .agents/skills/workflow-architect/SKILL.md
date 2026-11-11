---
name: workflow-architect
description: >-
  Design an implementable business automation workflow with triggers, integrations, state, retries, idempotency, approvals and recovery. Use after identifying a candidate process; not for deploying or running live workflows without permission.
---

# Workflow Architect

## Scope
Design the **smallest reliable workflow** that satisfies a verified business outcome. This skill documents a workflow; it does not activate integrations. For selecting the opportunity first, use `automation-discovery`.

## Design sequence
1. Specify owner, trigger, expected output, source of truth, relevant volume, deadlines and allowed failure behavior. Distinguish known system capabilities from proposed ones. If APIs or events are unverified, create a targeted discovery task.
2. Map states and transitions: received → validated → accepted/rejected → processed → completed/failed/needs review. Include duplicate events, partial completion, retries and manual correction where relevant.
3. Assign each step to an existing system or proposed component. For each external integration record direction, data fields (without secrets), authentication ownership, rate limits if verified, and fallback if unavailable.
4. Choose deterministic rules before AI. If probabilistic classification is needed, specify model input/output schema, confidence threshold, review path, cost controls and safe fallback. Never assume an LLM decision is suitable for irreversible actions.
5. Make side effects safe: idempotency key; retry with bounded backoff; queue or scheduler where justified; timeout; audit log; no double charge/message; compensating or rollback action when possible. Match controls to risk rather than adding every technology by default.
6. Identify approval points, access permissions, personal-data exposure and retention constraints. Define how an operator observes a failure and reruns only the safe part.
7. Produce a 3–6 task implementation plan, then acceptance scenarios for success, duplicate event, external-service failure and manual intervention.

## Deliverable
One-line objective; text flow diagram; step table (input/action/output/system/error); decisions and assumptions; data/access requirements; minimal implementation tasks; measurable acceptance and recovery scenarios.

## Constraints
Do not invent endpoints, credentials, database tables or deployment details. No production execution, scheduling, database writes, customer notifications or destructive changes without explicit authorization. Mention `ai-feasibility` when AI adds a material uncertainty and `software-planner` for code-oriented task planning.
