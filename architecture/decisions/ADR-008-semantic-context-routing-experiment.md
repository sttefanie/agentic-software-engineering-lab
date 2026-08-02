# ADR-008 — Define Semantic Context Routing as Key Experimental Variable

**Date:** 2026-08-02

**Status:** ACCEPTED

## Context

A central hypothesis of the laboratory is:

> Semantic Context Routing can reduce irrelevant context provided to agents during software development tasks, with measurable impact on token consumption and quality.

This hypothesis remains **UNPROVEN** and is the focus of planned experiments.

However, the architecture must be designed to enable this hypothesis to be tested.

The architecture must support:

- Providing complete context (baseline)
- Providing routed context (treatment)
- Measuring differences in token consumption and quality
- Separating "context routing" effects from "agent specialization" effects

## Decision

**Semantic Context Routing** is defined as a key experimental variable.

The architecture will include:

1. **Context Abstraction** — Context provided through abstraction, not hard-coded
2. **Routing Layer** — Pluggable routing strategy (can swap between full and routed)
3. **Measurement** — Instrumentation to measure what context was selected
4. **Baseline Support** — Both "no routing" (full context) and "routed" strategies supported
5. **Strategy Independence** — Routing strategy independent from agent implementation

## Rationale

1. **Experimental Rigor** — Clear isolation of "context routing" as a variable
2. **Comparative Analysis** — Can measure routing impact separately from other changes
3. **Vendor Independence** — Routing strategy not coupled to specific LLM vendor
4. **Measurement** — Architecture supports measuring context precision and recall
5. **Hypothesis-Driven** — Design explicitly supports testing the context routing hypothesis
6. **Reproducibility** — Future experiments can use same routing infrastructure

## What This Architecture Does NOT Assume

The architecture does NOT assume:

- Semantic routing is superior (it may not be)
- Semantic routing reduces hallucinations (unproven)
- Semantic routing improves code quality (to be measured)
- Any specific routing algorithm

The architecture simply enables these hypotheses to be tested.

## Context Routing Conceptual Model

```text
REQUEST
   ↓
INTENT ANALYSIS
   ↓
DOMAIN IDENTIFICATION
   ↓
CAPABILITY IDENTIFICATION
   ↓
KNOWLEDGE OBJECT SELECTION
   ↓
CONTEXT PACKAGE
   ↓
AGENT
```

**Baseline A (No Routing):**
CONTEXT PACKAGE = all available context

**Treatment B (Routed):**
CONTEXT PACKAGE = selected context based on routing strategy

## Consequences

1. **Context Provider Pattern** — Context abstracted behind interface
2. **Routing Adapters** — Different routing strategies (full, semantic, etc.) as adapters
3. **Context Metadata** — Context includes metadata (domain, capability, type, priority)
4. **Selection Instrumentation** — Measurement of what was selected vs. available
5. **Precision/Recall Metrics** — Tracking how much relevant vs. irrelevant context was selected

## Important Disclaimer

This ADR establishes the architectural support for testing context routing.

It does NOT claim that context routing:
- Reduces token consumption
- Improves code quality
- Reduces hallucinations
- Is a best practice

These are hypotheses to be tested, not facts to be assumed.

## Revisit Conditions

- If experimental results show context routing doesn't impact outcomes
- If simpler routing strategy proves sufficient
- If measurement shows context routing adds unacceptable overhead
- If vendor-specific context handling makes abstraction impractical
