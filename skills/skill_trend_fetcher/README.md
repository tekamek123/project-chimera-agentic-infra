# Skill: Trend Fetcher

## Purpose
Fetches trending topics from various platforms for content inspiration.

## Input Contract
```json
{
  "platform": "string",  // twitter, instagram, tiktok
  "region": "string"     // ethiopia, global, etc.
}
```

## Output Contract
```json
[
  {
    "topic": "string",
    "score": "number",
    "source": "string",
    "timestamp": "string"
  }
]
```

## Methods
- `validate_input(input_dict) -> bool`
- `fetch_trends(platform: str, region: str) -> List[Dict]`

## Error Handling
- Raises ValueError for invalid platforms
- Returns empty list for API failures
