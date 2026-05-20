# Flock Hands-on

Dieses Blatt ist der Realprojekt-Track für den Workshop. Der kleine Issue Tracker bleibt gut für den ersten Aha-Moment. Flock zeigt danach, worum es wirklich geht: einen Agenten durch ein echtes Repo führen.

## Ziel

Studierende sollen an einem echten Bug arbeiten, der klein aussieht, aber ohne gutes Lesen schwer zu finden ist.

Sie üben:

- Repo-Onboarding mit `AGENTS.md`, README und Testdateien
- einen schlechten Auftrag in einen Agent Contract verwandeln
- eine Mini-Spec schreiben, bevor Code geändert wird
- einen engen Regressionstest als Beweis verwenden
- Diff und Tests vor der Abschlussantwort prüfen

## Setup

Voraussetzungen:

- Git
- Python 3.12+
- `uv`
- ein Coding-Agent-Harness wie Codex, Claude Code, GitHub Copilot, Cursor, Cline oder Windsurf

Clone:

```bash
git clone https://github.com/whiteducksoftware/flock.git
cd flock
git checkout lecture/timer-precision-bug-start
```

Der Branch enthält einen bewusst fehlschlagenden Regressionstest für einen Timer-Bug.

Prüfe den Startzustand:

```bash
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

Erwartung:

```text
FAILED tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds
```

Wenn dein Harness oder Rechner langsam ist: Die erste Ausführung darf etwas dauern, weil `uv` die Umgebung anlegt. Für diese Aufgabe brauchst du keinen API-Key.

## Wichtige Dateien

Lass den Agenten diese Dateien zuerst lesen:

```text
AGENTS.md
README.md
src/flock/components/orchestrator/scheduling/timer.py
tests/test_timer_component.py
```

Nicht zuerst lesen:

```text
https://github.com/whiteducksoftware/flock/pull/412
```

Der PR ist die Lösung. Er ist gut für den Abschlussvergleich, aber schlecht für den Lernmoment.

## Schlechter Auftrag

Gib deinem Agenten zuerst absichtlich wenig Kontext:

```text
Fix the failing test.
```

Beobachte:

- Findet der Agent die richtige Datei?
- Liest er `AGENTS.md`?
- Erklärt er den Zeit-/Microsecond-Fall?
- Ändert er nur Code, oder auch den Test?
- Nennt er am Ende den exakten Testbefehl?

Stoppe den Lauf, wenn er zu stark driftet.

## Besserer Agent Contract

Danach gib denselben Auftrag sauber:

```text
Goal:
Fix the failing timer precision regression on the current Flock branch.

Context:
Read AGENTS.md, README.md,
src/flock/components/orchestrator/scheduling/timer.py,
and tests/test_timer_component.py first.

Constraints:
Do not read PR #412 before diagnosing.
Do not change the regression test unless it is demonstrably wrong.
Keep the fix scoped to timer scheduling.
Do not add dependencies.

Done when:
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q passes.

Work style:
Read first. Explain the likely root cause. Propose a short plan. Then edit.
Report the exact verification output and changed files.
```

## Mini-Spec Prompt

```text
Write a mini-spec for the failing timer precision regression.
Do not edit files.

Include:
- observed failure
- current behavior inferred from code
- desired behavior inferred from the regression test
- non-goals
- acceptance criteria
- verification command

Keep it under 250 words.
```

## Ralph Loop Prompt

```text
Use the Ralph loop.

Read:
Inspect AGENTS.md, README.md, timer.py, and the failing test. Do not edit.

Ask:
Ask at most one blocking question. If none is needed, say "No blocker".

Lock:
Restate scope, non-goals, likely files to change, and done criteria.
Wait for confirmation.

Produce:
Implement the smallest fix and run the focused pytest command.

Halt:
Stop. Report changed files, verification, and residual risk.
```

## Abschluss-Audit

Nach der Agent-Änderung:

```bash
git diff
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

Fragen:

- Ist die Änderung kleiner als erwartet?
- Bleibt der Regressionstest unverändert?
- Erklärt der Code sowohl "später heute" als auch "schon vorbei"?
- Hat der Agent eine Abschlussantwort mit Beweis geliefert?

Zum Schluss darfst du den echten PR anschauen:

```text
https://github.com/whiteducksoftware/flock/pull/412
```

Vergleiche nicht nur die Lösung, sondern auch den Arbeitsweg.
