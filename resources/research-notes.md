# Research Notes

Diese Quellen sind die belastbare Basis für den Workshop. Die Einordnung ist absichtlich praktisch: Was hilft beim Unterrichten von High-Level Coding Agents?

## Offizielle Quellen

- OpenAI Codex CLI: Codex kann lokal im Terminal Code lesen, ändern und ausführen. Quelle: <https://developers.openai.com/codex/cli>
- OpenAI Codex Best Practices: gute Prompts enthalten Goal, Context, Constraints und Done-when; `AGENTS.md`, MCP, Skills und Reviews sind zentrale Reliability-Hebel. Quelle: <https://developers.openai.com/codex/learn/best-practices>
- OpenAI Codex Skills: Skills paketieren Instructions, Ressourcen und optionale Scripts; Codex nutzt progressive disclosure. Quelle: <https://developers.openai.com/codex/skills>
- OpenAI Codex Plugins: Plugins bündeln Skills, Apps und MCP-Server als wiederverwendbare Workflows. Quelle: <https://developers.openai.com/codex/plugins>
- OpenAI Codex MCP: MCP verbindet Codex mit externen Tools und Kontextquellen. Quelle: <https://developers.openai.com/codex/mcp>
- Anthropic Claude Code Features: CLAUDE.md, Skills, Subagents, MCP, Hooks und Plugins sind unterschiedliche Erweiterungsmechaniken, die kombiniert werden können. Quelle: <https://code.claude.com/docs/en/features-overview>
- Anthropic Claude Code Plugins: Plugins können Skills, Agents, Hooks und MCP-Server teilen. Quelle: <https://code.claude.com/docs/en/plugins>
- Anthropic Agent Skills: Skills sind modell-invoked, reduzieren repetitive Prompts und können im Team geteilt werden. Quelle: <https://docs.claude.com/en/docs/claude-code/skills>
- GitHub Copilot Cloud Agent: Copilot kann mit custom instructions, MCP servers, custom agents, hooks und skills angepasst werden. Quelle: <https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent>
- GitHub Copilot Agent Skills: Copilot unterstützt Skills im offenen Agent-Skills-Format, unter anderem in `.agents/skills`. Quelle: <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
- Agent Skills Specification: ein Skill ist mindestens ein Ordner mit `SKILL.md`; optionale Ordner sind `scripts`, `references` und `assets`. Quelle: <https://agentskills.io/specification>
- Model Context Protocol Specification: MCP standardisiert Resources, Prompts und Tools für LLM-Anwendungen; Security und User Consent sind zentrale Prinzipien. Quelle: <https://modelcontextprotocol.io/specification/2025-06-18/basic>
- GitHub Spec Kit: Spec-driven Development mit AI ist als offenes Toolkit für Copilot, Claude Code, Gemini CLI und andere Agents gedacht. Quelle: <https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/>
- Spec Kit Methodology: SDD behandelt Specs als zentrale Quelle der Wahrheit, aus der Pläne und Code entstehen. Quelle: <https://github.com/github/spec-kit/blob/main/spec-driven.md>

## Lokale Research-Artefakte

- `cc-ecosystem/RESEARCH-REPORT.md`: Ökosystem-Überblick über Claude Code Plugins, Skills, MCP-Server, Hooks und Agent-Tools.
- `cc-ecosystem/CC-TO-CODEX-PORTABILITY.md`: Portabilitätsthese: Skills und MCP sind relativ portabel, Hooks und Subagents brauchen Adapter.
- `spec-compare-codex/.internal/research/skills-drift-2026-03-15.md`: Skills sind nicht mehr nur Prompt-Packs, sondern oft UX-, Workflow- und Tool-Orchestrierungs-Schichten.
- `basic-memory/shared/projects/spec-driven-skills/report.md`: Spec Kit plus task graph plus MCP ist eine starke Kombination für agentische Softwarearbeit.

## Aha-Beispiel

- `JuliusBrussee/caveman`: Ein Skill/Plugin, das mit einer einfachen Verhaltensregel Token spart und trotzdem technische Präzision behalten will. Der Wert für diesen Workshop ist nicht "sprech wie Caveman", sondern: Skills können Verhalten und Methodik so kompakt verpacken, dass ein Agent anders arbeitet. Quelle: <https://github.com/JuliusBrussee/caveman>

## Synthese für den Workshop

Die stabilste, harness-neutrale Lehrlinie:

```text
Context tells the agent what world it is in.
MCP gives the agent hands.
Skills give the agent habits.
Specs give the agent direction.
Orchestration gives the agent rhythm.
Verification gives the human confidence.
```
