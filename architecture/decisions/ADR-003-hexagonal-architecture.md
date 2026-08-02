# ADR-003 — Adopt Hexagonal Architecture (Ports and Adapters)

**Date:** 2026-08-02

**Status:** ACCEPTED

## Context

A key research question in the laboratory is:

> How can architectural boundaries be enforced when AI agents generate or modify software?

To investigate this, the laboratory requires:

- Explicit, verifiable architectural boundaries
- Clear dependency direction
- Isolable domain from infrastructure
- Measurable violations when agents cross boundaries
- Pedagogical clarity for architecture study

Architectural styles considered:
- Hexagonal (Ports and Adapters): Explicit boundaries, clear flow
- Layered: Simpler, but boundary enforcement less explicit
- Clean Architecture: Similar to Hexagonal, terminology differences
- Microservices: Over-scoped for laboratory
- Event-Driven: Suitable for eventual consistency (not primary focus)

## Decision

**Hexagonal Architecture (Ports and Adapters)** adopted as the laboratory's architectural style.

## Rationale

1. **Explicit Boundaries** — The "hexagon" makes domain boundaries visible and measurable
2. **Dependency Direction** — Dependencies point inward; infrastructure cannot depend on domain
3. **Testing Support** — Clear separation enables isolated domain testing without infrastructure
4. **Measurability** — Violations become detectable (crucial for agentic evaluation)
5. **Pedagogical Value** — Architectural intent is clear; suitable for educational use
6. **Infrastructure Agnostic** — Domain remains independent of technology choices
7. **Comparison Study** — Provides baseline for evaluating whether agents respect architecture

## Alternatives Considered

- **Layered Architecture**: Simpler, but dependency direction less enforced; harder to detect violations
- **Clean Architecture**: Similar structure, different terminology; layering sometimes less explicit
- **Microservices**: Over-scoped for laboratory; adds complexity not needed for experimental control

## Benefits

1. **Boundary Clarity** — Explicit ports make architectural intent unmistakable
2. **Testability** — Domain can be tested without infrastructure (fast, deterministic)
3. **Adaptability** — Technology swaps (database, API framework) don't affect domain logic
4. **Measurable Violations** — Agent-generated code crossing boundaries is detectable
5. **Framework Independence** — Domain contains no FastAPI, SQLAlchemy, or other infrastructure imports
6. **Scalable Learning** — Clear patterns for adding new features while maintaining structure

## Trade-offs

- **Upfront Effort** — Requires discipline; violated discipline is immediately visible
- **Some Indirection** — Ports/adapters add layers; business logic not in top-level code
- **Not a Panacea** — Hexagonal architecture doesn't prevent poor domain logic (only organizes it)
- **Dogmatism Risk** — Can become overly rigid if applied without pragmatism

## Risks

1. **Architectural Drift** — Without discipline, layers may blur (mitigated: explicit dependency rules in constitution)
2. **Over-Engineering** — Temptation to add unnecessary abstractions (mitigated: pattern introduced when solving problems, not proactively)
3. **Performance Overhead** — Indirection adds small overhead (negligible for laboratory)
4. **Team Discipline** — Requires commitment to not bypass architecture (mitigated: explicit constitution)

## Consequences

1. **Domain Layer** — Isolated from frameworks; contains entities, value objects, services, exceptions
2. **Application Layer** — Orchestrates domain; defines input/output ports; framework-agnostic
3. **Adapter Layer** — Implements ports; contains HTTP handlers, persistence, external service integration
4. **No Circular Dependencies** — Tooling can enforce inbound → outbound dependency direction
5. **Explicit Contracts** — Ports define clear interfaces between layers
6. **Testing Patterns** — Domain testable without infrastructure; integration testing of adapters

## Important Disclaimer

**This architecture style is chosen for the laboratory's pedagogical and experimental value, NOT because it has been empirically proven to reduce token consumption, prevent hallucinations, or improve agentic code quality.**

The laboratory will investigate whether agents respect these boundaries and measure the impact of architectural discipline on task outcomes.

## Revisit Conditions

- If experimental results suggest Hexagonal Architecture introduces unacceptable overhead for agents
- If a simpler architecture proves sufficient for experimental scope
- If evaluation reveals that boundary enforcement doesn't correlate with output quality
- If pedagogical value decreases due to complexity
