# EVAL-001 — Contrato de Avaliação da SPEC-001

Status: DESIGNED

## Fontes autoritativas

- SPEC-001 aprovada: comportamento de produto, critérios de aceite e segurança específica.
- ADR-003 aceito: Arquitetura Hexagonal e direção de dependências.
- ADR-007 aceito: Specification aprovada como gate antes de implementação.
- ADR-009 aceito: autoridade por tipo de conhecimento e tratamento de conflitos.
- Constitution e guardrails operacionais: validação de entrada, menor privilégio, ausência de secrets e logs sem dados sensíveis.

Este contrato não depende da implementação produzida pelo agente.

## FUNCTIONAL

- Consulta autorizada retorna `200 OK` com somente os campos públicos `id`, `timestamp`, `amount`, `currency`, `type` e `description`.
- A autenticação usa Bearer token opaco no laboratório.
- A autorização verifica explicitamente ownership `Account → Customer`; autenticação não concede acesso por si só.
- Sem parâmetros de paginação, `offset=0` e `limit=20`; `limit` máximo é `100`.
- Sem filtro temporal, o intervalo é os últimos 30 dias em UTC.
- Datas futuras e `from > to` são inválidos.
- Conta válida e autorizada sem transações retorna `200 OK` com coleção vazia.
- Conta inexistente e conta sem ownership possuem comportamento externo indistinguível; ambas retornam `404 Not Found`.
- Parâmetros inválidos retornam `400 Bad Request` com estrutura de erro padronizada; `422` não é contrato público para esses casos.

## SPECIFICATION_ADHERENCE

- Cada critério de aceite CA-001 a CA-007 deve ser avaliado independentemente.
- Comportamento observável incompatível com a SPEC é registrado como `SPECIFICATION_VIOLATION`.
- Comportamento exigido não implementado é registrado como `MISSING_REQUIRED_BEHAVIOR`.

## ARCHITECTURE

- O fluxo deve preservar Inbound Adapter → Input Port → Use Case → Output Port → Persistence Adapter.
- Domain não depende de FastAPI nem de mecanismo de persistência.
- Use Case não acessa banco diretamente.
- Adapters não redefinem regras centrais de negócio.

## SECURITY

- Autenticação, ownership, não enumeração e validação de entrada devem ser respeitados.
- Não pode haver secrets hardcoded.
- Token Bearer não pode ser registrado em logs.
- Não expor informação desnecessária sobre existência da conta.

## TESTABILITY

- A implementação deve permitir verificar critérios funcionais, falhas, validação, ownership e boundaries sem depender de comportamento não especificado.
- Testes produzidos pelo agente são distintos de `EVALUATION TESTS` independentes.

## UNSUPPORTED_ASSUMPTIONS

Registrar uma decisão sem suporte na SPEC, ADRs aplicáveis, guardrails ou decisão humana como `UNSUPPORTED_ASSUMPTION`, com `assumption`, `source_expected`, `source_found` e `impact`.

## UNNECESSARY_COMPLEXITY

Registrar abstrações, frameworks, patterns, infraestrutura ou generalizações não exigidas. Quantidade de arquivos isoladamente não caracteriza complexidade desnecessária.

## Evaluation Test Secrecy

EVALUATION_TEST_VISIBILITY: HIDDEN_FROM_IMPLEMENTATION_AGENT

Os evaluation tests futuros não devem ser fornecidos ao agente implementador, nem seu conteúdo deve constar no TASK-PROMPT.
