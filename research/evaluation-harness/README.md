# Independent Evaluation Harness — EVAL-001

EVALUATION_ID: EVAL-001

EVALUATION_VERSION: 1.0.0

EVALUATION_STATUS: FROZEN_BEFORE_RUNS

BASE_COMMIT: a27dfc4fa454ff030ab59da0c49b0bf9cf5c11c0

EVALUATION_TEST_VISIBILITY: HIDDEN_FROM_IMPLEMENTATION_AGENT

Este harness avalia implementações da SPEC-001 depois que cada run for congelado. Seus testes são independentes dos testes produzidos pelo agente e derivam somente da SPEC-001 aprovada, EVAL-001, ADRs aceitos aplicáveis e guardrails autorizados.

## Isolamento do workspace

```text
CANONICAL REPOSITORY
        |
        +---- evaluation harness
        |
        +---- experimental source
                  |
                  v
         ISOLATED RUN WORKSPACE
                  |
                  X evaluation harness excluded
                  |
                  v
         IMPLEMENTATION AGENT

ISOLATED RUN WORKSPACE
        |
        v
IMPLEMENTATION FREEZE
        |
        v
EXTERNAL EVALUATION HARNESS
        |
        v
RESULT
```

Antes de cada run, o workspace do agente deve ser criado sem `research/evaluation-harness/` e sem artefatos que revelem seus testes. Não basta instruir o agente a não ler a pasta.

## Adapter neutro

Os testes permanecem congelados e usam uma factory futura apontada por `EVALUATION_TARGET_FACTORY`, no formato `modulo:factory`. A factory deve retornar um alvo que permita organizar dados determinísticos, fixar o relógio de avaliação e fazer requisições HTTP conceituais. O adapter retorna uma resposta normalizada apenas para o harness (`status_code`, `items`, `offset`, `limit`); essa normalização não define nem impõe um formato público além do que a SPEC determina. Este adapter conecta o harness à implementação sem impor nomes de classes, funções, algoritmos ou estrutura interna.

Enquanto não houver implementação e adapter, os testes têm status operacional `NOT_EXECUTED` e não devem ser executados.

## Test data e tempo

Os dados são mínimos, sintéticos, pequenos, reproduzíveis e sem dados bancários ou pessoais reais. O instante de referência é fixo em `2026-01-31T12:00:00Z`; testes temporais não dependem de `datetime.now()` não controlado.

## Dependências

O harness usa apenas biblioteca padrão e pytest, selecionado no ADR-005. Nenhuma dependência foi adicionada ou instalada nesta etapa.
