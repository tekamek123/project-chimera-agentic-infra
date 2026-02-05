# Skill: Publisher

## Purpose
Publishes content to social media platforms via MCP tools.

## Input Contract
```json
{
  "content": "string",
  "platform": "string",    // twitter, instagram, threads
  "metadata": "object"      // media urls, hashtags, etc.
}
```

## Output Contract
```json
{
  "success": "boolean",
  "post_id": "string",
  "platform": "string",
  "timestamp": "string",
  "error": "string or null"
}
```

## Methods
- `validate_input(input_dict) -> bool`
- `publish(content: str, platform: str, metadata: Dict) -> Dict`
- `validate_platform(platform: str) -> bool`

## Error Handling
- Raises ValueError for unsupported platforms
- Returns error details for API failures
- Never makes direct API calls - uses MCP tools only
