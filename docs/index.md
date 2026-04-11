# Claude Skills Marketplace

Claude skills are ready-made capabilities that extend what Claude Code can do. Instead of explaining your workflow to Claude from scratch every time, you install a skill once and invoke it with a single command.

This marketplace is where Mirantis teams share the skills they've built.

---

## Prerequisites

You need **Claude Code** installed and running. If you haven't done that yet, ask IT — setup takes about five minutes and your Mirantis credentials are all you need.

---

## One-time setup

Add the Mirantis skills marketplace to your Claude Code installation. Open a terminal, start Claude Code, and run:

```
/plugin marketplace add https://ai.mirantis.com/claude-skills/marketplace.json
```

You only need to do this once. Claude Code will remember it.

---

## Browse available skills

To see what's available:

```
/plugin list
```

---

## Install a skill

```
/plugin install <skill-name>@mirantis-skills
```

Replace `<skill-name>` with the name of the skill you want. For example:

```
/plugin install example-skill@mirantis-skills
```

---

## Use a skill

Once installed, invoke a skill by typing `/` followed by its name:

```
/example-skill
```

Claude Code will run the skill in the context of whatever you're working on.

---

## Keep skills up to date

When new skills are added or existing ones are updated, refresh your local list:

```
/plugin marketplace update mirantis-skills
```

Then reinstall any skills you want to update.

---

## Contribute a skill

Built something useful? The skills in this marketplace are maintained in a shared repository. Reach out to your team lead or open a pull request — the more skills we share, the less we each have to reinvent.
