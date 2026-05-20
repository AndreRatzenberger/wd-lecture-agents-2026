# Harness Matrix

Die Namen unterscheiden sich, die Konzepte sind erstaunlich stabil.

| Konzept | Codex | Claude Code | GitHub Copilot | Harness-neutrale Idee |
| --- | --- | --- | --- | --- |
| Dauerhafter Repo-Kontext | `AGENTS.md` | `CLAUDE.md` | `.github/copilot-instructions.md` oder repo instructions | Agent Contract: Was gilt immer? |
| Skill | `.agents/skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` oder Plugin-Skill | `.github/skills`, `.agents/skills`, personal skills | Wiederholbare Expertise als Ordner |
| Plugin | Codex Plugin mit Skills, Apps, MCP | Claude Code Plugin mit Skills, Agents, Hooks, MCP | eher Skills, custom agents, MCP, instructions | Verteilbares Capability-Paket |
| MCP | `config.toml`, CLI/App MCP setup | `.mcp.json`, settings, plugin MCP | repo/custom-agent MCP settings | Standardisierte Tool- und Kontextbrücke |
| Subagent / Custom Agent | Codex subagents, custom TOML agents | subagents und agent teams | custom agents, cloud agent tasks | Isolierte Rolle mit eigenem Kontext |
| Hook / Automation | Codex hooks, automations | Claude Code hooks | Copilot hooks für cloud agent | Wiederholbare Event-Reaktion |
| Spec Flow | Plan Mode, skills, external Spec Kit | Plan Mode, plugins, Spec Kit | Copilot tasks, Spec Kit, custom prompts | Von Absicht zu Spec zu Plan zu Tasks |

## Faustregeln

- `AGENTS.md` und Verwandte: für Regeln, die fast immer gelten.
- Skills: für Methoden, die manchmal gebraucht werden und mehr Kontext brauchen.
- MCP: für externe Systeme, Live-Daten und Werkzeuge.
- Plugins: für Team-Verteilung und Versionierung.
- Subagents: für isolierte Recherche, Reviews oder parallele Hypothesen.
- Hooks: für stabile Automatisierung, nicht für unsichere Denkarbeit.

## Portabilität

Sehr portabel:

- Skill-Idee und `SKILL.md`-Körper
- Referenzmaterial, Checklisten, Beispiele
- MCP-Server als Protokollkonzept

Teilweise portabel:

- Skill-Speicherorte
- Plugin-Manifeste
- Custom agents/subagents
- Hooks und Berechtigungsmodelle

Praktische Workshop-Regel:

> Schreibe die Methode harness-neutral. Packe die Harness-Details in kleine Adaptertabellen.
