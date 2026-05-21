# 07 Verification and Safety

## One-liner

Ein Agent ist erst fertig, wenn es Beweise gibt. Plausible Sprache ist kein Beweis.

## Warum das wichtig ist

Coding Agents optimieren stark auf Hilfreichkeit. Das kann zu Abschlussantworten führen, die besser klingen als der Arbeitsstand ist.

Typische Risiken:

- Tests wurden nicht wirklich ausgeführt.
- Der falsche Test wurde ausgeführt.
- Unrelated files wurden verändert.
- Security oder Datenzugriff wurden nicht bedacht.
- Der Agent hat einen Workaround statt die Ursache gebaut.
- Das Ergebnis passt zum Plan, aber nicht zum ursprünglichen Ziel.

## Verifikationspyramide

Von schwach zu stark:

```text
"Looks good"                  schwach
Agent summary                 schwach
Diff gelesen                  mittel
Narrow test passed            gut
End-to-end behavior observed  sehr gut
Review against spec           sehr gut
```

## Gute Done-Kriterien

Ein gutes Done-Kriterium ist:

- konkret
- ausführbar
- relevant
- klein genug für die Aufgabe
- berichtet mit echtem Output oder klarer Blockerbeschreibung

Beispiel:

```text
Done when:
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q passes.
Final answer must include changed files and any unverified assumptions.
```

## Safety für MCP und Plugins

Bei externen Tools:

- Prüfe Berechtigungen.
- Vertraue Tool-Beschreibungen nicht blind.
- Gib Schreibaktionen explizit frei.
- Halte Secrets aus Prompts und Logs.
- Nutze read-only, wo read-only reicht.

Bei Skills und Plugins:

- Lies `SKILL.md`.
- Prüfe Scripts.
- Prüfe Installationsbefehle.
- Nutze vertrauenswürdige Quellen.
- Versioniere Team-Skills im Repo.

## Failure Modes benennen

Viele Agentenläufe scheitern nicht spektakulär, sondern leise:

- zu früh editieren
- Scope vergrößern
- Tests schwächen
- Verification behaupten statt ausführen
- Tool-Ausgaben zu stark vertrauen

Nutze den [Agent Failure Modes Catalog](../../resources/agent-failure-modes.md), um solche Muster im Lauf zu benennen und gezielt zu stoppen.

## Takeaway

Agentenarbeit ohne Verifikation ist Theater. Agentenarbeit mit Verifikation ist Engineering.
