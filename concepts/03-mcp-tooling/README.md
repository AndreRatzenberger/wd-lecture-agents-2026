# 03 MCP Tooling

## One-liner

MCP ist USB-C fuer Agentenwerkzeuge: ein Standard, damit unterschiedliche Agent Hosts externe Tools, Daten und Workflows anschliessen koennen.

## Warum das wichtig ist

Ohne MCP kopieren Menschen Kontext in Prompts:

- "Hier ist der aktuelle Issue."
- "Hier ist der Datenbankauszug."
- "Hier ist die API-Doku."
- "Hier ist ein Browser-Screenshot."

Mit MCP kann der Agent diese Dinge als Tool oder Resource abrufen, wenn der Host es erlaubt.

## Was MCP bereitstellt

Die Spezifikation unterscheidet vor allem:

- **Tools**: Funktionen, die der Agent ausfuehren kann.
- **Resources**: Kontext oder Daten, die gelesen werden koennen.
- **Prompts**: wiederverwendbare Vorlagen oder Workflows.

Merksatz:

```text
Resources geben Augen.
Tools geben Haende.
Prompts geben Startbahnen.
```

## Wann MCP sinnvoll ist

Nutze MCP, wenn:

- Kontext ausserhalb des Repos liegt
- Daten aktuell sein muessen
- ein Tool reproduzierbar angebunden werden soll
- mehrere Personen denselben Zugriff brauchen
- Copy/Paste zum Engpass wird

Nutze MCP nicht reflexartig, wenn:

- eine kleine Datei im Repo reicht
- ein einmaliger Prompt reicht
- das Tool zu viele Rechte braucht
- niemand den Server geprueft hat

## Security-Haken

MCP-Tools koennen echte Aktionen ausfuehren. Tool-Beschreibungen und externe Daten koennen prompt-injection-artig wirken. Deshalb:

- nur vertrauenswuerdige Server einbinden
- Rechte klein halten
- vor Tool-Ausfuehrung verstehen, was passiert
- Secrets nicht leichtfertig exponieren
- Outputs kritisch lesen

## Live-Demo

Zeige [../../examples/mcp/sample-configs.md](../../examples/mcp/sample-configs.md).

Frage:

> Was ist hier stabil, und was ist nur Harness-Adapter?

Antwort:

- Stabil: Agent Host verbindet sich zu einem MCP Server, der Tools/Resources/Prompts anbietet.
- Adapter: JSON vs TOML, Installbefehl, Auth, Scope.

## Takeaway

MCP macht den Agenten nicht automatisch klug. MCP macht relevante Welt zugaenglich. Klug wird es erst mit gutem Scope und guter Verifikation.
