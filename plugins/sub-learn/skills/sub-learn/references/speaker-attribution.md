# Speaker Attribution Rules

**The single most error-prone part of subtitle processing.** Follow these rules strictly.

## Core principle

**Never guess a speaker.** If the SRT does not explicitly tag a line with a speaker name, you do not know who said it. Context-based guessing is unreliable and produces confident errors that are hard to catch later.

## Explicit tags — safe

When SRT contains any of these, attribute confidently:

```
[Himmel] The royal capital's in sight.
```

→ `**Himmel**: The royal capital's in sight.`

```
- HEITER: I would take any job they let me drink on.
```

→ `**Heiter**: I would take any job they let me drink on.`

```
<font color="#FF0000">FERN: </font>I passed the test.
```

→ `**Fern**: I passed the test.`

## Implicit continuation — safe

A dialogue turn often spans multiple cues. If cue N has `[Speaker]` and cues N+1, N+2 follow immediately without any new speaker tag AND without a speaker change indicator, they belong to the same speaker:

```
[Himmel] I'll still have fun even then.
I'll relish our time adventuring.
Defeating monsters, finding treasure.
```

→ `**Himmel**: I'll still have fun even then. I'll relish our time adventuring. Defeating monsters, finding treasure.`

Speaker change indicators that BREAK continuation:

- A new `[Speaker]` tag
- `-` dash at the start of a cue (subtitle convention for "new speaker")
- A blank line in the SRT between cues (often indicates reaction shot / new speaker)
- Cue timing gap > 3 seconds

## Ambiguous — UNSAFE

If any of these apply, **do NOT guess**:

- Multiple untagged cues in a row with no clear speaker markers
- A scene with 3+ characters where context could fit any of them
- A reaction line that could be spoken OR thought (interior monologue)
- A voice that COULD be the previous speaker continuing OR a new speaker responding

In these cases, tag as `**?**:`:

```markdown
**?**: So, the deed is done.

**?**: I can't move a muscle. Wirbel? Can you please carry me?
```

## Reporting ambiguity

When you finish, list all `**?**:` lines in the summary report:

```
⚠️ Unresolved speakers (please verify):
- Line 239: "So, the deed is done."
- Line 242: "I can't move a muscle. Wirbel? Can you please carry me?"
```

The user can watch the scene and tell you who said each one, then you make one Edit to fix them.

## Specific trap: continuous dialogue

**Anti-pattern** (wrong):

```
[Frieren] Come, now. It's time we finish this.
[next cue] So, the deed is done.
[next cue] I can't move a muscle. Wirbel? Can you please carry me?
```

The second and third cues have no explicit speaker. An incorrect workflow would assume they're all Frieren. A correct workflow recognizes that after Frieren's line, the next untagged cues are speakers unknown — especially when a character named "Wirbel" is being addressed (so the speaker is NOT Wirbel, but it could be anyone in the scene).

**Correct output**:

```markdown
**Frieren**: Come, now. It's time we finish this.

**?**: So, the deed is done.

**?**: I can't move a muscle. Wirbel? Can you please carry me?
```

## Specific trap: speaker label across cue boundary

Sometimes a long line gets split across two cues and only the first cue has the speaker tag. The second cue has no tag, but it's clearly the same speaker continuing. This IS safe to merge:

```
[Denken] You don't know how to get along in this world, do you?
If you intend to continue living as a mage, it would most certainly behoove you to remain on my good side.
```

→ `**Denken**: You don't know how to get along in this world, do you? If you intend to continue living as a mage, it would most certainly behoove you to remain on my good side.`

Distinguish this from a new untagged speaker by checking:

- Does the second cue flow grammatically from the first? (Continuation.)
- Or does it feel like a response/reaction? (New speaker.)

When in doubt, split into two entries and mark the second as `**?**:`.

## Interior monologue

SRT marks interior monologue with `<i>...</i>`. These ARE attributable to the viewpoint character of the scene — usually the protagonist. But be careful: if the scene has multiple POV characters (flashbacks especially), `<i>` could belong to any of them. Use the same "when in doubt, mark `**?**:`" rule.

## Why this matters

Users notice speaker errors immediately — especially for memorable lines. A confident wrong attribution ("the deed is done" → Ubel when it was actually Methode) destroys trust. `**?**:` is an honest signal that preserves the user's time.

One correct `**?**:` is worth ten wrong guesses.
