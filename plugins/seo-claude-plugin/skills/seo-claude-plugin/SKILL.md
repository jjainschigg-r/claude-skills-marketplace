---
name: seo-claude-plugin
description: Produces a complete, SEO-optimized Mirantis article from a ProductiveShop brief through a 9-step research-and-writing workflow.
---

# EXECUTION SEMANTICS

* ACTION: An executable step. Perform it.
* READ FILE: Load the full contents of the file into working context. Treat it as authoritative unless explicitly overridden.
* IF / ELIF / ELSE: Control flow. Evaluate top-to-bottom; execute the first matching branch only.
* STOP: Halt and await user instructions. Do not continue or improvise.
* NOTE: Non-executable explanatory text.

---

You are orchestrating the Mirantis SEO Article Workflow. This workflow takes a ProductiveShop article outline and produces a fully-researched, SEO-optimized Mirantis blog article through nine sequential steps.

## Path variables

- **plugin-root**: `${CLAUDE_PLUGIN_ROOT}` — bundled read-only files (step docs, writing rules, JSON schema)
- **plugin-data**: `${CLAUDE_PLUGIN_DATA}` — persistent plugin config only (credentials, preferences)
- **system-dir**: `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system`
- **steps-dir**: `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps`
- **project-dir**: established in step 01 from `pwd` — all project output lives here

## Step sequence

ACTION: Read and execute each step file below in order. Each file contains a sequence of ACTIONs — perform them all exactly and in sequence before moving to the next step. Step files will instruct you to STOP at their conclusion; await user instruction before advancing.

1. `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps/01-pre-flight-checks.md`
2. `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps/02-data-extraction.md`
3. `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps/03-mirantis-take.md`
4. `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps/04-topic-direction-goal.md`
5. `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps/05-invoke-researcher.md`
6. `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps/06-draft-article-1-outline-and-stats.md`
7. `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps/07-draft-article-2-write-sections.md`
8. `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps/08-edit-article-1-support-assertions.md`
9. `${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/steps/09-edit-article-2-uniform-voice.md`

ACTION: When all nine steps are complete, inform the user that the SEO article workflow is complete and STOP.
