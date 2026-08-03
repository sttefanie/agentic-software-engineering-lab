# OBS-001 — Auditoria de Consistência do Conhecimento

Status: EXPLORATORY

## Objetivo

Auditar a consistência, atualização, cobertura e governança do conhecimento presente no repositório, com foco em arquitetura, contexto, especificação e roteamento semântico, de forma a identificar riscos para agentes de IA ao selecionar e interpretar contexto.

## Escopo

Prioridade de leitura:
- .agent/constitution.md (ausente no repositório atual)
- architecture/overview.md
- architecture/stack.md
- architecture/patterns.md
- architecture/boundaries.md
- architecture/decisions/
- specs/SPEC-001-consulta-transacoes-recentes.md
- context/domains/
- context/capabilities/
- intents/intent-map.md

## Arquivos consultados

- [architecture/overview.md](../../architecture/overview.md)
- [architecture/stack.md](../../architecture/stack.md)
- [architecture/patterns.md](../../architecture/patterns.md)
- [architecture/boundaries.md](../../architecture/boundaries.md)
- [architecture/decisions/ADR-001-python.md](../../architecture/decisions/ADR-001-python.md)
- [architecture/decisions/ADR-002-fastapi.md](../../architecture/decisions/ADR-002-fastapi.md)
- [architecture/decisions/ADR-003-hexagonal-architecture.md](../../architecture/decisions/ADR-003-hexagonal-architecture.md)
- [architecture/decisions/ADR-004-postgresql.md](../../architecture/decisions/ADR-004-postgresql.md)
- [architecture/decisions/ADR-005-pytest.md](../../architecture/decisions/ADR-005-pytest.md)
- [architecture/decisions/ADR-006-vendor-neutral-agentic-layer.md](../../architecture/decisions/ADR-006-vendor-neutral-agentic-layer.md)
- [architecture/decisions/ADR-007-spec-driven-development.md](../../architecture/decisions/ADR-007-spec-driven-development.md)
- [architecture/decisions/ADR-008-semantic-context-routing-experiment.md](../../architecture/decisions/ADR-008-semantic-context-routing-experiment.md)
- [architecture/decisions/README.md](../../architecture/decisions/README.md)
- [specs/SPEC-001-consulta-transacoes-recentes.md](../../specs/SPEC-001-consulta-transacoes-recentes.md)
- [context/domains/account.md](../../context/domains/account.md)
- [context/domains/transaction.md](../../context/domains/transaction.md)
- [context/capabilities/transactions_read.md](../../context/capabilities/transactions_read.md)
- [intents/intent-map.md](../../intents/intent-map.md)
- [README.md](../../README.md)
- [research/hypotheses.md](../../research/hypotheses.md)

## Findings

### CONS-001

Título: Ausência de constitution explícita no repositório

Tipo: MISSING_SOURCE_OF_TRUTH

Fonte A: [architecture/decisions/ADR-003-hexagonal-architecture.md](../../architecture/decisions/ADR-003-hexagonal-architecture.md)

Afirmação A: A arquitetura depende de regras explícitas de dependência e disciplina.

Fonte B: Repositório atual

Afirmação B: Não existe arquivo .agent/constitution.md nem equivalente no workspace.

Descrição: O projeto referencia uma constitution como fonte importante de governança, mas o arquivo não está presente. Isso cria lacunas na autoridade e no rastreamento de guardrails.

Impacto potencial no agente: Alto. Agentes podem não receber uma fonte estável de regras arquiteturais e de governança.

Severidade: HIGH

Autoridade conhecida: Não explicitamente definida no repositório.

Correção determinística possível: Sim, criar ou restaurar o arquivo de constitution com conteúdo compatível com os ADRs aceitos, mas isso seria uma mudança de conteúdo e não uma simples sincronização.

Decisão humana necessária: Sim. Definir se a constitution deverá ser introduzida formalmente como fonte de autoridade.

Recomendação: Registrar a ausência como uma lacuna de governança e definir uma hierarquia de autoridade antes de expandir a documentação.

### CONS-002

Título: Drift entre ADR aceitos e documentação arquitetural corrente

Tipo: KNOWLEDGE_DRIFT

Fonte A: [architecture/decisions/ADR-003-hexagonal-architecture.md](../../architecture/decisions/ADR-003-hexagonal-architecture.md)

Afirmação A: Hexagonal Architecture foi adotada como estilo arquitetural aceito.

