# sub-learn

Turn an SRT subtitle file into two companion markdown notes for language learning:

1. `{basename}-dialogue.md`: cleaned, human-readable dialogue with speaker tags
2. `{basename}-expressions.md`: curated expressions, vocabulary, grammar notes, Korean-friendly explanations, and writing prompts

## Usage

This is an agent skill, not a shell command. Paste one of these prompts into Codex or Claude instead of running `sub-learn` in a terminal.

```text
Use $sub-learn with ~/Downloads/episode.srt
Use $sub-learn with ~/Downloads/episode.srt --lang ko
Use $sub-learn with ~/Downloads/episode.srt --lang ja --test celpip
Use $sub-learn with C:/subs/E01.srt --output ~/notes/ --lang es --test ielts
```

Default explanation language is Korean (`--lang ko`). Use `--lang none` for English-only notes.

## Install with Codex

Paste this into Codex:

```text
Use $skill-installer to install this Codex skill:
https://github.com/evanshlee/agent-skills/tree/main/skills/sub-learn
```

Restart Codex after installation.

## Install with Claude Code

```text
/plugin marketplace add evanshlee/agent-skills
/plugin install sub-learn@evanshlee/agent-skills
```

## Files

- `skills/sub-learn/SKILL.md`: canonical skill entry point
- `skills/sub-learn/references/dialogue-format.md`: dialogue output spec
- `skills/sub-learn/references/expressions-format.md`: expressions output spec
- `skills/sub-learn/references/speaker-attribution.md`: speaker safety rules

The plugin package includes a copied version of the canonical skill for Claude Code plugin installation.
