# Step 04: Topic, Direction, and Goal for Research

ACTION: Reread `{project-dir}/article-data.json` to refresh context on article topic, structure, and the Mirantis perspective.

ACTION: Derive the three research parameters automatically from the article data:

1. **Topic** — derive from `meta_title`, `article_outline.h1_title`, and `keywords`. Should be broad enough to find authoritative resources, specific enough to stay on-topic.

2. **Direction** — derive from the H2 headings (which aspects need research support) and `mirantis_perspective.key_points` (which angles to substantiate). Apply standard source constraints:
   - Recency: 2024 or later; prefer 2025–2026
   - Authority: major media, analyst firms (Gartner, Forrester, IDC), official standards bodies, government sources
   - Exclude resources from: Red Hat, VMware, Rafay, Spectro Cloud
   - Prefer resources from Mirantis partners: NVIDIA, Pure Storage

3. **Goal** — derive from `mirantis_perspective.summary` and `mirantis_perspective.key_points`. Frame as what the research should indirectly demonstrate in support of Mirantis's position.

ACTION: Present the derived topic, direction, and goal to the user in a concise summary. Ask: "Does this research brief look right? Correct anything before I proceed." Apply any corrections the user provides.

ACTION: Write `{project-dir}/topic-direction-goal.md` recording the final topic, direction, and goal.

ACTION: Continue immediately to step 05 — do not STOP.
