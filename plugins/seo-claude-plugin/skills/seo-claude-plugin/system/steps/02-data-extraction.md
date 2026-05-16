# Step 02: Data Extraction

ACTION: Read and understand the base-article-data.json schema at:
`${CLAUDE_PLUGIN_ROOT}/skills/seo-claude-plugin/system/base-article-data.json`

Each field contains an `intent` explaining why it exists and a `prompt` explaining what data to extract and how to parse it.

ACTION: Ask the user:
1. The full path to the ProductiveShop article outline file they want to process
2. A short project name to use for naming output files — retain as `project-name`

ACTION: Read the article outline file at the path the user specified.

IF the outline appears to be missing required elements (Wrike task, meta title, meta description, URL slug, keywords, H2 headings, or a structured article outline with per-section writing instructions):
  STOP and inform the user of what is missing.
ELSE:
  ACTION: Create `{project-dir}/article-data.json` as a copy of base-article-data.json, then extract all data from the outline according to the intent and prompt instructions in each field. Populate `{project-dir}/article-data.json` with the extracted data.

ACTION: Inform the user that data extraction is complete and STOP. Please await further instructions.
