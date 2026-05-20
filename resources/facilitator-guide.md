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

Die Playground-Tests duerfen am Anfang rot sein. Das ist Absicht. Der Playground ist nur der Warm-up.

Halte fuer den Greenfield-Track bereit:

```text
resources/greenfield-puzzle-game.md
resources/greenfield-facilitator-notes.md
```

Der Greenfield-Track braucht kein vorbereitetes Repo. Studierende koennen in einem leeren Ordner arbeiten. Wichtig ist: erst PRD und Mechanics Spec, dann eine kleine Slice.

Bereite zusaetzlich den Flock-Track vor:

```bash
git clone https://github.com/whiteducksoftware/flock.git
cd flock
git checkout lecture/timer-precision-bug-start
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

Der Flock-Test muss rot sein. Die Failure-Zeile soll auf `2026-05-20` vs `2026-05-19` zeigen. Siehe [flock-facilitator-notes.md](flock-facilitator-notes.md).

## Live-Demo-Ideen

### Demo 1: Schlechter Prompt vs Agent Contract

Schlecht:

```text
Fix the app.
```

Besser:

```text
Goal: Fix the failing Flock timer precision regression.
Context: Start by reading AGENTS.md, README.md, timer.py, and tests/test_timer_component.py.
Constraints: Do not read PR #412 before diagnosing. Do not change the regression test unless it is wrong.
Done when: the focused pytest command passes and you summarize the changed behavior.
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

### Demo 4: Greenfield vs Brownfield

Zeige die zwei Arbeitsarten nebeneinander:

```text
Greenfield Puzzle:
Erst PRD -> Mechanics Spec -> Testplan -> Slice -> Code

Brownfield Flock:
Erst Repo lesen -> Failure verstehen -> Scope locken -> Fix -> Beweis
```

Die Aha-Antwort: Greenfield braucht mehr explizite Produktform, Brownfield braucht mehr Respekt vor bestehender Form.

## Zeitmanagement

Wenn die Gruppe sehr frisch ist:

- Modul 03 MCP kuerzen
- Modul 06 Orchestration einfacher halten
- Greenfield nur bis PRD und erste Slice fuehren
- mehr Zeit fuer Modul 02 und 07 geben
- Flock nur als gefuehrte Demo verwenden, nicht als freie Aufgabe

Wenn die Gruppe sehr stark ist:

- Modul 04 Skill bauen lassen
- Modul 05 Greenfield-Spec in echte Tasks splitten lassen
- Modul 06 mit zwei parallelen Agent-Rollen simulieren lassen
- Browser-Automation fuer die Puzzle-Slice wirklich laufen lassen
- Nach dem Fix den echten PR #412 als Review-Vergleich nutzen

## Moderationssaetze

- "Der Agent ist schnell. Wir muessen langsam genug sein, dass er nicht in die falsche Richtung schnell wird."
- "Wenn ihr den Prompt nicht reviewen koennt, koennt ihr den Output auch nicht gut reviewen."
- "MCP gibt Haende. Skills geben Gewohnheiten. Specs geben Richtung. Reviews geben Bremsen."
- "Wir wollen keine perfekten Prompts. Wir wollen robuste Arbeitsablaeufe."
- "Toy-Projekte zeigen, dass Agents Code schreiben koennen. Flock zeigt, ob wir Agents fuehren koennen."
- "Greenfield braucht Spec, weil noch keine Codebase widerspricht."

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
