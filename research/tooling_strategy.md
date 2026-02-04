# Tooling Strategy

## Developer MCP Tools
Used during development:
- filesystem-mcp: file operations
- git-mcp: version control
- sqlite-mcp: local persistence

## Runtime Agent Skills
Skills are NOT MCP servers.
They are internal capability modules with strict contracts.

Examples:
- skill_trend_fetcher
- skill_content_generator
- skill_publisher

Each skill defines:
- Input schema
- Output schema
- Error behavior