Fonte B: [architecture/overview.md](../../architecture/overview.md)

Afirmação B: O documento afirma que a arquitetura ainda não foi definida e que decisões não foram tomadas.

Descrição: A documentação corrente ainda descreve o estado bootstrap como se decisões arquiteturais não existissem, enquanto os ADRs já registram decisões aceitas.

Impacto potencial no agente: Médio/alto. Um agente pode receber instruções conflitantes sobre o estado atual da arquitetura.

Severidade: HIGH

Autoridade conhecida: ADRs aceitos, com precedência provável em relação à documentação de overview em estado bootstrap.

Correção determinística possível: Sim, mas somente como sincronização documental, sem criar novas decisões.

Decisão humana necessária: Sim, para confirmar se a overview deve refletir o estado atual dos ADRs aceitos.

Recomendação: Sincronizar a overview com os ADRs aceitos, sem alterar o conteúdo decisório.

### CONS-003

Título: Documentação de boundaries não reflete decisões arquiteturais aceitas

Tipo: KNOWLEDGE_DRIFT

Fonte A: [architecture/decisions/ADR-003-hexagonal-architecture.md](../../architecture/decisions/ADR-003-hexagonal-architecture.md)

Afirmação A: A arquitetura hexagonal exige fronteiras explícitas e dependências direcionadas para dentro.

Fonte B: [architecture/boundaries.md](../../architecture/boundaries.md)

Afirmação B: O documento afirma que as boundaries ainda não foram definidas.

Descrição: O documento de boundaries está em estado não definido, mesmo após a adoção explícita da arquitetura hexagonal. Isso reduz a utilidade do documento como guia operacional para agentes.

Impacto potencial no agente: Alto. O agente pode não ter clareza sobre como respeitar fronteiras arquiteturais.

Severidade: HIGH

Autoridade conhecida: ADR aceito, com provável precedência sobre o estado de bootstrap da documentação corrente.

Correção determinística possível: Sim, como atualização de documentação para refletir o estado já decidido.

Decisão humana necessária: Sim, para decidir o nível de detalhe das boundaries a registrar.

Recomendação: Transformar boundaries em um documento operável, ainda que mínimo, alinhado ao ADR-003.

### CONS-004

Título: Stack, patterns e overview ainda descrevem estado bootstrap

Tipo: INCOMPLETE

Fonte A: [architecture/decisions/ADR-001-python.md](../../architecture/decisions/ADR-001-python.md), [architecture/decisions/ADR-002-fastapi.md](../../architecture/decisions/ADR-002-fastapi.md), [architecture/decisions/ADR-004-postgresql.md](../../architecture/decisions/ADR-005-pytest.md)

Afirmação A: Existem decisões aceitas para linguagem, framework, banco e testes.

Fonte B: [architecture/stack.md](../../architecture/stack.md), [architecture/patterns.md](../../architecture/patterns.md), [architecture/overview.md](../../architecture/overview.md)

Afirmação B: Esses documentos ainda declaram que a stack, padrões e overview não foram definidos.

Descrição: A documentação corrente está incompleta em relação às decisões aceitas já documentadas em ADRs. Isso aumenta o risco de os agentes consumirem informação obsoleta ou incompleta.

Impacto potencial no agente: Médio/alto. O agente pode ignorar decisões aceitas e depender de documentos desatualizados.

Severidade: MEDIUM

Autoridade conhecida: ADRs aceitos.

Correção determinística possível: Sim, como sincronização documental.

Decisão humana necessária: Sim, para confirmar o grau de detalhe a ser incluído na documentação corrente.

Recomendação: Atualizar stack, patterns e overview para refletir as decisões aceitas, sem inventar novas decisões.

### CONS-005

Título: Classificação de domínio na SPEC-001 é ambígua

Tipo: AMBIGUOUS

Fonte A: [specs/SPEC-001-consulta-transacoes-recentes.md](../../specs/SPEC-001-consulta-transacoes-recentes.md)

Afirmação A: A SPEC identifica Account como domínio principal e Transaction como domínio de suporte.

Fonte B: [context/domains/transaction.md](../../context/domains/transaction.md)

Afirmação B: O domínio Transaction é descrito como de alta relevância para a feature e como o centro da capability de leitura.

Descrição: A correlação entre domínio principal e capability sugere que Transaction poderia ser interpretado como domínio principal da capability, enquanto Account continua relevante para ownership e autorização. A classificação atual não é totalmente estável para roteamento semântico.

