# Agent Guide

This repo is a collection of provider-independent agent skills. If you are an LLM coding agent reading this file, use it as the contract for how to operate in this workspace.

## Repo purpose

- Each subdirectory under `plugins/` is a self-contained unit with one or more skills under `skills/<name>/SKILL.md`.
- Skills are authored to be tool-agnostic: they describe intent (read, search, edit, run) rather than vendor-specific tool names.

## Conventions

- **Frontmatter**: every `SKILL.md` must have `name` and `description` fields at minimum.
- **Tool-agnostic language**: do not hardcode `Read`, `Grep`, `Edit`, or other Claude Code tool names inside skill bodies. Write "read the file at X" instead of "use the Read tool on X".
- **File paths**: use forward slashes for cross-platform compatibility.
- **No vendor lock-in assets**: avoid referencing `.claude/`, `.cursor/`, `.codex/` inside skill content. Vendor-specific manifests belong in their own directories (e.g., `.claude-plugin/`).

## Adding a skill

1. Pick or create a plugin directory under `plugins/<plugin-name>/`.
2. Add `.claude-plugin/plugin.json` with `name`, `version`, `description`.
3. Create `skills/<skill-name>/SKILL.md` with YAML frontmatter and body.
4. Register the plugin in `.claude-plugin/marketplace.json` under `plugins[]`.
5. Update the root `README.md` skill list if applicable.

## Testing a skill

Before committing:

- Invoke the skill in at least one agent (Claude Code recommended) and confirm the body is actionable without requiring platform-specific knowledge.
- If the skill references a shell command, verify it runs on both bash and PowerShell, or note the shell explicitly.

## License

MIT. See `LICENSE`.
