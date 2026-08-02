# ADR-006 — Design Vendor-Neutral Agentic Integration Layer

**Date:** 2026-08-02

**Status:** ACCEPTED

## Context

The laboratory investigates agentic software engineering across multiple contexts.

Future experiments may require evaluation with:
- Different LLM vendors (OpenAI, Anthropic, Google, etc.)
- Different agent frameworks and runtimes
- Different context sources and routing strategies
- Comparative analysis between approaches

A rigid vendor-specific architecture would:
- Limit experimental flexibility
- Confound vendor choice with hypothesis testing
- Reduce reproducibility
- Create unnecessary coupling

## Decision

The laboratory will design an **agent integration layer** that:

1. Abstracts vendor-specific details
2. Defines clear contracts for agent communication
3. Enables vendor swaps without changing domain logic
4. Remains decoupled from core application architecture

## Rationale

1. **Experimental Flexibility** — Can test with different vendors without major refactoring
2. **Clear Boundaries** — Vendor integration isolated to specific adapters
3. **Reproducibility** — Easier to reproduce results with different vendors
4. **Hypothesis Independence** — Can separate "vendor choice" from "hypothesis under test"
5. **Maintainability** — Future vendor changes don't ripple through codebase
6. **Governance** — Easier to enforce that domain logic remains vendor-neutral

## Alternative Approaches Considered

- **Vendor-Locked**: Direct dependency on specific vendor SDK (simpler initially, limits flexibility)
- **Framework-Specific**: Using vendor-specific agentic frameworks (same limitation)
- **Complete Abstraction**: Elaborate abstraction layer (may introduce unnecessary complexity)

## Design Principles

### Contracts, Not Implementations

Agent communication defined via abstract contracts (input/output structures), not specific implementations.

### Adapter Pattern

Vendor-specific code isolated in adapters, not in application logic.

### Clear Separation

```text
Application Domain
       ↑
       │ (abstract contract)
       │
Agent Integration Layer (vendor-neutral)
       ↑
       │ (adapter pattern)
       │
Vendor Adapters (OpenAI, Anthropic, etc.)
```

### Configuration-Driven

Agent vendor selection via configuration, not code changes.

## What This Does NOT Mean

- The laboratory will implement full vendor abstraction layer in Phase 02
- Multiple vendors will be integrated initially
- The application becomes vendor-neutral magically

Rather:

- The architecture leaves room for vendor abstraction
- When vendors are integrated, they're integrated via adapters
- The design doesn't lock domain logic to specific vendor
- Future vendor additions don't require domain logic changes

## Consequences

1. **Adapter Architecture** — Vendor-specific code in `adapters/outbound/agents/`
2. **Abstract Contracts** — Agent requests/responses defined as domain-neutral structures
3. **Configuration** — Agent vendor selection via environment or configuration
4. **Testing** — Agents can be tested via mock adapters
5. **Documentation** — Clear specification of agent integration contracts

## Implementation Timeline

- **Phase 02** (This Phase): Define contracts and adapter structure
- **Phase 03+** (Future): Implement vendor adapters as needed

## Revisit Conditions

- If vendor abstraction proves unnecessarily complex
- If all experiments use single vendor (then revisit cost/benefit)
- If new vendor requirements emerge
- If abstraction layer becomes performance bottleneck
