# 04 Agent Skills and Plugins

## One-liner

Skills sind wiederverwendbare Arbeitsgewohnheiten für Agents. Plugins sind die Verpackung, mit der man solche Fähigkeiten verteilt.

## Warum das wichtig ist

Wenn du denselben Prompt zum dritten Mal schreibst, hast du wahrscheinlich keinen Prompt mehr. Du hast eine Methode.

Eine Agent Skill macht daraus ein kleines Paket:

```text
skill-name/
  SKILL.md
  scripts/
  references/
  assets/
```

Das `SKILL.md` sagt:

- wann die Skill relevant ist
- was der Agent tun soll
- welche Inputs und Outputs erwartet werden
- welche Referenzen oder Scripts bei Bedarf helfen

## Progressive Disclosure

Der große Trick ist Kontext-Sparsamkeit:

1. Der Agent sieht zuerst nur Name und Beschreibung.
2. Wenn die Aufgabe passt, lädt er das volle `SKILL.md`.
3. Weitere Dateien werden nur bei Bedarf gelesen.

Deshalb sind Skills so interessant: Sie bringen Methode in den Agenten, ohne jede Session mit allen Details zu fluten.

## Caveman als Aha-Beispiel

`JuliusBrussee/caveman` zeigt den Effekt sehr schön:

- kleine Idee: weniger Füllwörter
- agent-native Verpackung: Skill/Plugin/Rules für viele Harnesses
- messbarer Nutzen: weniger Output-Tokens
- hoher Wiedererkennungswert: man versteht sofort, was passiert

Der Kurs kopiert nicht den Stil. Der Kurs kopiert die Lektion:

> Eine gute Skill ist ein Verhalten, das man installieren kann.

## Skill vs Instruction vs MCP

| Ding | Zweck |
| --- | --- |
| Instruction file | dauerhaft gültige Projektregeln |
| Skill | on-demand Methode oder Expertise |
| MCP | externe Tools, Daten, Aktionen |
| Plugin | verteilbares Paket aus Skills, Tools und Integrationen |

## Live-Demo

Zeige [../../examples/skills/repo-cartographer/SKILL.md](../../examples/skills/repo-cartographer/SKILL.md).

Frage:

> Warum ist das besser als jedes Mal "please inspect the repo first" zu tippen?

Antwort:

- klare Trigger-Beschreibung
- definierter Output
- wiederverwendbar
- reviewbar im Git
- portabel zwischen Teams und Harnesses

## Takeaway

Skills sind nicht nur Prompt-Schnipsel. Gute Skills sind miniaturisierte Methodik.
