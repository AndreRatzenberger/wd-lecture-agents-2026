---
name: repo-cartographer
description: Map a codebase before editing. Use when a user asks where a feature lives, how a flow works, what files matter, or when implementation should start with read-only orientation.
---

# Repo Cartographer

Use this skill before changing unfamiliar code.

## Inputs

- user goal or bug report
- current working directory
- any named files, errors, tests, or commands

## Workflow

1. Restate the task in one sentence.
2. Inspect repo shape with fast file search.
3. Read only files that can plausibly affect the task.
4. Identify entry points, data flow, tests, and risky assumptions.
5. Return a short map, not a full essay.
6. Do not edit files unless the user explicitly asks for implementation after the map.

## Output

```text
Task:
Relevant files:
Flow:
Likely change points:
Tests/checks:
Risks or unknowns:
Smallest next action:
```

## Rules

- Prefer real file references over guesses.
- Mark uncertainty explicitly.
- If the repo has instructions, read them before conclusions.
- Stop when the map is useful enough to guide the next action.
