# 01 Agent Mindset

## One-liner

Ein Coding Agent ist kein besseres Autocomplete. Er ist ein schneller, werkzeugfaehiger Mitarbeiter mit begrenztem Situationsbewusstsein.

## Warum das wichtig ist

Viele schlechte Agent-Erfahrungen kommen aus einem falschen Interface-Modell:

```text
Mensch: "Fix das."
Agent: liest irgendwas, macht irgendwas, klingt sicher.
Mensch: "Warum ist jetzt alles anders?"
```

Das Problem ist selten nur das Modell. Das Problem ist oft die Arbeitsumgebung:

- Ziel unklar
- Kontext zufaellig
- Constraints fehlen
- Done-Kriterien fehlen
- Verifikation wird erst am Ende erfunden

Ein Agent wird besser, wenn du ihn wie Arbeit fuehrst:

```text
Goal -> Context -> Constraints -> Done when -> Verification
```

## Kurztheorie

High-Level Coding Agents koennen typischerweise:

- Dateien lesen und aendern
- Shell-Kommandos ausfuehren
- Tests starten
- Web oder Dokumentation recherchieren
- externe Tools ueber MCP oder Integrationen nutzen
- laengere Aufgaben planen und in Schritte zerlegen

Das macht sie maechtig, aber auch gefaehrlich. Ein plausibler Agent ist nicht automatisch ein korrekter Agent.

Die wichtigste Nutzerfaehigkeit ist deshalb nicht "prompt magic", sondern Aufgabenarchitektur:

1. Was ist das Ziel?
2. Welche Welt soll der Agent sehen?
3. Welche Grenzen darf er nicht ueberschreiten?
4. Woran erkennt er Fertigstellung?
5. Welche Beweise muss er liefern?

## Live-Demo

Zeige denselben Flock-Bug mit zwei Prompts.

Schlecht:

```text
Fix the failing test.
```

Besser:

```text
Goal: Fix the failing Flock timer precision regression.
Context: Read AGENTS.md, README.md, timer.py, and tests/test_timer_component.py first.
Constraints: Do not read PR #412 before diagnosing. Do not change the regression test unless it is wrong.
Done when: uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q passes.
Work style: Read first, explain the likely cause, then make the smallest change.
```

Die Aha-Frage:

> Welcher Prompt macht Review einfacher?

## Kernbegriffe

- **Harness**: Die Umgebung, in der der Agent laeuft, zum Beispiel Codex, Claude Code oder Copilot.
- **Context window**: Das Arbeitsgedaechtnis des Modells.
- **Tool use**: Der Agent kann Funktionen, Shell, Dateien, Browser oder MCP-Tools verwenden.
- **Agent Contract**: Die explizite Vereinbarung ueber Ziel, Grenzen und Beweise.
- **Operator Skill**: Deine Faehigkeit, die Arbeit so zu strukturieren, dass der Agent weniger raten muss.

## Takeaway

Je groesser die Autonomie, desto wichtiger ist der Auftrag. Gute Agentenarbeit beginnt vor dem ersten Edit.
