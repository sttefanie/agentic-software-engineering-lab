# SPEC-001 — Consulta de transações recentes

Status: WAITING_HUMAN_INPUT

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
ambiguities:
  - "Mecanismo de autenticação (ex.: JWT, OAuth2, session) não definido"
  - "Estratégia de paginação (cursor vs offset) e tamanho padrão não definidos"
  - "Intervalo temporal padrão quando nenhum filtro é informado (ex.: últimos 30 dias) não definido"
  - "Campos do recurso Transaction a expor na API não definidos"
  - "Comportamento para contas sem transações (200 lista vazia vs 204) não definido"

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
- Authentication: REQUIRED — é necessário identificar o usuário (mecanismo não definido).
- Authorization: REQUIRED — garantir que o usuário só acesse suas próprias contas/transações.
- Validation: REQUIRED — validar parâmetros de consulta (datas, paginação, filtros).
- Observability: REQUIRED — registrar métricas de sucesso/erro/latência e contagem de resultados (sem dados sensíveis).
- Security: REQUIRED — proteger exposição de dados, evitar enumeração de contas.
- Testing: POSSIBLY_REQUIRED — unitário e integração para casos de sucesso e falhas.

Justificativas sucintas estão mantidas nos itens acima.

## Requisitos funcionais confirmados

- RF-001: O sistema deve permitir que um cliente consulte transações recentes associadas à(s) sua(s) conta(s).

(Nota: o escopo temporal, paginação, filtros e formato de resposta NÃO estão definidos e são exigências em aberto.)

## Requisitos não funcionais confirmados

- RNF-001: A operação deve ser tratada como leitura (sem efeito sobre estado) e otimizada para baixa latência.
- RNF-002: Nenhuma informação sensível (por exemplo, PAN completo) deve ser logada em texto claro.

## Critérios de aceite confirmados

### Confirmados
- CA-001: Um cliente autenticado consegue receber uma lista de transações (estrutura e campos exatos pendentes).

### Pendentes
- CA-002: Definir paginação (cursor vs. offset) e tamanho padrão da página.
- CA-003: Definir intervalo temporal padrão retornado (por ex., 30 dias) ou parâmetro obrigatório.
- CA-004: Definir comportamento quando não houver transações (resposta vazia vs. 204).

## Cenário feliz (Happy Path)

1. Cliente autenticado faz requisição GET ao endpoint de transações recentes para uma conta que lhe pertence.
2. Sistema valida autenticação e autorização (conta pertence ao cliente).
3. Sistema valida parâmetros de consulta (datas, paginação, filtros).
4. Use case consulta o repositório de transações via Output Port.
5. Adapter de persistência retorna transações ordenadas por data decrescente.
6. Sistema devolve resposta paginada com metadados (p.ex., total estimado, cursor/página).

## Cenários de falha

- Usuário não autenticado: requisição rejeitada (detalhes do mecanismo de autenticação OPEN_QUESTION).
- Usuário autenticado mas não autorizado para a conta: retorno de erro de autorização.
- Conta inexistente: retornar indicação de recurso não encontrado ou erro de autorização (policy-dependent).
- Parâmetros inválidos (ex.: formato de data incorreto): validação e erro apropriado.
- Falha de persistência: retorno de erro 5xx com observabilidade para investigação.
- Resultado vazio: resposta válida com lista vazia (ou 204 — decisão pendente).

## Casos de borda

- Conta sem transações: RECOMMENDED_FOR_DISCUSSION — decidir resposta padrão.
- Grande volume de transações: RECOMMENDED_FOR_DISCUSSION — exigir paginação e limites.
- Paginação e ordenação: REQUIRED to decide paging strategy (OPEN_QUESTION).
- Intervalo temporal/Timezone: OPEN_QUESTION — definir padrão (UTC?) e comportamento.
- Transações com mesmo timestamp: OUT_OF_SCOPE_CANDIDATE — tratar ordenação secundária é detalhe de implementação.
- Parâmetros extremos (datas no futuro): OPEN_QUESTION — validar e rejeitar/excluir.

