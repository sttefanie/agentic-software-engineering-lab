# ADR-004 — Select PostgreSQL as Primary Database

**Date:** 2026-08-02

**Status:** ACCEPTED

## Context

The laboratory requires a database for:

- Persistent state for banking API examples (customers, accounts, transactions)
- Realistic persistence scenarios for code generation evaluation
- Reproducible test data
- Transactional guarantees for financial operations modeling
- Support for complex queries and relationships

Database options considered:
- PostgreSQL: Mature, ACID, rich types, JSON support, open-source
- SQLite: Simple, good for testing, limited concurrency
- MySQL: Mature, but fewer advanced features
- MongoDB: Schema-flexible, but poor fit for structured financial data
- Redis: In-memory, but not suitable as primary store

## Decision

**PostgreSQL** selected as the primary relational database.

## Rationale

1. **ACID Guarantees** — Critical for modeling financial transactions reliably
2. **Data Integrity** — Strong constraints and type system reduce invalid states
3. **Open-Source** — Aligns with laboratory's open-source commitment
4. **Rich Ecosystem** — Extensive Python drivers, migration tools, monitoring
5. **Advanced Types** — JSON, arrays, custom types useful for experimentation
6. **Industry Standard** — Familiar to most developers; reduces barrier to contribution
7. **Testability** — Can run in Docker/container for isolated test environments

## Alternatives Considered

- **SQLite**: Would simplify local testing, but lacks concurrency features; poor for realistic scenarios
- **MySQL**: Mature, but fewer advanced features; less suitable for complex queries
- **MongoDB**: Schema-less approach conflicts with need for structured domain modeling
- **Redis**: Excellent for caching, but not suitable as primary store for persistent state

## Benefits

1. **Transactional Consistency** — ACID properties model real financial reliability requirements
2. **Complex Queries** — Joins and aggregations support realistic reporting scenarios
3. **Constraint Enforcement** — Database-level constraints prevent invalid states
4. **Migration Support** — Alembic integrates seamlessly for version-controlled schema changes
5. **Developer Familiarity** — Most Python developers have PostgreSQL experience
6. **Observability** — Rich tooling for query analysis, performance monitoring
7. **Realistic Scenarios** — Database-side transactions model real-world constraints agents must respect

## Trade-offs

- **Complexity** — More complex than SQLite, but necessary for realistic modeling
- **Setup Overhead** — Requires running PostgreSQL server (mitigated: Docker)
- **Deployment Considerations** — Production deployment requires more configuration than embedded databases
- **Learning Curve** — Advanced features not needed for basic use, but available for complexity

## Risks

1. **Data Loss** — Misconfigured persistence layer can lose data (mitigated: explicit tests for persistence)
2. **Migration Failures** — Schema changes can break existing data (mitigated: careful migration planning)
3. **Query Performance** — Poor queries can be slow (mitigated: observability and testing)
4. **Connection Pool Issues** — Async code can exhaust connections (mitigated: SQLAlchemy connection pooling)

## Consequences

1. **Schema Management** — Alembic for versioned migrations
2. **ORM Integration** — SQLAlchemy 2.x for object-relational mapping
3. **Development Setup** — Local PostgreSQL instance required (Docker recommended)
4. **Testing Strategy** — Test database separate from development
5. **Environment Configuration** — Database URL in configuration management
6. **Connection Handling** — Async connection pool configuration for FastAPI

## Revisit Conditions

- If laboratory experiments require different persistence semantics
- If schema complexity grows beyond PostgreSQL's practical limits
- If performance becomes problematic (unlikely at laboratory scale)
- If simpler database proves sufficient for experimental scope
