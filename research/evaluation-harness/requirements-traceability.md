# Rastreabilidade — EVAL-001 v1.0.0

| Evaluation ID | Fonte autoritativa | Método de avaliação |
| --- | --- | --- |
| EVAL-FUNC-001 | SPEC RF-001, CA-001 | Consulta autorizada e resposta `200 OK` |
| EVAL-FUNC-002 | SPEC RF-006, CA-001 | Campos públicos exatos da Transaction |
| EVAL-FUNC-003 | SPEC RF-007, CA-004 | Resultado vazio: `200 OK` e coleção vazia |
| EVAL-API-001 | SPEC RF-004, CA-002 | Defaults `offset=0`, `limit=20` e limite 100 |
| EVAL-API-002 | SPEC RNF-004, RNF-005, CA-007 | Paginação inválida retorna `400`, não `422` |
| EVAL-API-003 | SPEC RF-005, RNF-003, CA-003 | Janela padrão de 30 dias em UTC, com tempo controlado |
| EVAL-API-004 | SPEC RNF-003, RNF-005, CA-007 | Data futura e `from > to` retornam `400`, não `422` |
| EVAL-SEC-001 | SPEC RF-002, CA-005 | Bearer token ausente ou inválido é rejeitado |
| EVAL-SEC-002 | SPEC RF-003, CA-006 | Ownership Account → Customer é obrigatório |
| EVAL-SEC-003 | SPEC CA-006 | Conta inexistente e sem ownership retornam `404` indistinguível |
| EVAL-SEC-004 | EVAL-001 Security; Guardrails | Checagens simples de secrets e token em logs |
| EVAL-ARCH-001 | ADR-003; SPEC restrições arquiteturais | Domain sem FastAPI/persistência e Use Case sem acesso direto ao banco |
| EVAL-ARCH-002 | ADR-003; EVAL-001 Architecture | Fluxo Ports and Adapters e regra de negócio fora de adapters |

Nenhum check sem fonte autoritativa integra este harness.
