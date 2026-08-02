# ADR-005 — Select pytest as Testing Framework

**Date:** 2026-08-02

**Status:** ACCEPTED

## Context

The laboratory requires comprehensive testing to:

- Validate domain logic and business rules
- Test agent-generated code quality
- Verify architectural boundary compliance
- Support Spec-Driven Development workflow
- Enable regression testing across experiments
- Provide fast feedback during development

Testing frameworks considered:
- pytest: Modern, fixture-rich, plugin ecosystem, industry standard
- unittest: Python standard library, more verbose
- nose2: Legacy, less actively maintained
- hypothesis: Property-based testing (complementary, not a replacement)

## Decision

**pytest** selected as the primary testing framework.

**hypothesis** will be considered for property-based testing when appropriate.

## Rationale

1. **Simplicity** — Clean, Pythonic test syntax (functions vs. classes)
2. **Fixtures** — Powerful fixture system for test setup and teardown
3. **Plugins** — Rich ecosystem: pytest-asyncio, pytest-cov, pytest-mock, etc.
4. **Parametrization** — Built-in support for testing multiple scenarios
5. **Assertion Introspection** — Clear assertion failures with detailed output
6. **Performance** — Fast test discovery and execution
7. **CI/CD Integration** — Standard in modern Python CI/CD pipelines

## Alternatives Considered

- **unittest**: Standard library, but verbose; class-based; fewer features
- **nose2**: Legacy ecosystem; less community activity
- **Twisted Trial**: Overkill for laboratory; designed for reactive systems

## Benefits

1. **Test Clarity** — Readable test code communicates intent
2. **Rapid Feedback** — Quick test discovery and parallel execution
3. **Debugging** — Excellent tools for test debugging (pdb integration, verbose output)
4. **Coverage Measurement** — pytest-cov plugin for code coverage analysis
5. **Async Testing** — pytest-asyncio enables testing async code
6. **Mocking Support** — pytest-mock for dependency isolation
7. **Scalability** — Performs well from dozens to thousands of tests

## Trade-offs

- **Learning Curve** — Fixtures are powerful but require understanding of scope
- **Dependency Management** — Additional dependencies beyond Python standard library
- **Backwards Compatibility** — pytest versions have some breaking changes between major versions (mitigated: pin version)

## Risks

1. **Test Complexity** — Deeply nested fixtures can become difficult to understand (mitigated: clear naming, documentation)
2. **Async Test Errors** — Improper async setup can hide errors (mitigated: clear async testing patterns)
3. **Slow Tests** — Tests touching persistence layer can be slow (mitigated: separate fast/slow tests)
4. **Over-Testing** — Temptation to test implementation rather than behavior (mitigated: focus on behavior)

## Consequences

1. **Test Organization** — Tests organized in `tests/` directory mirroring source structure
2. **Fixture Patterns** — Common fixtures defined in `conftest.py`
3. **Test Markers** — Tests marked for categorization (unit, integration, slow, etc.)
4. **Coverage Baseline** — Target coverage defined; measured in CI/CD
5. **Parametrized Tests** — Multiple scenarios tested via single parametrized test
6. **Async Tests** — Async test support via pytest-asyncio

## Important Context

In the laboratory, tests are not supplementary — they are part of implementation.

Spec-Driven Development requires test definitions before implementation begins.

## Revisit Conditions

- If testing requirements change (e.g., property-based testing becomes primary)
- If pytest incompatibility is discovered with agentic evaluation tools
- If performance becomes problematic at scale
