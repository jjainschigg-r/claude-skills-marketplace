#!/usr/bin/env python3
"""
Walks the plugins/ directory, reads each plugin's .claude-plugin/plugin.json,
and writes a marketplace.json index to site/marketplace.json.

Run by CI after mkdocs build, before pushing site/ to gh-pages.
"""

import json
import os
import sys

REPO = "jjainschigg-r/claude-skills-marketplace"
MARKETPLACE_NAME = "mirantis-skills"
PLUGINS_DIR = "plugins"
OUTPUT_PATH = os.path.join("site", "marketplace.json")


def load_plugin(plugin_dir):
    manifest_path = os.path.join(PLUGINS_DIR, plugin_dir, ".claude-plugin", "plugin.json")
    if not os.path.isfile(manifest_path):
        print(f"  WARNING: no plugin.json found in {plugin_dir}, skipping", file=sys.stderr)
        return None

    with open(manifest_path) as f:
        manifest = json.load(f)

    return {
        "name": manifest["name"],
        "description": manifest.get("description", ""),
        "version": manifest.get("version", "1.0.0"),
        "source": {
            "source": "github",
            "repo": REPO,
            "path": f"./plugins/{plugin_dir}"
        }
    }


def main():
    if not os.path.isdir(PLUGINS_DIR):
        print(f"ERROR: {PLUGINS_DIR}/ directory not found. Run from repo root.", file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir("site"):
        print("ERROR: site/ directory not found. Run mkdocs build first.", file=sys.stderr)
        sys.exit(1)

    plugins = []
    for entry in sorted(os.listdir(PLUGINS_DIR)):
        if os.path.isdir(os.path.join(PLUGINS_DIR, entry)):
            print(f"Processing plugin: {entry}")
            plugin = load_plugin(entry)
            if plugin:
                plugins.append(plugin)

    marketplace = {
        "name": MARKETPLACE_NAME,
        "owner": {"name": "Mirantis"},
        "plugins": plugins
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(marketplace, f, indent=2)

    print(f"Wrote {len(plugins)} plugin(s) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
