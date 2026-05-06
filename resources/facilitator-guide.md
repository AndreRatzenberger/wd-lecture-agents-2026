# Facilitator Guide

Dies ist der Spickzettel fuer die Person vorne im Raum.

## Didaktischer Kern

Die Session soll sich nicht anfuehlen wie "Tool X kann Feature Y". Sie soll sich anfuehlen wie:

> Ich kann einen Agenten so fuehren, dass aus unklarer Absicht ein pruefbarer Arbeitsstand wird.

Jedes Modul hat deshalb denselben Rhythmus:

1. Kurztheorie: 5 bis 7 Minuten.
2. Live-Demo oder Beispiel: 3 bis 5 Minuten.
3. Hands-on: 15 bis 25 Minuten.
4. Mini-Retro: 2 Minuten. Was hat den Agenten besser gemacht?

## Setup vor der Veranstaltung

- Stelle sicher, dass mindestens ein Agent-Harness verfuegbar ist.
- Empfohlen: Codex CLI, Claude Code oder GitHub Copilot mit Agent Mode.
- Pruefe, ob Python 3 verfuegbar ist:

```bash
python --version
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

Die Tests duerfen am Anfang rot sein. Das ist Absicht. Das Playground-Projekt ist ein Arbeitsobjekt.

## Live-Demo-Ideen

### Demo 1: Schlechter Prompt vs Agent Contract

Schlecht:

```text
Fix the app.
```

Besser:

```text
Goal: Fix the failing tests in playground/tiny-issue-tracker.
Context: Start by reading README.md, issue_tracker.py, and tests.
Constraints: Keep the app dependency-free. Make the smallest change that explains the test failure.
Done when: unittest passes and you summarize the changed behavior.
```

Der Effekt ist sofort sichtbar: Der Agent exploriert gezielter, macht kleinere Diffs und erklaert besser.

### Demo 2: Skill als Methodentransfer

Zeige [examples/skills/repo-cartographer/SKILL.md](../examples/skills/repo-cartographer/SKILL.md). Frage:

> Ist das "nur Prompting", oder ist das schon ein kleines Stueck Team-Wissen?

Die Aha-Antwort: Es ist Team-Wissen als portable, agent-native Verpackung.

### Demo 3: Ralph Loop

An die Tafel:

```text
Read -> Ask -> Lock -> Produce -> Halt
```

Dann mit einem Agenten live anwenden:

- Read: relevante Dateien lesen lassen
- Ask: eine Rueckfrage erzwingen
- Lock: Scope und Done-Kriterien festlegen
- Produce: kleinste Aenderung bauen
- Halt: stoppen, Diff und Tests zeigen

## Zeitmanagement

Wenn die Gruppe sehr frisch ist:

- Modul 03 MCP kuerzen
- Modul 06 Orchestration einfacher halten
- mehr Zeit fuer Modul 02 und 07 geben

Wenn die Gruppe sehr stark ist:

- Modul 04 Skill bauen lassen
- Modul 05 Mini-Spec in echte Tasks splitten lassen
- Modul 06 mit zwei parallelen Agent-Rollen simulieren lassen

## Moderationssaetze

- "Der Agent ist schnell. Wir muessen langsam genug sein, dass er nicht in die falsche Richtung schnell wird."
- "Wenn ihr den Prompt nicht reviewen koennt, koennt ihr den Output auch nicht gut reviewen."
- "MCP gibt Haende. Skills geben Gewohnheiten. Specs geben Richtung. Reviews geben Bremsen."
- "Wir wollen keine perfekten Prompts. Wir wollen robuste Arbeitsablaeufe."

## Abschlussfrage

Jede Person schreibt am Ende eine persoenliche Regel:

```text
Ab morgen gebe ich meinem Coding Agent immer ...
```

Beispiele:

- "Done when" Kriterien.
- Den Testbefehl.
- Eine explizite Nicht-Anforderung.
- Den Auftrag, vor dem Editieren kurz den Plan zu zeigen.
