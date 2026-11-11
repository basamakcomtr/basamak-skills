---
name: subscription-lifecycle
description: >-
  Design and assess subscription renewal journeys, notices, payment status, grace periods, expiry, suspension and reactivation. Use for recurring-service operations and customer communication logic; not for making real billing or account changes.
---

# Subscription Lifecycle

## Goal
Make renewals **predictable for customers and safe for operators**, including non-payment and service restoration. This skill is applicable to annual SaaS subscriptions, hosted services and recurring contracts.

## Method
1. Define the authoritative subscription fields: contract start/end, renewal basis, invoice/payment state, service state, contact channels, notice consent/preferences and responsible owner. Distinguish contractual obligation from product convention.
2. Model a small state machine: active → renewal upcoming → due → grace period (if agreed) → expired/suspended → renewed/reactivated. Avoid forcing grace periods or automatic suspension where contracts do not permit them.
3. Define **separate** processes for renewal calculation, notice preparation, message delivery, delivery status, payment confirmation and service-state change. Preparing a message never proves it was delivered.
4. For each transition, specify timing, timezone, idempotency, owner, user-facing explanation, exception handling and audit record. Duplicate scheduled jobs must not double-charge or double-notify.
5. Account for edge cases: payment received near expiry, manual renewal, changed contract dates, bounced notices, bank transfer delay, billing dispute, suspended service with retained data, reactivation and missing contact consent.
6. Recommend the narrowest safe automation. A notification schedule is not permission to disable a site. For suspension or deletion, require documented business rules, notice requirements, approved authorization, backup/retention review and a reversible recovery path.
7. Define measures: upcoming renewals, confirmed notices, payment reconciliation errors, false suspensions, reactivation time, and unresolved exceptions—without manufacturing rates.

## Output
State table (state/trigger/action/owner/evidence), notice schedule if verified, safety rules, exceptional journeys, measurable acceptance cases and human review checkpoints.

## Guardrails
Never invent legal notices, contracted inflation formulas, renewal amounts, tax calculation or delivery success. Do not send messages, charge customers, suspend services, purge data or modify subscription records without permission. Work with `workflow-architect` for implementation and `pricing-review` for price decisions.
