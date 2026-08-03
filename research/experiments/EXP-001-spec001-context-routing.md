# EXP-001 — Context Routing e Agentic Workflow na SPEC-001

Status: DESIGNED

## Research Questions

- **RQ1:** Como a seleção controlada de contexto afeta quantidade e relevância do contexto usado por um agente?
- **RQ2:** Como essa seleção afeta a aderência da implementação à Specification?
- **RQ3:** Como `Planner → Implementer → Reviewer → Validator` se compara a single-agent na mesma tarefa?
- **RQ4:** Como Knowledge Governance e Source Authority afetam a detecção de conflitos, contexto desatualizado e decisões sem autoridade?

Esta experiência não responde às RQs nesta etapa.

## Hypotheses

- **H1 — Context Efficiency:** Semantic Context Routing pode reduzir contexto carregado sem reduzir suficiência. `UNTESTED`.
- **H2 — Context Precision:** pode aumentar Context Precision sem comprometer Context Recall. `UNTESTED`.
- **H3 — Specification Adherence:** relevância + autoridade + freshness podem aumentar aderência à SPEC. `UNTESTED`.
- **H4 — Architectural Compliance:** Context Routing e conhecimento arquitetural podem reduzir violações de boundaries. `UNTESTED`.
- **H5 — Agentic Workflow:** workflow especializado pode detectar mais defeitos antes da validação final que single-agent. `UNTESTED`.
- **H6 — Cost:** redução de contexto pode reduzir tokens e custo quando métricas confiáveis existirem. `UNTESTED`.

Hipóteses não são evidência, conclusão ou promessa de resultado.

## Experimental Conditions

| Condição | Contexto | Workflow | Objetivo |
| --- | --- | --- | --- |
| A — BASELINE | Acesso amplo ao repositório; sem pacote otimizado | SINGLE_AGENT | Baseline sem roteamento especializado |
| B — ROUTED CONTEXT | Intent, Domain, Capability, Candidate Knowledge, Relevance, Authority, Freshness, Conflict Check e Context Package | SINGLE_AGENT | Isolar Context Routing |
| C — AGENTIC WORKFLOW | Mesma estratégia roteada de B | Planner → Implementer → Reviewer → Validator | Avaliar workflow especializado |

A pode navegar o repositório conforme necessário, respeitando SPEC e regras fundamentais, sem ser artificialmente prejudicada. Nenhuma condição usa Semantic Router implementado nesta etapa.

- **A vs B:** investiga principalmente Context Routing.
- **B vs C:** investiga principalmente workflow especializado.
- **A vs C:** compara o sistema completo; não atribui causalidade apenas ao workflow, pois duas variáveis mudam.

## Controlled Variables

Controlar, quando tecnicamente possível: SPEC, estado inicial, tarefa, critérios de aceite, dataset, modelo e versão, parâmetros, infraestrutura, limite de tempo, interação humana, ferramentas e política de acesso externo. Registrar qualquer diferença como possível confounder.

Todas as condições partem do mesmo `BASE_COMMIT` e registram `base_commit`, `condition`, `run_id`, `timestamp`, `model`, `model_version` e `tooling`. Não criar branches.

## Independent Variables

### IV1 — Context Strategy

`BROAD_REPOSITORY_ACCESS` e `ROUTED_CONTEXT`.

### IV2 — Workflow Strategy

`SINGLE_AGENT` e `SPECIALIZED_AGENTIC_WORKFLOW`.

Mapeamento: A = BROAD_REPOSITORY_ACCESS + SINGLE_AGENT; B = ROUTED_CONTEXT + SINGLE_AGENT; C = ROUTED_CONTEXT + SPECIALIZED_AGENTIC_WORKFLOW.

## Dependent Variables

- context files loaded; context bytes loaded; token usage quando disponível; elapsed time;
- acceptance criteria pass rate; test pass rate; specification violations;
- architecture violations; unsupported assumptions; human intervention count; rework count;
- para C: reviewer findings e validator failures.

## Metrics

### Context

- **Context Files Loaded:** quantidade de arquivos consultados.
- **Context Bytes Loaded:** bytes/caracteres aproximados, quando mensurável.
- **Input Tokens / Output Tokens / Total Tokens:** registrar somente valor confiável; total é a soma quando ambos estiverem disponíveis. Nunca estimar como token real.
- **Context Precision:** Relevant Context Loaded / Total Context Loaded; relevância será classificada posteriormente com critérios registrados.
- **Context Recall:** Required Relevant Context Loaded / Total Required Relevant Context; o denominador requer avaliação posterior e tem limitação subjetiva.
- **Context Authority Coverage:** Authoritative Required Sources Loaded / Total Authoritative Required Sources. `PROPOSED_METRIC`.
- **Stale Context Rate:** Outdated Sources Loaded / Total Sources Loaded. `PROPOSED_METRIC`.
- **Knowledge Conflict Rate:** Detected Knowledge Conflicts / Context Selection Operations. `PROPOSED_METRIC`.

### Functional Quality

- **Acceptance Criteria Pass Rate:** Acceptance Criteria Passed / Total Acceptance Criteria.
- **Test Pass Rate:** Tests Passed / Tests Executed, distinguindo testes do agente de testes independentes.
- **Specification Violations:** incompatibilidades com a SPEC aprovada, incluindo 422 em vez de 400, enumeração, paginação, janela temporal ou resultado vazio incorretos.
- **MISSING_REQUIRED_BEHAVIOR:** comportamento exigido pela SPEC que não foi implementado.

