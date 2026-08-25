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
| [scripts/validate_manifests.py](scripts/validate_manifests.py) | Manifest validator (expects 96 manifests) |
| [scripts/generate_catalog.py](scripts/generate_catalog.py) | Regenerate canonical catalog stubs |

Validate manifests:

```bash
python3 scripts/validate_manifests.py
```

## For agents

1. Read [SKILL.md](SKILL.md) — especially **Section 1.6 combo table** and the eight `splits_skills` boards.
2. Load manifests from `directories/*.yaml`; respect `status`, `listing_unit`, and `access.class`.
3. Copy [templates/.agent-directory-submissions/log.yaml](templates/.agent-directory-submissions/log.yaml) into the **target project** if missing.
4. Propose → wait for approval → file → update log → delete catalog forks.
5. Never clone catalog repos; use `gh` / GitHub API only.

## Directory catalog

**96 manifests** under `directories/` (plus `_template.yaml`). Each filename is the canonical `id` (e.g. `cursor-directory.yaml`, `skills-sh.yaml`).

- **Verified / active** where submission paths are documented (e.g. `cursor-directory`, `cursor-marketplace`, `claude-plugins-official`, `skills-sh`)
- **`status: wait`** stubs where the board exists but access needs verification
- **`status: skip`** for meta/duplicate/reference entries (e.g. `duplicate-awesome-claude-code-clones`, `anthropics-skills`)

Only these eight may use `splits_skills: true` with `listing_unit: skill`:

`skills-sh`, `skills-re`, `skillsplayground`, `agentskill-sh`, `github-gh-skill-index`, `localskills-sh`, `vskill`, `skillsdirectory-com`

See `directories/` for the full catalog and [docs/status-and-access.md](docs/status-and-access.md) for semantics.

## Contributing

Add or fix one directory at a time. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache License 2.0 — see [LICENSE](LICENSE).
