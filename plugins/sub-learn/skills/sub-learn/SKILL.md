---
name: sub-learn
description: 'Convert a subtitle file (SRT) into structured language-learning notes: a cleaned dialogue transcript plus an expressions/vocabulary/grammar companion. Defaults to Korean learner-friendly explanations when no --lang is supplied. Use when the user provides a subtitle path and asks for "same treatment", "study notes", "learning notes", "dialogue + expressions", or invokes /sub-learn.'
---

# sub-learn

Turn a subtitle file into two companion markdown notes:

1. **`{basename}-dialogue.md`** - cleaned, human-readable dialogue with speaker tags
2. **`{basename}-expressions.md`** - curated expressions, vocabulary, grammar notes, Korean-friendly explanations, and writing prompts

No vault structure assumptions. No external files touched beyond the two outputs.

**Important:** This is an agent skill, not a shell command or installed CLI. Do not run `sub-learn` in Bash, zsh, or PowerShell. Treat `sub-learn <path>` examples as prompts/arguments for the agent to process.

## Purpose

Learning a language from film/TV subtitles is high-leverage: spoken dialogue is rich in idioms, collocations, and register shifts that textbooks miss. But raw SRT files are unreadable (timestamps, SFX, italics tags). This skill converts one episode's SRT into notes that are both a readable script and a targeted study aid.

## When to use

Invoke this skill when the user:

- Provides a path to an `.srt` file and says "same treatment", "study notes", "learning notes", "dialogue + expressions", or similar
- Types `/sub-learn <path>`
- Asks to "convert this subtitle to study material"
- References a previous output pattern and wants another episode processed the same way

Do **not** invoke for: general subtitle cleaning (no learning aid), translation-only tasks, or when the user wants raw plain text.

## Arguments

| Argument | Required | Default | Purpose |
|---|---|---|---|
| `<srt-path>` | Yes | - | Absolute or relative path to the SRT file |
| `--lang <code>` | No | `ko` | ISO 639-1 code for explanation language (e.g., `ko`, `ja`, `es`, `zh`). Default is `ko` because the primary audience is Korean English learners. Use `--lang none` for English-only notes. |
| `--test <id>` | No | `none` | Target English test for annotations. Accepts `celpip`, `ielts`, `toefl`, `none`. When set, mark relevant expressions with gold-standard tags (e.g., "**CELPIP Writing gold**"). |
| `--output <dir>` | No | Same folder as SRT | Directory where both output files are written |

### Invocation examples

These are prompts for the agent, not terminal commands:

```text
Use $sub-learn with ~/Downloads/episode.srt
Use $sub-learn with ~/Downloads/episode.srt --lang ko
Use $sub-learn with ~/Downloads/episode.srt --lang ja --test celpip
Use $sub-learn with C:/subs/E01.srt --output ~/notes/ --lang es --test ielts
```

If a user types `sub-learn ~/Downloads/episode.srt`, interpret it as an invocation request and process the file. Do not execute `sub-learn` in a shell.

## Workflow

### Step 1 - Read the SRT in chunks

SRT files are often long. Read in 800-line chunks using your agent's file-read offset/limit capability. If the first chunk is short (<500 lines), one read suffices. If larger, read sequentially until EOF.

### Step 2 - Parse metadata

Extract:

- **File basename** (without `.srt` extension) → used for output filenames
- **Series hint** from filename if present (e.g., `Show.S01E05.Title.en.srt` → series=`Show`, episode=`S01E05`, title=`Title`). Store for frontmatter. If no structure is detectable, use `basename` as-is.
- **Total cue count** (for sanity check)

### Step 3 - Resolve output directory

1. If `--output <dir>` is given, use it. Create the directory only if your agent environment provides a safe file/directory creation capability.
2. Else, use the directory of the input SRT.
3. Avoid shelling out unless necessary. If shell access fails with `command not found`, `permission denied`, or `missing file/path`, stop retrying the same command and switch to the agent's normal file tools or ask the user to verify the path.

