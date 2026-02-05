# Skills Directory - Project Chimera

## Overview
This directory contains the **runtime skills** that Chimera agents will use to perform tasks.

## Important: Skills vs MCP Tools
- **Skills**: Internal capability modules with strict contracts
- **MCP Tools**: External bridges (database connectors, APIs)

## Available Skills

### 1. skill_trend_fetcher
Fetches trending topics from social platforms for content inspiration.

### 2. skill_content_generator  
Generates content based on trends and persona constraints.

### 3. skill_publisher
Publishes content via MCP tools (no direct API calls).

## Skill Contract Requirements
Each skill MUST define:
- Input schema validation
- Output schema compliance  
- Error handling behavior
- Interface methods

## Implementation Status
🟡 **Intentionally Incomplete** - Tests exist, implementation pending
This follows the TDD approach: failing tests define the requirements that AI agents will fulfill.

## Usage
```python
from skills.skill_trend_fetcher import TrendFetcher

fetcher = TrendFetcher()
trends = fetcher.fetch_trends("twitter", "ethiopia")
```
