# ADR-009 — Governança de Conhecimento e Autoridade das Fontes

**Data:** 2026-08-02

**Status:** ACCEPTED

## Contexto

O laboratório evoluiu por bootstrap estrutural, definição arquitetural, Spec-Driven Development (SDD), Human-in-the-Loop (HITL), auditorias de consistência e recuperação de artefatos `.agent/`. Nesse percurso, uma auditoria real identificou uma lacuna: o projeto não possui política explícita para determinar qual fonte pode decidir quando artefatos de contexto apresentam informações conflitantes.

Esta ADR propõe a governança mínima para conhecimento selecionado durante tarefas. Ela define conceitos e contratos futuros; não implementa roteador, parser, metadados, versionamento, agentes, métricas ou automação.

## Problema

Foi observado cenário equivalente a:

```text
ADR
Architecture = ACCEPTED

        VS

Architecture Documentation
Architecture = NOT DEFINED
```

Esse cenário evidencia que:

```text
CONTEXT AVAILABLE
≠
CONTEXT CONSISTENT

CONTEXT RELEVANT
≠
CONTEXT AUTHORITATIVE
```

Selecionar conteúdo semanticamente relevante não basta: o sistema também precisa conhecer a autoridade e o estado do conhecimento. Trata-se de um problema de consistência documental identificado no laboratório. Esta proposta não afirma reduzir alucinação, tokens, custo, nem melhorar qualidade, precisão ou produtividade; tais impactos exigem avaliação experimental.

## Decisão proposta

Adotar como princípio de governança que **a autoridade de uma fonte depende do tipo de conhecimento avaliado**. Não será usada uma hierarquia universal simples entre Constitution, ADR, SPEC e demais documentos, pois esses artefatos têm responsabilidades distintas.

Para cada afirmação relevante, a seleção futura deverá classificar o tipo de conhecimento, identificar a fonte autorizada a decidir, verificar a atualidade e detectar conflitos. A escolha do contexto privilegiará conteúdo relevante, suficiente, autoritativo e atual. Minimizar o volume de contexto é objetivo secundário à correção e à suficiência.

`priority != authority`: prioridade pode orientar relevância ou ordem de carregamento; autoridade indica a capacidade de decidir um tipo de conhecimento. Um arquivo muito relevante não pode, apenas por isso, sobrescrever outro.

De modo equivalente:

```text
semantic_similarity
        ≠
authority
```

Um documento semanticamente próximo pode estar desatualizado, em `DRAFT`, `SUPERSEDED` ou fora da autoridade necessária.

## Tipos de conhecimento

Os tipos iniciais são:

- **GOVERNANCE:** princípios globais, guardrails, regras de comportamento, políticas de workflow e restrições globais para agentes. Fontes candidatas: `.agent/constitution.md`, `.agent/guardrails.md` e `.agent/workflow.md`. A Constitution não decide automaticamente requisitos de produto ou regras específicas de domínio.
- **ARCHITECTURE:** linguagem, framework, estilo arquitetural, banco de dados, direção de dependências, limites e padrões. ADRs aceitos são a fonte de decisão; documentos em `architecture/` representam a visão operacional corrente.
- **PRODUCT:** comportamento de feature, requisitos funcionais e não funcionais específicos, critérios de aceite, decisões do Product Owner e contrato público de API. SPEC aprovada é a fonte de decisão. SPEC em `DRAFT` ou `WAITING_HUMAN_INPUT` não é definitiva para decisões pendentes.
- **DOMAIN:** conceitos de negócio, terminologia, invariantes confirmadas, relações entre entidades e regras de domínio confirmadas. A fonte são Domain Knowledge Objects, por exemplo em `context/domains/`. O agente não deve inventar regras não confirmadas.
- **CAPABILITY:** capacidades reutilizáveis, como API, persistência, autenticação, autorização, testes, observabilidade e leitura de transações. A fonte são Capability Knowledge Objects, por exemplo em `context/capabilities/`. Capabilities não definem silenciosamente requisitos de produto.
- **SECURITY:** regras de segurança que podem atravessar governança, arquitetura, produto ou objetos de segurança. Podem originar-se de Constitution, decisão arquitetural, SPEC aprovada ou Security Knowledge Object.
- **EXECUTION:** contexto da execução corrente: tarefa, plano, arquivos modificados, resultados temporários de ferramentas e informações fornecidas durante a execução. Não sobrescreve decisões persistentes de arquitetura, produto, domínio ou governança.
- **EXPERIMENTAL:** hipóteses, observações, experimentos, resultados exploratórios e métricas em `research/`, `evals/` e `metrics/`. Conteúdo experimental não se torna automaticamente regra arquitetural. Por exemplo, observar que cinco arquivos bastaram em uma execução não estabelece que sempre se devem carregar cinco arquivos.

