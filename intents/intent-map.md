# Semantic Intent Routing - Intent Map

**STATUS: EXPERIMENTAL**

This document describes the conceptual framework for Semantic Intent Routing in the Agentic Software Engineering Lab.

⚠️ **Important:** The routing strategy described here is currently experimental and has not yet been validated. Implementation, evaluation methodology, and effectiveness remain to be determined.

## Conceptual Flow

The following illustrates the conceptual flow for semantic intent routing:

```
                REQUEST
                   ↓
                INTENT
           (What does the request seek?)
                   ↓
                DOMAIN
        (Which domain(s) does this belong to?)
                   ↓
            CAPABILITIES
    (What capabilities are needed to fulfill this?)
                   ↓
          KNOWLEDGE OBJECTS
    (What information is relevant to this task?)
                   ↓
            CONTEXT PACKAGE
        (Curated context for the agent)
```

## Components

### REQUEST

The incoming request from a user or system.

- Can be explicit (a direct question or command)
- Can be implicit (inferred from context or prior conversation)
- May be ambiguous or incomplete

### INTENT

The semantic intent extracted from the request.

- What the request is asking for
- What problem the request is trying to solve
- What outcome is desired
- Conceptually determined, not keyword-based

### DOMAIN

The business domain(s) or problem space(s) relevant to the intent.

- Helps classify the type of task
- Enables domain-specific knowledge injection
- May be single or multi-domain

### CAPABILITIES

The technical or functional capabilities required to fulfill the intent.

- Skills agents need to possess
- Tools and libraries that will be needed
- Patterns and approaches relevant to the task
- Not all capabilities are used in every context

### KNOWLEDGE OBJECTS

Specific information relevant to this particular intent, domain, and capability combination.

- Code samples
- Documentation
- Standards and patterns
- Test cases
- Similar examples
- Constraints and requirements

### CONTEXT PACKAGE

The final, curated context provided to the agent.

- Selective subset of relevant knowledge
- Ordered by estimated relevance
- Includes metadata about each context element
- Excludes estimated-irrelevant information
- Designed to minimize token consumption while maintaining task completeness

## Key Questions

The following research questions drive the design of intent routing:

1. Can intent be reliably extracted from requests without manual specification?
2. Should intent extraction be independent from context selection?
3. How should conflicts between multiple possible intents be handled?
4. Can domain and capability classification be automated?
5. What is the optimal ordering of knowledge objects in context?
6. How sensitive is agent performance to context order and selection?
7. What is the minimum viable context for successful task completion?
8. How often should context be re-evaluated during multi-turn interactions?

## Current State

No intent routing system has been implemented. The framework above represents a conceptual model to guide future implementation research.

## Next Steps

1. Define intent taxonomy for laboratory tasks
2. Identify domain and capability hierarchies
3. Design semantic matching mechanism
4. Build knowledge object catalog
5. Implement and evaluate routing algorithm
6. Measure impact on token consumption and quality
