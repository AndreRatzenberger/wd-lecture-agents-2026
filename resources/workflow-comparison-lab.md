# Manual vs Superpowers vs OpenSpec Comparison Lab

Dieses Lab vergleicht drei Arten, denselben kleinen Agentenauftrag zu führen.

Die Aufgabe bleibt absichtlich klein:

```text
Fix the tiny issue tracker search so matching is case-insensitive.
```

Der Lernpunkt ist nicht der Bug. Der Lernpunkt ist die Arbeitsform.

## Ziel

Teilnehmende sehen denselben Change in drei Modi:

1. **Manual**: Prompt-Karten und menschliche Gate-Kontrolle.
2. **Superpowers**: Methodik als installierte Skill-/Plugin-Gewohnheit.
3. **OpenSpec**: Spec und Tasks als repo-lokale Artefakte.

Am Ende soll klarer sein:

- Wann reicht ein guter Prompt?
- Wann lohnt sich ein Skill-System?
- Wann lohnt sich ein formales Spec-Artefakt?

## Dauer

45 bis 75 Minuten.

Kurzvariante: Nur beobachten und vergleichen.

Langvariante: Drei Gruppen arbeiten parallel und präsentieren ihre Ergebnisse.

## Setup

Arbeite in drei frischen Kopien oder drei Worktrees, damit sich die Ansätze nicht überschreiben.

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

Erwartung: Ein Test ist rot:

```text
test_search_is_case_insensitive
```

Nicht committen. Nicht pushen. Dieses Lab ist zum Vergleichen der Arbeitsform.

## Track A: Manual Prompt Cards

Nutze die Prompt Cards aus [prompt-cards.md](prompt-cards.md).

Prompt:

```text
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
Read first.
Write a concise mini-spec and at most 3-step plan.
Do not edit until the plan is coherent.
After implementation, audit the diff against the mini-spec.
```

Beobachte:

- Wie gut bleibt der Agent im Scope?
- Wie viel Gatekeeping muss der Mensch aktiv machen?
- Verschwindet die Spec im Chat?

## Track B: Superpowers

Nutze [superpowers-hands-on.md](superpowers-hands-on.md).

Prompt:

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

Beobachte:

- Welche Skills werden aktiv?
- Hilft die Methodik oder wirkt sie bei diesem kleinen Bug schwer?
- Ist der Abschlussbericht besser als im manuellen Track?

## Track C: OpenSpec

Nutze [openspec-hands-on.md](openspec-hands-on.md).

Start:

```text
/opsx:propose "Fix tiny issue tracker search so title and body matching are case-insensitive without changing the public API"
```

Vor `/opsx:apply` prüfen:

```text
Read the generated OpenSpec artifacts.
Check proposal.md, design.md, tasks.md, and specs.
Non-goals must exclude fuzzy search, ranking, persistence, UI changes, and API changes.
Do not implement until the artifacts are coherent.
```

Dann:

```text
/opsx:apply <change-name>
```

Verifikation:

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
openspec validate --all
```

Beobachte:

- Welche Artefakte bleiben im Repo?
- Ist der Overhead für diesen kleinen Bug gerechtfertigt?
- Wäre der Ansatz bei einem größeren Team-Change wertvoller?

## Vergleichstabelle

| Frage | Manual | Superpowers | OpenSpec |
| --- | --- | --- | --- |
| Setup-Aufwand | | | |
| Menschliches Gatekeeping | | | |
| Scope-Kontrolle | | | |
| TDD/Debugging-Signal | | | |
| Reviewbarkeit nach der Session | | | |
| Artefakte im Repo | | | |
| Verifikationsevidence | | | |
| Overhead für kleinen Bug | | | |
| Eignung für Teamarbeit | | | |
| Eignung für riskante Änderungen | | | |

## Debrief

Diskutiere nach den drei Tracks:

```text
Welcher Track war am schnellsten?
Welcher Track war am reviewbarsten?
Welcher Track hat Scope am besten geschützt?
Welcher Track wäre bei einem echten Kunden- oder Teamprojekt am sichersten?
Welcher Track war für diesen kleinen Bug zu schwer?
```

## Facilitator Notes

Erwartbare Spannung:

- Manual ist schnell und universell, aber die Spec lebt im Chat.
- Superpowers zeigt, wie Methodik als Agentenverhalten installiert wird.
- OpenSpec erzeugt mehr Artefakte, macht aber Intent und Aufgaben reviewbar.

Guter Abschluss:

> Es gibt nicht "den besten" Agentenworkflow. Es gibt Arbeit, Risiko und Teamkontext. Der Workflow muss dazu passen.

## Ergebnis

Am Ende sollte jede Person eine Regel formulieren:

```text
Für kleine Änderungen nutze ich ...
Für riskante Änderungen nutze ich ...
Für Team-Changes nutze ich ...
```