O tema `Account × Transaction` permanece com **Status: OPEN**. Esta ADR não decide o Primary Domain da SPEC-001.

## Authority Matrix

| Tipo | Fonte de decisão | Representação operacional |
| --- | --- | --- |
| Governance | Constitution / Guardrails | `.agent/` |
| Architecture | Accepted ADR | `architecture/` |
| Product | Approved SPEC | `specs/` |
| Domain | Confirmed Domain Knowledge | `context/domains/` |
| Capability | Confirmed Capability Knowledge | `context/capabilities/` |
| Security | Fonte aplicável ao tipo e à regra de segurança | artefato de origem aplicável |
| Execution | Current Task Context | runtime/task |
| Experimental | Research artifacts | `research/`, `evals/`, `metrics/` |

Esta matriz é uma decisão de governança do projeto, não evidência científica.

## Source Authority

**Source Authority** é o artefato autorizado a decidir determinado tipo de conhecimento. Em arquitetura, por exemplo, um ADR com status `ACCEPTED` decide; na ocorrência de conflito com documentação operacional, a documentação deve ser marcada como potencialmente desatualizada.

O metadata `authority` declara o papel que se pretende atribuir à fonte, mas **não concede autoridade por si só**. A autoridade decorre da Authority Matrix, do tipo de conhecimento, da origem rastreável e, quando exigível, da aprovação registrada pela fonte competente. Um objeto não pode tornar-se autoritativo apenas por conter `authority: ...`.

Um Knowledge Object `ACTIVE` que funcione como fonte autoritativa deve ter origem (`provenance`) registrada e aprovação explícita, ou referência verificável à aprovação, pela autoridade definida para seu tipo. Sem esses elementos, o objeto pode ser contexto candidato, mas não deve decidir conflitos nem substituir uma fonte autoritativa.

Para segurança, não se deve escolher automaticamente a opção menos restritiva. Quando a autoridade não for determinística, o conflito deve ser registrado e encaminhado para decisão humana.

## Source of Truth

**Source of Truth** é o local em que o estado vigente daquele conhecimento deve estar registrado. Não é necessariamente igual à Source Authority.

```text
Accepted ADR
    ↓
SOURCE AUTHORITY para decisão arquitetural

architecture/boundaries.md
    ↓
CURRENT OPERATIONAL REPRESENTATION
```

Se divergirem, o documento operacional pode estar desatualizado. A identificação dessa divergência não autoriza sua modificação automática.

## Freshness

Contexto relevante deve também possuir noção de atualidade (freshness). O modelo futuro poderá adotar metadados como:

```yaml
version:
status:
last_reviewed:
```

O status mínimo proposto é:

- `DRAFT`: ainda não deve ser considerado autoridade definitiva.
- `ACTIVE`: conhecimento vigente.
- `DEPRECATED`: permanece por compatibilidade ou histórico, mas não deve ser preferido.
- `SUPERSEDED`: foi explicitamente substituído.

Esta ADR não exige inserir esses campos nos documentos existentes.

## Knowledge Object Contract

Propõe-se, para adoção futura, o contrato conceitual:

```yaml
id:
type:
domain:
capability:
summary:
applies_when:
dependencies:
priority:
version:
status:
authority:
provenance:
derived_from:
source_of_truth:
last_reviewed:
supersedes:
```

