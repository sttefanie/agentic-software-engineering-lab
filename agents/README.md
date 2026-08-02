# Agents

This directory contains specifications for agents used in agentic software engineering workflows.

## Purpose

Agents are defined roles that can participate in software development tasks. Current agent definitions include:

- **Planner** — Responsible for task planning and decomposition
- **Implementer** — Responsible for code generation and implementation
- **Reviewer** — Responsible for code review and quality assessment
- **Validator** — Responsible for validation and testing

## Important Note

⚠️ These agent definitions are **NOT IMPLEMENTED**. They represent placeholder responsibility areas for future experimental agents. Each agent definition is a template showing what will eventually be specified once agent architectures and workflows are designed.

## Human-in-the-Loop Principle

An important principle across all agents:

When information necessary for a critical decision is:
- Missing
- Ambiguous
- Conflicting

Agents should prefer:

```
        STOP
         ↓
IDENTIFY MISSING INFORMATION
         ↓
REQUEST HUMAN INPUT
         ↓
UPDATE SPECIFICATION
         ↓
      CONTINUE
```

Instead of silently assuming a rule or making an unevidenced decision.

This mechanism has **NOT YET BEEN IMPLEMENTED**.

## Next Steps

Agent specifications will be developed and formalized as the laboratory defines specific agentic workflows for experimentation.
