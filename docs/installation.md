# Installation, updates and removal

[**Türkçe**](kurulum.md) · [Home](../README.md)

Git and Bash are required. Codex must be able to load local SKILL.md files.

## Install for current user

```bash
git clone https://github.com/basamakcomtr/basamak-skills.git
bash basamak-skills/scripts/install.sh --user
```

Skills are symlinked into `~/.agents/skills/`. The source stays in the cloned directory.

## Install for one project

```bash
bash basamak-skills/scripts/install.sh --project /absolute/path/to/project
```

Skills are linked under that project's `.agents/skills/` directory. The installer pre-checks names and **never overwrites** existing directories, files or unrelated links.

## Use and verify

Start a new Codex session and ask it to use a skill. If automatic discovery is unavailable:

```text
Read ~/.agents/skills/code-reviewer/SKILL.md before reviewing this PR.
Do not change files.
```

A successful symlink check does not establish that your Codex build auto-discovers skills.

## Update

```bash
git -C basamak-skills status
git -C basamak-skills pull --ff-only
```

This updates linked instructions. Review the [changelog](../CHANGELOG.md) before updating.

## Remove

Remove only symlinks you have confirmed point into this checkout, either in `~/.agents/skills/` or in your project. Don't remove unrelated skills. You can then delete the cloned repository.

The scripts do not request credentials or access external services. Canonical `SKILL.md` instructions are in English. Every skill includes `SKILL.tr.md` containing the original Turkish instructions. The model should respond in your requested language; English model behavior has not yet been validated in an end-to-end Codex test.
