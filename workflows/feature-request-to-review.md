# From customer request to code review

[**Türkçe**](feature-request-to-review.tr.md)

**Goal:** Classify a feature request, turn an approved change into an implementable plan, and review actual code changes using evidence.

This is a documented handoff, **not an autonomous orchestration**. Each step may be a separate Codex task; **the user passes its output to the next step**. No CRM connection or product repository access is provided by these skills.

## Before starting

The paths below assume a user-level Codex installation at `~/.agents/skills/`. For a project-level setup, use the project's `.agents/skills/` directory.

- Establish the product, customer request, and any known support ticket.
- Redact personal information, keys, and private logs. Never publish customer data in this repository.
- Code review requires access to the real **product repository**, not this skills distribution.
- If automatic skill discovery is unavailable, load the appropriate `SKILL.md` directly.

## Stage 1 — Support assessment

**Skill:** `support-assistant` — `.agents/skills/support-assistant/SKILL.md`

**Codex task:**

```text
Read ~/.agents/skills/support-assistant/SKILL.md and follow the instructions.

Customer request: [REQUEST]
Known customer and product context: [AVAILABLE CONTEXT]

Provide type and provisional priority with evidence; verified facts and unknowns;
a CRM task draft for internal use; and a brief customer reply.
Do not assume a feature exists. Do not ask again for known details.
Do not create records, send messages, or change any system.
```

**Handoff:** Request summary, desired outcome, facts versus unknowns, possible development need, and actions that did not occur.

**Decision gate:** If the customer is asking whether an existing feature is available, confirm that first. A usage question is not automatically an approved development request.

## Stage 2 — Software planning

**Skill:** `software-planner` — `.agents/skills/software-planner/SKILL.md`

**Codex task:**

```text
Read ~/.agents/skills/software-planner/SKILL.md and follow the instructions.

Stage 1 summary: [HANDOFF FROM STAGE 1]
Approved scope: [APPROVED CHANGE]
Product repository or technical evidence: [IF AVAILABLE]

Distinguish verified behavior from assumptions. Define the smallest viable scope,
explicit exclusions, ordered implementation tasks with definitions of done,
and acceptance criteria for normal and important error/permission scenarios.
Do not invent tables, APIs, or components when source access is unavailable.
Do not edit files, commit, push, or deploy.
```

**Handoff:** Agreed scope and exclusions, technical decisions and assumptions, work packages, acceptance criteria, dependencies, minimal checks, and any data or release risks.

**Decision gate:** An authorized owner must approve scope and acceptance criteria before implementation. Resolve critical technical unknowns through a short discovery task.

## Stage 3 — Implementation by the authorized team

The approved work happens in the actual **product repository**, not this skills repository. Development requires separate authorization, a suitable branch or PR, and relevant checks.

**Handoff:** Real PR URL or available diff, changed behavior, acceptance criteria, commands/results of tests actually run, and known limitations. **Without a real PR/diff, no code review has been performed.**

## Stage 4 — Code review

**Skill:** `code-reviewer` — `.agents/skills/code-reviewer/SKILL.md`

**Codex task:**

```text
Read ~/.agents/skills/code-reviewer/SKILL.md and follow the instructions.

Actual PR/diff: [PR URL / DIFF]
Approved scope and acceptance criteria: [STAGE 2 HANDOFF]
Developer's test results: [IF AVAILABLE]

Review actual changes against the approved behavior. Report only evidence-backed
functional, security, or regression findings with real file/line references.
Say clearly if no substantiated issues were found.
Do not claim to have run tests you did not run.
Do not modify code, approve or merge a PR, or deploy.
```

**Handoff:** Prioritized supported findings, what test results really demonstrate, remaining uncertainty, and decisions needed before merge.

**Decision gate:** A review does not authorize merging or production rollout; the authorized owner decides.

## Minimal handoff template

```text
Request / desired outcome:
Verified current state:
Unknowns:
Approved scope:
Acceptance criteria:
Product repository / PR:
Actions and tests actually performed:
Next decision / responsible owner:
```

Do not fill unknown fields with assumptions. Never copy confidential customer material into the public skills repository.

## Optional supporting skills

- `technical-troubleshooter` for observed production failures requiring diagnosis.
- `web-audit` when user-experience or conversion evidence motivates the change.

Neither is mandatory for every request.