Impacto potencial no agente: Médio. A seleção de contexto pode depender de uma interpretação diferente do domínio principal, afetando a composição do contexto.

Severidade: MEDIUM

Autoridade conhecida: A própria SPEC e os context candidates, mas sem regra explícita de precedência.

Correção determinística possível: Não de forma determinística; exige decisão de governança ou refinamento semântico.

Decisão humana necessária: Sim, para decidir se a classificação deve ser reforçada como Account-centric ou Transaction-centric.

Recomendação: Registrar a ambiguidade no modelo de routing e usar uma abordagem de múltiplos domínios quando necessário.

### CONS-006

Título: Capability de leitura mistura domínio, contrato HTTP e requisitos de arquitetura

Tipo: AMBIGUOUS

Fonte A: [context/capabilities/transactions_read.md](../../context/capabilities/transactions_read.md)

Afirmação A: A capability descreve responsabilidades, dependências e interface conceitual.

Fonte B: [specs/SPEC-001-consulta-transacoes-recentes.md](../../specs/SPEC-001-consulta-transacoes-recentes.md)

Afirmação B: A SPEC define requisitos e questões abertas, mas não estabelece o contrato HTTP final.

Descrição: O documento da capability inclui detalhes conceituais de API e arquitetura que podem ser interpretados tanto como conhecimento relevante da capability quanto como decisões que deveriam permanecer na SPEC ou nos ADRs. Há risco de mistura de camadas de conhecimento.

Impacto potencial no agente: Médio. O agente pode confundir regra de negócio, decisões de especificação e restrições arquiteturais.

Severidade: MEDIUM

Autoridade conhecida: Não explicitamente definida.

Correção determinística possível: Não completamente; exige refinamento editorial e de governança.

Decisão humana necessária: Sim, para decidir onde cada tipo de informação deve residir.

Recomendação: Separar claramente capability knowledge, specification requirements e architectural constraints.

### CONS-007

Título: O fluxo de roteamento semântico está documentado, mas não há governança de autoridade de conhecimento

Tipo: MISSING_SOURCE_OF_TRUTH

Fonte A: [intents/intent-map.md](../../intents/intent-map.md)

Afirmação A: O sistema de roteamento depende de intent, domain, capability, knowledge objects e context package.

Fonte B: Repositório atual

Afirmação B: Não há documento que defina autoridade, status, revisão, supersedência ou prioridade dos knowledge objects.

Descrição: O projeto está avançando em um modelo de context routing, mas a governança mínima para evitar consumo de informação conflitante ou obsoleta ainda não está formalizada.

Impacto potencial no agente: Alto. Em cenários de conflito, o agente pode não ter um critério claro para escolher a fonte correta.

Severidade: HIGH

Autoridade conhecida: Não definida.

Correção determinística possível: Não sem decisão de governança.

Decisão humana necessária: Sim. Definir se os knowledge objects precisarão de metadados de autoridade e ciclo de revisão.

Recomendação: Introduzir um modelo mínimo de metadados para knowledge objects e um mecanismo de resolução de conflito.

## Knowledge Drift

- [architecture/overview.md](../../architecture/overview.md) e [architecture/stack.md](../../architecture/stack.md) ainda descrevem o projeto como bootstrap, apesar de ADRs aceitos já existirem.
- [architecture/boundaries.md](../../architecture/boundaries.md) não reflete a adoção da arquitetura hexagonal registrada em [architecture/decisions/ADR-003-hexagonal-architecture.md](../../architecture/decisions/ADR-003-hexagonal-architecture.md).
- A documentação de contexto de domínio e capability está em estado DRAFT, o que é apropriado para contexto inicial, mas ainda não está integrada a uma governança clara de autoridade.

## Conflicts

Não foram identificados conflitos diretos entre duas fontes atuais que afirmem coisas incompatíveis de forma inequívoca. Os problemas principais são de drift, incompletude, ambiguidade e falta de autoridade.

## Ambiguities

- Classificação de Account vs. Transaction como domínio principal da feature.
- Separação entre knowledge de capability, requirements de SPEC e constraints arquiteturais.
- Uso de uma constitution formal como fonte de autoridade, sem o arquivo correspondente presente.

## Source of Truth Issues

- Não existe uma governança explícita de precedência entre Constitution, ADRs, architecture docs, specs, domain knowledge e capability knowledge.
- A ausência de uma constitution formal reforça a lacuna de autoridade.
- O repositório depende de convenções implícitas, o que é frágil para agentes automáticos.

