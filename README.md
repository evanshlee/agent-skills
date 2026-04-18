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

## Install (other agents)

Clone the repo and point your agent at the `skills/` directory inside any plugin:

```bash
git clone https://github.com/evanshlee/agent-skills.git
```

Then configure your agent to load `plugins/<name>/skills/<skill>/SKILL.md`. Each SKILL.md is self-contained.

## Authoring a new skill

1. Create `plugins/<plugin-name>/` with `.claude-plugin/plugin.json` and `skills/<skill-name>/SKILL.md`
2. Write SKILL.md with frontmatter (`name`, `description`)
3. Keep instructions tool-agnostic — describe *what* to do, not *which* tool to call
4. Add an entry under `plugins[]` in `.claude-plugin/marketplace.json`

## License

MIT
