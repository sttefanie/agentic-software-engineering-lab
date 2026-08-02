# ADR-002 — Select FastAPI as Web Framework

**Date:** 2026-08-02

**Status:** ACCEPTED

## Context

The laboratory requires an HTTP API framework for:

- Receiving external requests
- Testing agentic workflows end-to-end
- Integrating with CI/CD and evaluation systems
- Demonstrating complete workflows
- Built-in API documentation
- Strong integration with modern Python async capabilities

Frameworks considered:
- FastAPI: Modern, async-native, automatic OpenAPI docs, strong validation
- Django: Mature, batteries-included, heavier weight
- Flask: Lightweight, but minimal batteries
- Starlette: Low-level async framework (FastAPI built on it)

## Decision

**FastAPI** selected as the web framework.

## Rationale

1. **Async-Native** — Built from ground-up with async/await, suitable for I/O-bound agentic workflows
2. **Automatic OpenAPI** — Generates API documentation automatically (valuable for experimentation)
3. **Type Hints** — Leverages Python type hints for validation and documentation
4. **Pydantic Integration** — Native support for input/output validation and serialization
5. **Performance** — Competitive performance with other modern Python frameworks
6. **Modern Practices** — Encourages dependency injection and testing-friendly patterns
7. **Learning Curve** — Relatively gentle for modern Python developers

## Alternatives Considered

- **Django**: More mature, batteries-included; but heavier, slower to iterate, older patterns
- **Flask**: Lightweight, but requires assembling components; manual validation handling
- **Starlette**: More minimal, but loses convenience of FastAPI's automatic docs and validation

## Benefits

- Rapid API development without boilerplate
- Automatic interactive API documentation (Swagger UI)
- Strong validation through Pydantic
- Excellent for testing (TestClient)
- Natural fit for async operations (agent coordination, long-running tasks)
- Clean separation of concerns (routes, validation, business logic)

## Trade-offs

- **Learning Curve**: Requires understanding of async Python (mitigated by good documentation)
- **Ecosystem Size**: Smaller than Django, but sufficient for laboratory scope
- **Convention vs Configuration**: Less opinionated than Django (acceptable for controlled lab)
- **Maturity**: Younger than Django, but stable and production-ready

## Risks

- Breaking changes in major versions (mitigated: pin to stable minor version)
- Dependencies on Pydantic v2 may introduce surprises (mitigated: clear version specification)
- Async complexity if mishandled (mitigated: clear guidelines in constitution)

## Consequences

1. HTTP API provided via FastAPI
2. Input/output validation via Pydantic models
3. Async-first request handling
4. Built-in endpoint documentation at `/docs` and `/redoc`
5. TestClient for endpoint testing
6. Dependency injection handled explicitly
7. CORS and middleware configuration required

## Revisit Conditions

- If laboratory scope expands beyond HTTP API (e.g., gRPC, GraphQL)
- If async patterns prove problematic for experimental workflows
- If performance characteristics change
- If breaking changes in FastAPI/Pydantic create unsustainable migration burden
