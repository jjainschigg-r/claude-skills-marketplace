# seo-claude-plugin

Produces a complete, SEO-optimized Mirantis blog article from a ProductiveShop article brief. The workflow guides Claude through nine sequential steps: brief extraction, Mirantis positioning, research brief, researcher handoff, outline-and-stats annotation, drafting, and two editing passes for sourced assertions and uniform voice.

---

## Prerequisites

- **`/researcher-claude-plugin`** must be installed — it handles the web research phase (step 5)
- A ProductiveShop article outline `.md` file to process
- Optionally: a local Mirantis resources directory containing whitepapers, deep dives, and product overviews

## Install

If you haven't added the marketplace yet:

```
/plugin marketplace add https://jjainschigg-r.github.io/claude-skills-marketplace/marketplace.json
```

Then install the plugin:

```
/plugin install seo-claude-plugin@mirantis-plugins
```

## Use

```
/seo-claude-plugin
```

Claude will guide you through the workflow interactively. Each of the nine steps ends with a STOP — review the output, then instruct Claude to continue.

At step 5, the workflow pauses and asks you to invoke `/researcher-claude-plugin` with the assembled researcher call packet. Once research is complete and resources are saved, return and confirm to resume from step 6.

**Project output** is written to:
```
~/.claude/plugins/data/seo-claude-plugin-mirantis-plugins/projects/<project-name>/
```

Key output files:
- `<project-name>-article-data.json` — structured article data, Mirantis take, and research allocations
- `<project-name>-article.md` — the finished article draft
- `topic-direction-goal.md` — research brief
- `researcher-call.md` — researcher handoff packet
- `candidate-links.md` — index of retrieved resources (written by researcher plugin)
- `resources/*.txt` — full text of retrieved resources (written by researcher plugin)

## How it works

The plugin encodes the Mirantis SEO article workflow as a nine-step prompt sequence. Each step reads a bundled instruction file from the plugin root, performs its work, writes outputs to the plugin data directory, and stops for user review before advancing.

Steps 1–4 extract the article brief, gather the Mirantis perspective, and define the research brief. Step 5 assembles a structured handoff packet and passes control to `/researcher-claude-plugin`, which retrieves authoritative web resources and saves them as text files. Steps 6–9 resume with the researched material: annotating the outline with narrative arc notes and stats allocations, drafting the full article, sourcing every factual assertion with a linked citation, and applying a final voice and style pass.

## Details

| | |
|---|---|
| **Version** | 1.0.0 |
| **Tier** | platform |
| **Maintained by** | Mirantis |
| **Depends on** | `researcher-claude-plugin` |
| **Project data** | `~/.claude/plugins/data/seo-claude-plugin-mirantis-plugins/projects/` |
