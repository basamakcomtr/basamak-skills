# Basamak Skills

**Open-source AI skills for Codex and compatible agents, created by Basamak Bilişim.**

[**Türkçe**](README.tr.md) · [Installation](docs/installation.md) · [Changelog](CHANGELOG.md) · [MIT license](LICENSE)

Each skill is a self-contained `SKILL.md` workflow with scope, evidence requirements, useful outputs, and safety boundaries.

## Available skills

| Skill | Purpose |
| --- | --- |
| [web-audit](.agents/skills/web-audit/SKILL.md) | Evidence-led website UX, content and conversion assessment |
| [technical-troubleshooter](.agents/skills/technical-troubleshooter/SKILL.md) | Safe technical diagnosis of application and infrastructure problems |
| [support-assistant](.agents/skills/support-assistant/SKILL.md) | Support triage, CRM task and customer reply drafts |
| [code-reviewer](.agents/skills/code-reviewer/SKILL.md) | Focused review of pull requests for concrete bugs and regression risk |
| [software-planner](.agents/skills/software-planner/SKILL.md) | Turn feature requests into scoped implementation tasks and acceptance criteria |

**Language:** The skill instructions are currently in Turkish. Ask your AI model to respond in your preferred language; English-language performance has not yet been independently tested.

## Quick installation

Requirements: Git and Bash, on the machine where Codex runs.

```bash
git clone https://github.com/basamakcomtr/basamak-skills.git
bash basamak-skills/scripts/install.sh --user
```

This links all five skills into `~/.agents/skills/`. For one project:

```bash
bash basamak-skills/scripts/install.sh --project /path/to/project
```

**No existing skill is overwritten.** Keep the cloned directory in place: the links point into it. Start a new Codex session after installation.

Example prompt:

```text
Use web-audit to evaluate https://example.com.
If the skill is not automatically discovered, first read
~/.agents/skills/web-audit/SKILL.md.
```

See [installation, updates and removal](docs/installation.md) for details.

## Combining skills

[From support request to code review](workflows/feature-request-to-review.md) documents the handoff:
`support-assistant` → `software-planner` → authorized development → `code-reviewer`.

This is a guided workflow, not an autonomous CRM or deployment integration.

## Safety

These are **instructions, not hosted services**. They do not contain credentials or provide access to any private system. They do not independently authorize code changes, deployments or customer communications. Static tests check package structure and installation, not the AI model's real-world accuracy.

**Version:** [1.0.0](VERSION) · [Changes](CHANGELOG.md). GitHub tag/release is a separate step.

**License:** [MIT](LICENSE), Copyright © 2026 Basamak Bilişim. Not an official OpenAI product.
