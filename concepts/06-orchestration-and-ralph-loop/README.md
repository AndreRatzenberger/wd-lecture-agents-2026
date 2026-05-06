# 06 Orchestration and Ralph Loop

## One-liner

Orchestrierung ist die Kunst, Agenten nicht nur arbeiten zu lassen, sondern Arbeit in sinnvolle Phasen, Rollen und Stopps zu zerlegen.

## Warum das wichtig ist

Ein einzelner langer Agent-Lauf wirkt bequem:

```text
Do everything.
```

Aber lange Laeufe driften:

- Kontext wird laut
- Zwischenentscheidungen verschwimmen
- Tools erzeugen Nebenwirkungen
- der Agent will "fertig" klingen
- Review wird schwer

Orchestrierung bringt Rhythmus.

## Der Ralph Loop

Fuer diesen Workshop verwenden wir Ralph als einfache Merkform:

```text
Read -> Ask -> Lock -> Produce -> Halt
```

### Read

Erst lesen. Nicht editieren. Relevante Dateien, Tests, Docs, Fehler.

### Ask

Maximal eine echte Blockerfrage. Nicht zehn Designfragen.

### Lock

Scope, Non-goals, Done-Kriterien festhalten.

### Produce

Kleinste sinnvolle Einheit bauen.

### Halt

Stoppen. Diff, Tests, Risiken zeigen. Nicht heimlich weitermachen.

## Andere Orchestrierungsformen

- **Plan then execute**: Erst Plan, dann Code.
- **Researcher / Builder / Reviewer**: Rollen trennen.
- **Parallel hypotheses**: Zwei Agenten untersuchen unterschiedliche Ursachen.
- **Worktree isolation**: parallele Agenten in getrennten Arbeitsbereichen.
- **Review gates**: Nach jedem Schritt menschliche oder agentische Pruefung.

## Harness-neutraler Trick

Auch wenn dein Tool keine echten Subagents hat, kannst du Rollen simulieren:

```text
Act as read-only investigator. Do not edit.
```

Dann:

```text
Act as implementer. Use the investigator notes. Edit only listed files.
```

Dann:

```text
Act as skeptical reviewer. Lead with concrete risks.
```

## Takeaway

Gute Orchestrierung ist nicht mehr Agenten. Gute Orchestrierung ist bessere Phasentrennung.
