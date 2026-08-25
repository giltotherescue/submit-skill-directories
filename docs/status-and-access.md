# Status, access, and listing units

This document explains how the Submit skill directories playbook classifies directories and how agents should act on each class.

## Status values

| Status | Meaning | Agent action |
|--------|---------|--------------|
| `active` | Directory is open and the manifest is current enough to target. | Include in proposals when the project matches `hosts` and `item_types`. |
| `wait` | Blocked by prerequisites (org plan, invite, queue, manual review backlog) or manifest needs verification. | Mention in the plan with blockers; do not file until unblocked. |
| `skip` | Deprecated, duplicate, or out of scope for this project. | Do not propose or file. |

Update `status` in the manifest when you learn a directory changed policy. Prefer a PR to this repo over ad-hoc notes in project logs.

## Access classes

| Class | Description | Typical workflow |
|-------|-------------|------------------|
| `web_form` | Browser submission (GitHub OAuth, org admin portal). | Collect fields from `proposal_fields`, propose, file after approval. |
| `github_pr` | Curated list or catalog in a GitHub repo. | Use `gh` or GitHub API to read structure; open **one YAML PR per directory** in *this* repo for manifest fixes, and a separate PR in the *catalog* repo for the listing. |
| `github_api` | Programmatic registration (GitHub App, API hook). | Follow manifest `access.notes`; never clone the catalog repo. |
| `cli_publish` | Host or registry CLI (`gh skill publish`, vendor CLI). | Document the command in the proposal; run only after user approval. |
| `email` | Human gate via email. | Draft email in the proposal; send only after approval. |
| `invite_only` | No public submission path. | `wait` unless the user has an invite. |
| `auto_index` | Crawls public repos or well-known paths. | Ensure repo layout matches discovery rules; no separate filing step. |

### Catalog repo rules

- **Never clone** directory or catalog repositories. Use `gh api`, `gh pr view`, or raw GitHub URLs.
- If you fork a catalog repo to open a listing PR, **delete the fork** after the PR merges or closes.
- For manifest maintenance in *this* repo, follow [CONTRIBUTING.md](../CONTRIBUTING.md): one directory = one YAML PR.

## Listing unit (`listing_unit`)

Directories disagree on what a single listing represents. The playbook normalizes four units:

| Unit | One listing is… | Use when… |
|------|-------------------|-----------|
| `skill` | A single `SKILL.md` (or skill folder). | Directory imports repos and may fan out to many cards. |
| `plugin` | A host plugin package (manifest + bundled components). | Cursor/Claude plugin marketplaces, `plugin.json` / `.cursor-plugin/` layouts. |
| `product` | A product or suite (may include plugin + docs + MCP). | Team marketplaces, monorepos marketed as one offering. |
| `either` | Directory accepts more than one shape; agent must choose. | Community indexes with auto-detection. |

### Section 1.6 combo table (SKILL.md)

| Project shape | Strategy |
|---------------|----------|
| Bundled plugin | Plugin/product channels only; skip splits_skills boards and per-skill CLIs unless user opts in |
| Plugin + standalone skills | Union of plugin + skill directories |
| Plugin + MCP / skill + MCP / all three | Union of matching channels, honoring `listing_unit` per manifest |

## `splits_skills`

When `splits_skills: true`, the directory ingests a GitHub repo and may register **each** discovered `SKILL.md` separately (common on repo-import skill boards).

Default agent behavior:

1. **Skip** these directories for bundled plugins unless the user opts into per-skill cards.
2. For single-skill repos or explicit per-skill campaigns, set `listing_unit: skill` in the proposal.
3. Prefer directories with `listing_unit: plugin` or `product` for bundled host plugins.

Repo-import skill boards in this catalog — **only these eight** may use `splits_skills: true` with `listing_unit: skill`:

- `skills-sh`
- `skills-re`
- `skillsplayground`
- `agentskill-sh`
- `github-gh-skill-index`
- `localskills-sh`
- `vskill`
- `skillsdirectory-com`

No other manifest may set `splits_skills: true`. The validator enforces this.

## Install copy (end users)

When writing README or directory descriptions, recommend:

- **Host marketplace or plugin install** (Cursor Marketplace, Claude plugin marketplaces, team marketplace import, in-app plugin browser).

Do **not** lead with:

- `npx skills add …`
- `gh skill install …` (as the primary distribution story)
- Per-path skill CLIs as the main install path

CLI commands are fine as secondary/advanced options after the host-native install path.

## Logging

Record every proposal and filed submission in the **target project** at:

```
.agent-directory-submissions/log.yaml
```

Copy the template from [templates/.agent-directory-submissions/](../templates/.agent-directory-submissions/). One log entry per directory touch (proposed, approved, filed, merged, rejected, skipped).
