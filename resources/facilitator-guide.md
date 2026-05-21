# Facilitator Guide

Dies ist der Spickzettel für die Person vorne im Raum.

## Didaktischer Kern

Die Session soll sich nicht anfühlen wie "Tool X kann Feature Y". Sie soll sich anfühlen wie:

> Ich kann einen Agenten so führen, dass aus unklarer Absicht ein prüfbarer Arbeitsstand wird.

Jedes Modul hat deshalb denselben Rhythmus:

1. Kurztheorie: 5 bis 7 Minuten.
2. Live-Demo oder Beispiel: 3 bis 5 Minuten.
3. Hands-on: 15 bis 25 Minuten.
4. Mini-Retro: 2 Minuten. Was hat den Agenten besser gemacht?

## Setup vor der Veranstaltung

- Stelle sicher, dass mindestens ein Agent-Harness verfügbar ist.
- Empfohlen: Codex CLI, Claude Code oder GitHub Copilot mit Agent Mode.
- Prüfe, ob Python 3 verfügbar ist:

```bash
python --version
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

Die Playground-Tests dürfen am Anfang rot sein. Das ist Absicht. Der Playground ist nur der Warm-up.

Halte für den Greenfield-Track bereit:

```text
resources/greenfield-puzzle-game.md
resources/greenfield-facilitator-notes.md
resources/superpowers-hands-on.md
resources/openspec-hands-on.md
```

Der Greenfield-Track braucht kein vorbereitetes Repo. Studierende können in einem leeren Ordner arbeiten. Wichtig ist: erst PRD und Mechanics Spec, dann eine kleine Slice.

Bereite zusätzlich den Flock-Track vor:

```bash
git clone https://github.com/whiteducksoftware/flock.git
cd flock
git checkout lecture/timer-precision-bug-start
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

Der Flock-Test muss rot sein. Die Failure-Zeile soll auf `2026-05-20` vs `2026-05-19` zeigen. Siehe [flock-facilitator-notes.md](flock-facilitator-notes.md).

Optional für die Industrie-Workflow-Labs:

```bash
node --version
npm view @fission-ai/openspec version engines --json
```

Wenn du Superpowers live installierst, nutze den jeweiligen Harness-Installationsweg statt Shell-Magie:

- Claude Code: `/plugin install superpowers@claude-plugins-official`
- Codex: `/plugins` öffnen, nach `superpowers` suchen und installieren
- Gemini CLI: `gemini extensions install https://github.com/obra/superpowers`

Wichtig: Die Labs gehören in eine Kopie, einen Fork oder ein Worktree. OpenSpec erzeugt `openspec/` Artefakte im Projekt; Superpowers verändert das Agentenverhalten für den jeweiligen Harness.

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

Der Effekt ist sofort sichtbar: Der Agent exploriert gezielter, macht kleinere Diffs und erklärt besser.

### Demo 2: Skill als Methodentransfer

Zeige [examples/skills/repo-cartographer/SKILL.md](../examples/skills/repo-cartographer/SKILL.md). Frage:

> Ist das "nur Prompting", oder ist das schon ein kleines Stück Team-Wissen?

Die Aha-Antwort: Es ist Team-Wissen als portable, agent-native Verpackung.

### Demo 3: Ralph Loop

An die Tafel:

```text
Read -> Ask -> Lock -> Produce -> Halt
```

Dann mit einem Agenten live anwenden:

- Read: relevante Dateien lesen lassen
- Ask: eine Rückfrage erzwingen
- Lock: Scope und Done-Kriterien festlegen
- Produce: kleinste Änderung bauen
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

### Demo 5: Prompt-Disziplin vs installiertes Workflow-System

Zeige die manuelle Prompt-Karte aus Modul 05 und dann zwei aktuelle Werkzeuge:

```text
Superpowers:
Skill-Bündel erzwingt Methodik im Agenten.

OpenSpec:
Repo-Artefakte halten Proposal, Spec-Deltas, Design und Tasks fest.
```

Leitsatz:

> Man kann eine eigene Spec-driven-Development-Skill bauen. Im Workshop schauen wir uns bewusst zwei lebendige Standards an, damit Studierende echte Arbeitsflaechen sehen.

## Zeitmanagement

Wenn die Gruppe sehr frisch ist:

- Modul 03 MCP kürzen
- Modul 06 Orchestration einfacher halten
- Greenfield nur bis PRD und erste Slice führen
- mehr Zeit für Modul 02 und 07 geben
- Flock nur als geführte Demo verwenden, nicht als freie Aufgabe

Wenn die Gruppe sehr stark ist:

- Modul 04 Skill bauen lassen
- Modul 05 Greenfield-Spec in echte Tasks splitten lassen
- Superpowers oder OpenSpec als Industrie-Workflow-Lab auswählen
- Modul 06 mit zwei parallelen Agent-Rollen simulieren lassen
- Browser-Automation für die Puzzle-Slice wirklich laufen lassen
- Nach dem Fix den echten PR #412 als Review-Vergleich nutzen

## Moderationssätze

- "Der Agent ist schnell. Wir müssen langsam genug sein, dass er nicht in die falsche Richtung schnell wird."
- "Wenn ihr den Prompt nicht reviewen könnt, könnt ihr den Output auch nicht gut reviewen."
- "MCP gibt Hände. Skills geben Gewohnheiten. Specs geben Richtung. Reviews geben Bremsen."
- "Wir wollen keine perfekten Prompts. Wir wollen robuste Arbeitsabläufe."
- "Toy-Projekte zeigen, dass Agents Code schreiben können. Flock zeigt, ob wir Agents führen können."
- "Greenfield braucht Spec, weil noch keine Codebase widerspricht."

## Abschlussfrage

Jede Person schreibt am Ende eine persönliche Regel:

```text
Ab morgen gebe ich meinem Coding Agent immer ...
```

Beispiele:

- "Done when" Kriterien.
- Den Testbefehl.
- Eine explizite Nicht-Anforderung.
- Den Auftrag, vor dem Editieren kurz den Plan zu zeigen.