Classificações acima indicam se devem ser tratadas antes da implementação.

## Segurança

- AUTENTICAÇÃO: OPEN_QUESTION — mecanismo de autenticação não definido no projeto. Esta SPEC NÃO assume JWT, OAuth2 ou outro.
- AUTORIZAÇÃO: REQUIRED — garantir isolamento de dados por cliente; evitar enumeração de contas (por ex., não revelar existência de conta por mensagem de erro distinta).
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
- Mecanismo de autenticação (ex.: JWT, session cookie)
- Estratégia de paginação (cursor vs offset) e tamanho de página padrão
- Intervalo temporal padrão (ex.: últimos 30 dias) ou se data_range é obrigatório
- Formato e extensão do recurso de transação (quais campos expor)

Por que cada item é necessário
- Autenticação/Autorização: imprescindível para segurança e isolamento de dados.
- Paginação/Intervalo: necessário para performance e UX; sem isso, a API pode retornar volumes excessivos.
- Campos do recurso: necessários para que front-end/aplicação consumidor decida se a informação é útil.

## Suposições não confirmadas

- ASSUMP-001: O usuário deseja consultar transações somente da(s) conta(s) que ele próprio possui — plausível, mas precisa confirmação.
- ASSUMP-002: A resposta será paginada — recomendação técnica, mas precisa decisão humana sobre tipo de paginação.

## Questões em aberto (resumo)

- Q-001: Qual mecanismo de autenticação e identidade o projeto usará? (impacta headers, tokens, fluxo de autorização)
- Q-002: Qual estratégia de paginação adotar (cursor vs offset) e qual o tamanho padrão da página?
- Q-003: Qual é o intervalo temporal padrão retornado quando nenhum filtro é informado (ex.: últimos 30 dias)? É obrigatório informar filtro temporal?
- Q-004: Quais campos de Transaction devem ser expostos na API (ex.: id, amount, currency, type, description, merchant, timestamp, balance_after)?
- Q-005: Como tratar contas sem transações (lista vazia vs. 204)?
- Q-006: Qual política de ordenação (timestamp desc)? Como tratar timezone?

## Decisões humanas necessárias

Q-001

Pergunta: Qual mecanismo de autenticação e identidade será adotado para a API (ex.: JWT bearer tokens, OAuth2, sessão cookie, outro)?

Por que precisamos dessa decisão: Determina formato de cabeçalhos, fluxo de validação e integração com o componente de identidade/authorization.

Impacto: Alto — afeta inbound adapter, middleware e exemplos de chamadas.

Opções possíveis:
- JWT Bearer tokens
- OAuth2 (authorization code / token)
- Session cookie com backend de sessão

Recomendação técnica: Preferir JWT/OAuth2 para APis públicas; documentar escopo/claims necessários.

Resposta: [PENDING]

Q-002

Pergunta: Qual estratégia de paginação adotar e qual o tamanho padrão de página?

Por que precisamos dessa decisão: Afeta contrato da API (parametrização), complexidade de implementação no persistence adapter e UX.

Impacto: Médio — influência em performance e consistência de resultados.

Opções possíveis:
- Offset + limit (mais simples)
- Cursor-based pagination (melhor para grandes volumes e consistência)

Recomendação técnica: Cursor é preferível para listas de transações grandes; se complexidade é uma preocupação, iniciar com offset e evoluir.

Resposta: [PENDING]

Q-003

Pergunta: Qual o intervalo temporal padrão quando nenhum filtro de data é fornecido?

Por que precisamos dessa decisão: Limita volume de dados retornados e define expectativas do usuário.

Impacto: Médio

Opções possíveis:
- Últimos 30 dias (padrão comum)
- Últimos 90 dias
- Sem padrão — exigir parâmetro (força o cliente a especificar)

