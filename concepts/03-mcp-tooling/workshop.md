# Workshop: MCP-Tool-Plan statt Tool-Sammelwut

## Ziel

Du entscheidest für ein Szenario, ob MCP sinnvoll ist, und entwirfst eine sichere Tool-Anbindung.

## Dauer

25 bis 30 Minuten.

## Szenario

Du willst, dass ein Coding Agent einen Flock-Bug aus einem GitHub-Issue oder PR-Kontext nachvollzieht. Er braucht:

- den aktuellen Issue
- Repo-Dateien
- Testbefehle
- vielleicht den Lösungs-PR zum späteren Vergleich
- vielleicht PR-Erstellung

## Schritt 1: Kontext klassifizieren

Füllen:

| Information | Liegt wo? | Ändert sich oft? | MCP sinnvoll? |
| --- | --- | --- | --- |
| Repo-Code | lokal | ja | eher nein, Host kann Dateien lesen |
| Testbefehl | Repo-Doku | selten | nein, gehört in Instructions |
| Issue Beschreibung | GitHub/Linear/Jira | ja | ja |
| Lösungs-PR | GitHub | ja | ja, aber erst nach eigener Diagnose |
| Browser-Zustand | laufende App | ja | ja, wenn UI relevant |
| Coding Style | Repo-Regel | selten | nein, Instructions/Skill |

## Schritt 2: Minimalen MCP-Satz wählen

Wähle maximal zwei MCP-Server für das Szenario.

Beispiel:

```text
1. GitHub MCP: Issues und PRs lesen/schreiben.
2. Playwright MCP: UI-Flow reproduzieren und Screenshots machen, falls der Bug sichtbar ist.
```

Begründung:

- GitHub hat Live-Kontext.
- Browser-Zustand ist nicht im Repo.
- Style-Regeln und Tests bleiben im Repo.

## Schritt 3: Safety-Fragen beantworten

Vor Installation:

```text
Welche Daten sieht der MCP-Server?
Welche Aktionen kann er ausführen?
Welche Tokens/Secrets braucht er?
Kann ich ihn auf read-only beschränken?
Wie erkenne ich falsche oder bösartige Tool-Ausgaben?
```

## Schritt 4: Agent-Prompt schreiben

```text
You may use MCP tools only for:
- reading the issue
- reading PR #412 after your own diagnosis
- reproducing the UI if needed

Do not use MCP tools to write, close, delete, or publish anything unless I explicitly approve.
Before using a tool, say which tool you plan to use and why.
After using it, summarize the evidence it returned.
```

## Schritt 5: Optional lokal konfigurieren

Nutze [../../examples/mcp/sample-configs.md](../../examples/mcp/sample-configs.md) als Formatreferenz. Installiere nur Server, denen du in deiner Umgebung vertraust.

## Ergebnis

Du hast keine MCP-Wunschliste gebaut, sondern einen Werkzeugplan mit Scope.