### Architecture

- **Architecture Violations:** por exemplo, Domain depender de FastAPI/SQLAlchemy, Use Case acessar banco diretamente ou Adapter conter regra central.
- **Dependency Direction Compliance:** `PASS` ou `FAIL`, ou equivalente definido depois.

### Security

Observar autenticação, ownership, não enumeração, ausência de secrets, logs sem dados sensíveis quando aplicável e validação conforme SPEC. Não criar security score arbitrário.

### Workflow, Time e Cost

- Registrar **Human Intervention Count** como `REQUIREMENT_HITL`, `ARCHITECTURE_HITL`, `KNOWLEDGE_CONFLICT_HITL` ou `EXECUTION_ASSISTANCE`, além de Agent Iterations, Reviewer Findings, Validator Failures e Rework Count.
- Registrar `start_time`, `end_time`, `elapsed_time`, `agent_time` e `human_time` quando mensuráveis; não fingir precisão.
- Custo só por fonte confiável: `input_tokens`, `output_tokens`, `total_tokens`, `estimated_cost`, `currency`, `pricing_source`; usar `NOT_AVAILABLE` se indisponível.

### Observational Categories

- **UNNECESSARY_COMPLEXITY:** abstrações, frameworks, patterns, infraestrutura ou generalizações não exigidas; quantidade de arquivos isoladamente não basta.
- **UNSUPPORTED_ASSUMPTION:** decisão sem suporte na SPEC, ADRs, conhecimento autoritativo ou decisão humana aplicável. Registrar `assumption`, `source_expected`, `source_found` e `impact`.

## Evaluation Strategy

Avaliar separadamente correctness, specification adherence, architecture adherence, maintainability, unnecessary complexity, security behavior e testability. Não usar score subjetivo agregado inicialmente.

Aplicar `PARTIAL_BLIND_EVALUATION` quando possível: testes e critérios objetivos devem ser executados sem depender da condição A/B/C. Nem toda avaliação será cega, pois estrutura e artefatos podem revelar a condição.

## Independent Evaluation Tests

`EVALUATION TESTS` serão preparados futuramente, sem serem fornecidos ao agente durante implementação. Eles verificam a SPEC independentemente dos testes do agente e reduzem o risco de autoavaliação. Não são escritos nesta etapa.

## Run Protocol

Uma unidade experimental é uma execução completa da mesma tarefa, a partir do mesmo estado inicial, sob uma condição experimental específica. Cada run tem ID único, como `A-RUN-001`, `B-RUN-001` ou `C-RUN-001`, e usa os templates deste protocolo.

O prompt principal será versionado como `TASK_PROMPT_VERSION`; tarefa e critérios não podem mudar entre condições. Planejar no mínimo 3 runs exploratórios por condição e preferencialmente 5. Esse número é pragmático e não implica poder estatístico para generalizações amplas. Alternar ou aleatorizar a ordem dos runs quando possível.

Registrar e evitar `CROSS_RUN_CONTAMINATION`: reutilização de implementação, resultados, dicas, contexto persistente ou vazamento de testes de avaliação.

## Human Intervention Policy

Intervir apenas quando o protocolo permitir, houver HITL obrigatório, bloqueio técnico externo ou interrupção de segurança. Registrar toda intervenção e não dar dicas diferentes entre condições.

## Stop Conditions

- **SUCCESS:** critérios obrigatórios satisfeitos.
- **AGENT_STOP:** agente declara conclusão.
- **TIME_LIMIT:** limite atingido.
- **BLOCKED:** dependência externa impede continuação.
- **HUMAN_ABORT:** interrupção humana justificada.

O resultado futuro é `SUCCESS`, `PARTIAL`, `FAILURE` ou `BLOCKED`, definido por critérios objetivos, não apenas autodeclaração.

## Analysis Plan

Estudo exploratório: reportar valores individuais, média quando apropriada, mediana, mínimo, máximo, dispersão e comparações descritivas. Reportar diferenças absolutas e relativas sem calculá-las nesta etapa. Uma observação de um run é `RUN-SPECIFIC OBSERVATION`; não gerar percentuais promocionais ou inferência forte.

## Threats to Validity

- **Internal Validity:** diferenças de prompt, ferramentas, intervenção humana, contexto persistente e estado inicial.
- **External Validity:** uma feature, um domínio, possível modelo único, repositório pequeno e laboratório.
- **Construct Validity:** qualidade e relevância subjetivas, proxies de unsupported assumption e tokens indisponíveis.
- **Conclusion Validity:** poucas repetições, variabilidade e caráter exploratório.

## Exclusion Criteria

Critérios pré-definidos: `INFRASTRUCTURE_FAILURE`, `WRONG_BASE_COMMIT`, `WRONG_MODEL_CONFIGURATION`, `EVALUATION_TEST_LEAK` e `PROTOCOL_VIOLATION`. `BAD_RESULT` não é critério de exclusão. Toda exclusão deve ser registrada.

## Reporting Rules

Cada resultado futuro indica `condition`, `run_id`, `model`, `base_commit` e `task_prompt_version`. Afirmações devem distinguir `OBSERVED`, `INFERRED` e `UNTESTED`. Resultados negativos devem ser preservados.
