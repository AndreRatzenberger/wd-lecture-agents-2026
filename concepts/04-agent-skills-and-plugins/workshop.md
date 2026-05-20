# Workshop: Baue deine erste Agent Skill

## Ziel

Du baust eine kleine Skill, die einen Agenten vor Code-Änderungen zum Codebase-Mapping zwingt.

## Dauer

30 bis 35 Minuten.

## Schritt 1: Skill-Ziel festlegen

Wir bauen:

```text
repo-cartographer
```

Zweck:

> Wenn ein Agent eine unbekannte Codebase bearbeiten soll, soll er erst die relevanten Pfade, Tests, Risiken und kleinste nächste Aktion kartieren.

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

Wähle den passenden Ort:

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
Map the Flock timer scheduling path before any edits.
Task after mapping: identify why the focused timer regression fails and propose the smallest fix.
Do not edit yet.
```

## Schritt 5: Beschreibung testen

Eine Skill steht und fällt mit der `description`.

Teste zwei Prompts:

```text
Where does Flock calculate the next fire time for scheduled agents?
```

```text
I want to fix a timer precision bug in Flock, but first map the relevant code.
```

Frage:

- Würde der Agent die Skill finden?
- Ist die Beschreibung zu breit?
- Ist sie zu vage?

## Schritt 6: Mini-Iteration

Verbessere die Beschreibung so, dass sie echte Trigger enthält:

```yaml
description: Map a codebase before editing. Use when a user asks where a feature lives, how a flow works, what files matter, or when implementation should start with read-only orientation.
```

## Ergebnis

Du hast eine Skill als portablen Methodentransfer gebaut.

Bonus:

Verpacke sie als Plugin-Idee mit [../../examples/plugins/lecture-mini-plugin](../../examples/plugins/lecture-mini-plugin).
