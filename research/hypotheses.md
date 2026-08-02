# Research Hypotheses

This document tracks hypotheses about agentic software engineering practices. Hypotheses progress through defined states as evidence is gathered.

## Hypothesis States

- **PROPOSED** — Hypothesis has been formulated and is pending testing
- **TESTING** — Active experiment is in progress to evaluate hypothesis
- **SUPPORTED** — Experimental evidence supports the hypothesis
- **PARTIALLY_SUPPORTED** — Experimental evidence partially supports the hypothesis
- **NOT_SUPPORTED** — Experimental evidence contradicts the hypothesis
- **INCONCLUSIVE** — Evidence is insufficient to reach a conclusion

## Hypothesis Template

```
### HYP-XXX

**Status:** PROPOSED

**Statement:**

**Motivation:**

**Independent Variables:**

**Dependent Variables:**

**Control Variables:**

**Metrics:**

**Experiment:**

**Evidence:**

**Result:**

**Conclusion:**
```

## Active Hypotheses

### HYP-001

**Status:** PROPOSED

**Statement:** Semantic Context Routing can reduce the quantity of irrelevant context provided to an agent during a software development task.

**Motivation:** Current approaches provide complete or near-complete context to coding agents. Hypothesis: selective context routing may reduce information noise while maintaining task completeness.

**Independent Variables:** Context routing strategy (full context vs. semantic routing)

**Dependent Variables:** Quantity of irrelevant context provided to agent

**Control Variables:** Task complexity, agent implementation, model used

**Metrics:** Context size, relevant context ratio, irrelevant context ratio

**Experiment:** *To be defined*

**Evidence:** *Pending*

**Result:** *Pending*

**Conclusion:** *Pending*

---

### HYP-002

**Status:** PROPOSED

**Statement:** Reducing irrelevant context can decrease token consumption without necessarily reducing implementation quality.

**Motivation:** If Semantic Context Routing (HYP-001) succeeds, the resulting reduction in context should lower API costs and latency. Hypothesis: this reduction does not materially harm code quality.

**Independent Variables:** Context selection strategy

**Dependent Variables:** Token consumption, implementation quality metrics

**Control Variables:** Task definition, model, agent implementation

**Metrics:** Input tokens, output tokens, total tokens, test pass rate, code quality score

**Experiment:** *To be defined*

**Evidence:** *Pending*

**Result:** *Pending*

**Conclusion:** *Pending*

---

### HYP-003

**Status:** PROPOSED

**Statement:** Specialized agents may demonstrate different behavior compared to a single well-contextualized agent when performing complex Software Engineering tasks.

**Motivation:** Multi-agent architectures are proposed in agentic engineering workflows. Hypothesis: task decomposition and specialization may produce measurably different outcomes than a monolithic approach.

**Independent Variables:** Agent architecture (single agent vs. specialized agents)

**Dependent Variables:** Task completion quality, planning iterations, implementation time, token consumption

**Control Variables:** Task complexity, agent capabilities, context availability

**Metrics:** Quality score, iteration count, execution time, token usage, architecture violations

**Experiment:** *To be defined*

**Evidence:** *Pending*

**Result:** *Pending*

**Conclusion:** *Pending*

---

### HYP-004

**Status:** PROPOSED

**Statement:** Human-in-the-Loop checkpoints at critical decision points can reduce errors based on missing or ambiguous requirements.

**Motivation:** Agentic systems may make incorrect assumptions when specifications are incomplete. Hypothesis: explicit human review at decision points improves outcome quality.

**Independent Variables:** Presence and placement of Human-in-the-Loop checkpoints

**Dependent Variables:** Requirement-based errors, implementation rework, human intervention count

**Control Variables:** Requirement quality, task complexity, agent implementation

**Metrics:** Error count, rework iterations, human intervention frequency, task success rate

**Experiment:** *To be defined*

**Evidence:** *Pending*

**Result:** *Pending*

**Conclusion:** *Pending*

---

## Important Principle

⚠️ **Never treat a hypothesis as fact.** Hypotheses progress through evidence-based states. A hypothesis remains "PROPOSED" or "TESTING" until experimental data supports changing its status. Avoid language that presents hypotheses as established truths.
