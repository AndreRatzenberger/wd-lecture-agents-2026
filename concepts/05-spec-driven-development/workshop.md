# Workshop: Spec fuer Greenfield und Flock

## Ziel

Du lernst zwei Spec-Arten:

- Greenfield: erst Produktform schaffen, bevor Code existiert.
- Brownfield: bestehendes Verhalten verstehen und den Fix begrenzen.

## Dauer

30 bis 35 Minuten.

## Track A: Greenfield Puzzle Game

Nutze [../../resources/greenfield-puzzle-game.md](../../resources/greenfield-puzzle-game.md).

### Schritt 1: Konzeptoptionen

```text
Do not implement.

Return three puzzle game concepts.
For each concept include:
- one-sentence core mechanic
- why it is novel enough
- why it is easy to learn
- why it is hard to master
- procedural generation approach
- losing condition
- mobile interaction model
- main implementation risk

Then recommend one concept and explain why it is the best workshop candidate.
```

### Schritt 2: PRD und Mechanics Spec

```text
Write a PRD and mechanics spec for the recommended puzzle game.
Do not implement.

Include:
- product goal
- target player
- core loop
- board/state model
- legal moves
- procedural generation rules
- scoring
- losing condition
- non-goals
- production-ready definition
- deterministic seed behavior for tests
```

### Schritt 3: Testvertrag und erste Slice

```text
Write the test plan and define the first implementation slice.
Do not implement.

The slice must include:
- one core mechanic
- deterministic seed mode
- unit-testable game logic separated from UI
- one losing condition
- one restart flow
- unit tests
- browser automation checks
```

Review-Frage:

```text
Could another developer implement this slice without guessing the game rules?
```

## Track B: Brownfield Flock-Bug

Jetzt dieselbe Spec-Disziplin in einer bestehenden Codebase.

### Schritt 1: Problem beobachten

Fuehre aus:

```bash
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

Notiere:

- Welche Tests schlagen fehl?
- Welches Verhalten erwarten sie?
- Was ist nicht Teil des Problems?

### Schritt 2: Spec-Prompt

```text
Write a mini-spec for fixing the failing Flock timer precision regression.
Do not edit files.

Include:
- problem
- current behavior inferred from code
- desired behavior inferred from tests
- non-goals
- acceptance criteria
- verification command

Keep it under 250 words.
```

### Schritt 3: Spec reviewen

Pruefe:

- Enthalten die Acceptance Criteria alle fehlschlagenden Tests?
- Gibt es versteckte neue Features?
- Ist ein Non-goal genannt?
- Ist der Testbefehl konkret?

Wenn noetig:

```text
Revise the spec. Remove any feature not required by the tests.
```

### Schritt 4: Plan erzeugen

```text
Based on the approved mini-spec, propose an implementation plan.
Use at most 3 steps.
Name the exact file(s) to change.
Do not edit yet.
```

### Schritt 5: Implementieren

```text
Implement the plan.
Keep the public timer API stable.
Run:
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

### Schritt 6: Review gegen Spec

```text
Audit the final diff against the mini-spec.
Return:
- acceptance criteria satisfied
- verification evidence
- unrelated changes, if any
- remaining risks
```

## Ergebnis

Du hast einen vollstaendigen kleinen Spec-Loop durchlaufen:

```text
Problem -> Spec -> Plan -> Code -> Verification -> Audit
```

Und du hast den Unterschied gesehen:

```text
Greenfield: Spec erzeugt die Arbeitsform.
Brownfield: Spec begrenzt die Aenderung in bestehender Form.
```
