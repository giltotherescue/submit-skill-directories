# Submit skill directories

Reusable agent skill and playbook for listing **agent skills**, **host plugins**, and **MCP servers** on public directories and catalogs.

Licensed under **Apache-2.0**. Copyright 2026 Gil Hildebrand.

## For humans

This repository is a **generic submission playbook** — not tied to any single product. Point an agent at your project repo, load `SKILL.md`, and it will:

1. Auto-detect whether you have a standalone skill, bundled host plugin, or MCP server
2. Match you to directory manifests under `directories/`
3. **Propose** listings (title, description, listing unit, install copy)
4. **File only after your approval**
5. Log everything in your project at `.agent-directory-submissions/log.yaml`

### Bundled plugins = one listing

If your repo ships a **host plugin manifest** plus **two or more** first-party `SKILL.md` files, list it as **one plugin/product**, not one card per skill. Repo-import skill boards (`splits_skills: true`) are skipped for bundled plugins unless you want per-skill cards.

### Install copy

Recommend **host marketplace or plugin install** for end users — not `npx skills add`, `gh skill publish`, or per-path skill CLIs as the primary story.

### Contents

| Path | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Agent instructions (load this in Cursor or any Agent Skills host) |
| [directories/](directories/) | One YAML manifest per directory/board |
| [schema/directory.schema.json](schema/directory.schema.json) | Manifest JSON Schema |
| [docs/status-and-access.md](docs/status-and-access.md) | Status, access classes, listing units, fork rules |
| [CONTRIBUTING.md](CONTRIBUTING.md) | One directory = one YAML PR |
| [onboarding-questions.md](onboarding-questions.md) | Intake questions for agents |
| [templates/.agent-directory-submissions/](templates/.agent-directory-submissions/) | Log template for target projects |
| [scripts/validate_manifests.py](scripts/validate_manifests.py) | Manifest validator |

Validate manifests:

```bash
python3 scripts/validate_manifests.py
```

## For agents

1. Read [SKILL.md](SKILL.md) — especially **Section 1.6** (bundled plugin listing unit) and **splits_skills** behavior.
2. Load manifests from `directories/*.yaml`; respect `status`, `listing_unit`, and `access.class`.
3. Copy [templates/.agent-directory-submissions/log.yaml](templates/.agent-directory-submissions/log.yaml) into the **target project** if missing.
4. Propose → wait for approval → file → update log → delete catalog forks.
5. Never clone catalog repos; use `gh` / GitHub API only.

## Directory coverage

Manifests include official and community boards, for example:

- Cursor: `cursor-directory`, `cursor-marketplace-official`
- Claude: `claude-plugin-directory`, `claude-connectors-directory`
- ChatGPT / OpenAI: `chatgpt-plugins-directory`
- Repo-import skill boards (all `splits_skills: true`): `skills-sh`, `skills-re`, `skillsplayground`, `agentskill-sh`, `github-gh-skill-index`, `localskills-sh`, `vskill`, `skillsdirectory-com`
- Awesome / curated lists: `awesome-agent-skills`, `awesome-claude-code`, and others

See `directories/` for the full set and [docs/status-and-access.md](docs/status-and-access.md) for semantics.

## Contributing

Add or fix one directory at a time. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache License 2.0 — see [LICENSE](LICENSE).
