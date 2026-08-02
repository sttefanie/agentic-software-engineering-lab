# Human-in-the-Loop

Status: OPERATIONAL

## Fluxo

REQUEST
   ↓
ANALYZE
   ↓
CRITICAL INFORMATION MISSING?
   │
   ├── YES
   │     ↓
   │   STOP
   │     ↓
   │   DOCUMENT GAP
   │     ↓
   │   REQUEST HUMAN DECISION
   │     ↓
   │   UPDATE SPECIFICATION
   │
   └── NO
         ↓
       CONTINUE

## Informação crítica

A intervenção humana é necessária quando houver:

- regra de negócio ausente;
- requisito de segurança indefinido;
- autorização indefinida;
- comportamento financeiro ambíguo;
- requisito conflitante;
- mudança arquitetural relevante;
- operação potencialmente destrutiva.

Este fluxo não responde automaticamente às decisões humanas da SPEC-001; ele apenas registra a necessidade de decisão humana quando a informação crítica estiver ausente.
