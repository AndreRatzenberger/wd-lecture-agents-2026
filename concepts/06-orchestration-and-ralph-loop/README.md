# 06 Orchestration and Ralph Loop

## One-liner

Orchestrierung ist die Kunst, Agenten nicht nur arbeiten zu lassen, sondern Arbeit in sinnvolle Phasen, Rollen und Stopps zu zerlegen.

## Warum das wichtig ist

Ein einzelner langer Agent-Lauf wirkt bequem:

```text
Do everything.
```

Aber lange Läufe driften:

- Kontext wird laut
- Zwischenentscheidungen verschwimmen
- Tools erzeugen Nebenwirkungen
- der Agent will "fertig" klingen
- Review wird schwer

Orchestrierung bringt Rhythmus.

## Der Ralph Loop

Für diesen Workshop verwenden wir Ralph als einfache Merkform:

```text
Read -> Ask -> Lock -> Produce -> Halt
```

### Read

Erst lesen. Nicht editieren. In Greenfield liest der Agent die approved Spec. In Brownfield liest er relevante Dateien, Tests, Docs und Fehler.

### Ask

Maximal eine echte Blockerfrage. Nicht zehn Designfragen.

### Lock

Scope, Non-goals, Done-Kriterien festhalten.

### Produce

Kleinste sinnvolle Einheit bauen. Greenfield: erste Slice. Brownfield: kleinster sicherer Fix.

### Halt

Stoppen. Diff, Tests, Risiken zeigen. Nicht heimlich weitermachen.

## Andere Orchestrierungsformen

- **Plan then execute**: Erst Plan, dann Code.
- **Researcher / Builder / Reviewer**: Rollen trennen.
- **Parallel hypotheses**: Zwei Agenten untersuchen unterschiedliche Ursachen.
- **Worktree isolation**: parallele Agenten in getrennten Arbeitsbereichen.
- **Review gates**: Nach jedem Schritt menschliche oder agentische Prüfung.

## Greenfield vs Brownfield

Der Loop bleibt gleich, aber die Bedeutung der Phasen ändert sich:

| Phase | Greenfield Puzzle | Brownfield Flock |
| --- | --- | --- |
| Read | PRD, Mechanics Spec, Testplan | AGENTS.md, Code, Tests, Failure |
| Ask | Produkt-/Scope-Blocker | Repo-/Verhaltens-Blocker |
| Lock | erste Slice und Non-goals | Fix-Scope und betroffene Dateien |
| Produce | neue Slice mit Tests | kleine Änderung mit Regressionstest |
| Halt | Gates und Browser-Beweis | Diff, pytest, Restrisiko |

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
