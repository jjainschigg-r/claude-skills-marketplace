---
name: plugin-scaffold
description: Generates a complete, correctly structured Claude Code plugin directory from a plain-language description
---

Generate a new Claude Code plugin directory. Gather the following from the user before creating any files:

1. What the plugin should do (plain language)
2. Plugin name — suggest a kebab-case name based on their description and confirm it
3. Does it need external code?
   - **No** — pure prompt/skill with no scripts
   - **Helper scripts (no MCP)** — bundled Python or Bash scripts called from the SKILL.md
   - **MCP server — Python** (via `uv`)
   - **MCP server — Node.js** (via `npm`)
4. Which tier: `platform`, `local`, or `extended`
5. Their name or team name (for the README maintainer field)

Create a new directory named `<plugin-name>` in the current working directory containing the following files:

---

### `.claude-plugin/plugin.json`

```json
{
  "name": "<plugin-name>",
  "description": "<one-sentence description derived from what the user told you>",
  "version": "1.0.0"
}
```

Add `"mcpServers": "./.mcp.json"` if the plugin uses MCP.

---

### `skills/<plugin-name>/SKILL.md`

Write a real SKILL.md prompt based on what the user described — not a placeholder. Keep it concise and action-oriented. If you cannot write the full logic from the description alone, write the best stub you can and note clearly what the user needs to fill in.

---

### `README.md`

Generate a complete README with these sections in order:
- `# <plugin-name>` — H1 heading
- Description paragraph (what it does and why it's useful)
- `## Prerequisites` — if the plugin requires any tools, accounts, or permissions; omit this section if there are none
- `## Install` — with the `/plugin install <plugin-name>@mirantis-plugins` command
- `## Use` — with the `/<plugin-name>` invocation and a brief description of what happens
- `## How it works` — one short paragraph on the implementation approach
- `## Details` — table with Version, Tier, and Maintained by fields

---

### For plugins with helper scripts (no MCP), also create:

**`skills/<plugin-name>/scripts/<plugin-name>.py`** (Python) or **`skills/<plugin-name>/scripts/<plugin-name>.sh`** (Bash) — a real, self-documenting script stub based on what the user described. Include:

- A module-level docstring listing all subcommands and their arguments
- At least one meaningful subcommand stub (not just `pass`) that reflects the plugin's actual purpose
- Argparse (Python) or `case` statement (Bash) for structured CLI invocation

In the `SKILL.md`, reference the script using `${CLAUDE_PLUGIN_ROOT}`:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/<plugin-name>/scripts/<plugin-name>.py" <subcommand> [args]
```

Do **not** place scripts at the plugin root — the loader only allows `skills/`, `server/`, `.claude-plugin/`, `.mcp.json`, `run-server.sh`, and `README.md` at the top level.

---

### For MCP Python plugins, also create:

**`.mcp.json`**
```json
{
  "<plugin-name>-server": {
    "command": "uv",
    "args": ["run", "${CLAUDE_PLUGIN_ROOT}/server/mcp_server.py"]
  }
}
```

**`server/mcp_server.py`** — FastMCP stub with PEP 723 inline dependencies and one placeholder tool named after the plugin's purpose. Include the uv script header:
```python
# /// script
# dependencies = ["mcp", "fastmcp"]
# ///
```

---

### For MCP Node.js plugins, also create:

**`.mcp.json`**
```json
{
  "<plugin-name>-server": {
    "command": "bash",
    "args": ["${CLAUDE_PLUGIN_ROOT}/run-server.sh"]
  }
}
```

**`run-server.sh`** — install-and-run wrapper that checks for `node_modules` in `${CLAUDE_PLUGIN_DATA}`, runs `npm install` on first run, copies the server to the data directory, and starts it with Node. Make it executable.

**`server/package.json`** — minimal package with `"type": "module"` and `@modelcontextprotocol/sdk` as a dependency.

**`server/index.js`** — ES module MCP server stub with one placeholder tool.

---

After creating all files, summarize what was created and what the user needs to fill in. Suggest running `/plugin-docs-lint` on the README as they develop, and `/plugin-security-check` when they think it's ready.
