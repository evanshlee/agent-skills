# Agent Guide

This repository publishes portable Agent Skills for Codex, Claude Code, and other agents that can read `SKILL.md` files.

## Source of truth

- `skills/<skill-name>/` is the canonical skill location.
- `plugins/<skill-name>/skills/<skill-name>/` is the Claude Code plugin copy.
- Do not edit plugin skill copies directly unless you also update the canonical copy.
- After editing `skills/`, run `python scripts/sync-claude-plugins.py` to refresh plugin copies.

## Skill conventions

- Every `SKILL.md` must include YAML frontmatter with `name` and `description`.
- Keep frontmatter portable. Do not add vendor-specific fields such as `allowed-tools` to canonical skills.
- Keep skill bodies tool-agnostic. Prefer "read the file" or "search for the pattern" over tool names like `Read`, `Grep`, or `Bash`.
- Add `agents/openai.yaml` for Codex-friendly UI metadata when creating a new skill.
- Use forward slashes in documentation paths when possible.
- Keep `SKILL.md` concise. Move long examples, schemas, and formatting rules into `references/`.
- Optional resources:
  - `references/` for material the agent should load only when needed.
  - `scripts/` for deterministic helper scripts.
  - `assets/` for templates or files used in outputs.

## Claude plugin conventions

- Each plugin lives under `plugins/<plugin-name>/`.
- Each plugin must include `.claude-plugin/plugin.json`.
- The root `.claude-plugin/marketplace.json` must list installable plugins.
- Plugin skill folders should mirror the canonical skill folders under `skills/`.

## Validation checklist

Before committing:

1. Confirm each `skills/<skill-name>/SKILL.md` has valid `name` and `description` frontmatter.
2. Confirm each `skills/<skill-name>/agents/openai.yaml` has useful UI metadata.
3. Confirm `.claude-plugin/marketplace.json` and each `plugin.json` parse as JSON.
4. Run `python scripts/sync-claude-plugins.py` after canonical skill edits.
5. Confirm install URLs in `README.md` point to `https://github.com/evanshlee/agent-skills/tree/main/skills/<skill-name>`.
6. Avoid secrets, tokens, local absolute paths, and vendor-specific tool names inside canonical skills.

## License

MIT. See `LICENSE`.
