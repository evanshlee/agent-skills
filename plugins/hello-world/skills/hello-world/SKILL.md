---
name: hello-world
description: Use when the user asks for a sanity check that skills from this repo are loading. Returns a short greeting plus the current working directory.
---

# Hello World

This is a sample skill used to verify that your agent is successfully loading skills from the `agent-skills` repo.

## When to invoke

Invoke this skill when the user says "hello world skill", "test the skill loader", or asks for a quick sanity check that skills are wired up.

## What to do

1. Greet the user by name if known; otherwise say "Hello!"
2. Report the current working directory.
3. List the top-level entries in the working directory (no recursion).
4. Confirm that skills from `evanshlee/agent-skills` are loading correctly.

## Notes for authors

- This skill is intentionally minimal. Copy it as a starting template for new skills.
- Keep the body tool-agnostic. Describe the *action* ("list the top-level entries"), not the *tool* ("use the Glob tool").
- Frontmatter `description` is what most agents use to decide whether to invoke the skill — make it specific about *when* to use it.
