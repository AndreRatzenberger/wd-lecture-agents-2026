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
Make search better.
```

Spec:

```text
Problem:
Issue search currently misses titles with different casing.

Desired behavior:
Searching "login" finds an issue titled "Fix Login".

Non-goals:
No fuzzy search, no persistence, no CLI.

Acceptance:
- search trims surrounding whitespace
- search is case-insensitive
- existing create/list/close behavior remains unchanged
- test suite passes
```

## Live-Demo

Bitte den Agenten:

```text
Write a mini-spec for fixing the failing search test. Do not edit code yet.
```

Dann:

```text
Review the spec against the tests. What is missing?
```

## Takeaway

Specs machen Agenten nicht langsamer. Specs machen falsche Geschwindigkeit sichtbar.
