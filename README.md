# agent-skills

Provider-independent agent skills collection. Works with any LLM coding agent that can read markdown and frontmatter: Claude Code, Codex CLI, Cursor, Gemini CLI, Aider, and others.

## Why provider-independent?

Skills here are plain markdown with YAML frontmatter. They describe **intent** ("read the file", "search for the pattern") rather than vendor-specific tool names (`Read`, `Grep`), so any capable agent can map them to its own toolset.

## Structure

```
agent-skills/
├── AGENTS.md                          # cross-vendor repo guide
├── .claude-plugin/
│   └── marketplace.json               # Claude Code plugin marketplace manifest
└── plugins/
    └── <plugin-name>/
        ├── .claude-plugin/plugin.json # Claude Code plugin manifest
        ├── README.md
        └── skills/
            └── <skill-name>/
                └── SKILL.md           # frontmatter + skill body
```

Each subdirectory under `plugins/` is an independently installable unit.

## Install (Claude Code)

Add this repo as a marketplace, then install individual plugins:

```bash
/plugin marketplace add evanshlee/agent-skills
/plugin install hello-world@evanshlee/agent-skills
```

## Install (Codex CLI)

Codex CLI does not have a plugin marketplace; it relies on `AGENTS.md` context. Clone the repo once, then reference skills from your global or project `AGENTS.md`.

```bash
# clone once (update later with `git pull`)
git clone https://github.com/evanshlee/agent-skills.git ~/agent-skills
```

**Option A — global (every Codex session):** add to `~/.codex/AGENTS.md`:

```markdown
# Personal Skills

When the user's request matches one of these, read the corresponding SKILL.md and follow its instructions:

- hello-world: `~/agent-skills/plugins/hello-world/skills/hello-world/SKILL.md`
```

**Option B — per project:** add the same block to the project's `AGENTS.md` so the skill is only loaded for that repo.

**Option C — ad-hoc:** just tell Codex `follow ~/agent-skills/plugins/<name>/skills/<name>/SKILL.md` whenever you want it.

## Install (Cursor / Gemini CLI / Aider / other agents)

Any agent that can read markdown files works. Two common patterns:

1. **Reference from the agent's config file** — e.g., Cursor `.cursorrules`, Gemini CLI `GEMINI.md`, Aider `.aider.conf.yml` + CONVENTIONS.md. Point it at the SKILL.md path(s) you care about.
2. **Paste the skill body** into the agent's context at invocation time — works everywhere, no config needed.

Each `SKILL.md` is self-contained and does not depend on any vendor-specific tool names.

## Authoring a new skill

1. Create `plugins/<plugin-name>/` with `.claude-plugin/plugin.json` and `skills/<skill-name>/SKILL.md`
2. Write SKILL.md with frontmatter (`name`, `description`)
3. Keep instructions tool-agnostic — describe *what* to do, not *which* tool to call
4. Add an entry under `plugins[]` in `.claude-plugin/marketplace.json`

## License

MIT
