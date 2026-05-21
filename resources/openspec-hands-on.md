# OpenSpec Hands-on

Dieses Blatt ist die Industrie-Workflow-Vertiefung für Spec-driven Development.

Die manuellen Prompt-Karten aus Modul 05 zeigen das Prinzip:

```text
Problem -> Spec -> Plan -> Code -> Verification -> Audit
```

OpenSpec macht daraus repo-lokale Artefakte:

```text
openspec/changes/<change>/
  proposal.md
  design.md
  tasks.md
  specs/
```

## Aktueller Stand

Stand der Recherche: 2026-05-21.

- Website: <https://openspec.dev/>
- Repository: <https://github.com/Fission-AI/OpenSpec>
- npm-Paket: `@fission-ai/openspec`
- Aktuelle npm-Version im Check: `1.3.1`
- Neuestes sichtbares Release: `v1.3.1` vom 2026-04-21.
- Voraussetzung laut README: Node.js `20.19.0` oder höher.
- Standardworkflow ist inzwischen OPSX: `/opsx:propose`, `/opsx:explore`, `/opsx:apply`, `/opsx:sync`, `/opsx:archive`.
- Erweiterte Workflows können zusätzlich `/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:bulk-archive`, `/opsx:onboard` erzeugen.
- Alte Befehle wie `/openspec:proposal` existieren noch, aber die aktuellen Docs empfehlen OPSX.

## Lernziel

Studierende sollen sehen, dass Spec-driven Development nicht nur ein langer Prompt sein muss. Specs können als reviewbare Dateien im Repo leben.

Die Aha-Frage:

> Was wird besser, wenn die Spec nicht im Chat verschwindet?

## Dauer

45 bis 60 Minuten.

## Vorbereitung

Nutze eine Kopie, einen Fork oder ein Worktree. OpenSpec erzeugt Dateien im Projekt.

```bash
node --version
npm install -g @fission-ai/openspec@latest
openspec --version
```

Wenn Node zu alt ist, nicht im Raum debuggen. Die Lehrperson zeigt den Flow live oder nutzt Screenshots/Artefakte aus einer vorbereiteten Kopie.

## Projekt initialisieren

Im Workshop-Repo oder in einer Kopie:

```bash
openspec init --tools codex
```

Andere Beispiele:

```bash
openspec init --tools claude
openspec init --tools cursor
openspec init --tools github-copilot
openspec init --tools opencode
openspec init --tools all
```

Wenn du die erweiterten Befehle wie `/opsx:verify` oder `/opsx:onboard` zeigen willst:

```bash
openspec config profile
openspec update
```

Wähle dabei die zusätzlichen Workflows aus und aktualisiere danach die generierten Agent-Instructions.

## Aufgabe A: Tiny Search Change als OpenSpec Change

Baseline:

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

Starte im Agenten:

```text
/opsx:propose "Fix tiny issue tracker search so title and body matching are case-insensitive without changing the public API"
```

Erwartete Artefakte:

```text
openspec/changes/<change-name>/
  proposal.md
  design.md
  tasks.md
  specs/
```

Review vor Implementierung:

```text
Read the generated OpenSpec artifacts.
Check:
- proposal.md names the failing search behavior
- specs include case-insensitive title and body substring matching
- design.md keeps Issue and IssueTracker public API stable
- tasks.md includes baseline test, minimal fix, and verification
- non-goals exclude fuzzy search, ranking, persistence, UI changes, and API changes
Do not implement until these artifacts are coherent.
```

Implementierung:

```text
/opsx:apply <change-name>
```

Verifikation:

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
openspec validate --all
```

Wenn `/opsx:verify` aktiviert ist:

```text
/opsx:verify <change-name>
```

Archivieren:

```text
/opsx:archive <change-name>
```

## Aufgabe B: Spec während der Arbeit korrigieren

OpenSpec ist interessant, weil Artefakte editierbar bleiben.

Simuliere eine Drift:

```text
The generated proposal accidentally mentions fuzzy search.
Update the OpenSpec artifacts so this change stays limited to case-insensitive substring matching.
Then continue implementation.
```

Beobachte:

- Wurde `proposal.md` angepasst?
- Wurde die Spec-Delta angepasst?
- Wurde `tasks.md` kleiner?
- Hat der Agent die Implementierung an die korrigierte Spec gebunden?

## Aufgabe C: Chat-Plan vs Repo-Artefakt

Vergleiche mit Modul 05:

| Frage | Manueller Prompt | OpenSpec |
| --- | --- | --- |
| Wo lebt die Spec nach der Session? | Chat | Repo |
| Kann ein anderer Developer sie reviewen? | schwer | ja |
| Kann der Agent später daran anknüpfen? | nur mit Chat-Kontext | ja |
| Ist es schneller für kleine Aufgaben? | oft ja | nicht immer |
| Ist es besser für Teamarbeit? | begrenzt | meist ja |

## Facilitator Notes

OpenSpec ist nicht "Plan Mode mit anderem Namen". Der Unterschied ist nicht, dass mehr Text entsteht. Der Unterschied ist, dass Intent, Spec-Delta, Design und Tasks versionierbare Arbeitsprodukte werden.

Guter Lehrsatz:

> Prompting steuert diese Session. OpenSpec steuert den nächsten Developer mit.

## Abschlussfragen

- Welche OpenSpec-Datei wäre in einem PR am wertvollsten?
- Welche Datei war zu schwergewichtig für den kleinen Bug?
- Wann wuerdest du `/opsx:propose` nutzen, und wann reicht eine Prompt-Karte?
- Welche Non-goals haben verhindert, dass der Agent ein größeres Suchsystem baut?
