---
name: setup
description: One-time setup for researcher. Run this after installing the plugin.
---

Run the following checks in order. Report the result of each step clearly. Stop and report if any step fails — do not proceed past a failure.

## Step 1 — Check Node.js version

!`node --version 2>&1`

Node.js 18 or higher is required. If the version shown is below 18, or if `node` is not found, stop and tell the user to install Node.js from https://nodejs.org before continuing.

## Step 2 — Install Playwright browser

Run:

!`npx playwright install chromium 2>&1`

This downloads the Chromium binary that the Playwright MCP server requires. It is safe to run on a machine where Chromium is already installed — it will confirm the binary is up to date.

If this fails, report the error in full and stop. Playwright is required for retrieving JS-rendered pages and gated PDFs.

## Step 3 — Check credentials file

!`test -f "${CLAUDE_PLUGIN_DATA}/.env" && echo "found" || echo "missing"`

If the file is missing, create a blank template:

!`mkdir -p "${CLAUDE_PLUGIN_DATA}" && cat > "${CLAUDE_PLUGIN_DATA}/.env" << 'EOF'
RESEARCHER_NAME=
RESEARCHER_EMAIL=
RESEARCHER_COMPANY=
RESEARCHER_TITLE=
RESEARCHER_PHONE=
RESEARCHER_COUNTRY=
RESEARCHER_STATE=
EOF`

Then tell the user:

> Your credentials file has been created at `$CLAUDE_PLUGIN_DATA/.env`. Please open it and fill in your work contact details (name, email, company, title, phone, country, state). These are used to fill forms on gated research landing pages. The file stays on your machine and is never shared.

If the file already exists, check that none of the RESEARCHER_ fields are empty:

!`grep -E "^RESEARCHER_" "${CLAUDE_PLUGIN_DATA}/.env"`

If any values are blank, prompt the user to complete them before running research.

## Step 4 — Verify Playwright MCP is available

Attempt to use a playwright tool (e.g., navigate to about:blank). If playwright tools are available and responding, confirm this to the user.

If playwright tools are not available, tell the user:

> The Playwright MCP server is not running. It is configured in `.mcp.json` and starts automatically when Claude Code loads the plugin. Try restarting Claude Code. If it still fails, check that `npx` is available in your PATH and that Step 2 (chromium install) completed successfully.

## Step 5 — Verify extract-pdf MCP is available

Attempt to call the `extract_pdf` tool with a clearly invalid source to confirm the server is responding. It should return an error message (not a connection failure). If it responds at all — even with an error — the server is running correctly.

If the tool is not available, tell the user:

> The extract-pdf MCP server is not running. It starts automatically via `run-server.sh` when the plugin loads. Check that Node.js and npm are available in your PATH. You can test it manually by running `bash run-server.sh` from the plugin directory (after setting CLAUDE_PLUGIN_ROOT and CLAUDE_PLUGIN_DATA environment variables).

## Done

If all steps pass, tell the user:

> Setup complete. You're ready to run `/research`.
>
> To start a research project, type: `/research`
