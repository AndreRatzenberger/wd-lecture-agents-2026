# Workshop: Vom vagen Wunsch zum Agent Contract

## Ziel

Du wandelst einen schlechten Agent-Auftrag in einen robusten Arbeitsauftrag um und testest ihn am Playground.

## Dauer

20 bis 25 Minuten.

## Vorbereitung

Vom Repo-Root:

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

Die Tests duerfen fehlschlagen. Das ist Arbeitsmaterial.

## Schritt 1: Schlechten Prompt bewusst ausprobieren

Gib deinem Agenten:

```text
Fix the failing tests.
```

Beobachte:

- Fragt der Agent nach dem richtigen Ordner?
- Liest er die Tests?
- Macht er zu grosse Aenderungen?
- Nennt er den Verifikationsbefehl?

Stoppe den Agenten, wenn er zu viel driftet.

## Schritt 2: Agent Contract schreiben

Kopiere und fuelle aus:

```text
Goal:
Fix the failing tests in playground/tiny-issue-tracker.

Context:
Read playground/tiny-issue-tracker/README.md,
playground/tiny-issue-tracker/issue_tracker.py,
and playground/tiny-issue-tracker/tests/test_issue_tracker.py first.

Constraints:
No external dependencies.
Keep the public IssueTracker API stable.
Make the smallest change that explains the failing tests.

Done when:
python -m unittest discover -s playground/tiny-issue-tracker/tests passes.

Work style:
Read first. Explain likely causes. Then edit. Report exact verification.
```

## Schritt 3: Agent arbeiten lassen

Fuehre den Contract in deinem Harness aus.

Wenn dein Harness Plan Mode hat, nutze ihn. Wenn nicht, schreibe dazu:

```text
Before editing, show a short plan.
```

## Schritt 4: Mini-Retro

Vergleiche die beiden Laeufe:

- Welche Dateien wurden gelesen?
- Wie gross war der Diff?
- Hat der Agent Done-Kriterien beachtet?
- War die Abschlussantwort pruefbar?

## Ergebnis

Du hast einen wiederverwendbaren Task-Prompt fuer Coding Agents.

Speichere deine beste Version lokal in deinen Notizen oder in `resources/prompt-cards.md`, wenn du den Kurs weiterentwickelst.
