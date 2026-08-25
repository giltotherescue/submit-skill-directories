# Contributing

Thank you for improving the Submit skill directories playbook.

## One directory = one YAML PR

Each pull request should change **exactly one** file under `directories/` (or add one new manifest). This keeps review focused and matches how agents file catalog updates.

Examples:

- Good: `directories/cursor-directory.yaml` only
- Bad: `directories/cursor-directory.yaml` + `directories/skills-sh.yaml` in the same PR

Exception: typo fixes across docs/schema that a single manifest depends on may ride along if tiny and clearly linked — prefer splitting when in doubt.

## Adding or updating a manifest

1. Copy `directories/_template.yaml` to `directories/<id>.yaml`.
2. Fill required fields: `id`, `name`, `status`, `access`.
3. Set `listing_unit` and `splits_skills` accurately (see [docs/status-and-access.md](docs/status-and-access.md)).
4. Run validation:

   ```bash
   python3 scripts/validate_manifests.py
   ```

5. Open a PR with:
   - What directory changed and why
   - Links to official submission docs you used
   - Whether you verified access requirements (org plan, invite, etc.)

## Manifest quality bar

- Prefer **official** submission pages and docs over blog posts.
- Use `status: wait` when requirements are unclear; add `access.notes` explaining the blocker.
- Use `status: skip` for deprecated directories instead of deleting manifests (preserves history).
- Keep manifests **generic** — no product-specific examples in shared fields.
- `id` must match the filename (`cursor-directory.yaml` → `id: cursor-directory`).

## Schema changes

If you change `schema/directory.schema.json`:

- Update `scripts/validate_manifests.py` if needed.
- Migrate affected manifests in separate one-directory PRs when possible.

## SKILL.md and agent behavior

Changes to [SKILL.md](SKILL.md) affect all agents that load this skill. Call out behavioral changes in the PR description (proposal-before-file, bundled plugin listing unit, fork cleanup, etc.).

## License

By contributing, you agree that your contributions are licensed under the Apache License 2.0.
