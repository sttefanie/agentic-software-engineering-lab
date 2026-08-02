# Checklist de baseline run — Condition A

## Metadados do congelamento

- BASE_COMMIT: `a27dfc4fa454ff030ab59da0c49b0bf9cf5c11c0`
- BASE_COMMIT_SOURCE: `HUMAN_VERIFIED_GIT_OUTPUT`
- EXTERNAL_EXECUTION_BLOCKER: `git unavailable in agent environment`
- HUMAN_INTERVENTION_COUNT: `1`
- HUMAN_INTERVENTION_TYPE: `EXTERNAL_EXECUTION_BLOCKER`
- token_budget: `NOT_ENFORCED`
- time_budget: `NOT_DEFINED`
- model_name/model_version/model_configuration: `NOT_EXPOSED` quando a plataforma não expuser os valores.

## Limitação de observabilidade de contexto

`FILES_ACCESSED` não equivale a `TOKENS_ACTUALLY_ATTENDED`. Um arquivo consultado não prova que todo o seu conteúdo influenciou a resposta do modelo.

## Condition A Contract

- Context Strategy: `BROAD_REPOSITORY_ACCESS`.
- Workflow: `SINGLE_AGENT`.
- Entrada: `TASK-PROMPT-001` versão `1.0.0` e acesso normal ao repositório.
- O agente pode navegar os arquivos conforme julgar necessário.
- Não fornecer manualmente context package, semantic routing, lista de arquivos recomendados, manifest pré-selecionado ou Planner/Reviewer/Validator separados.
- A baseline é justa: mantém acesso ao repositório, SPEC, ADRs, instruções e ferramentas permitidas.

Condition B será `ROUTED_CONTEXT + SINGLE_AGENT`; Condition C será `ROUTED_CONTEXT + SPECIALIZED_AGENTIC_WORKFLOW`. Nenhuma das duas está implementada nesta etapa.

## Antes do run futuro

- [ ] Working state corresponde ao BASE_COMMIT.
- [ ] TASK-PROMPT versão `1.0.0` confirmada.
- [ ] Metadados do modelo e ferramentas registrados.
- [ ] Evaluation tests permanecem ocultos.
- [ ] Não existe implementação de run anterior.
- [ ] Nenhum pacote manual de contexto foi fornecido.
- [ ] Run manifest foi inicializado.
- [ ] Start time foi registrado.

## Após o run futuro

- [ ] End time registrado.
- [ ] Files accessed registrados quando observáveis.
- [ ] Intervenções humanas registradas.
- [ ] Implementação congelada.
- [ ] Avaliação executada independentemente.
- [ ] Métricas registradas.
- [ ] Resultado classificado.

## Métricas futuras

Para cada métrica, registrar quando aplicável: `value`, `unit`, `measurement_method`, `source` e `confidence`. Não preencher valores nesta etapa.

## Política de intervenção humana

São permitidas somente `REQUIREMENT_HITL`, `ARCHITECTURE_HITL`, `KNOWLEDGE_CONFLICT_HITL` e `EXTERNAL_EXECUTION_BLOCKER`. Toda intervenção deve ser registrada e não pode introduzir dicas específicas de implementação entre condições.
