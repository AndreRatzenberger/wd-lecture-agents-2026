# Workshop: Ralph Loop am Playground

## Ziel

Du fuehrst einen Agenten in fuenf klaren Phasen durch eine kleine Reparatur.

## Dauer

25 bis 30 Minuten.

## Schritt 1: Read

```text
Ralph loop, phase Read.
Do not edit files.
Inspect playground/tiny-issue-tracker README, implementation, and tests.
Return the relevant facts and likely failure causes.
```

## Schritt 2: Ask

```text
Ralph loop, phase Ask.
Ask at most one blocking question.
If no question is needed, say "No blocker" and explain why.
```

## Schritt 3: Lock

```text
Ralph loop, phase Lock.
Restate:
- scope
- non-goals
- files likely to change
- done criteria
Wait for confirmation before editing.
```

Wenn du alleine arbeitest, bestaetige selbst:

```text
Confirmed. Continue to Produce.
```

## Schritt 4: Produce

```text
Ralph loop, phase Produce.
Implement the smallest change that satisfies the locked scope.
Run the verification command.
```

## Schritt 5: Halt

```text
Ralph loop, phase Halt.
Stop working.
Report:
- changed files
- verification command and result
- risks
- anything not verified
Do not make further changes.
```

## Variation: Drei Rollen

Wenn dein Harness Subagents oder custom agents kann:

1. Investigator: read-only map.
2. Builder: implement smallest fix.
3. Reviewer: compare diff against request.

Wenn nicht, fuehre die drei Prompts nacheinander im selben Chat aus.

## Ergebnis

Du hast aus einem amorphen "fix it" eine kontrollierte Arbeitssequenz gemacht.
