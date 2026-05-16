# Step 01: Pre-flight Checks

## Establish project directory

ACTION: Run `pwd` and retain the result as `project-dir`. This directory is the project root — all article data, research output, and the finished article will be written here.

ACTION: Create the following subdirectories inside `project-dir` if they do not already exist:
- `{project-dir}/resources/` — research resources written by the researcher plugin
- `{project-dir}/outputs/` — finished article and other deliverables

## Mirantis resources

ACTION: Ask the user whether they have a local Mirantis resources directory — a folder of canonical Mirantis reference documents such as whitepapers, deep dives, and product overviews. If yes, record its path as `mirantis-resources-dir`. If no, set `mirantis-resources-dir` to null.

## Credentials note

NOTE: Credentials used for filling gated PDF forms during research are stored by the researcher plugin at `${CLAUDE_PLUGIN_DATA}/config/` or `~/.claude/plugins/data/researcher-mirantis-plugins/.env`. The researcher plugin manages these — run `/setup` within the researcher plugin if credentials have not been configured.

ACTION: Inform the user that pre-flight checks are complete and STOP. Please await further instructions.
