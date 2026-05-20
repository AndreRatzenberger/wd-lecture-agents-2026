# 05 Spec-driven Development

## One-liner

Spec-driven Development dreht die Richtung um: Nicht Code ist die erste Wahrheit, sondern Absicht, Verhalten und Akzeptanzkriterien.

## Warum das wichtig ist

Agenten sind schnell genug, um falsche Annahmen sofort in Code zu verwandeln.

Ohne Spec passiert oft:

```text
Idee -> Agent schreibt Code -> Mensch entdeckt Missverstaendnis -> Patch auf Patch
```

Mit Spec:

```text
Idee -> Spec -> Plan -> Tasks -> Implementierung -> Review gegen Spec
```

Das ist nicht mehr Papierkram. Es ist Drift-Kontrolle.

## Was eine gute Mini-Spec enthaelt

- Problem
- Nutzer oder Stakeholder
- aktuelles Verhalten
- gewuenschtes Verhalten
- Non-goals
- Akzeptanzkriterien
- Edge Cases
- Verifikationsbefehle

## Spec Kit als Oekosystemsignal

GitHub Spec Kit macht diesen Ablauf agententauglich und spricht explizit mehrere Coding Agents an. Wichtig ist nicht, dass jeder Spec Kit installieren muss. Wichtig ist das Prozessmuster:

```text
specify -> plan -> tasks -> implement
```

## Mini-Beispiel

Vage:

```text
Fix the timer test.
```

Spec:

```text
Problem:
Daily time schedules can wrap to tomorrow even when execution is still inside the target second.

Desired behavior:
If now is 12:00:00.500 and the schedule is time(12, 0, 0), the next fire time stays today.

Non-goals:
No cron rewrite, no new time abstraction, no dependency changes.

Acceptance:
- the focused timer regression passes
- existing interval, datetime, and cron behavior remains unchanged
- the regression test is not weakened
```

## Live-Demo

Bitte den Agenten:

```text
Write a mini-spec for fixing the failing Flock timer precision regression. Do not edit code yet.
```

Dann:

```text
Review the spec against the tests. What is missing?
```

## Takeaway

Specs machen Agenten nicht langsamer. Specs machen falsche Geschwindigkeit sichtbar.
