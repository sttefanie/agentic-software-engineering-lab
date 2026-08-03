# SPEC-001 — Consulta de transações recentes

Status: APPROVED

## Problema

Como cliente de um banco digital, o usuário deseja consultar as transações recentes de sua conta para acompanhar movimentações financeiras. A solicitação inicial é vaga (não define escopo [...]

## Objetivo de negócio

Permitir que clientes verifiquem, de forma segura e eficiente, as movimentações recentes de suas contas para acompanhar saldos, detectar transações inesperadas e manter controle financeiro pes[...]

## Atores

- Cliente (usuário autenticado)
- Sistema (API do Digital Banking)
- Componentes de autenticação/identidade (externos ou internos)
- Adapter de persistência (banco de dados de transações)
- Observability/monitoring (por exemplo, registro de eventos de consulta)

## Intenção semântica

request_id: SPEC-001
intent: "Recuperar lista paginada de atividades financeiras recentes associadas à(s) conta(s) do cliente para visualização e auditoria pessoal"
operation: "read"
domain: "Account"
capabilities:
  API: REQUIRED
  Persistence: REQUIRED
  Authentication: REQUIRED
  Authorization: REQUIRED
  Validation: REQUIRED
  Observability: REQUIRED
  Security: REQUIRED
confidence: 0.85
ambiguities: []

Intenção: Recuperar uma lista paginada de atividades financeiras recentes associadas à conta(s) do cliente para fins de visualização e auditoria pessoal.

## Domínio principal

Account (conta)

## Domínios de suporte

- Transaction (transação) — REQUIRED
- Customer (cliente) — REQUIRED (para autorização e contexto do usuário)
- Transfer — POSSIBLY_REQUIRED (se for necessário agregar transações de transferência interna ou externa)

## Domínios desnecessários para esta SPEC

- Product (ex.: cartões de crédito com regras complexas) — NOT_REQUIRED (a menos que o cliente peça transações de cartão, o que é um caso específico)

## Capacidades necessárias

- API: REQUIRED — a funcionalidade expõe um endpoint de leitura.
- Persistence: REQUIRED — leitura de registros de transação no banco.
- Authentication: REQUIRED — identificar o usuário com Bearer token opaco no laboratório.
- Authorization: REQUIRED — garantir que o usuário só acesse suas próprias contas/transações.
- Validation: REQUIRED — validar parâmetros de consulta (datas, paginação, filtros).
- Observability: REQUIRED — registrar métricas de sucesso/erro/latência e contagem de resultados (sem dados sensíveis).
- Security: REQUIRED — proteger exposição de dados, evitar enumeração de contas.
- Testing: POSSIBLY_REQUIRED — unitário e integração para casos de sucesso e falhas.

Justificativas sucintas estão mantidas nos itens acima.

## Requisitos funcionais confirmados

- RF-001: O sistema deve permitir que um cliente consulte transações recentes associadas à(s) sua(s) conta(s).
- RF-002: A autenticação deve usar Bearer token opaco no laboratório; a identidade autenticada não concede, por si só, acesso à conta.
- RF-003: O sistema deve verificar explicitamente o ownership da conta pela relação `Account → Customer` autenticado antes de consultar dados.
- RF-004: A consulta deve usar paginação `offset/limit`, com `offset` padrão `0`, `limit` padrão `20` e `limit` máximo `100`.
- RF-005: Sem filtros temporais, a consulta deve considerar o intervalo de `now UTC - 30 dias` até `now UTC`.
- RF-006: A resposta deve expor somente `id`, `timestamp`, `amount`, `currency`, `type` e `description` para cada Transaction.
- RF-007: Para conta válida e autorizada sem transações no intervalo, o sistema deve retornar `200 OK` com coleção vazia.

## Requisitos não funcionais confirmados

- RNF-001: A operação deve ser tratada como leitura (sem efeito sobre estado) e otimizada para baixa latência.
- RNF-002: Nenhuma informação sensível (por exemplo, PAN completo) deve ser logada em texto claro.
- RNF-003: Datas devem ser interpretadas em UTC. Datas futuras e intervalos em que `from > to` são inválidos.
- RNF-004: Valores negativos de `offset`, `limit` inválido ou `limit` superior a `100` são inválidos.
- RNF-005: Parâmetros inválidos devem retornar `400 Bad Request` com estrutura de erro padronizada, sem adotar `422` como contrato público.

## Critérios de aceite confirmados

- CA-001: DADO um cliente autenticado e autorizado, QUANDO consultar uma conta própria, ENTÃO recebe `200 OK` com transações contendo exclusivamente os campos públicos aprovados.
- CA-002: DADO que `offset` e `limit` não são enviados, QUANDO a consulta é realizada, ENTÃO são usados `offset=0` e `limit=20`; `limit` não pode exceder `100`.
- CA-003: DADO que filtros temporais não são enviados, QUANDO a consulta é realizada, ENTÃO o intervalo corresponde aos últimos 30 dias em UTC.
- CA-004: DADA uma conta válida e autorizada sem transações no intervalo, QUANDO a consulta é realizada, ENTÃO a resposta é `200 OK` com coleção vazia.
- CA-005: DADO um token ausente ou inválido, QUANDO a consulta é realizada, ENTÃO a requisição é rejeitada sem acesso aos dados da conta.
- CA-006: DADO um cliente sem ownership da conta, ou uma conta inexistente, QUANDO a consulta é realizada, ENTÃO a resposta externa é `404 Not Found` e não revela a existência da conta.
- CA-007: DADO um parâmetro inválido, data futura, `from > to`, `offset` negativo ou `limit` fora do intervalo permitido, QUANDO a consulta é realizada, ENTÃO a resposta é `400 Bad Request` com erro padronizado.

## Cenário feliz (Happy Path)

1. Cliente autenticado faz requisição GET ao endpoint de transações recentes para uma conta que lhe pertence.
2. Sistema identifica o cliente pelo Bearer token opaco e verifica explicitamente o ownership da conta.
3. Sistema valida parâmetros de consulta: UTC, intervalo temporal, `offset` e `limit`.
4. Use case consulta o repositório de transações via Output Port.
5. Adapter de persistência retorna transações ordenadas por data decrescente.
6. Sistema devolve resposta `200 OK`, paginada por `offset/limit`, com os campos públicos aprovados.

## Cenários de falha

- Usuário não autenticado: requisição rejeitada sem acesso aos dados.
- Usuário autenticado mas não autorizado para a conta: `404 Not Found`, externamente indistinguível de conta inexistente.
- Conta inexistente: `404 Not Found`, sem revelar a existência do recurso.
- Parâmetros inválidos, datas futuras, `from > to`, `offset` negativo ou `limit` inválido: `400 Bad Request` com estrutura de erro padronizada.
- Falha de persistência: retorno de erro 5xx com observabilidade para investigação.
- Resultado vazio: `200 OK` com coleção vazia.

## Casos de borda

- Conta sem transações: `200 OK` com coleção vazia.
- Grande volume de transações: paginação `offset/limit`, com `limit` máximo `100`.
- Paginação e ordenação: `offset/limit`; ordenação por data decrescente.
- Intervalo temporal/Timezone: últimos 30 dias por padrão, em UTC.
- Transações com mesmo timestamp: OUT_OF_SCOPE_CANDIDATE — tratar ordenação secundária é detalhe de implementação.
- Parâmetros extremos (datas no futuro): inválidos; retornar `400 Bad Request`.

Classificações acima indicam se devem ser tratadas antes da implementação.

## Segurança

- AUTENTICAÇÃO: Bearer token opaco para o laboratório, sem JWT ou OAuth2.
- AUTORIZAÇÃO: verificação explícita de ownership `Account → Customer` autenticado; autenticação e autorização são responsabilidades distintas.
- ISOLAMENTO DE DADOS: REQUIRED — somente devolver transações pertencentes às contas autorizadas do cliente.
- VALIDAÇÃO DE ENTRADA: REQUIRED — validar todos os parâmetros de consulta.
- LOGGING: registrar eventos de consulta (sucesso/erro) sem dados sensíveis; mascarar identificadores sensíveis.

## Observabilidade

Sugerir pontos de instrumentação (não implementar):
- Métrica: consultas_transacoes_success (contador)
- Métrica: consultas_transacoes_error (contador) — por categoria (auth, validation, persistence)
- Métrica: consultas_transacoes_latency (histograma)
- Evento de auditoria: consulta_transacoes_executada (registrar actor_id, account_id(s), result_count, request_id) — sem incluir dados transacionais sensíveis

## Testabilidade

Categorias de teste necessárias:
- Unit tests para validação de parâmetros e regras de autorização.
- Use-case tests (integração leve) simulando output port.
- Adapter tests para persistência: leitura correta, ordenação e paginação.
- API tests: cenários de autenticação/autorization/validation.

## Dependências

- Adapter de persistência para transações (Output Port)
- Serviço/componente de autenticação/identity
- Observability/metrics adapter

## Restrições arquiteturais

- Respeitar a Arquitetura Hexagonal: o fluxo deve atravessar Inbound Adapter → Input Port → Use Case → Output Port → Persistence Adapter.
- Não acoplar Use Case a frameworks web ou banco de dados.

## Context Package Candidate

Context Package Candidate

Global Constraints
- Arquitetura Hexagonal definida no projeto — necessário para respeitar boundaries.
- Política de idioma: pt-BR para documentação.

Architecture Context
- Inbound Adapter esperado: HTTP API (FastAPI)
- Use Case será responsabilidade do domínio Account/Transaction
- Output Port: interface para leitura de transações

Domain Context
- Modelos conceituais: Account, Customer, Transaction (somente os conceitos; não criar entidades ainda)
- Regras de propriedade: conta pertence a um cliente; apenas o titular/autorizados podem visualizar

Capability Context
- Authentication/Authorization: identificar e autorizar o cliente
- Persistence (consulta de transações): filtros por data, ordenação, paginação
- Observability: métricas e eventos de auditoria

Specification Context
- Endpoint HTTP de leitura (GET) para "transações recentes" — contrato ainda indefinido em detalhes.

Skills
- Capacidade de validar formatos de data e paginação
- Capacidade de cumprir política de não exposição de dados sensíveis

Unknown / Missing Context
- Não há contexto crítico ausente para o escopo aprovado.

Por que cada item é necessário
- Autenticação/Autorização: imprescindível para segurança e isolamento de dados.
- Paginação/Intervalo: necessário para performance e UX; sem isso, a API pode retornar volumes excessivos.
- Campos do recurso: necessários para que front-end/aplicação consumidor decida se a informação é útil.

## Escopo

- Consultar transações recentes de uma conta por cliente autenticado e autorizado.
- Aplicar paginação `offset/limit` e filtro temporal opcional.

## Fora de escopo

- Implementação de endpoint, models, migrations, testes ou qualquer código.
- Integração com JWT, OAuth2 ou sessão.
- Inclusão de campos públicos além dos explicitamente aprovados.

## API Behavior

- A operação é uma leitura HTTP para transações recentes de uma conta.
- `offset` padrão é `0`; `limit` padrão é `20`; `limit` máximo é `100`.
- Sem filtros temporais, `from = now UTC - 30 dias` e `to = now UTC`.
- A resposta bem-sucedida é `200 OK` com coleção paginada de Transaction.
- Conta inexistente e conta sem autorização retornam externamente `404 Not Found`.
- Parâmetros inválidos retornam `400 Bad Request` com estrutura de erro padronizada.

## Domain Context

- Account pertence a Customer e é o contexto de ownership para a consulta.
- Transaction pertence a Account.
- O Primary Domain entre Account e Transaction permanece fora desta decisão; não bloqueia a Specification aprovada.

## Capabilities

- API, Persistence, Authentication, Authorization, Validation, Observability e Security são necessárias.
- Authentication identifica o ator; Authorization verifica ownership e permanece responsabilidade distinta.

## Business Rules

- Somente transações de conta cujo ownership seja confirmado para o Customer autenticado podem ser retornadas.
- Datas futuras e intervalos em que `from > to` são inválidos.
- A API não deve expor campos de Transaction além de `id`, `timestamp`, `amount`, `currency`, `type` e `description` sem nova decisão de produto.
- A resposta externa não deve revelar se uma conta inexistente existe ou se uma conta existente não está autorizada.

## Failure Scenarios

- Token ausente ou inválido: requisição rejeitada sem acesso aos dados.
- Conta inexistente ou sem ownership: `404 Not Found`.
- Data inválida, futura, intervalo inválido, `offset` negativo ou `limit` inválido: `400 Bad Request` com estrutura de erro padronizada.
- Falha de persistência ou dependência indisponível: erro 5xx observável, sem exposição de dados sensíveis.

## Test Scenarios

- Happy path para cliente autenticado e proprietário da conta.
- Resultado vazio para conta autorizada.
- Token ausente ou inválido.
- Conta inexistente e conta sem ownership com comportamento externo indistinguível.
- `offset/limit` padrão, máximo e inválido.
- Filtro temporal padrão, data futura e `from > to`.
- Falha de persistência ou dependência indisponível.

## Human Decisions

### DEC-SEC-001

Question: Como identificar o usuário e verificar o acesso à conta?

Decision: Bearer token opaco para o laboratório; autenticação identifica o usuário e autorização verifica explicitamente `Account → Customer` autenticado.

Rationale: Manter o laboratório simples, sem complexidade de JWT/OAuth, e preservar a separação entre autenticação e autorização.

Authority: HUMAN_PRODUCT_DECISION

Status: RESOLVED

### DEC-API-002

Question: Qual estratégia e valores de paginação usar?

Decision: `offset/limit`, com `offset=0`, `limit=20` e limite máximo `100`; valores negativos ou limite superior ao máximo são inválidos.

Rationale: Contrato simples, determinístico e suficiente para o primeiro experimento.

Authority: HUMAN_PRODUCT_DECISION

Status: RESOLVED

### DEC-PRODUCT-003

Question: Qual é a semântica temporal de transações recentes?

Decision: Últimos 30 dias em UTC quando filtros temporais estiverem ausentes; `from = now UTC - 30 dias` e `to = now UTC`. Datas futuras e `from > to` são inválidos.

Rationale: Comportamento determinístico e testável sem exigir parâmetros temporais em todas as chamadas.

Authority: HUMAN_PRODUCT_DECISION

Status: RESOLVED

### DEC-PRODUCT-004

Question: Quais campos de Transaction são públicos?

Decision: `id`, `timestamp`, `amount`, `currency`, `type` e `description`; não adicionar outros campos sem nova decisão de produto.

Rationale: Contrato mínimo suficiente, sem expansão desnecessária da exposição de dados.

Authority: HUMAN_PRODUCT_DECISION

Status: RESOLVED

### DEC-API-005

Question: Como responder para conta válida e autorizada sem transações?

Decision: `200 OK` com coleção vazia; não usar `204`.

Rationale: Manter a estrutura de resposta consistente independentemente da quantidade de resultados.

Authority: HUMAN_PRODUCT_DECISION

Status: RESOLVED

### DEC-SEC-006

Question: Como tratar externamente conta inexistente e conta não autorizada?

Decision: Ambas retornam `404 Not Found`, sem revelar se a conta existe.

Rationale: Evitar exposição desnecessária da existência de recursos e manter comportamento consistente.

Authority: HUMAN_PRODUCT_DECISION

Status: RESOLVED

### DEC-API-007

Question: Qual contrato usar para parâmetros inválidos?

Decision: `400 Bad Request` com estrutura de erro padronizada para datas inválidas ou futuras, `from > to`, `offset` negativo, `limit` inválido ou superior a `100`; não usar `422` como contrato público.

Rationale: Manter contrato explícito e uniforme, independentemente dos defaults do framework.

Authority: HUMAN_PRODUCT_DECISION

Status: RESOLVED

## Open Questions

Não há questões críticas abertas para o escopo desta Specification. A classificação de Primary Domain entre Account e Transaction permanece uma questão não crítica de governança de domínio e não altera o comportamento aprovado.

## Traceability

- DEC-SEC-001 → RF-002, RF-003, CA-005.
- DEC-API-002 → RF-004, CA-002.
- DEC-PRODUCT-003 → RF-005, RNF-003, CA-003.
- DEC-PRODUCT-004 → RF-006, CA-001.
- DEC-API-005 → RF-007, CA-004.
- DEC-SEC-006 → CA-006.
- DEC-API-007 → RNF-004, RNF-005, CA-007.

## Arquitetura (fluxo conceitual)

HTTP Request (Inbound Adapter - FastAPI)
    ↓
Request Validation (Adapter layer / DTO de entrada)
    ↓
Input Port (controller/handler delega ao Use Case)
    ↓
Use Case (RecuperarTransacoesRecentes)
    ↓
Output Port (interface de leitura de transações)
    ↓
Persistence Adapter (SQLAlchemy -> PostgreSQL)
    ↓
Database (tabela de transações)

Boundaries a respeitar:
- Use Case não deve acessar diretamente o DB; usar Output Port.
- Autorização deve ocorrer antes de acessar dados sensíveis.

## Contexto utilizado nesta análise

Arquivo: README.md
Motivo da consulta: Entender objetivo geral do laboratório e áreas de pesquisa
Relevância: HIGH

Arquivo: agents/README.md
Motivo da consulta: Confirmar responsabilidades dos agentes (Planner, Implementer, Reviewer, Validator)
Relevância: MEDIUM

Arquivo: evals/README.md
Motivo da consulta: Entender metodologia esperada para avaliações futuras (não implementadas)
Relevância: LOW

Arquivo: research/hypotheses.md
Motivo da consulta: Verificar hipóteses relacionadas a context routing e agentes
Relevância: MEDIUM

Arquivo: architecture/overview.md
Motivo da consulta: Confirmar arquitetura Hexagonal e restrições arquiteturais
Relevância: HIGH

Arquivo: architecture/boundaries.md
Motivo da consulta: Entender boundaries e políticas arquiteturais
Relevância: HIGH

Arquivo: architecture/patterns.md
Motivo da consulta: Padrões arquiteturais recomendados (ports & adapters)
Relevância: MEDIUM

Arquivo: architecture/stack.md
Motivo da consulta: Confirmar stack (Python, FastAPI, SQLAlchemy, etc.)
Relevância: HIGH

## Contexto considerado mas não carregado

Arquivo/Área: docs/ (completo)
Motivo para não carregar: Escopo desta análise restrito à SPEC; documentos de tutoriais e labs podem ser consultados posteriormente.

Arquivo/Área: specs/ (outros specs)
Motivo para não carregar: Esta é a primeira SPEC criada; revisar specs existentes se houver será etapa posterior.

## Snapshot de métricas (observacional)

Arquivos disponíveis: NOT_AVAILABLE
Arquivos consultados: 8
Arquivos modificados: 0
Input tokens: NOT_AVAILABLE
Output tokens: NOT_AVAILABLE
Total tokens: NOT_AVAILABLE
Tempo de execução: NOT_AVAILABLE

## Atualizar Context Taxonomy

(sem criação de arquivos automáticos) — candidatos iniciais DRAFT podem ser adicionados após decisões humanas.

## Validação final (checklist)

Solicitação analisada: YES
Semantic Intent identificado: YES
Domínio analisado: YES
Capabilities analisadas: YES
Context Package candidato criado: YES
Happy Path analisado: YES
Unhappy Paths analisados: YES
Edge Cases analisados: YES
Segurança analisada: YES
Observabilidade analisada: YES
Testabilidade analisada: YES
Gap Analysis realizada: YES
Human-in-the-Loop acionado se necessário: YES
SPEC-001 criada: YES

Código de negócio implementado: NO
Endpoint implementado: NO
Testes implementados: NO
Banco alterado: NO
Agentes implementados: NO
Experimento executado: NO
Resultado experimental inventado: NO

## Próximos passos recomendados (apenas orientação)

1. Planejar a implementação respeitando a Arquitetura Hexagonal e os requisitos aprovados.
2. Implementar e testar os comportamentos definidos nesta Specification em etapa posterior.
