# AI Coding Agents: 4h Praxisworkshop

Dieses Repo ist ein kompletter Workshop-Kit für eine 4-stündige Vorlesung, Hackathon-Session oder Hands-on-Class zu modernen Coding Agents wie Codex, Claude Code, GitHub Copilot und ähnlichen High-Level-Harnesses.

Ziel: Studierende sollen nicht nur wissen, dass Agents Code schreiben können. Sie sollen spüren, dass Agentenführung ein eigener Skill ist: Kontext geben, Werkzeuge anbinden, Skills bauen, Specs scharf machen, Loops orchestrieren, Ergebnisse verifizieren.

Der Kurs ist bewusst harness-neutral. Die Beispiele sind für Codex, Claude Code und GitHub Copilot gedacht, aber die Konzepte tragen auch zu Cursor, Cline, Windsurf, Gemini CLI, OpenCode und anderen Agent-Umgebungen.

Die Hands-ons haben drei Ebenen:

- `playground/tiny-issue-tracker`: sehr kleiner Warm-up für den ersten Agent-Contract.
- [Greenfield Puzzle Game](resources/greenfield-puzzle-game.md): neues Produkt erst spezifizieren, dann in eine kleine Slice schneiden.
- [Flock Hands-on](resources/flock-hands-on.md): echtes Repo, echter Bug, echter Verifikationsdruck.

## Lernversprechen

Nach 4 Stunden können Teilnehmende:

- einen Coding Agent wie einen Junior-Kollegen mit Werkzeugen führen, nicht wie eine Suchmaschine befragen
- stabile Kontextregeln formulieren (`AGENTS.md`, `CLAUDE.md`, Copilot instructions)
- MCP als Werkzeug- und Kontextbrücke erklären und sinnvoll einsetzen
- eine kleine Agent Skill im offenen `SKILL.md`-Format bauen
- Spec-driven Development als Anti-Drift-Mechanik verwenden
- einfache Orchestrierungsformen wie den Ralph Loop praktisch anwenden
- Agent-Ergebnisse mit Tests, Diffs, Reviews und Sicherheitschecks absichern

## 4h Run of Show

| Zeit | Modul | Kernfrage | Output |
| --- | --- | --- | --- |
| 00:00-00:10 | Setup und framing | Was ist heute anders als Autocomplete? | gemeinsames Mentalmodell |
| 00:10-00:35 | [01 Agent Mindset](concepts/01-agent-mindset/README.md) | Wie führt man einen Agenten? | guter Task-Prompt |
| 00:35-01:05 | [02 Context and Instructions](concepts/02-context-and-instructions/README.md) | Was gehört dauerhaft in den Kontext? | kleines Agent Contract File |
| 01:05-01:35 | [03 MCP Tooling](concepts/03-mcp-tooling/README.md) | Wann braucht ein Agent echte Tools? | MCP-Tool-Plan |
| 01:35-01:45 | Pause | Kopf kurz lüften | Kaffee |
| 01:45-02:20 | [04 Agent Skills and Plugins](concepts/04-agent-skills-and-plugins/README.md) | Wie verpackt man wiederholbare Expertise? | eigene `SKILL.md` |
| 02:20-02:55 | [05 Spec-driven Development](concepts/05-spec-driven-development/README.md) | Wie stoppt man Vibe-Drift? | Mini-Spec und Task-Slice |
| 02:55-03:25 | [06 Orchestration and Ralph Loop](concepts/06-orchestration-and-ralph-loop/README.md) | Wie lässt man Agents arbeiten, ohne Kontrolle zu verlieren? | Loop-Protokoll |
| 03:25-03:50 | [07 Verification and Safety](concepts/07-verification-and-safety/README.md) | Wie weiß man, dass der Agent nicht nur plausibel klingt? | Verifikations-Checkliste |
| 03:50-04:00 | Wrap | Was nehmt ihr morgen in euren Workflow? | persönlicher Agent-Spickzettel |

## Repo-Struktur

```text
concepts/
  01-agent-mindset/
    README.md
    workshop.md
    further-reading.md
  ...
playground/tiny-issue-tracker/
  Kleine Warm-up-Codebase für Agentenaufgaben
examples/
  skills/
  plugins/
  mcp/
resources/
  facilitator-guide.md
  greenfield-puzzle-game.md
  greenfield-facilitator-notes.md
  flock-hands-on.md
  flock-facilitator-notes.md
  harness-matrix.md
  prompt-cards.md
  research-notes.md
```

Jeder Konzeptordner folgt demselben Muster:

- `README.md`: Theorie, Live-Demo-Idee, Kernbegriffe
- `workshop.md`: Schritt-für-Schritt Hands-on
- `further-reading.md`: offizielle Docs und gute Beispiele

## Schnellstart für Teilnehmende

1. Dieses Repo klonen oder lokal öffnen.
2. Einen Agent-Harness wählen: Codex, Claude Code, GitHub Copilot, Cursor, Cline, Windsurf oder ähnlich.
3. Warm-up testen:

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

4. Greenfield-Track lesen:

```text
resources/greenfield-puzzle-game.md
```

5. Realprojekt-Track vorbereiten:

```bash
git clone https://github.com/whiteducksoftware/flock.git
cd flock
git checkout lecture/timer-precision-bug-start
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q
```

6. Mit Modul 01 starten. Ab Modul 05 werden Greenfield Puzzle und Flock bewusst verglichen.

## Haltung

Dieser Kurs ist kein Prompt-Museum. Alles hier ist so gebaut, dass Studierende direkt mit einem echten Agenten arbeiten können.

Die Grundregel:

> Ein Agent ist kein Orakel. Ein Agent ist ein sehr schneller Mitarbeiter mit unvollständigem Situationsbewusstsein. Deine Aufgabe ist, die Situation so zu bauen, dass gute Arbeit wahrscheinlicher wird.

## Quellenbasis

Die Inhalte wurden aus drei Richtungen gebaut:

- aktuelle offizielle Docs von OpenAI Codex, Anthropic Claude Code, GitHub Copilot, MCP und Agent Skills
- lokale Research-Artefakte aus `spec-compare-codex` und `cc-ecosystem`
- Pyros Vorgabe, den "aha!"-Charakter von Projekten wie `JuliusBrussee/caveman` ernst zu nehmen: kleine Form, großer Effekt

Siehe [resources/research-notes.md](resources/research-notes.md) für die belegten Quellen.
