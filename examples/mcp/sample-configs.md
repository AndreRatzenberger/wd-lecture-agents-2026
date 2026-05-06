# MCP Sample Configs

These examples are intentionally small. Do not install random MCP servers during a workshop without checking what they can access.

## Codex `config.toml`

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
startup_timeout_sec = 30
tool_timeout_sec = 60
```

## Claude Code `.mcp.json`

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

## Teaching Point

MCP config is the adapter. The concept is stable:

```text
Agent host <-> MCP client <-> MCP server <-> external tool/data
```

The exact file format changes by harness.
