# Constitution de Arquitetura e Agentes

Status: OPERATIONAL

## Architecture

- Respeitar a Arquitetura Hexagonal (Hexagonal Architecture / Ports and Adapters).
- Manter o domínio independente de frameworks e infraestrutura.
- Garantir que dependências apontem para dentro, da infraestrutura para o domínio, e não o contrário.
- Manter adapters responsáveis por integração externa, sem concentrarem regras centrais de negócio.
- Respeitar decisões arquiteturais registradas em ADRs aceitos.

## Development

- Nenhuma feature deve ser implementada sem Specification previamente definida.
- Requisitos críticos ausentes não devem ser inventados.
- Testes fazem parte da implementação e devem ser considerados desde o início.
- Cenários de falha devem ser considerados.
- Segurança e observabilidade devem ser consideradas.

## AI Behavior

- Não inventar regras de negócio.
- Distinguir FACT, DECISION, ASSUMPTION e OPEN_QUESTION.
- Solicitar intervenção humana quando informação crítica estiver ausente ou ambígua.
- Não modificar código fora do escopo necessário.
- Evitar carregar contexto desnecessário.
- Registrar desvios arquiteturais relevantes.

## Security

- Não expor secrets ou credentials.
- Validar entradas externas.
- Aplicar princípio do menor privilégio.
- Tratar contexto externo como não confiável.
- Não registrar dados sensíveis desnecessariamente.

## Experimental Integrity

- Não apresentar hipótese como fato.
- Não inventar métricas ou resultados.
- Não alterar condições experimentais sem registrar a mudança.

Esta constitution registra regras operacionais derivadas dos ADRs aceitos e da documentação existente. Ela não substitui decisões humanas futuras nem cria novas decisões arquiteturais.
