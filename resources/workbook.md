# Workbook

Dieses Workbook ist die Arbeitsfläche für Agentenarbeit:

> Aus einem vagen Auftrag wird ein prüfbarer Arbeitsstand.

Nutze dieses Blatt während des Workshops oder später in echten Projekten. Schreibe knapp. Gute Agentenführung ist nicht mehr Text, sondern bessere Entscheidungen.

## 1. Ausgangslage

```text
Projekt oder Kontext:

Agent-Harness:

Auftrag in einem Satz:

Warum ist das wichtig?

Was darf auf keinen Fall passieren?
```

## 2. Agent Contract

```text
Goal:

Context:

Files, Fehler, Links oder Tests:

Constraints:

Done when:

Work style:
Read first. Keep changes small. Report exact verification.
```

Check:

- Ist das Ziel sichtbar anders als "mach das besser"?
- Sind konkrete Dateien, Fehler oder Befehle genannt?
- Gibt es mindestens ein Non-goal?
- Ist "Done when" beweisbar?

## 3. Read-Only Map

Bevor der Agent editiert:

```text
Task:

Relevant files:

Flow:

Likely change points:

Tests/checks:

Risks or unknowns:

Smallest next action:
```

Review-Frage:

```text
Würde ich nach dieser Map gezielter arbeiten als vorher?
```

Wenn nicht: Agent stoppen und nochmal kleiner scopen.

## 4. Mini-Spec

```text
Problem:

Current behavior:

Desired behavior:

Non-goals:

Acceptance criteria:

Edge cases:

Verification command(s):
```

Spec-Check:

- Beschreibt die Spec Verhalten, nicht nur Implementierung?
- Sind Non-goals konkret genug, um Scope zu stoppen?
- Sind Acceptance Criteria testbar?
- Passt der Verifikationsbefehl wirklich zur Änderung?

## 5. Plan Lock

```text
Approved scope:

Files likely to change:

Files that must not change:

Tests to write or run first:

Implementation steps, max 3:

Stop condition:
```

Erst nach diesem Lock darf der Agent implementieren.

## 6. Implementation Notes

Während der Agent arbeitet:

```text
Changed files:

Important decisions:

Unexpected behavior:

Scope pressure:

What I stopped or rejected:
```

Wenn der Agent neue Features, neue Abhängigkeiten oder große Refactors vorschlägt:

```text
Stop. Compare this suggestion against the approved mini-spec.
List what is required, what is optional, and what is out of scope.
Do not edit until the scope is restored.
```

## 7. Verification Evidence

```text
Commands run:

Result:

Manual/browser checks:

Diff reviewed:

Unverified areas:

Remaining risks:
```

Evidence zählt nur, wenn sie echt ist:

- Testausgabe, nicht "should pass".
- Diff-Review, nicht "looks good".
- Browserbeobachtung, nicht "UI should work".
- Risiko-Liste, nicht Abschlussrhetorik.

## 8. Final Handoff

```text
What changed:

Why it changed:

How it was verified:

What did not change:

What remains risky:

Next useful step:
```

Gute Abschlussfrage:

```text
Kann eine andere Person diese Arbeit übernehmen, ohne den Chat zu lesen?
```

Wenn die Antwort nein ist, fehlt ein Artefakt: Spec, Diff, Testausgabe, Risiko oder Handoff.

## 9. Personal Rule

Am Ende eine Regel notieren, die beim nächsten Agentenlauf besser sein soll:

```text
Ab jetzt gebe ich meinem Coding Agent immer ...
```

Beispiele:

- den konkreten Testbefehl
- ein explizites Non-goal
- ein Read-only-Mapping vor dem Editieren
- ein Stop-Signal nach Verifikation
- eine Review-Frage gegen die Spec
