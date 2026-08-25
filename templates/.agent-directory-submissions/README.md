# Directory submission log

This folder tracks skill, plugin, and MCP directory submissions for **this project**.

Agents using the [Submit skill directories](https://github.com/giltotherescue/submit-skill-directories) playbook should append entries to `log.yaml` — never overwrite history.

## What to log

- Proposals (before user approval)
- Filed submissions (PR URLs, form confirmations)
- Outcomes (merged, rejected, withdrawn)
- Skipped directories and why

## Rules

- One entry per directory touch; use `status` on the entry to mark lifecycle.
- Record `listing_unit` used (`skill`, `plugin`, `product`) for auditability.
- If a catalog fork was created, note `fork_deleted: true` when cleaned up.
- Do not clone catalog repos; link `gh`/`api` references only.

See `log.yaml` for the schema and examples.