Recomendação técnica: Usar 30 dias como padrão, mas confirmar com produto/regulatório.

Resposta: [PENDING]

Q-004

Pergunta: Quais campos do recurso Transaction devem ser expostos na API?

Por que precisamos dessa decisão: Evita exposição indevida e define o contrato de front-end.

Impacto: Alto

Opções possíveis:
- Campos mínimos: id, timestamp, amount, currency, type, description
- Campos estendidos: merchant, category, balance_after, status

Recomendação técnica: Começar com campos mínimos e adicionar campos estendidos por versionamento.

Resposta: [PENDING]

Q-005

Pergunta: Como tratar contas sem transações? Retornar lista vazia (200) ou 204 No Content?

Por que precisamos dessa decisão: Afeta front-end e critérios de aceite.

Impacto: Baixo

Opções possíveis:
- 200 OK com lista vazia
- 204 No Content

Recomendação técnica: 200 OK com lista vazia (menos ambíguo para clientes).

Resposta: [PENDING]

## Gap Analysis

Gap ID: GAP-001
Descrição: Mecanismo de autenticação não definido.
Categoria: SECURITY
Impacto: CRITICAL
Criticidade: CRITICAL
Pode prosseguir sem resposta humana?: NÃO
Opções conhecidas: JWT, OAuth2, Session
Recomendação técnica: Definir JWT/OAuth2 para APIs; documentar claims necessários.
Decisão humana necessária: SIM

Gap ID: GAP-002
Descrição: Estratégia de paginação e parâmetros (cursor vs offset, tamanho de página).
Categoria: API
Impacto: HIGH
Criticidade: HIGH
Pode prosseguir sem resposta humana?: NÃO
Opções conhecidas: Offset/limit, Cursor-based
Recomendação técnica: Preferir cursor; aceitar offset para MVP se houver restrição de tempo.
Decisão humana necessária: SIM

Gap ID: GAP-003
Descrição: Intervalo temporal padrão não definido.
Categoria: BUSINESS
Impacto: MEDIUM
Criticidade: MEDIUM
Pode prosseguir sem resposta humana?: NÃO
Opções conhecidas: 30 dias, 90 dias, obrigatório
Recomendação técnica: 30 dias como padrão; confirmar.
Decisão humana necessária: SIM

Gap ID: GAP-004
Descrição: Especificação dos campos de Transaction expostos.
Categoria: DATA
Impacto: HIGH
Criticidade: HIGH
Pode prosseguir sem resposta humana?: NÃO
Opções conhecidas: conjunto mínimo vs estendido
Recomendação técnica: definir conjunto mínimo e versionar para campos adicionais.
Decisão humana necessária: SIM

Gap ID: GAP-005
Descrição: Política de resposta para listas vazias (200 vs 204).
Categoria: API
Impacto: LOW
Criticidade: LOW
Pode prosseguir sem resposta humana?: SIM (mas alinhamento recomendável)
Opções conhecidas: 200 OK (lista vazia) recomendado.
Recomendação técnica: 200 OK com lista vazia.
Decisão humana necessária: NÃO (opcional)

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

## Histórico de decisões

(nenhuma decisão tomada localmente nesta SPEC — todas pendentes)

Decision ID: DEC-001
Date:
Question: Definição de autenticação para transações
Decision:
Decision Maker:
Impact:
Related Gap: GAP-001

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

## Fora de escopo

- Implementação de endpoint, models, migrations, testes ou qualquer código.
- Alteração de ADRs ou da constituição arquitetural atual.

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

1. Decidir mecanimos essenciais (Q-001 a Q-004) para remover bloqueios técnicos.
2. Com as decisões, completar a SPEC com contratos de API (parâmetros, exemplos, schemas) e critérios de aceite.
3. Planejar tasks para implementação respeitando a Arquitetura Hexagonal.
