# Onboarding questions

Agents should ask these (or infer from the repo) before proposing directory submissions. Skip questions already answered in the project or prior log entries.

## Project shape

1. What are we listing?
   - Standalone skill(s)
   - Bundled host plugin (manifest + 2+ `SKILL.md`)
   - MCP server only
   - Mixed plugin (skills + MCP + rules/commands)

2. Where do the artifacts live?
   - Repo URL and default branch
   - Paths to plugin manifest(s) and `SKILL.md` files
   - Public vs private repo (most directories require public)

3. Which agent hosts matter for this launch?
   - Cursor, Claude Code/Cowork, ChatGPT/Codex, Copilot, cross-platform, etc.

## Listing strategy

4. **Bundled plugin check (Section 1.6 combo table):**
   - Bundled plugin → plugin/product dirs only; skip splits_skills boards unless per-skill opt-in
   - Plugin + standalone skills → union of plugin + skill dirs
   - Any combo with MCP → union, honoring listing_unit per manifest

5. Which directories are in scope for this pass?
   - All `active` matches, or a named subset?
   - Any directories to `skip` (competitor, wrong audience, already listed)?

## Access and approvals

6. Do we have required access?
   - Org admin / Team plan for Claude directory forms
   - Cursor team marketplace admin
   - GitHub account linked to registry sites

7. **Approval gate:** Confirm before filing anything.
   - Propose title, description, URLs, and listing unit per directory
   - Wait for explicit approval (or configured auto-approve policy)

## Install story

8. What install path should README/directory copy emphasize?
   - Default: host marketplace or plugin install
   - Avoid leading with `npx skills add`, `gh skill install`, or per-path skill CLIs

## Logging

9. Confirm log location: `.agent-directory-submissions/log.yaml` in the **target project** (not this playbook repo).

## Follow-ups after filing

10. Track PR/issue URLs per directory in the log.
11. Delete catalog forks after merge/close.
12. Update manifest `status` here if a directory policy changes during review.
