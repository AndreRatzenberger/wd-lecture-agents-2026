# Greenfield Facilitator Notes

Diese Notizen sind für die Person vorne im Raum.

## Warum diese Übung existiert

Der Flock-Bug ist Brownfield: Die Wahrheit liegt im bestehenden Repo.

Das Puzzle-Spiel ist Greenfield: Die Wahrheit muss erst gebaut werden. Genau dort passieren typische Agentenfehler:

- Agent baut sofort UI statt Produktentscheidung.
- "Novel and addictive" wird zu Marketingtext statt Mechanik.
- "Production ready" wird behauptet, aber nicht verifiziert.
- Tests prüfen Rendering, nicht Spielregeln.
- Browser-Automation wird versprochen, aber nie wirklich ausgeführt.

## Empfohlene Position im Ablauf

Kurzform für 4 Stunden:

- Modul 05: Greenfield PRD + Mechanics Spec als Hauptübung
- Modul 06: Ralph Loop auf erster Implementierungsscheibe
- Flock danach als Brownfield-Kontrast oder umgekehrt, je nach Gruppe

Wenn wenig Zeit bleibt:

- Nur Konzeptoptionen, PRD und erste Slice machen
- Nicht implementieren

Wenn die Gruppe stark ist:

- Eine echte erste Slice bauen lassen
- Playwright-Test oder Browser-MCP-Check wirklich ausführen
- Danach Flock-Bug als "jetzt dasselbe in fremder Codebase" nutzen

## Gute Puzzle-Kandidaten

Gute Kandidaten für eine erste Slice:

- kleines Raster
- klare Einzelaktion
- deterministischer Seed
- sofort sichtbare Losing Condition
- keine Physik-Engine
- kein Sound als Pflichtmechanik
- keine komplexe Animation als Kernregel

Beispiele für passende Mechanik-Richtungen:

- Linien/Flüsse umleiten, bis Überdruck entsteht
- begrenzte Energie in einem prozeduralen Raster verteilen
- Symmetrien brechen oder erhalten
- Token mit einfachen Regeln fusionieren, aber Board-Space verlieren

Schlechte Kandidaten:

- "wie Tetris, aber anders"
- Story-/Dialogspiele
- Sound-Rhythmus-Spiele
- komplexe Echtzeit-Physik
- Multiplayer
- Puzzle mit vielen handgebauten Levels

## Was "Novel" hier heißt

Novel muss nicht patentfähig sein. Für den Workshop reicht:

- nicht nur ein Klon von 2048, Minesweeper, Tetris oder Sudoku
- ein klarer Twist in der Entscheidung pro Zug
- eine Losing Condition, die aus der Kernmechanik entsteht
- genug Tiefe, dass ein zweiter Versuch anders läuft

## Review-Rubrik

Bewerte Agentenoutput hart:

| Kriterium | Grün | Gelb | Rot |
| --- | --- | --- | --- |
| Mechanik | in einem Satz spielbar erklärt | interessant, aber schwammig | nur Thema oder Mood |
| Scope | erste Slice klar | mehrere Features vermischt | ganzes Spiel auf einmal |
| Tests | Regeln und Generator testbar | nur UI-Smoke | keine echten Assertions |
| Losing Condition | fair und aus Regeln abgeleitet | funktioniert, aber willkürlich | Timer/Random-Strafe |
| Mobile | Touch konkret beschrieben | "responsive" behauptet | Desktop-only |
| Production Ready | Commands und Gates konkret | allgemeine Checkliste | reine Behauptung |

## Moderationssätze

- "Eine gute Spielidee ist kein Feature-Haufen. Sie ist eine Entscheidung, die man immer wieder treffen will."
- "Production ready ist kein Adjektiv. Es ist eine Liste von Beweisen."
- "Wenn die Spielregel nicht ohne DOM testbar ist, ist sie noch nicht sauber verstanden."
- "Greenfield braucht mehr Spec, nicht weniger, weil noch keine Codebase widerspricht."

## Beispiel für eine gute erste Slice

```text
Game: Pulse Grid
Core: Place mirrors on a small grid to route pulses into sinks before pressure overflows.
Slice:
- 5x5 seeded grid
- one pulse source, two sinks, five placeable mirrors
- each turn pulse advances one step
- score for delivered pulses
- lose when pressure reaches 10
- restart with next seed
Tests:
- seeded grid repeats
- mirror changes direction
- sink reduces pressure
- overflow triggers loss
- Playwright covers start, one move, loss, restart
```

Das Beispiel ist nicht als Pflichtidee gedacht. Es zeigt nur die richtige Granularität.
