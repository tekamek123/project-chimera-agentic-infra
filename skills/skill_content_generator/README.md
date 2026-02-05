# Skill: Content Generator

## Purpose
Generates content (text, captions, posts) based on trends and persona constraints.

## Input Contract
```json
{
  "topic": "string",
  "persona": "string",     // witty, empathetic, technical
  "format": "string",      // caption, post, reply
  "constraints": "object"  // brand voice, length limits
}
```

## Output Contract
```json
{
  "content": "string",
  "metadata": {
    "word_count": "number",
    "tone": "string",
    "confidence": "number"
  }
}
```

## Methods
- `validate_input(input_dict) -> bool`
- `generate_content(topic: str, persona: str, format: str) -> Dict`
- `validate_persona(persona: str) -> bool`

## Error Handling
- Raises ValueError for invalid formats
- Returns fallback content for generation failures
