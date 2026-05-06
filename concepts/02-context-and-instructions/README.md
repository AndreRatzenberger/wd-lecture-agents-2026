# 02 Context and Instructions

## One-liner

Kontext ist nicht "mehr Text". Kontext ist die richtige Weltbeschreibung zur richtigen Zeit.

## Warum das wichtig ist

Coding Agents sind erstaunlich gut darin, Muster zu vervollstaendigen. Sie sind aber nicht magisch in deinem Kopf, deinem Team oder deiner Architektur.

Wenn du jedes Mal dieselben Dinge sagst, gehoeren sie nicht in den Prompt. Sie gehoeren in eine dauerhafte Agent-Instruktion.

Beispiele:

- "Nutze `uv`, nicht `pip`."
- "Tests muessen vor Abschluss laufen."
- "Keine grossen Refactors ohne Auftrag."
- "Docs sind Teil von Done."
- "In diesem Repo ist `src/api` der oeffentliche Contract."

## Die Kontext-Leiter

```text
Immer gueltig       -> AGENTS.md / CLAUDE.md / copilot-instructions
Manchmal relevant   -> Skill
Live extern         -> MCP
Einmalig fuer Task  -> Prompt
Zu laut geworden    -> Referenzdatei oder Tool
```

## Harness-neutraler Blick

| Bedarf | Geeigneter Ort |
| --- | --- |
| Repo-Regeln, Build/Test, Architektur | `AGENTS.md`, `CLAUDE.md`, Copilot instructions |
| Wiederholbarer Workflow | `SKILL.md` |
| Live-Daten oder externe Tools | MCP |
| Einmaliger Auftrag | Prompt |
| Grosse Referenz | separate Markdown-Datei, die der Agent bei Bedarf liest |

## Mini-Theorie: Context Cost

Jede Instruktion konkurriert mit dem eigentlichen Problem um Aufmerksamkeit.

Gute dauerhafte Regeln sind:

- kurz
- konkret
- beobachtbar
- aktuell
- an echte Fehler gekoppelt

Schlechte Regeln sind:

- motivational
- widerspruechlich
- global, obwohl nur fuer ein Modul relevant
- zu lang, um gelesen zu werden

## Live-Demo

Lass den Agenten eine schlechte Regel verbessern:

```text
Always write good clean code and be careful.
```

Besser:

```text
Before editing unfamiliar code, identify the relevant files and the verification command.
Keep changes scoped to the requested behavior.
Report any unverified assumption before saying done.
```

## Takeaway

Ein guter Agent Contract reduziert Raten. Ein gutes Repo-Instructions-File reduziert Wiederholung.
