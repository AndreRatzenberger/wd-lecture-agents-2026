# Workshop: Mini-Spec fuer den Playground

## Ziel

Du schreibst eine kleine Spec, laesst den Agenten daraus einen Plan machen und implementierst erst danach.

## Dauer

30 bis 35 Minuten.

## Schritt 1: Problem beobachten

Fuehre aus:

```bash
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

Notiere:

- Welche Tests schlagen fehl?
- Welches Verhalten erwarten sie?
- Was ist nicht Teil des Problems?

## Schritt 2: Spec-Prompt

```text
Write a mini-spec for fixing the failing behavior in playground/tiny-issue-tracker.
Do not edit files.

Include:
- problem
- current behavior inferred from code
- desired behavior inferred from tests
- non-goals
- acceptance criteria
- verification command

Keep it under 250 words.
```

## Schritt 3: Spec reviewen

Pruefe:

- Enthalten die Acceptance Criteria alle fehlschlagenden Tests?
- Gibt es versteckte neue Features?
- Ist ein Non-goal genannt?
- Ist der Testbefehl konkret?

Wenn noetig:

```text
Revise the spec. Remove any feature not required by the tests.
```

## Schritt 4: Plan erzeugen

```text
Based on the approved mini-spec, propose an implementation plan.
Use at most 3 steps.
Name the exact file(s) to change.
Do not edit yet.
```

## Schritt 5: Implementieren

```text
Implement the plan.
Keep the public API stable.
Run:
python -m unittest discover -s playground/tiny-issue-tracker/tests
```

## Schritt 6: Review gegen Spec

```text
Audit the final diff against the mini-spec.
Return:
- acceptance criteria satisfied
- verification evidence
- unrelated changes, if any
- remaining risks
```

## Ergebnis

Du hast einen vollstaendigen kleinen Spec-Loop durchlaufen:

```text
Problem -> Spec -> Plan -> Code -> Verification -> Audit
```
