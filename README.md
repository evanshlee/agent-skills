# agent-skills

Reusable Agent Skills by Evan Lee. The repository is designed to be friendly for both Codex users and Claude users while staying close to the portable Agent Skills convention: each skill is a folder with a `SKILL.md` entry point and optional `references/`, `scripts/`, or `assets/` resources.

## Skills

| Skill | What it does | Codex install prompt |
| --- | --- | --- |
| `hello-world` | Minimal sanity check that confirms a skill can load. | `https://github.com/evanshlee/agent-skills/tree/main/skills/hello-world` |
| `sub-learn` | Converts an SRT subtitle file into cleaned dialogue plus English-learning expressions, vocabulary, grammar notes, and prompts. | `https://github.com/evanshlee/agent-skills/tree/main/skills/sub-learn` |

## Repository layout

```text
agent-skills/
|-- README.md
|-- AGENTS.md
|-- skills/                         # Canonical skill folders for Codex and other skill loaders
|   |-- hello-world/
|   |   |-- SKILL.md
|   |   `-- agents/openai.yaml
|   `-- sub-learn/
|       |-- SKILL.md
|       |-- agents/openai.yaml
|       `-- references/
|-- plugins/                        # Claude Code plugin packages
|   |-- hello-world/
|   |   |-- .claude-plugin/plugin.json
|   |   `-- skills/hello-world/
|   `-- sub-learn/
|       |-- .claude-plugin/plugin.json
|       `-- skills/sub-learn/
|-- .claude-plugin/
|   `-- marketplace.json            # Claude Code marketplace manifest
`-- scripts/
    `-- sync-claude-plugins.py      # Copies canonical skills into Claude plugin packages
```

`skills/` is the canonical source of truth. The copies under `plugins/*/skills/` exist so Claude Code users can install the same skills through the Claude plugin marketplace.

## Install with Codex

The easiest path is to paste an install prompt into Codex.

### Install one skill

```text
Use $skill-installer to install this Codex skill:
https://github.com/evanshlee/agent-skills/tree/main/skills/sub-learn
```

Then restart Codex so it can discover the new skill.

### Install all current skills

```text
Use $skill-installer to install these Codex skills:
https://github.com/evanshlee/agent-skills/tree/main/skills/hello-world
https://github.com/evanshlee/agent-skills/tree/main/skills/sub-learn
```

Then restart Codex.

### Manual Codex install

If the installer is unavailable, copy a skill folder into your Codex skills directory.

PowerShell on Windows:

```powershell
$CodexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
New-Item -ItemType Directory -Force (Join-Path $CodexHome "skills") | Out-Null
Copy-Item -Recurse -Force ".\skills\sub-learn" (Join-Path $CodexHome "skills\sub-learn")
```

bash or zsh on macOS/Linux:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./skills/sub-learn "${CODEX_HOME:-$HOME/.codex}/skills/sub-learn"
```

Restart Codex after a manual install.

## Install with Claude Code

Claude Code users can install this repository as a plugin marketplace.

```text
/plugin marketplace add evanshlee/agent-skills
/plugin install sub-learn@evanshlee/agent-skills
```

To test the marketplace setup:

```text
/plugin install hello-world@evanshlee/agent-skills
```

## Manual Claude skill install

If you prefer plain skills instead of plugins, copy a folder from `skills/` into your Claude skills directory.

PowerShell on Windows:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\sub-learn" "$HOME\.claude\skills\sub-learn"
```

bash or zsh on macOS/Linux:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R ./skills/sub-learn "$HOME/.claude/skills/sub-learn"
```

Restart Claude Code after a manual install.

## Authoring a new skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Keep `SKILL.md` frontmatter minimal: `name` and `description` only.
3. Add `agents/openai.yaml` with UI metadata for Codex-friendly skill lists.
4. Put long supporting material in `references/` and reusable code in `scripts/`.
5. Keep instructions tool-agnostic. Write actions like "read the file" instead of vendor tool names.
6. Add a Claude plugin package under `plugins/<skill-name>/` with `.claude-plugin/plugin.json`.
7. Run the sync script so the plugin copy matches the canonical skill:

```bash
python scripts/sync-claude-plugins.py
```

8. Add the plugin entry to `.claude-plugin/marketplace.json`.
9. Update the skill table in this README.

## Maintenance

When you edit a skill, edit the canonical copy under `skills/` first. Then run:

```bash
python scripts/sync-claude-plugins.py
```

This keeps the Claude plugin packages in sync without making `plugins/` the source of truth.

## License

MIT
