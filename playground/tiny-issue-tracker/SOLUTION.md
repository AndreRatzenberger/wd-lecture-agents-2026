# Solution Notes

Spoiler fuer Facilitators und Selbstlernende.

## Erwarteter Startzustand

Der Testbefehl:

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

sollte importieren koennen und dann genau an `test_search_is_case_insensitive` scheitern.

## Ursache

`IssueTracker.search()` trimmt zwar den Suchtext, vergleicht aber case-sensitive:

```python
needle = text.strip()
return [issue for issue in self._issues if needle in issue.title]
```

Dadurch findet `"login"` nicht den Titel `"Fix Login"`.

## Kleinster Fix

```python
def search(self, text: str) -> list[Issue]:
    needle = text.strip().casefold()
    return [
        issue
        for issue in self._issues
        if needle in issue.title.casefold()
    ]
```

`casefold()` ist fuer case-insensitive Vergleiche robuster als `lower()`.

## Erwarteter Endzustand

Nach dem Fix:

```text
Ran 4 tests
OK
```

## Gute Agent-Antwort

Eine gute Abschlussantwort enthaelt:

- geaenderte Datei: `playground/tiny-issue-tracker/issue_tracker.py`
- Verifikation: exakter `python -m unittest ...` Befehl
- Scope: keine neuen Dependencies, keine API-Aenderung
- Restrisiko: keine Persistenz, keine fuzzy search, nur Titel-Suche getestet
