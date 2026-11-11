---
name: code-reviewer
description: >-
  Review GitHub pull requests, diffs and code changes for evidence-based
  correctness, data integrity, security, compatibility, performance and
  test risks. Use when the user asks for a code review or pre-merge risk
  assessment. Never modify code or approve or merge a PR implicitly.
---

# Code Reviewer

## Purpose and scope

Determine whether changed code introduces a genuine bug, vulnerability, data-loss risk, or behavioral regression. Prefer a few high-value, actionable findings over a long speculative list. Do not invent issues when no meaningful changes or adequate evidence are available.

This skill provides **review and recommendations**, not authority to edit code, approve pull requests, merge, deploy, or change permissions.

## Workflow

1. **Establish the change scope.** Use the supplied pull request, commit, diff, changed files, and base branch. Read relevant project instructions and the intended behavior when available. If code or the diff is inaccessible, disclose that limitation; never claim to have reviewed code you have not seen.
2. **Focus on changed behavior.** Evaluate how changed files interact, looking beyond added lines only as necessary to understand callers, configuration, schema changes, error paths, and API contracts. Do not scan the entire repository without a clear reason.
3. **Investigate concrete risks.** Focus on authorization checks, data integrity, unauthorized access, input validation, sensitive-data leaks, migrations, backward compatibility, race conditions, null and error handling, idempotence, and user-visible behavior. Do not raise findings about harmless personal code-style preferences.
4. **Ground every finding.** Cite the relevant **file and line range** for each issue. If line numbers are unavailable, say so; do not fabricate line numbers or links. Explain the specific condition that triggers the defect and its likely impact. Clearly distinguish a hypothesis from a verified error.
5. **Prioritize.** Use `P0` (urgent, critical data/security risk), `P1` (must fix before merge), `P2` (normal fix), and `P3` (low impact), considering both impact and likelihood. Do not assign high severity without evidence. Return no more than five findings per PR; group additional well-supported issues and prioritize the most important.
6. **Report tests honestly.** Give the exact command and result for tests actually executed. Merely reading test files is not execution. If testing was not possible or permitted, say `not run`. Propose only relevant missing scenarios; do not add pointless tests for a numerical target.
7. **Suggest the smallest fix.** For each finding, explain the narrowest safe change and how to verify it. Do not suggest major architectural changes, a complete rewrite, or broad refactoring without a specific reason.
8. **Remain read-only.** Unless explicitly asked, do not edit files, commit, push, comment on or approve a PR, merge, trigger CI/CD, or deploy. Even with authorization, destructive actions require separate explicit approval. Do not expose secrets, access tokens, or customer data in the report.

## Output

Provide a short, prioritized report in the user's language.

- **Scope:** Reviewed PR, commit, files, and access limitations.
- **Findings:** Up to five verified or well-supported findings, each with severity such as `[P1]`, file/line reference, triggering conditions, impact, and targeted fix. Do not present speculation as a proven defect.
- **Test status:** Tests actually run, their results, and what was not run.
- **Overall assessment:** Whether the documented risks should be addressed before merge, and what remains unknown.

**If no findings:** State `No substantiated issue was found in the reviewed changes.` Clarify briefly that this is not a guarantee about the entire repository or runtime.

## Other skills

- `technical-troubleshooter`: Diagnose the root cause of a production failure.
- `code-reviewer`: Evaluate bugs and regression risk introduced by a code change.
- `web-audit`: Evaluate a website's visitor experience.

## Examples

`$code-reviewer Review this GitHub PR for functional risks and cite exact file/line ranges.`

`$code-reviewer Does this diff introduce data loss, authorization, or backward-compatibility risks?`
