# Workshop: Baue deine erste Agent Skill

## Ziel

Du baust eine kleine Skill, die einen Agenten vor Code-Aenderungen zum Codebase-Mapping zwingt.

## Dauer

30 bis 35 Minuten.

## Schritt 1: Skill-Ziel festlegen

Wir bauen:

```text
repo-cartographer
```

Zweck:

> Wenn ein Agent eine unbekannte Codebase bearbeiten soll, soll er erst die relevanten Pfade, Tests, Risiken und kleinste naechste Aktion kartieren.

## Schritt 2: Skill-Datei ansehen

Lies:

```text
examples/skills/repo-cartographer/SKILL.md
```

Beachte besonders:

- `name`
- `description`
- Inputs
- Workflow
- Output-Format
- Regeln

## Schritt 3: In deinen Harness kopieren

Waehle den passenden Ort:

```text
Codex:        .agents/skills/repo-cartographer/SKILL.md
Claude Code:  .claude/skills/repo-cartographer/SKILL.md
Copilot:      .agents/skills/repo-cartographer/SKILL.md
```

Wenn du nichts installieren willst, kopiere die Skill einfach in den Prompt und simuliere sie.

## Schritt 4: Skill anwenden

Prompt:

```text
Use the repo-cartographer skill.
Map playground/tiny-issue-tracker before any edits.
Task after mapping: identify why the tests fail and propose the smallest fix.
Do not edit yet.
```

## Schritt 5: Beschreibung testen

Eine Skill steht und faellt mit der `description`.

Teste zwei Prompts:

```text
Where does the issue tracker decide which issue is next?
```

```text
I want to fix a bug in the issue tracker, but first map the relevant code.
```

Frage:

- Wuerde der Agent die Skill finden?
- Ist die Beschreibung zu breit?
- Ist sie zu vage?

## Schritt 6: Mini-Iteration

Verbessere die Beschreibung so, dass sie echte Trigger enthaelt:

```yaml
description: Map a codebase before editing. Use when a user asks where a feature lives, how a flow works, what files matter, or when implementation should start with read-only orientation.
```

## Ergebnis

Du hast eine Skill als portablen Methodentransfer gebaut.

Bonus:

Verpacke sie als Plugin-Idee mit [../../examples/plugins/lecture-mini-plugin](../../examples/plugins/lecture-mini-plugin).
