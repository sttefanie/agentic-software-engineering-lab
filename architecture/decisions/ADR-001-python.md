# ADR-001 — Select Python 3.12 as Primary Language

**Date:** 2026-08-02

**Status:** ACCEPTED

## Context

The Agentic Software Engineering Lab requires a language suitable for:

- Rapid prototyping and experimentation
- Integration with AI/LLM ecosystems
- Accessible implementation for educational purposes
- Clear, maintainable code for architecture studies
- Comprehensive testing frameworks
- Strong community support for agentic systems

Multiple language options were considered:
- Python: Strong AI ecosystem, rapid development, accessible
- TypeScript: Good ecosystem, web-first, growing agentic support
- Go: Performance, concurrency, but steeper learning curve
- Java: Enterprise maturity, verbose, higher complexity
- Rust: Performance, safety, but slower development cycle

## Decision

**Python 3.12** selected as the primary implementation language.

## Rationale

1. **AI Ecosystem** — Most mature and comprehensive ecosystem for LLM integration, prompt engineering, and agentic frameworks
2. **Development Speed** — Enables rapid iteration on experimental hypotheses
3. **Accessibility** — Lower barrier to entry for educational and open-source contributions
4. **Code Clarity** — Enforced indentation and simpler syntax facilitate architecture review and discussion
5. **Testing** — Mature testing frameworks (pytest) aligned with quality requirements
6. **Community** — Large, active community around AI development and best practices
7. **Laboratory Goals** — Reduces accidental complexity, allowing focus on experimental variables

## Alternatives Considered

- **TypeScript**: Would provide better type safety and web integration, but AI ecosystem less mature; learning curve for non-web developers
- **Go**: Would provide better performance and concurrency, but verbose error handling; AI ecosystem less established
- **Rust**: Would provide superior performance and memory safety, but longer development cycle; agentic ecosystem less mature

## Benefits

- Rapid experimentation with hypotheses
- Easy integration with LLM APIs and agentic libraries
- Lower barrier for educational use
- Strong ecosystem for testing and observability
- Good tooling for dependency management (poetry, uv)

## Trade-offs

- **Performance**: Not optimized for high-throughput production systems (acceptable for laboratory)
- **Deployment Complexity**: Requires runtime environment (Docker acceptable solution)
- **Concurrency**: GIL limits true parallelism (acceptable for laboratory scope)
- **Mobile**: Python not suitable for mobile deployment (not a laboratory requirement)

## Risks

- Python-specific idioms may not transfer to other languages (acceptable for laboratory context)
- Dependency bloat if libraries not carefully curated (mitigation: discipline in `pyproject.toml`)
- Version fragmentation if Python 3.12 features not available (mitigation: explicit version requirement)

## Consequences

1. All implementation will be Python 3.12
2. CI/CD and tooling must support Python ecosystem
3. Dependency management via `pyproject.toml` (PEP 517/518)
4. Virtual environment strategy required
5. Python-version-specific syntax available (e.g., pattern matching from 3.10)
6. Documentation should include Python setup instructions

## Revisit Conditions

- If agentic library ecosystem shifts significantly to another language
- If educational requirements prioritize a different language
- If performance requirements change substantially
- If experiment requires specialized language capabilities unavailable in Python
