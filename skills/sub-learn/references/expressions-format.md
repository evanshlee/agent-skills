# Expressions Output Format

Specification for `{basename}-expressions.md`.

## Overall structure

```markdown
---
created: 2026-04-12T23:00:00-04:00
updated: 2026-04-12T23:00:00-04:00
source: {original SRT basename}
tags:
  - language-learning
  - expressions
---

# {Title} - Expressions

> Themes: {one-sentence distillation of the episode's thematic focus}.  
> 한국어 포인트: {for --lang=ko, one Korean sentence explaining why the expressions are useful for Korean learners}.

## Expressions

### 1. "{expression}"

- **Meaning**: {translation or paraphrase. For --lang=ko, natural Korean first; add a short English gloss only when useful.}
- **Context**: {speaker}: "{exact quote from dialogue}"
- **Nuance**: {for --lang=ko, explain register, tone, and common Korean-speaker pitfalls in Korean. Omit if not useful.}
- **Usage**: {when/how to use, with 1-2 additional English example sentences in italics}
- **Similar**: {2-3 related expressions}

### 2. "{expression}"
...

## Vocabulary

| Word | Meaning | Example from episode |
|---|---|---|
| {word} | {translation} | "{snippet}" |
...

## Grammar Notes

- **"{pattern}"** - {explanation}. For --lang=ko, include a short Korean explanation after the English pattern. _"{example}"_
...

## Questions

- {Writing prompt that references 2-3 expressions from above}
...
```

## Sections in detail

### Theme line

One blockquote sentence summarizing the episode's themes. Helps the learner frame the expressions within a narrative context, which aids retention.

Examples:

- `> Themes: cooperation vs solo play, Himmel's joy in the journey, Fern's borrowed motivation from Frieren.`
- `> Themes: lost love and late redemption, small kindnesses outlasting grand deeds.`

### Expressions section (~25-40 entries)

**Selection priority** (see also `SKILL.md`):

1. Idioms and collocations
2. Register shifts (formal/casual/rude)
3. Phrasal verbs / multi-word verbs
4. Grammar patterns rendered through dialogue
5. High-value single words in vivid context

**Per-entry format:**

```markdown
### N. "{expression}"

- **Meaning**: {target-language meaning, or English paraphrase if --lang=none. For --lang=ko, use natural Korean first.}
- **Context**: {Speaker}: "{exact dialogue quote}"
- **Nuance**: {for --lang=ko, 1-2 Korean sentences explaining tone/register and why a literal Korean translation may be awkward. Omit if not useful.}
- **Usage**: {One paragraph explaining when/how to use, with 1-2 fresh English example sentences in _italics_ that are NOT from the episode. Optionally flag with **{test}-level gold** if --test is set and the expression merits it.}
- **Similar**: {2-3 comma-separated related expressions or synonyms}
```

**Numbering**: Sequential from 1. Don't skip numbers. If you remove an entry during editing, renumber.

**Gold tags** (only when `--test` is set):

- `**CELPIP Writing gold**` - useful for CELPIP Writing Task 1/2
- `**CELPIP Speaking gold**` - useful for CELPIP Speaking tasks
- `**IELTS Writing gold**` / `**IELTS Speaking gold**`
- `**TOEFL Writing gold**` / `**TOEFL Speaking gold**`
- Apply sparingly - only entries that truly raise a learner's register or demonstrate sophisticated English

### Vocabulary table (~20-30 rows)

For single-word items that are valuable but don't need the full Expression treatment. Sort by order of appearance in the episode.

| Column | Content |
|---|---|
| Word | The word, with `(v.)` / `(adj.)` etc. if ambiguous |
| Meaning | Target-language meaning (or English paraphrase) |
| Example from episode | Short direct quote containing the word |

Prefer vocabulary that is:

- Slightly above conversational level
- Used in a memorable context in the episode
- Not trivially inferable from cognates

Skip: proper nouns, in-universe jargon, function words.

### Grammar Notes (~5-8 bullets)

Observed grammar patterns, not a grammar textbook. Each entry:

```markdown
- **"{pattern template}"** - {one-sentence explanation}. For --lang=ko, add a short Korean explanation of why the pattern feels different from Korean. _"{fresh example sentence}"_ {optional: test gold tag}
```

Good candidates:

- Subjunctive constructions ("If I were you, I'd have…")
- Inversion ("Not only did X, but also Y")
- Concessive patterns ("As X as Y is, Z")
- Infinitive-of-purpose, reduced relative clauses, participial phrases
- Tense interactions that differ from target language

### Questions section (3 prompts)

Three writing prompts, each:

- References a thematic moment from the episode
- Requires the learner to use 2-3 specific expressions from the list above
- Is concrete enough to generate a paragraph-length response

Template:

```markdown
- {Situation from the episode, 1 sentence}. Write about {parallel in learner's own life, 1 sentence}. Use "{expression A}" and "{expression B}".
```

## Language and test conventions

### --lang=ko (default)

- `**Meaning**` field: natural Korean first, concise English gloss optional
- Add `**Nuance**` when Korean speakers may misread tone, register, collocation, or literal meaning
- `Vocabulary` table "Meaning" column: Korean meaning
- `Usage` paragraph: English explanation plus English example sentences; add Korean clarification only when it prevents confusion
- Grammar notes: English pattern plus a short Korean explanation
- Questions: stay in English for output practice; add a short Korean hint if needed

### --lang=none

- All meanings in English
- Explanations in English
- No target-language text anywhere
- Omit the Korean theme line and `Nuance` bullets unless they are useful in English

### --lang=ja / es / zh / etc

- Follow the same structure as `ko`, but use the requested target language for meanings and learner-facing explanations

### --test={id}

- Add gold tags to ~30-40% of expressions (not all - sparingly)
- Add 1-2 gold tags to Grammar Notes section
- Include 1 sentence in the final Question that mentions the test (e.g., "This structure is common in CELPIP Writing Task 2.")

## Quality bar

Before writing:

1. **Every expression has a direct quote**. No paraphrased contexts.
2. **No fabricated examples**. The "Context" must be exact from the dialogue file.
3. **Usage examples** (in italics) are genuine English, not awkward literal constructions.
4. **Meaning translations** are natural in the target language, not word-for-word calques. For Korean, avoid awkward dictionary Korean.
5. **Korean explanations** help comprehension without replacing English practice.
6. **Gold tags** are honest signals, not decorative.

## What NOT to include

- Plot spoilers for later episodes
- Opinions on characters
- Show-internal jargon unless idiomatic (e.g., skip "Spiegel" unless it became a common noun)
- References to this skill or its author
- Motivational filler ("you can do it!")
