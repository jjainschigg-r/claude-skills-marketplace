# researcher

Web research assistant that discovers, fetches, and synthesizes authoritative sources — including PDFs behind gated landing pages — based on a topic, direction, and goal. Supports exploratory, directed, and perspective research modes.

---

## Prerequisites

- [Node.js and npm](https://nodejs.org/) (18 or higher) — required for the Playwright MCP server
- Run `/setup` after installing to download the Chromium browser and configure your credentials for gated PDF forms

---

## Install

If you haven't added the marketplace yet:

```
/plugin marketplace add https://jjainschigg-r.github.io/claude-skills-marketplace/marketplace.json
```

Then install the plugin:

```
/plugin install researcher@mirantis-plugins
```

Run one-time setup:

```
/setup
```

---

## Skills

### `/research`

Run a web research project. Claude walks you through mode selection, generates search phrases, discovers candidate sources, fetches web pages and PDFs, and produces a synthesis summary.

**Research modes:**

- **Exploratory** — broad topic coverage across diverse source types
- **Directed** — targeted retrieval of authoritative, quantitative sources to support a specific argument
- **Perspective** — community and practitioner opinion from Reddit, Hacker News, dev.to, forums

Invoke with an optional project directory path:

```
/research
/research /path/to/project
```

If invoked from within another plugin workflow (such as `seo-claude-plugin`), the research profile and output directory are passed in context automatically — no interactive setup needed.

Output is written to the working project directory:
- `candidate-links.md` — indexed list of all sources with status and file paths
- `resources/*.txt` — full extracted text of each retrieved source
- `research-summary.md` — thematic synthesis of findings

### `/fetch-pdf`

Retrieve a single PDF from a URL, including gated landing pages that require form submission. Handles cookie banners, form-filling, thank-you page navigation, PDF download, and text extraction.

```
/fetch-pdf https://example.com/whitepaper-landing-page
```

### `/setup`

One-time setup: verifies Node.js version, installs the Playwright Chromium browser, creates a credentials file for gated PDF forms, and confirms both MCP servers are running.

```
/setup
```

---

## How it works

The researcher plugin uses two MCP servers running alongside Claude Code:

- **Playwright** (`@playwright/mcp`) — drives a real Chromium browser for JS-rendered pages, cookie banners, and gated form submission
- **extract-pdf** (Node.js) — downloads PDFs and extracts their text, falling back to OCR for scanned documents

Web page retrieval tries `WebFetch` first, escalates to Playwright if the response is thin or JS-rendered. Each URL gets at most two attempts. Gated landing pages are handled by the `/fetch-pdf` skill, which fills forms using credentials stored in `${CLAUDE_PLUGIN_DATA}/.env`.

The plugin is designed to be called standalone or inline from another plugin. When `project-dir` is set in context by a calling plugin, all output is written there. When invoked directly, it uses the current working directory.

---

## Details

| | |
|---|---|
| **Version** | 1.0.0 |
| **Tier** | platform |
| **Maintained by** | Mirantis |
| **Runtime** | Node.js via `npm` (Playwright), `npx` |
| **MCP servers** | Playwright, extract-pdf |
| **Credentials** | `${CLAUDE_PLUGIN_DATA}/.env` |
