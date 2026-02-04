# Architecture Strategy

## Agent Pattern
Chosen Pattern: **Planner–Worker–Judge (Hierarchical Swarm)**

### Rationale
- Planner maintains global campaign context
- Workers execute atomic tasks in parallel
- Judges enforce quality, safety, and governance

This pattern aligns with:
- FastRender Swarm Architecture
- Management-by-exception
- Horizontal scalability

## Human-in-the-Loop (HITL)
Humans intervene only when:
- Confidence score < 0.8
- Content is sensitive
- Financial transactions exceed thresholds

## Data Storage
- PostgreSQL: transactional data
- Weaviate: semantic memory
- Redis: queues and short-term state

## External Integration
All integrations occur via Model Context Protocol (MCP).
