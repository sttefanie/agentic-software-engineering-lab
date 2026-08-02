# Runs experimentais

Este diretório é reservado para runs futuros do EXP-001. Não contém resultados fictícios.

Convenção de identificação:

- `A-RUN-001`, `A-RUN-002`, ...: `BROAD_REPOSITORY_ACCESS` + `SINGLE_AGENT`.
- `B-RUN-001`, `B-RUN-002`, ...: `ROUTED_CONTEXT` + `SINGLE_AGENT`.
- `C-RUN-001`, `C-RUN-002`, ...: `ROUTED_CONTEXT` + `SPECIALIZED_AGENTIC_WORKFLOW`.

Cada run futuro deve conter seus próprios manifests e métricas, partir do `BASE_COMMIT` definido, usar workspace isolado ou estado equivalente reproduzível, não reutilizar implementação nem resultados de run anterior, não receber evaluation tests e registrar intervenções humanas, modelo e configuração quando disponíveis.

BASE_COMMIT: a27dfc4fa454ff030ab59da0c49b0bf9cf5c11c0

BASE_COMMIT_SOURCE: HUMAN_VERIFIED_GIT_OUTPUT
