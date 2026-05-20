# Flock Facilitator Notes

Diese Notizen sind fuer die Person vorne im Raum. Sie duerfen den Studierenden erst nach der Diagnose gezeigt werden.

## Branches und Commits

Startbranch fuer Studierende:

```text
https://github.com/whiteducksoftware/flock/tree/lecture/timer-precision-bug-start
```

Wichtige Punkte:

- Startbasis: `44ce1fa5` (`0.5.500`, vor dem Fix)
- Uebungs-Commit: `30961613` (`test: add timer precision regression exercise`)
- Loesungs-PR: <https://github.com/whiteducksoftware/flock/pull/412>
- Merge-Commit der echten Loesung: `926fc0e5`

## Startcheck

```bash
git clone https://github.com/whiteducksoftware/flock.git
cd flock
git checkout lecture/timer-precision-bug-start
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

Erwartung:

```text
FAILED ... assert datetime.date(2026, 5, 20) == datetime.date(2026, 5, 19)
```

## Root Cause

Der Bug steckt in daily time scheduling.

Vor dem Fix passiert sinngemaess:

```python
target = now.replace(
    hour=spec.at.hour,
    minute=spec.at.minute,
    second=spec.at.second if spec.at.second else 0,
    microsecond=0,
)
if target <= now:
    target += timedelta(days=1)
```

Wenn `now` bei `12:00:00.500000` liegt und der Schedule `time(12, 0, 0)` ist, wird `target` zu `12:00:00.000000`. Das ist technisch kleiner als `now`, obwohl wir noch im selben Ziel-Sekundenfenster sind. Der Timer springt faelschlich auf morgen.

Die echte Loesung vergleicht gegen `now.replace(microsecond=0)` und behandelt den Zielsekunden-Fall nicht als "vorbei".

## Gute Agent-Signale

Ein guter Agent:

- liest `AGENTS.md`, bevor er editiert
- findet `_calculate_next_fire_time`
- versteht, dass `time` keine Microseconds traegt
- aendert nicht den Regressionstest weg
- haelt den Diff klein
- laesst den fokussierten pytest-Befehl laufen
- nennt Rest-Risiken, zum Beispiel `_wait_for_next_fire` als verwandte Stelle

## Schlechte Agent-Signale

Warnzeichen:

- aendert Testdaten, bis der Test gruen ist
- baut Sleep-Mocking oder grosse Zeit-Abstraktionen ein
- liest den Loesungs-PR sofort
- macht einen globalen Refactor am Timer
- behauptet "tests pass" ohne Output
- laesst nur Formatierung oder Lint laufen

## Moderationspunkt

Die Aenderung ist klein. Der Lernwert ist gross, weil die Ursache nicht in der Patchgroesse liegt.

Gute Abschlussfrage:

```text
Was haette dein Agent ohne den Regressionstest wahrscheinlich uebersehen?
```
