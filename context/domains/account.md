# Domain Context Candidate: Account

Status: DRAFT

Nome: Account (Conta)

Descrição curta:
Entidade conceitual que representa uma conta bancária pertencente a um cliente; unidade sobre a qual transações são registradas e consultadas.

Confirmado / Evidência:
- Relevante para SPEC-001 (Consulta de transações recentes).
- Arquitetura do repositório e SPEC-001 mencionam Account como domínio principal.

Conceitos confirmados:
- Ownership: conta pertence a um Customer (titular).
- Escopo de leitura: transações associadas a uma Account são retornáveis via API de consulta.

Relações mínimas confirmadas:
- Account -> Customer (pertence a)
- Account -> Transaction (agrega)

Por que este contexto é necessário para esta feature:
- A API de "transações recentes" é centrada na consulta de atividades vinculadas a uma(s) Account(s). A análise de autorização e isolamento de dados requer entendimento do conceito de conta.

O que NÃO incluir neste candidato (por decisão DRAFT):
- Modelos de banco de dados, campos detalhados ou migrations.
- Regras de negócio não confirmadas (ex.: contadores, overdraft handling).

Relevância para SPEC-001: HIGH
