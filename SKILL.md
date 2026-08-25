---
name: Submit skill directories
description: >
  List agent skills, host plugins, and MCP servers on public directories and catalogs.
  Auto-detects project shape (standalone skill, bundled host plugin, MCP-only).
  Proposes submissions per directory manifest, files only after user approval,
  logs to .agent-directory-submissions/log.yaml in the target project.
  Use when the user wants directory listings, marketplace submissions, catalog PRs,
  or skill discovery board coverage.
---

# Submit skill directories

Generic playbook for proposing and filing listings on skill directories, host plugin marketplaces, and MCP catalogs. Stay product-neutral: describe the **target project** under submission, not this playbook repo.

## 0. Auto-detect project shape

Before reading manifests, classify the **target project** repository:

| Signal | Detection |
|--------|-----------|
| Standalone skill | One or few `SKILL.md` files, no host plugin manifest |
| Bundled host plugin | Host manifest (`.cursor-plugin/plugin.json`, `.claude-plugin/plugin.json`, Agent Plugins `plugin.json`) **and** 2+ first-party `SKILL.md` in that plugin |
| MCP server | `.mcp.json`, `mcp.json`, or MCP server package without skill bundle |
| Mixed plugin | Manifest + skills + MCP and/or rules/commands |

Also detect **host** affinity from paths:

- `.cursor/` → Cursor
- `.claude-plugin/` / `.claude/skills/` → Claude
- `.github/skills/` / Copilot docs → Copilot
- `.codex/` → Codex
- `.agents/skills/` → cross-platform

Load matching manifests from `directories/*.yaml` in this repo (or the installed copy). Filter by `status`, `hosts`, and `item_types`.

## 1. Workflow

### 1.1 Onboard

Ask or infer answers from [onboarding-questions.md](onboarding-questions.md). Confirm:

- Public repo URL and branch
- Listing goal (discovery, installs, credibility)
- Directories in scope

### 1.2 Initialize log (target project)

Ensure the **target project** has:

```
.agent-directory-submissions/log.yaml
```

Copy from [templates/.agent-directory-submissions/](templates/.agent-directory-submissions/) if missing. **Log in the target project**, not in this playbook repo.

### 1.3 Research manifests

For each candidate directory:

1. Read `directories/<id>.yaml`
2. Read [docs/status-and-access.md](docs/status-and-access.md)
3. Use `gh api` / `gh pr view` / official URLs only — **never clone catalog repos**

### 1.4 Propose (required)

For each `active` directory match, append a `proposed` entry to the target project's `log.yaml` with:

- `directory_id`, `listing_unit`, artifact paths
- Title, description, install copy
- Method (`web_form`, `github_pr`, `cli_publish`, …)

Present a single approval bundle to the user. **Do not file** until approved.

### 1.5 File (after approval)

After explicit approval:

1. Update log entry to `approved`, then `filed` with URLs/PR links
2. Execute submission (form, PR, CLI) per manifest
3. On completion, set `merged` / `rejected` / `skipped`
4. If you forked a catalog repo, **delete the fork** when the PR merges or closes

### 1.6 Listing unit — bundled plugins

When the target is a **bundled host plugin** (manifest + 2+ first-party `SKILL.md`):

- List as **one** `plugin` or `product` card per directory
- Do **not** create N skill cards for N skills

**Exception:** Directories with `splits_skills: true` import repos and may fan out per `SKILL.md`. **Skip** those for bundled plugins unless the user opts into per-skill cards.

Repo-import skill boards (`splits_skills: true`, default `listing_unit: skill`):

- `skills-sh`, `skills-re`, `skillsplayground`, `agentskill-sh`
- `github-gh-skill-index`, `localskills-sh`, `vskill`, `skillsdirectory-com`

For those, prefer plugin/product directories (`cursor-directory`, `claude-plugin-directory`, `cursor-marketplace-official`, team marketplaces) for bundled plugins.

### 1.7 Install copy

In proposals and directory descriptions, recommend:

- **Host marketplace / plugin install** (Cursor Marketplace, Claude plugin directory, team marketplace import, in-app plugin browser)

Do **not** lead with:

- `npx skills add …`
- `gh skill install …` as the primary story
- Per-path skill CLIs as the main distribution path

CLI install is fine as a secondary/advanced option.

## 2. Directory manifest fields

Manifests validate against [schema/directory.schema.json](schema/directory.schema.json).

| Field | Purpose |
|-------|---------|
| `status` | `active` / `wait` / `skip` |
| `access` | How to submit (`class`, `url`, `catalog_repo`) |
| `listing_unit` | `skill` / `plugin` / `product` / `either` |
| `splits_skills` | Repo-import fan-out behavior |
| `install_guidance` | End-user install wording |

## 3. Status handling

| Status | Action |
|--------|--------|
| `active` | Include in proposals when matched |
| `wait` | Note blockers; do not file |
| `skip` | Omit unless user overrides |

See [docs/status-and-access.md](docs/status-and-access.md).

## 4. Catalog PR hygiene

- **Never clone** directory/catalog repositories
- Use GitHub API / `gh` for read and PR operations
- **One YAML PR** per directory when updating manifests in this repo ([CONTRIBUTING.md](CONTRIBUTING.md))
- Delete catalog forks after PR merge/close

## 5. Validation

```bash
python3 scripts/validate_manifests.py
```

Run after editing manifests. Fix errors before proposing manifest changes upstream.

## 6. References in this repo

- [README.md](README.md) — human + agent overview
- [CONTRIBUTING.md](CONTRIBUTING.md) — one directory = one YAML PR
- [onboarding-questions.md](onboarding-questions.md) — intake checklist
- [directories/](directories/) — per-board manifests
