# Desarrollo de soluciones basadas en modelos generativos para consultas normativas

En el contexto de una institución financiera, debes construir una solución que utilice modelos generativos para responder consultas sobre la normativa interna. La solución debe recuperar contexto relevante, generar una salida estructurada y ser medible en términos de precisión y latencia. Los actores involucrados son el 'usuario interno', el'motor de búsqueda normativa' y el'sistema de respuesta automatizada'. La solución debe manejar un volumen de 100 consultas por hora con una latencia máxima de 2 segundos por consulta.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Aplicaciones sobre modelos generativos |
| **Nivel** | senior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 2 semanas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Recuperación de contexto

**Objetivo:** Implementar un mecanismo para recuperar contexto relevante de la normativa interna en respuesta a una consulta.

**Tiempo estimado:** 3 días

**Instrucciones:**

- Identificar las fuentes de información normativa relevantes.
- Definir criterios para la recuperación de contexto.
- Implementar un prototipo que recupere y devuelva contexto relevante en respuesta a una consulta.

**Entregable:** Prototipo funcional que recupera y devuelve contexto relevante en respuesta a una consulta.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la estructura y el lenguaje de la normativa interna.
- Piensa en cómo podrías evaluar la relevancia del contexto recuperado.

</details>

### Fase 2: Generación de salida estructurada

**Objetivo:** Implementar un mecanismo para generar una salida estructurada en respuesta a una consulta, utilizando el contexto recuperado.

**Tiempo estimado:** 4 días

**Instrucciones:**

- Definir el formato de la salida estructurada.
- Implementar un prototipo que genere una salida estructurada en respuesta a una consulta, utilizando el contexto recuperado.

**Entregable:** Prototipo funcional que genera una salida estructurada en respuesta a una consulta, utilizando el contexto recuperado.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la estructura y el lenguaje de la normativa interna.
- Piensa en cómo podrías evaluar la calidad de la salida generada.

</details>

### Fase 3: Evaluación medible

**Objetivo:** Implementar un mecanismo para evaluar la solución en términos de precisión y latencia.

**Tiempo estimado:** 3 días

**Instrucciones:**

- Definir métricas para evaluar la precisión y la latencia de la solución.
- Implementar un prototipo que evalúe la solución en términos de precisión y latencia.

**Entregable:** Prototipo funcional que evalúa la solución en términos de precisión y latencia.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el volumen de consultas y la latencia máxima permitida.
- Piensa en cómo podrías mejorar la precisión y la latencia de la solución.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un modelo generativo y cómo se aplica en este contexto?
- **paraQueSirve**: ¿Para qué sirve la recuperación de contexto en este escenario?
- **comoSeUsa**: ¿Cómo se utiliza la salida estructurada generada por el modelo?
- **erroresComunes**: ¿Qué errores comunes podrían ocurrir en la generación de la salida estructurada y cómo los evitas?
- **queDecisionesImplica**: ¿Qué decisiones implica la evaluación de la solución en términos de precisión y latencia?

## Criterios de Evaluacion

- Implementación de un mecanismo para recuperar contexto relevante de la normativa interna en respuesta a una consulta.
- Implementación de un mecanismo para generar una salida estructurada en respuesta a una consulta, utilizando el contexto recuperado.
- Implementación de un mecanismo para evaluar la solución en términos de precisión y latencia.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && pytest -q
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
