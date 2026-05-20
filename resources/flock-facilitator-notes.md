# Flock Facilitator Notes

Diese Notizen sind für die Person vorne im Raum. Sie dürfen den Studierenden erst nach der Diagnose gezeigt werden.

## Branches und Commits

Startbranch für Studierende:

```text
https://github.com/whiteducksoftware/flock/tree/lecture/timer-precision-bug-start
```

Wichtige Punkte:

- Startbasis: `44ce1fa5` (`0.5.500`, vor dem Fix)
- Übungs-Commit: `30961613` (`test: add timer precision regression exercise`)
- Lösungs-PR: <https://github.com/whiteducksoftware/flock/pull/412>
- Merge-Commit der echten Lösung: `926fc0e5`

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

Vor dem Fix passiert sinngemäß:

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

Wenn `now` bei `12:00:00.500000` liegt und der Schedule `time(12, 0, 0)` ist, wird `target` zu `12:00:00.000000`. Das ist technisch kleiner als `now`, obwohl wir noch im selben Ziel-Sekundenfenster sind. Der Timer springt fälschlich auf morgen.

Die echte Lösung vergleicht gegen `now.replace(microsecond=0)` und behandelt den Zielsekunden-Fall nicht als "vorbei".

## Gute Agent-Signale

Ein guter Agent:

- liest `AGENTS.md`, bevor er editiert
- findet `_calculate_next_fire_time`
- versteht, dass `time` keine Microseconds trägt
- ändert nicht den Regressionstest weg
- hält den Diff klein
- lässt den fokussierten pytest-Befehl laufen
- nennt Rest-Risiken, zum Beispiel `_wait_for_next_fire` als verwandte Stelle

## Schlechte Agent-Signale

Warnzeichen:

- ändert Testdaten, bis der Test grün ist
- baut Sleep-Mocking oder große Zeit-Abstraktionen ein
- liest den Lösungs-PR sofort
- macht einen globalen Refactor am Timer
- behauptet "tests pass" ohne Output
- lässt nur Formatierung oder Lint laufen

## Moderationspunkt

Die Änderung ist klein. Der Lernwert ist groß, weil die Ursache nicht in der Patchgröße liegt.

Gute Abschlussfrage:

```text
Was hätte dein Agent ohne den Regressionstest wahrscheinlich übersehen?
```
