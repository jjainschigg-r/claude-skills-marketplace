# seo-claude-plugin

Produces a complete, SEO-optimized Mirantis blog article from a ProductiveShop article brief. Guides Claude through nine sequential steps: brief extraction, Mirantis positioning, research brief derivation, web research (via the `researcher` plugin), outline annotation, drafting, and two editing passes for sourced assertions and uniform voice.

---

## Prerequisites

- The `researcher` plugin must be installed — it handles the web research phase
- A ProductiveShop article outline `.md` file
- Optionally: a local directory of canonical Mirantis reference documents (whitepapers, deep dives)

---

## Install

If you haven't added the marketplace yet:

```
/plugin marketplace add https://jjainschigg-r.github.io/claude-skills-marketplace/marketplace.json
```

Then install both plugins:

```
/plugin install researcher@mirantis-plugins
/plugin install seo-claude-plugin@mirantis-plugins
```

Run researcher setup:

```
/setup
```

---

## Use

Navigate to the directory where you want the article project to live, then invoke:

```
/seo-claude-plugin
```

Claude will guide you through the workflow interactively. **The working directory becomes the project root** — all output files are written there.

**Workflow overview:**

| Step | What happens | Pause? |
|------|-------------|--------|
| 1 | Establishes working directory, checks for Mirantis resources | Yes |
| 2 | Extracts structured data from the ProductiveShop outline | Yes |
| 3 | Gathers Mirantis perspective from you | Yes |
| 4 | Auto-derives research brief; asks for quick confirmation | Brief |
| 5 | Invokes the `researcher` plugin inline; runs full web research | No |
| 6 | Annotates outline with narrative arc and resource allocations | Yes |
| 7 | Drafts the full article in Markdown | Yes |
| 8 | Sources every factual assertion with a linked citation | Yes |
| 9 | Applies final voice and style pass; reports completion | Done |

**Output files written to the project directory:**

- `article-data.json` — structured brief data, Mirantis take, research allocations
- `topic-direction-goal.md` — research brief
- `candidate-links.md` — index of retrieved sources (written by researcher)
- `resources/*.txt` — full text of retrieved sources (written by researcher)
- `outputs/<project-name>-article.md` — the finished article draft

---

## How it works

The plugin encodes the Mirantis SEO article workflow as a nine-step prompt sequence. Each step reads a bundled instruction file from `${CLAUDE_PLUGIN_ROOT}`, performs its work, and writes output to the current working directory.

At step 5, the plugin locates the `researcher` plugin in the shared plugin cache (using `${CLAUDE_PLUGIN_ROOT}` to navigate to the sibling plugin directory) and executes its research skill inline — no manual re-invocation needed. The researcher detects the `topic-direction-goal.md` file written in step 4 and automatically enters directed research mode.

Both plugins use the current working directory as the project root, so the workflow is portable: run it from any directory, and all output lands there.

---

## Details

| | |
|---|---|
| **Version** | 1.0.0 |
| **Tier** | platform |
| **Maintained by** | Mirantis |
| **Depends on** | `researcher` |
| **Project output** | current working directory |
