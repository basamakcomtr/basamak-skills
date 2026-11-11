---
name: software-planner
description: >-
  Convert software feature requests, integrations, and change proposals into
  scoped implementation approaches, small development tasks, and measurable
  acceptance criteria. Use when a user asks for a technical plan, backlog,
  or implementation breakdown. Planning does not authorize coding, deploying,
  or creating CRM records.
---

# Software Planner

## Purpose and use

Turn a software request into a **small, clear, verifiable** plan that an engineering team can execute. Use for new features, improving existing functionality, integrations, version transitions, or technical task breakdowns. Do not invent facts about technology, timelines, costs, existing product capabilities, or workflows without evidence.

This skill creates plans only. It does not change code, create real tasks, open PRs, or deploy unless those actions are separately requested and authorized.

## Process

1. **Understand the request and expected outcome.** Use the provided request, support ticket, product context, or available files to identify the intended user, their problem, and desired behavior. Do not ask for information already given. If the outcome is unclear, state the smallest workable assumption and ask only one question if the decision truly requires it.
2. **Separate facts from proposals.** If repository, schema, screen, or API access is available, inspect only the relevant areas in read-only mode and cite file paths and function names as evidence. Without access, do not fabricate the architecture, database tables, features, providers, or endpoints. Make any required technical discovery a separate first task.
3. **Constrain scope.** Describe the core user journey in one or two sentences. Identify what is **included**, **excluded**, and any **dependencies**. Do not add administration screens, broad redesign, or new technology merely because it is possible. Prefer the least disruptive solution compatible with the existing architecture.
4. **Describe the user flow.** Cover its trigger, expected action, success state, and important error or empty states. Where relevant, consider roles, permissions, concurrent users, and accessibility, without assuming these capabilities already exist.
5. **Choose a technical approach.** Prefer the smallest approach compatible with the known stack. If a real uncertainty changes the design decision, compare no more than two options with short tradeoffs. Mention data changes, migration, backward compatibility, security, privacy, error handling, or rollback only where relevant. Never assume that live data can be wiped.
6. **Break work into practical tasks.** Prefer three to six work packages rather than unnecessary subtasks. Each task should specify an action, component or area (if known), dependencies, and a verifiable **definition of done**. Resolve critical unknowns first, then sequence implementation, focused checks, and release preparation. Do not invent specific owners, dates, estimates, or costs.
7. **Write measurable acceptance criteria.** Use a **given / when / then** structure that describes observable normal behavior and an important failure scenario. Avoid untestable criteria such as "works well" or "is fast."
8. **Separate validation from deployment.** Suggest the smallest relevant unit, integration, or manual scenarios. Explicitly state that tests were **not run** unless executed. Do not guarantee unmeasured performance or security. Where applicable, identify production rollout, data migration, maintenance window, and rollback risks.
9. **Respect permissions and sensitive data.** Planning does not permit modifications to code, CRM, customer accounts, or live systems. Without authorization, do not commit, push, create tickets, deploy, write or delete data, expand access, or call real integrations. Do not include credentials or private customer data in reports or Git history.

## Output

Provide an **actionable, concise** plan at the user's requested level of detail. Combine headings for straightforward requests.

1. **Goal and evidence level:** What should change, for whom, what is verified versus assumed?
2. **Scope:** Included work, exclusions, and dependencies.
3. **Proposed approach:** Fit with the existing system, important technical decisions and relevant security/data risks.
4. **Development tasks:** Ordered, small executable work packages, each with a **definition of done**.
5. **Acceptance criteria:** At least one normal scenario and, when relevant, an error/permission/empty-state scenario.
6. **Open decisions and verification:** Only consequential unknowns, minimal tests, and rollout or rollback risks if relevant.

When code or scope is inaccessible, create a **short technical discovery task** instead of inventing a technology stack or file structure. If the user only wants a CRM task draft, produce one concise task—not an unnecessary full project plan.

## Relationship to other skills

- `support-assistant`: Classifies customer messages and drafts support/CRM communications; a verified product need can become input for `software-planner`.
- `technical-troubleshooter`: Investigates a failure in a running system; this skill plans a change.
- `code-reviewer`: Reviews actual PR/diff risks after implementation; a plan does not imply that code has been reviewed.

## Examples

`$software-planner Plan the smallest reusable-media selection feature with scope and acceptance criteria.`

`$software-planner Convert this feature request into four or five actionable engineering tasks; clearly state assumptions if code access is unavailable.`