- `id`: identificador estável do objeto.
- `type`: categoria de conhecimento a que pertence.
- `domain`: domínio ao qual se aplica, quando aplicável.
- `capability`: capacidade reutilizável relacionada, quando aplicável.
- `summary`: resumo conciso do conteúdo.
- `applies_when`: condições em que o conhecimento deve ser aplicado.
- `dependencies`: conhecimentos ou condições dos quais depende.
- `priority`: relevância ou ordem de carregamento, sem expressar autoridade.
- `version`: versão identificável do conhecimento.
- `status`: estado de vigência (`DRAFT`, `ACTIVE`, `DEPRECATED` ou `SUPERSEDED`).
- `authority`: papel de autoridade declarado para a fonte; este campo não concede autoridade isoladamente.
- `provenance`: origem rastreável do conhecimento, incluindo artefato, decisão, evidência ou aprovação que o fundamenta.
- `derived_from`: identificadores ou referências dos conhecimentos de origem dos quais este objeto foi derivado.
- `source_of_truth`: local do registro vigente.
- `last_reviewed`: data da última revisão conhecida.
- `supersedes`: referência a conhecimento explicitamente substituído.

Exemplo conceitual:

```yaml
id: transaction-read
type: CAPABILITY
status: ACTIVE
authority: capability
provenance: aprovação registrada pela autoridade de capability
derived_from: context/capabilities/transactions_read-v0.md
source_of_truth: context/capabilities/transactions_read.md
version: 1
last_reviewed: YYYY-MM-DD
```

`supersedes` permitirá rastrear a relação entre versões, por exemplo, quando um Knowledge Object v2 substitui explicitamente o v1. Para atuar como fonte autoritativa, um objeto `ACTIVE` deverá ter `provenance` e aprovação registradas; `derived_from` deverá ser preenchido quando houver derivação de outra fonte. Não há migração de objetos nem implementação de versionamento nesta execução.

## Conflict Detection

Conflito é a situação em que duas fontes relevantes produzem afirmações incompatíveis sobre o mesmo tipo de conhecimento.

```text
REQUEST
   ↓
CONTEXT SELECTION
   ↓
RELEVANT SOURCES
   ↓
CONFLICT?
   │
   ├── NO → CONTINUE
   │
   └── YES
         ↓
     CLASSIFY KNOWLEDGE TYPE
         ↓
     CHECK AUTHORITY
```

## Deterministic Resolution

Quando o tipo de conhecimento estiver claro, existir fonte autoritativa definida e uma fonte for apenas desatualizada, a resolução conceitual poderá seguir:

```text
CONFLICT
↓
CLASSIFY TYPE
↓
IDENTIFY AUTHORITY
↓
USE AUTHORITATIVE SOURCE
↓
FLAG STALE SOURCE
↓
CONTINUE
```

Continuar a execução não significa modificar automaticamente o documento desatualizado.

## Human-in-the-Loop

O fluxo deve parar, documentar o conflito e solicitar intervenção humana quando o tipo for ambíguo, houver fontes de autoridade equivalente, não houver autoridade definida, ou a resolução alterar regra de negócio, segurança, contrato público ou exigir nova escolha arquitetural.

```text
CONFLICT
↓
CANNOT RESOLVE DETERMINISTICALLY
↓
STOP
↓
DOCUMENT CONFLICT
↓
HUMAN-IN-THE-LOOP
```

As categorias são distintas:

- `REQUIREMENT_HITL`: lacuna de requisito ou produto.
- `ARCHITECTURE_HITL`: nova decisão arquitetural necessária.
- `KNOWLEDGE_CONFLICT_HITL`: conflito entre fontes sem resolução determinística.

## Context Selection Model

O pipeline conceitual futuro é:

```text
REQUEST
   ↓
INTENT
   ↓
DOMAIN
   ↓
CAPABILITIES
   ↓
CANDIDATE KNOWLEDGE
   ↓
RELEVANCE FILTER
   ↓
AUTHORITY CHECK
   ↓
FRESHNESS CHECK
   ↓
CONFLICT CHECK
   ↓
CONTEXT PACKAGE
```