### Step 4 - Build dialogue file

Follow `references/dialogue-format.md` precisely. Core rules:

- Strip timestamps, cue numbers, SFX brackets like `[music playing]`, `<i>...</i>` tags (convert italicized interior monologue to `*italics*`), song lyrics (`♪` marked).
- Merge multi-line cues from the same speaker.
- Preserve speaker attribution ONLY when SRT tags it explicitly with `[Name]` or `- Name:`. **Never guess** speakers for untagged continuous dialogue - see `references/speaker-attribution.md`.
- Group dialogue into thematic scenes separated by `---`.
- Add brief `*(scene context)*` italic stage directions when they help the reader orient.

### Step 5 - Build expressions file

Follow `references/expressions-format.md`. Core sections (in order):

1. **Frontmatter** (minimal)
2. **Theme line** (single-sentence distillation of episode themes)
3. **Expressions** (~25-40 entries, numbered, each with Meaning/Context/Usage/Similar)
4. **Vocabulary** table (~20-30 rows)
5. **Grammar Notes** (~5-8 bullets)
6. **Questions** (3 writing prompts tying 2-3 expressions each)

If `--lang` is omitted, use `ko`. If `--lang` is set, provide learner-facing explanations in that language. If `--test` is set, tag standout entries with gold labels. Do not fabricate - only mark entries that genuinely fit the test's scoring criteria.

### Step 6 - Write both files

Write to `<output-dir>/<basename>-dialogue.md` and `<output-dir>/<basename>-expressions.md`. Do not create any other files (no index updates, no logs).

### Step 7 - Report

Summarize concisely:

- Both file paths
- Expression/vocab/grammar/question counts
- Any speakers left as `**?**:` that the user should verify

## Frontmatter template

Both output files use this minimal, portable frontmatter:

```yaml
---
created: {ISO 8601 with timezone}
updated: {ISO 8601 with timezone}
source: {original SRT basename}
tags:
  - language-learning
  - {dialogue|expressions}
---
```

No series-specific tags. No vault-specific tags. Users can add their own after generation.

## Korean learner defaults

When `--lang ko` is active, including by default:

- Keep the dialogue file in the original subtitle language. Do not translate the full dialogue.
- In the expressions file, write `Meaning` in natural Korean first, with a concise English gloss only when useful.
- Add Korean nuance explanations where they help Korean speakers avoid literal translation mistakes.
- Keep English example sentences in English, because the output is for English practice.
- Keep writing questions in English, but add a short Korean hint if the task would otherwise be unclear.
- Prefer practical explanations over textbook grammar labels. When a grammar term appears, explain it briefly in Korean.

## Side effects

**None.** This skill writes exactly two files and touches nothing else. It does not:

- Update any index, log, or central vocabulary file
- Modify daily notes or journals
- Assume any surrounding directory structure
- Require network access

Users who want their own workflow integrations (daily logs, central vocab aggregation) should layer those on top of this skill's output.

## Priorities when selecting expressions

Prefer (in order):

1. **Idioms and collocations** that don't map word-for-word from the learner's language
2. **Register shifts** (formal↔casual, polite↔rude) that subtitles teach well
3. **Multi-word verbs / phrasal verbs** that cluster meaningfully
4. **Grammar patterns** rendered through dialogue (`as X as Y`, `not one to X`, etc.)
5. **Single high-value words** only when they appear in vivid context

Avoid:

- Dictionary-obvious words (table, run, eat) unless used in idiomatic ways
- Pure proper nouns or in-universe jargon
- Filler ("um", "yeah", "you know")
- Expressions only understandable through the show's lore

## Reference docs

- `references/dialogue-format.md` - dialogue output spec
- `references/expressions-format.md` - expressions output spec
- `references/speaker-attribution.md` - speaker safety rules (critical)

Read these when you invoke the skill.
