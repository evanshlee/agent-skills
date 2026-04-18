# hello-world

A minimal sample plugin that ships one skill, `hello-world`, to demonstrate the repo conventions.

## Install with Codex

Paste this into Codex:

```text
Use $skill-installer to install this Codex skill:
https://github.com/evanshlee/agent-skills/tree/main/skills/hello-world
```

Restart Codex after installation.

## Install with Claude Code

```text
/plugin marketplace add evanshlee/agent-skills
/plugin install hello-world@evanshlee/agent-skills
```

## Authoring note

The canonical skill lives at `skills/hello-world/`. This plugin package contains a copied version for Claude Code plugin installation.
