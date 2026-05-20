# Workshop: Vom vagen Wunsch zum Agent Contract

## Ziel

Du wandelst einen schlechten Agent-Auftrag in einen robusten Arbeitsauftrag um. Erst am kleinen Playground, dann am echten Flock-Bug.

## Dauer

20 bis 25 Minuten.

## Vorbereitung

Vom Repo-Root:

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

Die Tests dürfen fehlschlagen. Das ist Arbeitsmaterial.

Für den Realprojekt-Track:

```bash
git clone https://github.com/whiteducksoftware/flock.git
cd flock
git checkout lecture/timer-precision-bug-start
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

Der Flock-Test muss fehlschlagen. Das ist der eigentliche Arbeitsfall.

## Schritt 1: Schlechten Prompt bewusst ausprobieren

Gib deinem Agenten:

```text
Fix the failing tests.
```

Beobachte:

- Fragt der Agent nach dem richtigen Ordner?
- Liest er die Tests?
- Macht er zu große Änderungen?
- Nennt er den Verifikationsbefehl?

Stoppe den Agenten, wenn er zu viel driftet.

## Schritt 2: Agent Contract schreiben

Kopiere und fülle aus:

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
Read first. Explain likely causes. Then edit. Report exact verification.
```

## Schritt 3: Agent arbeiten lassen

Führe den Contract in deinem Harness aus.

Wenn dein Harness Plan Mode hat, nutze ihn. Wenn nicht, schreibe dazu:

```text
Before editing, show a short plan.
```

## Schritt 4: Mini-Retro

Vergleiche die beiden Läufe:

- Welche Dateien wurden gelesen?
- Wie groß war der Diff?
- Hat der Agent Done-Kriterien beachtet?
- War die Abschlussantwort prüfbar?

## Ergebnis

Du hast einen wiederverwendbaren Task-Prompt für Coding Agents und hast gesehen, warum echte Repos bessere Agentenführung erzwingen als Spielzeug-Code.

Speichere deine beste Version lokal in deinen Notizen oder in `resources/prompt-cards.md`, wenn du den Kurs weiterentwickelst.
