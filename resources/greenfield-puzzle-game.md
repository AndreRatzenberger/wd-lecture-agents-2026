# Greenfield Puzzle Game

Dieses Blatt ist der Greenfield-Track für den Workshop. Hier gibt es noch kein bestehendes Produkt, keine Tests und keine Codebase. Genau deshalb ist die Aufgabe gefährlich: Ein Agent kann sofort eine hübsche Demo bauen und trotzdem am eigentlichen Produkt vorbeilaufen.

Der Lernpunkt:

> Greenfield-Agentenarbeit beginnt nicht mit Code. Sie beginnt mit Produktentscheidung, Scope, Spec, Testvertrag und erst dann mit einer kleinen Implementierungsscheibe.

## Ziel

Studierende sollen aus einem vagen Produktwunsch eine prüfbare erste Version eines Puzzle-Spiels ableiten.

Sie üben:

- einen offenen Kreativauftrag in klare Optionen zu zerlegen
- PRD, Mechanics Spec und Non-goals zu schreiben
- "production ready" als konkrete Gates zu definieren
- Tests vor der Implementierung zu planen
- eine erste Slice mit dem Ralph Loop zu bauen
- Browser-Automation als Beweis einzuplanen

## Ausgangsprompt

Gib deinem Agenten diesen Prompt zuerst nicht zum Implementieren, sondern zum Spezifizieren:

```text
We want to build a highly polished professional minimalistic puzzle game as a web app.
The puzzle game idea should be novel and addictive: easy to understand and play, hard to master.

Game requirements:
- procedural/generative levels, no handcrafted levels
- infinite replayability
- a fair losing condition
- works on mobile and desktop web
- playable without sound
- professional minimalistic look and feel
- extensive unit tests
- extensive browser automation tests
- production-ready enough to deploy and publish

Be creative, but do not write code yet.
Search the web for puzzle game design best practices and browser-game testing guidance.
Then propose three game concepts and recommend one.
```

## Schritt 1: Konzeptoptionen erzwingen

Der Agent soll erst mehrere Ideen liefern, nicht sofort die erste Idee bauen.

```text
Do not implement.

Return three puzzle game concepts.
For each concept include:
- one-sentence core mechanic
- why it is novel enough
- why it is easy to learn
- why it is hard to master
- procedural generation approach
- losing condition
- mobile interaction model
- main implementation risk

Then recommend one concept and explain why it is the best workshop candidate.
```

Review-Fragen:

- Ist die Mechanik in einem Satz erklärbar?
- Kann man nach 10 Sekunden losspielen?
- Ist die Losing Condition fair oder nur Straf-Zufall?
- Kann man die Logik ohne DOM testen?
- Ist die Idee in 45 bis 60 Minuten als erste Slice baubar?

## Schritt 2: PRD schreiben lassen

```text
Write a PRD for the recommended puzzle game.
Do not implement.

Include:
- product goal
- target player
- core loop
- controls for mobile and desktop
- progression and scoring
- losing condition
- accessibility constraints
- non-goals
- production-ready definition
- success criteria for the workshop slice

Keep it concrete. Avoid marketing language.
```

## Schritt 3: Mechanics Spec schreiben lassen

```text
Write a mechanics spec for the first playable slice.
Do not implement.

Include:
- board/state model
- legal moves
- procedural generation rules
- scoring rules
- losing condition algorithm
- deterministic seed behavior for tests
- edge cases
- examples of two turns
```

Wichtig: Die Mechanics Spec muss testbar sein. Wenn der Agent nur "make it fun" schreibt, ist das kein Spec.

## Schritt 4: Testvertrag schreiben lassen

```text
Write the test plan before implementation.
Do not implement.

Include:
- unit tests for game logic
- tests for procedural generation
- tests for losing condition
- tests for scoring/progression
- Playwright/browser tests for start, play, lose, restart
- mobile viewport test
- production readiness checks: build, no console errors, keyboard/touch usability

Name exact commands the final project should support.
```

## Schritt 5: Erste Slice locken

Jetzt wird der Scope klein gemacht.

```text
From the PRD, mechanics spec, and test plan, define the first implementation slice.

Rules:
- playable in browser
- one core mechanic only
- deterministic seed mode
- unit-testable game logic separated from UI
- one losing condition
- one restart flow
- no sound dependency
- no online services

Return:
- files likely to create
- acceptance criteria
- tests to write first
- explicit non-goals
```

## Schritt 6: Ralph Loop für die Implementierung

Jetzt erst darf gebaut werden.

```text
Use the Ralph loop for the first implementation slice.

Read:
Read the approved PRD, mechanics spec, and test plan. Do not edit.

Ask:
Ask at most one blocking question. If none is needed, say "No blocker".

Lock:
Restate the exact slice, non-goals, files likely to create, and done criteria.
Wait for confirmation.

Produce:
Implement only the locked slice. Write tests. Run unit tests, build, and browser automation.

Halt:
Stop after verification. Report changed files, commands run, browser evidence, and residual risk.
```

## Production-Ready Gates

"Production ready" zählt nur, wenn es konkrete Beweise gibt.

Minimum für die Workshop-Slice:

- Game startet ohne Setup-Theater
- Core-Mechanik ist spielbar
- UI passt auf Mobile und Desktop
- Spiel ist ohne Sound vollständig spielbar
- Losing Condition ist sichtbar und fair
- Restart funktioniert
- Logik ist von UI getrennt
- Unit Tests für Generator, Moves, Score und Loss laufen
- Browser-Automation testet Start, Move, Lose, Restart und Mobile Viewport
- Build läuft
- Browser-Konsole hat keine Fehler
- README erklärt Regeln, Commands und Deployment

## Abschlussfragen

- Was hätte der Agent ohne PRD wahrscheinlich erfunden?
- Welche Non-goals haben Scope gerettet?
- Welche Tests prüfen wirklich Spielregeln, nicht nur DOM?
- Wo klingt "production ready" noch wie Theater?
- Was wäre die nächste Slice?
