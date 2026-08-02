# Domain Context Candidate: Transaction

Status: DRAFT

Nome: Transaction (Transação)

Descrição curta:
Registro conceitual de uma operação financeira (crédito/débito) associada a uma Account; visível pelo titular conforme política de autorização.

Confirmado / Evidência:
- Transaction é referenciado como domínio de suporte na SPEC-001.

Conceitos confirmados:
- Identificador único (id) — conceitual; formato e exposição pendentes.
- Atributos principais (confirmados conceitualmente): timestamp, amount, currency, type, description — a exposição via API está pendente (Q-004).
- Ordenação por timestamp é presumida para consultas recentes (implementação e timezone pendentes).

Relações mínimas confirmadas:
- Transaction -> Account (pertence a uma conta)

Por que este contexto é necessário para esta feature:
- A funcionalidade solicita listagem de transações; o domínio Transaction contém os elementos conceituais que serão mapeados para persistência e para o contrato de API.

O que NÃO incluir neste candidato (por decisão DRAFT):
- Esquemas de persistência (colunas, índices) e detalhes de confidencialidade de cada campo.
- Políticas de retenção ou cálculos de saldo (balance_after) sem decisão humana.

Relevância para SPEC-001: HIGH
