# Basamak Skills

**Practical, open-source AI agent skills for building, growing and operating digital businesses. Created by Basamak Bilişim.**

[**Türkçe**](README.tr.md) · [Installation](docs/installation.md) · [Workflows](workflows/) · [Changelog](CHANGELOG.md) · [MIT license](LICENSE)

Basamak Skills is a library of **13 self-contained agent skills**. Each skill defines when to use it, an evidence-based workflow, concrete outputs and safety boundaries. Skills are instructions, **not hosted software or automatic access to your accounts**.

## Skills

### Websites and growth

| Skill | What it does |
| --- | --- |
| [web-audit](.agents/skills/web-audit/SKILL.md) | Review website usability, content, trust and visitor journeys |
| [conversion-optimizer](.agents/skills/conversion-optimizer/SKILL.md) | Identify conversion friction and prioritize small, evidence-backed improvements |
| [saas-positioning](.agents/skills/saas-positioning/SKILL.md) | Clarify SaaS audiences, differentiation, proof and messages |
| [pricing-review](.agents/skills/pricing-review/SKILL.md) | Evaluate SaaS packages, renewal pricing and transition risks |

### Software engineering

| Skill | What it does |
| --- | --- |
| [technical-troubleshooter](.agents/skills/technical-troubleshooter/SKILL.md) | Diagnose application or infrastructure failures safely |
| [software-planner](.agents/skills/software-planner/SKILL.md) | Turn feature requests into scoped tasks and acceptance criteria |
| [code-reviewer](.agents/skills/code-reviewer/SKILL.md) | Review real code changes for concrete bugs and regressions |
| [release-readiness](.agents/skills/release-readiness/SKILL.md) | Review evidence and risks before a production release |

### Automation and AI

| Skill | What it does |
| --- | --- |
| [automation-discovery](.agents/skills/automation-discovery/SKILL.md) | Find and rank worthwhile business automation opportunities |
| [workflow-architect](.agents/skills/workflow-architect/SKILL.md) | Design resilient workflows, exceptions and recovery |
| [ai-feasibility](.agents/skills/ai-feasibility/SKILL.md) | Compare AI, deterministic automation and hybrid approaches |

### Customer operations

| Skill | What it does |
| --- | --- |
| [support-assistant](.agents/skills/support-assistant/SKILL.md) | Triage support requests and draft customer responses and tasks |
| [subscription-lifecycle](.agents/skills/subscription-lifecycle/SKILL.md) | Design renewal, notice, expiry and reactivation processes |

**Languages:** English is canonical for automatic discovery (`SKILL.md`); a full Turkish reference (`SKILL.tr.md`) sits beside every skill. Ask the agent to reply in your preferred language. Packaging checks do **not** guarantee quality of model behavior in either language.

## Quick start for Codex

Git and Bash are required on the machine where Codex runs.

```bash
git clone https://github.com/basamakcomtr/basamak-skills.git
bash basamak-skills/scripts/install.sh --user
```

Install into one existing project instead:

```bash
bash basamak-skills/scripts/install.sh --project /path/to/project
```

The installer links **all 13 skills** into `~/.agents/skills/` or the project's `.agents/skills/`. It does not overwrite any existing skill. Keep the checkout in place and start a new agent session.

Example requests:

```text
Use automation-discovery to assess our manual invoice intake.
Rank opportunities without assuming AI is needed.
```

```text
Use conversion-optimizer to inspect the signup journey on our website.
Separate observed facts from hypotheses; suggest the top three fixes.
```

If the agent does not automatically discover a skill, ask it to read its `SKILL.md` directly. The documented installer targets Codex-compatible `.agents/skills/` layouts; other agents may require a different skill directory or installation method. **Claude Code, Cursor and other environments have not been independently verified here.** See [installation guidance](docs/installation.md).

## Guided workflows

- [From support request to code review](workflows/feature-request-to-review.md) ([Türkçe](workflows/feature-request-to-review.tr.md))
- [From automation opportunity to workflow design](workflows/automation-opportunity-to-design.md) ([Türkçe](workflows/automation-opportunity-to-design.tr.md))

These are **manual handoff guides**, not background agents or access to private product systems.

## Principles and boundaries

- Begin with the actual user goal; prefer the smallest useful change.
- Separate observed facts, supported claims, assumptions and missing evidence.
- Do not invent tests, analytics, competitor facts, financial outcomes or integrations.
- Use deterministic tools where they are simpler and safer than AI.
- Do not write to a live system, send customer messages, run paid API calls, deploy, bill, suspend or delete anything without separately granted authorization.

Run distribution checks from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

**Version:** [1.2.0](VERSION) · [Changes](CHANGELOG.md). Version in files does not imply a separate GitHub release/tag was created.

**License:** [MIT](LICENSE), Copyright © 2026 Basamak Bilişim. Not affiliated with or endorsed by OpenAI or any specific agent vendor.
