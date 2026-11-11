# From automation opportunity to workflow design

[**Türkçe**](automation-opportunity-to-design.tr.md) · [Home](../README.md)

**Goal:** Identify a recurring manual task, decide whether it merits automation or AI, and turn an approved candidate into a safe, implementable workflow.

This is a **manual sequence of agent tasks**, not autonomous orchestration or a connection to business systems. The user/owner provides the previous stage's output to the next one.

## 1. Discover

**Use:** [automation-discovery](../.agents/skills/automation-discovery/SKILL.md)

Example request:
```text
Assess our recurring customer document intake. Map inputs, frequency,
exceptions and human approvals. Rank up to three opportunities.
Do not assume AI is required or execute anything.
```

**Handoff:** Existing process map, ranked opportunities, evidence gaps, first automation slice.

**Gate:** The owner selects one candidate; do not silently automate all candidates.

## 2. Decide whether AI is useful (only if needed)

**Use:** [ai-feasibility](../.agents/skills/ai-feasibility/SKILL.md)

```text
Compare rules vs AI for the selected intake classification step.
Document data rights, error cost, cost controls, evaluation criteria
and a non-AI fallback. Do not make paid calls.
```

**Handoff:** AI / non-AI / hybrid decision, evidence, safeguards and validation plan.

**Gate:** No AI integration unless the decision and required approval are explicit.

## 3. Design the workflow

**Use:** [workflow-architect](../.agents/skills/workflow-architect/SKILL.md)

```text
Design the smallest reliable workflow for the approved candidate.
Include trigger, inputs, states, idempotency, exception handling,
permissions, recovery and human approval points.
Do not invent APIs or deploy.
```

**Handoff:** Flow, verified integrations vs assumptions, acceptance criteria, bounded implementation tasks.

## 4. Plan and assess release

Use [software-planner](../.agents/skills/software-planner/SKILL.md) for real product repository tasks; once implemented by an authorized team, use [code-reviewer](../.agents/skills/code-reviewer/SKILL.md) and [release-readiness](../.agents/skills/release-readiness/SKILL.md) with the **actual diff, commit and test outputs**.

**Gate:** Only the authorized owner approves implementation, merge or production rollout. Documentation alone does not grant access.

## Handoff card

```text
Business outcome:
Observed process and evidence:
Chosen candidate / rejected alternatives:
AI decision and rationale:
Required integrations / access owner:
Data risks and approval points:
Workflow states / retries / recovery:
Acceptance criteria:
Actual test evidence:
Next owner decision:
```

Never include customer secrets, private records, production tokens or undocumented performance claims in the public skills repository.
