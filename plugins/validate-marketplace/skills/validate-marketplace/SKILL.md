---
name: validate-marketplace
description: Walks all plugins in a marketplace repository and reports format compliance issues
---

Validate all plugins in a Claude Code marketplace repository. Look for a `plugins/` directory in the current working directory. If not found, ask the user for the repository path.

For each subdirectory found directly under `plugins/` (and one level deeper if tier subdirectories are present), check:

1. `.claude-plugin/plugin.json` exists and is valid JSON with `name`, `description`, and `version` fields
2. Plugin name in `plugin.json` matches the directory name
3. `skills/<name>/SKILL.md` exists, where `<name>` matches the plugin name
4. If `.mcp.json` is present: it is valid JSON and all referenced files exist within the plugin directory
5. `README.md` exists and is non-empty
6. A docs page exists somewhere under `docs/skills/` for this plugin (search by filename `<name>.md`)
7. The plugin appears in `mkdocs.yml` navigation

---

Produce a report listing each plugin found and its status:

✅ **<plugin-name>** — all checks passed
⚠️ **<plugin-name>** — non-blocking issues: (list)
🚫 **<plugin-name>** — failing: (list missing or invalid items)

End with a one-line summary:
> Checked N plugins: X healthy, Y with warnings, Z failing.

This tool is read-only. It does not modify any files.
