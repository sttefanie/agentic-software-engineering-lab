# EVAL-001 — Checklist de Avaliação da SPEC-001

Status: TEMPLATE — não executar nesta etapa.

## FUNCTIONAL

- [ ] Consulta autorizada retorna `200 OK` e somente os campos públicos aprovados.
- [ ] Bearer token opaco é exigido para identificação no laboratório.
- [ ] Ownership `Account → Customer` é verificado explicitamente.
- [ ] Ausência de paginação usa `offset=0` e `limit=20`.
- [ ] `limit` superior a `100` é inválido.
- [ ] Ausência de filtro temporal usa últimos 30 dias em UTC.
- [ ] Data futura e `from > to` são inválidos.
- [ ] Conta autorizada sem transações retorna `200 OK` com coleção vazia.
- [ ] Conta inexistente e não autorizada são externamente indistinguíveis e retornam `404`.
- [ ] Parâmetros inválidos retornam `400`, não `422`, nos casos definidos.

## ARCHITECTURE

- [ ] Fluxo Inbound Adapter → Input Port → Use Case → Output Port → Persistence Adapter preservado.
- [ ] Domain não depende de FastAPI ou persistência.
- [ ] Use Case não acessa banco diretamente.
- [ ] Adapters não contêm regras centrais de negócio.

## SECURITY

- [ ] Não há secrets hardcoded.
- [ ] Token Bearer não é registrado.
- [ ] Não há exposição indevida da existência da conta.
- [ ] Validação de entrada está alinhada à SPEC.

## QUALITY

- [ ] Violação de SPEC registrada quando observada.
- [ ] MISSING_REQUIRED_BEHAVIOR registrado quando aplicável.
- [ ] UNSUPPORTED_ASSUMPTION registrado quando aplicável.
- [ ] UNNECESSARY_COMPLEXITY registrado quando aplicável.
- [ ] Evaluation tests foram mantidos ocultos do agente implementador.