## Domain Classification

Status: DOMAIN_CLASSIFICATION_AMBIGUOUS

Justificativa: A SPEC-001 é centrada em transações, mas a navegação por autorização, ownership e conta reforça Account como contexto de suporte. Não há uma regra explícita de governança para decidir qual domínio deve ser tratado como primary domain para o roteamento. A interpretação mais segura para o agente é tratar os dois como relevantes e não impor uma única classificação sem contexto adicional.

## Capability Analysis

- [context/capabilities/transactions_read.md](../../context/capabilities/transactions_read.md) é relevante e bem direcionado para a feature.
- Há risco de mistura de níveis de abstração: a capability inclui dependências conceituais, interface e arquitetura, mas não define claramente o limite entre capability knowledge e specification/architecture constraints.
- O documento não parece conter regra de negócio não confirmada de forma problemática, mas sua estrutura poderia ser melhorada para reduzir ambiguidades futuras.

## Context Overfetch

Files Available: NOT_AVAILABLE

Files Considered: NOT_AVAILABLE

Files Loaded: 19

Files Actually Relevant: 10

Files Potentially Unnecessary: 9

Context Precision = 10 / 19 = 0.53

EXPLORATORY_METRIC

Observação: A métrica é exploratória e não representa uma validação científica. O número de arquivos carregados foi maior do que o estritamente necessário para a análise, o que sugere um risco real de overfetch, embora não seja possível afirmar que isso tenha prejudicado a execução anterior sem dados adicionais.

## Knowledge Object Governance

Objetos existentes: o repositório contém documentos de domínio, capability e intent map, mas não há catálogo formal de knowledge objects com metadados estruturados.

Campos que poderiam ser derivados em um futuro objeto formal:
- id
- type
- domain
- capability
- summary
- applies_when
- dependencies
- priority
- version
- status

Campos adicionais recomendados para governança futura:
- authority
- source_of_truth
- last_reviewed
- supersedes

Status da necessidade: RECOMMENDED

Justificativa: Para um ambiente com roteamento semântico e múltiplas fontes, a ausência de metadados de governança aumenta o risco de agentes consumirem informação desatualizada ou conflitante.

## Human Decisions Required

### Decisões arquiteturais/de governança
- Definir se existe uma constitution formal e se ela deve ter autoridade explícita sobre os ADRs e a documentação corrente.
- Definir uma hierarquia de autoridade entre Constitution, ADRs aceitos, arquitectura corrente, specs, domain/capability knowledge e task context.
- Definir se a documentação corrente deve refletir os ADRs aceitos imediatamente ou se a sincronização deve ser gradual.

### Decisões da SPEC-001
- Não foram respondidas nesta auditoria; a auditoria respeitou o estado WAITING_HUMAN_INPUT da SPEC.

## Safe Synchronization Candidates

- [architecture/overview.md](../../architecture/overview.md): sincronizar com ADRs aceitos sem criar novas decisões.
- [architecture/stack.md](../../architecture/stack.md): refletir as decisões já aceitas em ADR-001, ADR-002, ADR-004 e ADR-005.
- [architecture/patterns.md](../../architecture/patterns.md): refletir a adoção de padrões já documentados em ADR-003 e ADR-008.
- [architecture/boundaries.md](../../architecture/boundaries.md): registrar as boundaries mínimas exigidas pela arquitetura hexagonal já aceita.

Classificação: SAFE_SYNC

## Knowledge Health

Consistency: MEDIUM

Completeness: MEDIUM

Authority Clarity: LOW

Freshness: MEDIUM

Duplication Risk: LOW

Context Routing Readiness: MEDIUM

## Limitações

- Não foi possível verificar a existência de uma constitution porque o arquivo não está presente no repositório atual.
- A análise foi restrita aos documentos relevantes para a auditoria solicitada e não à totalidade do repositório.
- Não foram executados experimentos nem implementações; a avaliação é exclusivamente documental.

## Conclusão

O repositório apresenta sinais claros de desgaste de governança e consistência de conhecimento. Os ADRs aceitos são relativamente claros, mas a documentação operacional e os artefatos de contexto ainda não refletem plenamente esse estado. O principal risco para agentes de IA é a ausência de uma fonte de verdade explícita e de uma governança mínima para knowledge objects, o que pode levar a interpretação inconsistente de contexto, especialmente em tarefas de routing e especificação.
