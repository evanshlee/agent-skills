# Dialogue Output Format

Specification for `{basename}-dialogue.md`.

## Overall structure

```markdown
---
created: 2026-04-12T23:00:00-04:00
updated: 2026-04-12T23:00:00-04:00
source: {original SRT basename}
tags:
  - language-learning
  - dialogue
---

# {Title} - Dialogue

{optional: opening epigraph or cold open, in blockquote if one exists}

---

*(scene 1 context)*

**Speaker**: Line of dialogue.

**Speaker**: Another line, possibly on the same turn.

---

*(scene 2 context)*

...
```

## SRT → Markdown conversion rules

### Keep

- Every spoken line of dialogue
- Explicit speaker tags from SRT (e.g., `[Himmel]`, `- Fern:`)
- Interior monologue - render as `*italics*` (matches SRT `<i>...</i>` tags)
- Scene transitions (derive from mood/setting shifts, even if SRT has no marker)

### Strip

- Cue numbers (`1`, `2`, `3`...)
- Timestamps (`00:01:23,456 --> 00:01:25,789`)
- SFX brackets: `[music playing]`, `[wind whooshing]`, `[explosion]`, `[door creaks]`
- `<i>`, `</i>` HTML tags (convert content to `*italics*`)
- Song lyrics (lines containing `♪` or in opening/closing theme blocks)
- `[speaker grunts]`, `[coughs]`, `[laughs]` - these are performance notes, not dialogue
- Duplicate ellipses / extra whitespace

### Transform

- **Multi-line cues** (one sentence split across 2-3 cues for timing) → single continuous line
- **Interior monologue** (`<i>He thought it would work.</i>`) → `*He thought it would work.*`
- **Onscreen text** (ALL CAPS location/time cards) → render as `*[LOCATION]*` or omit if redundant
- **Overlapping dialogue** → keep on separate `**Speaker**:` lines in speaking order

## Speaker attribution

CRITICAL: see `speaker-attribution.md` for full rules. Key points:

- Use `**SpeakerName**:` for explicitly tagged speakers
- Use `**?**:` for lines whose speaker is genuinely ambiguous (no tag, context unclear)
- Never assume the speaker of unmarked continuous dialogue is the same as the previous tagged line

## Scene grouping

Divide the dialogue into scenes using `---` separators. A scene boundary typically falls at:

- Location change (cue timing gaps, ALL CAPS location cards, music cues)
- Time jump (indicated by fade-to-black SFX or large timestamp gaps)
- Character group change (new speakers appearing with no existing speakers)
- Opening/closing theme markers

If the SRT has no obvious markers, use dialogue rhythm: a 3-5 second silence between cues often signals a scene shift.

## Scene context lines

After a `---`, optionally add a one-line stage direction in italics to orient the reader:

```markdown
---

*(At the restaurant, one hour later)*

**Denken**: This is it.
```

Keep these brief (≤10 words). Derive from SFX cues, location cards, and dialogue content. Omit if context is obvious from the previous scene.

## Formatting conventions

- Each `**Speaker**:` block is a paragraph. Leave blank lines between speaker turns.
- Consecutive lines from the same speaker can be kept in one block if they were one continuous turn in the SRT.
- Use `…` (horizontal ellipsis) or `...` (three dots) consistently - prefer `…` to match modern subtitle style.
- Preserve original punctuation including em dashes (`-`) and interrobangs (`?!`).
- Do not translate or paraphrase - the dialogue file is the source-language text, cleaned up.

## What NOT to include

- Translator credits / OpenSubtitles headers
- Copyright notices
- Font styling (`{\an8}`, `{\c&HFFFFFF&}` in ASS files)
- Broadcast timing marks

## Verification before writing

Before finalizing:

1. **Spot-check speaker attribution** - any `**?**:` lines? Flag them in the final report.
2. **No raw timestamps** - search for `-->` and `0\d:\d\d` to confirm all removed.
3. **No SFX leakage** - search for `[` and `]` to confirm all SFX brackets removed (except when preserved as `*(scene context)*`).
4. **Epigraph quality** - if the episode opens with voice-over narration, render it as a blockquote at the top before the first `---`.
