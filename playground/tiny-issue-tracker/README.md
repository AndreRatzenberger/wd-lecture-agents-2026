# Tiny Issue Tracker

Mini-Codebase fuer die Hands-on-Aufgaben.

Es ist absichtlich klein, dependency-free und leicht kaputt. Der Punkt ist nicht Python. Der Punkt ist Agentenfuehrung.

## Dateien

- `issue_tracker.py`: kleine In-Memory Issue-Tracker-Logik
- `tests/test_issue_tracker.py`: Tests mit erwarteten Verhaltensweisen

## Tests

Vom Repo-Root:

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

Vom Playground-Ordner:

```bash
python -m unittest discover -s tests
```

## Typische Agent-Aufgabe

```text
Goal: Fix the failing tests in playground/tiny-issue-tracker.
Context: Read README.md, issue_tracker.py, and tests/test_issue_tracker.py first.
Constraints: No external dependencies. Keep the API stable unless a test proves otherwise.
Done when: unittest passes and you summarize the behavior change.
```

Wenn du festhaengst, lies [SOLUTION.md](SOLUTION.md). Nicht vorher. Der kleine Schmerz gehoert zum Lernmoment.