O Context Package deve buscar:

```text
RELEVANT
+
SUFFICIENT
+
AUTHORITATIVE
+
CURRENT
```

e não somente `SMALL`. Este ADR não implementa o pipeline.

## Métricas candidatas

Context Precision permanece candidata:

```text
Relevant Loaded Context
-----------------------
Total Loaded Context
```

Alta Context Precision não garante autoridade, atualidade, consistência ou Context Recall; portanto, ela não deve ser usada isoladamente como indicador de qualidade.

As métricas abaixo têm status `PROPOSED_METRIC` e não serão calculadas nesta execução:

- **Context Authority Coverage**

  ```text
  Authoritative Required Sources Loaded
  -------------------------------------
  Total Authoritative Required Sources
  ```

- **Stale Context Rate**

  ```text
  Outdated Sources Loaded
  -----------------------
  Total Sources Loaded
  ```

- **Knowledge Conflict Rate**

  ```text
  Detected Knowledge Conflicts
  ----------------------------
  Context Selection Operations
  ```

## Alternativas consideradas

### Alternative A — Universal hierarchy

Uma hierarquia única para todos os documentos é simples de explicar e executar, porém mistura responsabilidades: uma fonte de governança poderia indevidamente decidir produto ou domínio. Foi rejeitada como modelo geral.

### Alternative B — Authority by knowledge type

Autoridade definida por tipo de conhecimento preserva as responsabilidades dos artefatos e permite tratar divergências por contexto. É a alternativa proposta, com o custo de classificação e manutenção de regras explícitas.

### Alternative C — Timestamp-only

O documento mais recente vence. Atualidade isolada não implica autoridade: um artefato recente pode ser rascunho, observação experimental ou representação operacional sem poder de decisão. Foi rejeitada como regra de resolução.

### Alternative D — Semantic relevance only

O documento semanticamente mais próximo vence. Relevância não garante correção, vigência ou autoridade. Foi rejeitada como regra suficiente.

## Benefícios esperados

Espera-se estabelecer rastreabilidade explícita entre tipo de conhecimento, fonte autorizada, representação operacional e conflitos. Esses benefícios são objetivos de governança, não resultados empíricos sobre desempenho de agentes, custo ou qualidade.

## Trade-offs

```text
LESS GOVERNANCE
    ↓
simpler
cheaper
less maintenance

BUT

higher ambiguity
higher drift risk

VERSUS

MORE GOVERNANCE
    ↓
better traceability
explicit authority

BUT

higher complexity
more maintenance
```

O laboratório deverá investigar experimentalmente onde está o equilíbrio adequado.

## Riscos

- Aumento de complexidade e de metadados.
- Manutenção manual inconsistente.
- Knowledge Objects desatualizados ou com autoridade configurada incorretamente.
- Conflitos não detectados.
- Roteamento excessivamente rígido.
- Aumento do contexto devido às verificações.
- Falsa sensação de confiabilidade por haver governança declarada.

## Consequências

Futuras soluções de seleção de contexto deverão considerar tipo, autoridade, vigência e conflito, além de relevância. Documentos operacionais identificados como desatualizados deverão ser sinalizados, não alterados automaticamente. A adoção de metadados e automações dependerá de decisão posterior.

Esta ADR não altera `SPEC-001-consulta-transacoes-recentes.md`, que permanece `WAITING_HUMAN_INPUT`; não altera OBS-001, `.agent/constitution.md` nem Knowledge Objects.

## Limitações

Esta decisão não define algoritmo de classificação, parser de metadata, política completa de segurança, mecanismo de detecção, roteador semântico, versionamento ou medição. Também não resolve a escolha de domínio primário em `Account × Transaction`.

## Condições para revisão

- Revisão humana e possível aceitação desta ADR.
- Definição de autoridade para casos de segurança ainda ambíguos.
- Decisão sobre formato, manutenção e adoção gradual de metadados.
- Resultados de experimentos sobre métricas candidatas e custo operacional.
- Evidência de conflitos recorrentes, falsos positivos ou roteamento rígido demais.
