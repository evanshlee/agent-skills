# sub-learn

Turn an SRT subtitle file into two companion markdown notes for language learning:

1. `{basename}-dialogue.md`: cleaned, human-readable dialogue with speaker tags
2. `{basename}-expressions.md`: curated expressions, vocabulary, grammar notes, and writing prompts

## Usage

```text
sub-learn <srt-path> [--lang <code>] [--test <celpip|ielts|toefl|none>] [--output <dir>]
```

## Examples

```bash
sub-learn ~/Downloads/episode.srt
sub-learn ~/Downloads/episode.srt --lang ko
sub-learn ~/Downloads/episode.srt --lang ja --test celpip
sub-learn "C:/subs/E01.srt" --output ~/notes/ --lang es --test ielts
```

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
