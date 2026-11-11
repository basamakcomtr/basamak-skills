---
name: release-readiness
description: >-
  Assess a software change before production rollout using actual diff, test evidence, migration risk, operational impact and rollback readiness. Use for release go/no-go decisions, not as a claim that tests or deployment occurred.
---

# Release Readiness

## Mission
Provide a focused **go / conditional go / no-go recommendation** for a particular release. Optimize for meaningful risk reduction, not a sprawling generic checklist. Read actual change evidence when available.

## Review
1. Fix the release identity: repository, branch/commit, target environment, intended change, affected users and deploy method. If the actual version is unknown, say so; never substitute a remembered SHA.
2. Classify risk from the diff or verified change summary: authentication/permissions, data migrations, background jobs, billing, API contracts, SEO/public URLs, cache, dependencies and external integrations. Do not assert unaffected areas were inspected.
3. Map each material risk to **one relevant verification**: test output already provided, focused command to run, or manual scenario. Record who ran tests and their results; never say "passed" for a proposed command.
4. Check production dependencies only when relevant: env configuration, secrets available without exposing them, queue/cron readiness, database backup and migration compatibility, feature flags, monitoring and rollback.
5. State reversible versus irreversible changes. For a data migration, distinguish code rollback from **data restoration**; require a reviewed recovery plan where data loss is plausible.
6. Produce blockers, non-blocking cautions and the smallest safe rollout order: preflight → deploy → smoke check → watch → rollback trigger. No unapproved production commands.

## Format
Release identifier/evidence; concise change impact; verified tests versus missing checks; numbered blockers (if any); recommended go/no-go with justification; minimal rollout and rollback plan.

## Gate
A release is not "ready" solely because CI is green. Conversely, do not mandate a complete regression suite for a small copy change without material risk. Never execute deployment, merge a PR, rotate secrets or run migrations without explicit permission. Use `code-reviewer` for line-level defects and `technical-troubleshooter` for live incidents.
