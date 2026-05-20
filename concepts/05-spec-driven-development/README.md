# 05 Spec-driven Development

## One-liner

Spec-driven Development dreht die Richtung um: Nicht Code ist die erste Wahrheit, sondern Absicht, Verhalten und Akzeptanzkriterien.

## Warum das wichtig ist

Agenten sind schnell genug, um falsche Annahmen sofort in Code zu verwandeln.

Ohne Spec passiert oft:

```text
Idee -> Agent schreibt Code -> Mensch entdeckt Missverständnis -> Patch auf Patch
```

Mit Spec:

```text
Idee -> Spec -> Plan -> Tasks -> Implementierung -> Review gegen Spec
```

Das ist nicht mehr Papierkram. Es ist Drift-Kontrolle.

## Was eine gute Mini-Spec enthält

- Problem
- Nutzer oder Stakeholder
- aktuelles Verhalten
- gewünschtes Verhalten
- Non-goals
- Akzeptanzkriterien
- Edge Cases
- Verifikationsbefehle

Im Workshop gibt es zwei Varianten:

- **Greenfield**: Die Spec erzeugt erst die Produktform. Beispiel: ein neues Puzzle-Spiel braucht PRD, Mechanics Spec, Testvertrag und erste Slice.
- **Brownfield**: Die Spec begrenzt eine Änderung in vorhandener Form. Beispiel: der Flock-Timer-Bug braucht Failure, Scope, Non-goals und Verifikationsbefehl.

## Spec Kit als Ökosystemsignal

GitHub Spec Kit macht diesen Ablauf agententauglich und spricht explizit mehrere Coding Agents an. Wichtig ist nicht, dass jeder Spec Kit installieren muss. Wichtig ist das Prozessmuster:

```text
specify -> plan -> tasks -> implement
```

## Mini-Beispiel

Greenfield vage:

```text
Build a novel puzzle game.
```

Greenfield besser:

```text
First write three concepts, recommend one, then write a PRD, mechanics spec,
test plan, and first implementation slice. Do not implement yet.
```

Brownfield vage:

```text
Fix the timer test.
```

Brownfield Spec:

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
Write a PRD and mechanics spec for a novel minimal puzzle game. Do not edit code yet.
```

Danach:

```text
Write a mini-spec for fixing the failing Flock timer precision regression. Do not edit code yet.
```

Vergleiche:

```text
Which spec had to create product shape, and which spec had to respect existing shape?
```

## Takeaway

Specs machen Agenten nicht langsamer. Specs machen falsche Geschwindigkeit sichtbar.
