# Workshop: Baue ein kleines Agent Contract File

## Ziel

Du formulierst dauerhafte Repo-Regeln, die ein Agent wirklich nutzen kann.

## Dauer

25 bis 30 Minuten.

## Schritt 1: Reibung sammeln

Notiere drei Dinge, die Coding Agents in Projekten oft falsch machen.

Beispiele:

- Sie editieren zu viele Dateien.
- Sie vergessen Tests.
- Sie installieren Dependencies ohne Grund.
- Sie ignorieren vorhandene Patterns.
- Sie erklaeren viel, aber liefern keinen Beweis.

## Schritt 2: Regeln operationalisieren

Wandle jede Reibung in eine pruefbare Regel um.

Schlecht:

```text
Be careful with tests.
```

Besser:

```text
Before saying done, run the narrowest relevant test command.
If tests cannot run, report the exact blocker.
```

## Schritt 3: Mini-AGENTS.md schreiben

Erstelle in einer Scratch-Datei oder direkt im Prompt:

```markdown
# Agent Instructions

## Project Shape

- This task runs in the Flock repo.
- Flock is a Python 3.12+ project managed with uv.
- The current exercise branch is `lecture/timer-precision-bug-start`.
- The failing behavior lives in timer scheduling.

## Work Rules

- Read `AGENTS.md`, `README.md`, the relevant implementation file, and the failing test before editing.
- Keep changes scoped to timer scheduling.
- Do not read PR #412 before diagnosing.
- Do not add dependencies.
- Before saying done, run:
  `uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q`

## Done Means

- Tests pass, or the exact blocker is reported.
- The final answer names changed files and verification evidence.
```

## Schritt 4: Agent damit arbeiten lassen

Gib deinem Agenten zuerst die Instruktionen, dann den Auftrag:

```text
Use the following agent instructions for this task:

<paste mini instructions>

Task: Fix the failing Flock timer precision regression.
```

## Schritt 5: Scope-Check

Frage den Agenten nach Abschluss:

```text
Audit your own work against the agent instructions. Which rules did you follow, and what remains unverified?
```

## Ergebnis

Du hast eine erste Version eines Repo-Agent-Contracts und ein Gefuehl dafuer, welche Regeln wirklich helfen.
