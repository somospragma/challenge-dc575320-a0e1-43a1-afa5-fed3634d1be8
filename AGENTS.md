# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Desarrollo de soluciones basadas en modelos generativos para consultas normativas**.

| | |
|---|---|
| Tema | Aplicaciones sobre modelos generativos |
| Nivel | senior-l2 |
| Chapter | Ciencia de Datos — Ingeniero de IA |
| Especialidad | Ingeniero de IA |
| Stack | Python / FastAPI 0.115 |
| Patron arquitectonico | arquitectura basada en capas para RAG con evaluación automatizada |
| Tiempo estimado | 2 semanas |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `app/main.py con la API de inferencia`
- `app/prompts/ con los templates versionados`
- `app/retrieval con la indexacion y la busqueda vectorial`
- `app/chains con la orquestacion (cadena o grafo)`
- `app/eval con el conjunto de evaluacion y las metricas`
- `tests/ con casos deterministas de la cadena`

Dependencias:

- fastapi 0.115.0
- uvicorn 0.30.1
- pydantic 2.8.2
- langchain 0.2.5
- langchain-aws 0.1.6
- boto3 1.34.122
- numpy 1.26.4
- pandas 2.2.2
- pytest 8.2.0
- python-dotenv 1.0.1
- aws-cdk-lib 2.147.0
- terraform n/a

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && pytest -q` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && pytest -q` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Recuperación de contexto**: Prototipo funcional que recupera y devuelve contexto relevante en respuesta a una consulta.
- **Fase 2 — Generación de salida estructurada**: Prototipo funcional que genera una salida estructurada en respuesta a una consulta, utilizando el contexto recuperado.
- **Fase 3 — Evaluación medible**: Prototipo funcional que evalúa la solución en términos de precisión y latencia.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Lo que falta y tenes que completar

### 1. Referencias colgando (1)

Salieron de un analisis estatico del codigo que SI esta en el repo. Cada una rompe la compilacion:

- [ ] `app/schemas/query_schema.py` — `QueryMetadata.model_dump`
      Se invoca `model_dump` sobre `QueryMetadata`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

### Presentes (18)

- `requirements.txt`
- `app/main.py`
- `app/config/settings.py`
- `app/models/normative_response.py`
- `app/schemas/query_schema.py`
- `infra/terraform/variables.tf`
- `infra/terraform/main.tf`
- `app/prompts/normative_query_template.txt`
- `app/retrieval/context_retriever.py`
- `app/retrieval/vector_store.py`
- `app/chains/normative_chain.py`
- `app/eval/evaluation_metrics.py`
- `app/eval/evaluation_dataset.json`
- `app/config/aws_config.py`
- `tests/test_context_retrieval.py`
- `tests/test_chain_execution.py`
- `tests/test_evaluation_metrics.py`
- `README.md`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `app`
- `app/prompts`
- `app/retrieval`
- `app/chains`
- `app/eval`
- `app/models`
- `app/schemas`
- `app/config`
- `tests`
- `infra`

## Verificacion

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **arquitectura basada en capas para RAG con evaluación automatizada**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Ciencia de Datos, Especialidad Ingeniero de IA, Tecnología AWS Bedrock, Senior
- Brecha que el reto ataca: Construye soluciones sobre modelos generativos con recuperacion de contexto, salida estructurada y evaluacion medible
- Mision: Responder consultas sobre la normativa interna

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
