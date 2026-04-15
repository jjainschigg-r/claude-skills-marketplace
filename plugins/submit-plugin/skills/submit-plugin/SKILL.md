---
name: submit-plugin
description: Submits a Claude Code plugin to the Mirantis skills marketplace
---

You are managing the complete plugin submission workflow for the Mirantis Claude Skills Marketplace. Follow every step in order. Stop and explain clearly if any step fails. **Do not merge the PR** — merging is a decision for human curators.

---

## Step 1: Gather information

Ask the user for:
1. The path to their plugin folder (must contain `.claude-plugin/plugin.json`)
2. Which tier the plugin belongs to:
   - **platform** — a plugin dev tool (for building, reviewing, or submitting plugins)
   - **local** — prompt-only, no external tools, bounded blast radius
   - **extended** — MCP-equipped or accesses external services/systems

Read `.claude-plugin/plugin.json`. Confirm the plugin name with the user.

---

## Step 2: Security check

Perform a full security and compliance review of the plugin folder covering all of the following:

**Format compliance:** `plugin.json` valid with required fields; plugin name matches folder name; `skills/<name>/SKILL.md` exists; if MCP declared it references `.mcp.json` not inline; `.mcp.json` valid and referenced files exist; `README.md` present and non-empty.

**Credential and secret exposure:** API keys, tokens, bearer strings, AWS/GCP/Azure credential patterns, PEM blocks, private keys, password/secret/token variable assignments, included `.env` files.

**Dangerous behaviors:** Destructive operations without explicit user confirmation; sending external messages without confirmation; prompt injection risk (reading external content and passing it unsanitized to Claude); for MCP plugins, list all external endpoints contacted.

**Blast radius:** Rate LOCAL / MODERATE / ELEVATED with a one-paragraph justification.

**Dependencies (MCP plugins only):** Pinned vs. floating versions; known vulnerabilities; public registry use; license concerns.

**Documentation quality:** README accurately describes what the plugin does (compare to SKILL.md and server code); dangerous operations documented; prerequisites stated; MCP tools and services listed.

Rate each finding as 🚫 BLOCKER, ⚠️ WARNING, or ℹ️ INFO.

- If any **BLOCKERs** are found: stop. Tell the user what to fix. Do not continue until they confirm the issues are resolved and ask to try again.
- If **WARNINGs** are found: present each one and ask the user to explicitly acknowledge it before continuing. Do not proceed until all are acknowledged.

Record the full report text — it goes in the PR.

---

## Step 3: Test attestation

Ask: "Please briefly describe how you tested this plugin: what input did you use, what did it do, and what was the output?"

Record the response for the PR.

---

## Step 4: Clone the marketplace repository

```bash
rm -rf /tmp/cms-submit
git clone https://github.com/jjainschigg-r/claude-skills-marketplace.git /tmp/cms-submit
```

---

## Step 5: Create a PR branch

```bash
git -C /tmp/cms-submit checkout -b submit/<plugin-name>
```

---

## Step 6: Copy the plugin

Copy the plugin folder to `/tmp/cms-submit/plugins/<plugin-name>/`. Exclude files matching common ignore patterns: `.venv/`, `__pycache__/`, `node_modules/`, `.env`, `site/`, `*.pyc`.

---

## Step 7: Promote the README to docs

Determine the docs destination:
- **platform** → `/tmp/cms-submit/docs/skills/plugin-dev-tools/<plugin-name>.md`
- **local** → `/tmp/cms-submit/docs/skills/<plugin-name>.md`
- **extended** → `/tmp/cms-submit/docs/skills/<plugin-name>.md`

Copy the plugin's `README.md` to that path.

Then update `/tmp/cms-submit/mkdocs.yml`. Read the file first, find the correct nav section, and add the new entry:
- **platform** → under `Plugin Dev Tools:`
- **local** → under `General Purpose Skills:` (create the section if absent, after Plugin Dev Tools)
- **extended** → under `Extended Skills:` (create the section if absent, after General Purpose Skills)

---

## Step 8: Validate the docs build

```bash
cd /tmp/cms-submit && make setup && .venv/bin/mkdocs build --strict 2>&1
```

If this fails, stop. Show the user the error output. Do not push with a broken docs build.

---

## Step 9: Commit and push

```bash
git -C /tmp/cms-submit add -A
git -C /tmp/cms-submit commit -m "Add <plugin-name> plugin (<tier> tier)

<description from plugin.json>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git -C /tmp/cms-submit push -u origin submit/<plugin-name>
```

---

## Step 10: File the pull request

Run `gh pr create` from `/tmp/cms-submit` with a body matching this template exactly:

```
## Plugin submission: <plugin-name>

**Tier:** <tier>
**Description:** <description from plugin.json>
**Version:** <version from plugin.json>

---

## Security check report

<full report from Step 2>

---

## Test attestation

<user response from Step 3>

---

## Reviewer checklist

- [ ] README accurately describes what the plugin does
- [ ] Tier assignment is appropriate given the blast radius analysis
- [ ] No credentials, tokens, or PII hardcoded
- [ ] Warnings acknowledged by submitter (if any)
- [ ] Plugin tested by submitter (see attestation above)
```

Show the user the PR URL. Remind them that merging is a curator decision.

Clean up: `rm -rf /tmp/cms-submit`
