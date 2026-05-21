# Superpowers Hands-on

Dieses Blatt ist die Industrie-Workflow-Vertiefung für Skills und Plugins.

Die vorherigen Module zeigen die kleinste tragfähige Form:

```text
Prompt -> Spec -> Plan -> Tests -> Code -> Review
```

Superpowers zeigt die größere Variante:

```text
Installiertes Skill-Bündel -> Agent triggert Methodik selbst -> Gates werden Gewohnheit
```

## Aktueller Stand

Stand der Recherche: 2026-05-21.

- Repository: <https://github.com/obra/superpowers>
- Neuestes sichtbares Release: `v5.1.0` vom 2026-05-04.
- Verfügbare Installationswege laut README: Claude Code, Codex CLI, Codex App, Factory Droid, Gemini CLI, OpenCode, Cursor, GitHub Copilot CLI.
- Kernworkflow laut README: `brainstorming`, `using-git-worktrees`, `writing-plans`, `subagent-driven-development` oder `executing-plans`, `test-driven-development`, `requesting-code-review`, `finishing-a-development-branch`.
- Wichtiger Unterschied zu unseren Prompt-Karten: Superpowers will relevante Skills automatisch oder explizit als Pflicht-Workflow triggern, nicht nur als nette Vorschläge.

## Lernziel

Studierende sollen sehen, wie sich ein Agent verhält, wenn Methodik als Plugin/Skill-System installiert ist.

Sie sollen nicht blind glauben, dass Superpowers "besser" ist. Sie sollen beobachten:

- Welche Gates erzwingt das System?
- Wann ist das hilfreich?
- Wann ist es für eine kleine Aufgabe zu schwer?
- Welche Beweise liefert der Agent am Ende?

## Dauer

35 bis 50 Minuten.

## Vorbereitung

Nutze eine Kopie, einen Fork oder ein Worktree des Workshop-Repos.

```bash
git status --short
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

Erwartung: Am Anfang ist genau ein Test rot. Das ist der Warm-up-Bug.

## Installation

Wähle den Installationsweg deines Harnesses.

Claude Code:

```text
/plugin install superpowers@claude-plugins-official
```

Codex CLI:

```text
/plugins
```

Dann nach `superpowers` suchen und installieren.

Codex App:

```text
Plugins in der Seitenleiste öffnen, Superpowers in der Coding-Kategorie installieren.
```

Gemini CLI:

```bash
gemini extensions install https://github.com/obra/superpowers
```

Cursor:

```text
/add-plugin superpowers
```

GitHub Copilot CLI:

```bash
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace
```

Wenn Installation im Raum nicht klappt, macht die Lehrperson eine Live-Demo und die Gruppe nutzt die Reflexionsfragen trotzdem.

## Aufgabe: Tiny Issue Tracker mit Superpowers fixen

Gib dem Agenten:

```text
Use Superpowers for this change.

Goal:
Fix the failing tiny issue tracker search test.

Context:
Read playground/tiny-issue-tracker/README.md,
playground/tiny-issue-tracker/issue_tracker.py,
and playground/tiny-issue-tracker/tests/test_issue_tracker.py.

Constraints:
Keep the public Issue and IssueTracker API stable.
Do not add dependencies.
Do not broaden search semantics beyond case-insensitive substring matching.

Done when:
python -m unittest discover -s playground/tiny-issue-tracker/tests passes.

Work style:
Follow the relevant Superpowers skills for debugging, TDD, verification, and review.
Show the gates you used, not just the final patch.
```

## Beobachtungsauftrag

Notiere während des Laufs:

- Welche Skill oder welcher Workflow wurde aktiv?
- Hat der Agent vor dem Editieren gelesen?
- Wurde ein Test zuerst betrachtet oder geschrieben?
- Gab es ein Design-/Plan-Gate, obwohl die Aufgabe klein ist?
- Hat der Agent die Änderung reviewt?
- Welche Verification wurde wirklich ausgefuehrt?
- War der Prozess hilfreich oder übergewichtig?

## Vergleichslauf

Führe dieselbe Aufgabe danach mit einem normalen Prompt aus:

```text
Fix the failing tiny issue tracker test.
Run python -m unittest discover -s playground/tiny-issue-tracker/tests.
Keep the change minimal.
```

Vergleiche:

| Frage | Normaler Prompt | Superpowers |
| --- | --- | --- |
| Wie viele Dateien wurden geändert? | | |
| Wurde der Scope sichtbar gelockt? | | |
| Wurde TDD oder Debugging erkennbar? | | |
| Wie gut war der Abschlussbericht? | | |
| War die Extra-Methodik den Aufwand wert? | | |

## Facilitator Notes

Wenn Superpowers bei diesem kleinen Bug viel Prozess fordert, ist das kein Fehler der Demo. Es ist der Lernpunkt:

> Methodik ist ein Werkzeug. Ein gutes Werkzeug muss zur Größe der Arbeit passen.

Bei einer grossen Greenfield-Slice oder einem riskanten Brownfield-Fix sind die Gates wertvoller. Bei einem Zwei-Zeilen-Bug zeigen sie vor allem, wie ein installiertes Skill-System den Agenten bremst, fokussiert und reviewbar macht.

## Abschlussfragen

- Welche unserer manuellen Prompt-Regeln hat Superpowers automatisch erzwungen?
- Welche Regel würdest du für dein Team übernehmen?
- Welche Regel wäre für kleine Aufgaben zu schwer?
- Würdest du Superpowers global installieren oder nur projektweise nutzen?
