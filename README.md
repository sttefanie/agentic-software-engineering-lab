# Agentic Software Engineering Lab

## Project

Agentic Software Engineering Lab — A open-source experimental laboratory for investigating practices of Software Engineering applied to AI-assisted development.

## Purpose

This is an experimental laboratory designed to investigate, measure, and compare different approaches to AI-assisted software development. The lab provides a structured environment for testing hypotheses, documenting experiments, and building references for **Spec-Driven Development**, **Context Engineering**, and **Agentic Software Engineering** workflows.

## Research Areas

- **Spec-Driven Development** — Specification-first development methodologies
- **Context Engineering** — Designing and optimizing context for AI agents
- **Semantic Context Routing** — Intelligent routing of relevant context to agents
- **Agentic Software Engineering** — Multi-agent and specialized-agent workflows
- **Human-in-the-Loop** — Identifying critical checkpoints requiring human oversight
- **Software Architecture** — Architectural boundaries and enforcement with AI agents
- **AI Evaluation** — Methods for evaluating agentic development workflows
- **Context and Token Efficiency** — Measuring and optimizing token consumption
- **Observability** — Signals and metrics for understanding agentic workflows
- **Governance** — Standards and patterns for responsible agentic software development

## Initial Research Questions

1. Can semantic context routing reduce unnecessary context provided to coding agents?
2. What is the impact of context selection on token consumption?
3. How does context selection affect implementation quality?
4. When are specialized agents preferable to a single well-contextualized agent?
5. Where should Human-in-the-Loop checkpoints exist?
6. How should agentic software development workflows be evaluated?
7. What are the trade-offs between context reduction and loss of relevant information?
8. How can architectural boundaries be enforced when AI agents generate or modify software?
9. How can agentic workflows remain independent from specific LLM vendors?
10. What observability signals are useful for evaluating agentic development workflows?

## Status

**Experimental / Work in Progress**

⚠️ **Important:** This laboratory contains experimental patterns, hypotheses, and architectural approaches that will evolve as new experiments produce evidence. Patterns, hypotheses, and implementations documented here should not be considered stable or proven without explicit experimental validation.

No patterns, agents, workflows, or architectural decisions in this laboratory should be assumed to be best practices until they have been systematically tested and their results documented.

## Repository Structure

- **`docs/`** — Documentation and reference materials
- **`research/`** — Research hypotheses and experiments
- **`architecture/`** — Architectural decisions and documentation
- **`context/`** — Context Engineering infrastructure
- **`intents/`** — Semantic Intent Routing specifications
- **`agents/`** — Agent responsibility definitions
- **`skills/`** — Reusable capability definitions
- **`specs/`** — Feature specifications
- **`tasks/`** — Task definitions and examples
- **`evals/`** — Evaluation frameworks
- **`metrics/`** — Metrics and measurement definitions
- **`labs/`** — Experimental laboratories
- **`src/`** — Implementation (when applicable)

## Getting Started

1. Read [`docs/references.md`](docs/references.md) for research references
2. Review [`research/hypotheses.md`](research/hypotheses.md) for current research questions
3. Check [`research/experiments.md`](research/experiments.md) for active experiments
4. Explore [`architecture/overview.md`](architecture/overview.md) for architectural context

## License

See [`LICENSE`](LICENSE) file.

## Contributing

Contributions should follow the laboratory's commitment to separating FACT from HYPOTHESIS and documenting experiments rigorously.
