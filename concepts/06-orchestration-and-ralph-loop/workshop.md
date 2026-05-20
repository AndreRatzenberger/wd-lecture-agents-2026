# Workshop: Ralph Loop fuer Greenfield und Flock

## Ziel

Du fuehrst einen Agenten in fuenf klaren Phasen durch zwei Situationen:

- Greenfield: erste Puzzle-Spiel-Slice aus einer Spec bauen.
- Brownfield: Flock-Bug in bestehender Codebase reparieren.

## Dauer

25 bis 30 Minuten.

## Track A: Greenfield Puzzle Slice

Vorbereitung: Du hast PRD, Mechanics Spec und Testplan aus [../05-spec-driven-development/workshop.md](../05-spec-driven-development/workshop.md).

### Schritt 1: Read

```text
Ralph loop, phase Read.
Do not edit files.
Read the approved PRD, mechanics spec, and test plan for the puzzle game.
Return:
- the first implementation slice
- non-goals
- tests that must exist
- production-ready gates for this slice
```

### Schritt 2: Ask

```text
Ralph loop, phase Ask.
Ask at most one blocking question.
If no question is needed, say "No blocker" and explain why.
```

### Schritt 3: Lock

```text
Ralph loop, phase Lock.
Restate:
- exact first slice
- files likely to create
- tests to write first
- non-goals
- done criteria
Wait for confirmation before editing.
```

### Schritt 4: Produce

```text
Ralph loop, phase Produce.
Implement only the locked first slice.
Write tests.
Run unit tests, build, and browser automation or Playwright MCP checks.
```

### Schritt 5: Halt

```text
Ralph loop, phase Halt.
Stop working.
Report:
- changed files
- commands run
- browser evidence
- production-ready gates passed
- gates not yet met
- residual risks
Do not make further changes.
```

## Track B: Brownfield Flock-Bug

### Schritt 1: Read

```text
Ralph loop, phase Read.
Do not edit files.
Inspect AGENTS.md, README.md,
src/flock/components/orchestrator/scheduling/timer.py,
and tests/test_timer_component.py.
Return the relevant facts and likely failure causes.
```

### Schritt 2: Ask

```text
Ralph loop, phase Ask.
Ask at most one blocking question.
If no question is needed, say "No blocker" and explain why.
```

### Schritt 3: Lock

```text
Ralph loop, phase Lock.
Restate:
- scope
- non-goals
- files likely to change
- done criteria
Wait for confirmation before editing.
```

Wenn du alleine arbeitest, bestaetige selbst:

```text
Confirmed. Continue to Produce.
```

### Schritt 4: Produce

```text
Ralph loop, phase Produce.
Implement the smallest change that satisfies the locked scope.
Run:
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

### Schritt 5: Halt

```text
Ralph loop, phase Halt.
Stop working.
Report:
- changed files
- verification command and result
- risks
- anything not verified
Do not make further changes.
```

## Variation: Drei Rollen

Wenn dein Harness Subagents oder custom agents kann:

1. Investigator: read-only map.
2. Builder: implement smallest fix.
3. Reviewer: compare diff against request.

Wenn nicht, fuehre die drei Prompts nacheinander im selben Chat aus.

## Ergebnis

Du hast aus zwei amorphen Auftraegen kontrollierte Arbeitssequenzen gemacht:

- Greenfield: "build a game" wird zu PRD -> Slice -> Tests -> Beweis.
- Brownfield: "fix the bug" wird zu Repo-Lesen -> Scope -> Fix -> Beweis.
