# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `app/schemas/query_schema.py` — `QueryMetadata.model_dump`: Se invoca `model_dump` sobre `QueryMetadata`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

## Como saber que terminaste

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Ingeniero de IA, Tecnología AWS Bedrock, Senior

### Brecha de conocimiento
Construye soluciones sobre modelos generativos con recuperacion de contexto, salida estructurada y evaluacion medible

### Misión / candidato
Responder consultas sobre la normativa interna

### Datos adicionales
Candidato con 5 años en datos e IA

### Reto
- Tema: Aplicaciones sobre modelos generativos
- Seniority: senior-l2
- Tipo: practical
- Título: Desarrollo de soluciones basadas en modelos generativos para consultas normativas
- Tiempo estimado: 2 semanas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Recuperación de contexto — objetivo: Implementar un mecanismo para recuperar contexto relevante de la normativa interna en respuesta a una consulta. — entregable (NO resolver): Prototipo funcional que recupera y devuelve contexto relevante en respuesta a una consulta.
- Fase 2: Generación de salida estructurada — objetivo: Implementar un mecanismo para generar una salida estructurada en respuesta a una consulta, utilizando el contexto recuperado. — entregable (NO resolver): Prototipo funcional que genera una salida estructurada en respuesta a una consulta, utilizando el contexto recuperado.
- Fase 3: Evaluación medible — objetivo: Implementar un mecanismo para evaluar la solución en términos de precisión y latencia. — entregable (NO resolver): Prototipo funcional que evalúa la solución en términos de precisión y latencia.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: requirements.txt ===
fastapi==0.115.0
uvicorn==0.30.1
pydantic==2.8.2
langchain==0.2.5
langchain-aws==0.1.6
boto3==1.34.122
numpy==1.26.4
pandas==2.2.2
pytest==8.2.0
python-dotenv==1.0.1
aws-cdk-lib==2.147.0

// === ARCHIVO: app/main.py ===
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import logging
from app.config.settings import Settings
from app.chains.normative_chain import NormativeChain
from app.retrieval.context_retriever import ContextRetriever
from app.retrieval.vector_store import VectorStore
from app.eval.evaluation_metrics import EvaluationMetrics
import time
import os

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Normative Query Service", version="1.0.0")

# Inicialización de componentes
settings = Settings()
vector_store = VectorStore()
context_retriever = ContextRetriever(vector_store=vector_store)
normative_chain = NormativeChain(context_retriever=context_retriever)
evaluation_metrics = EvaluationMetrics()

class QueryRequest(BaseModel):
    question: str
    user_id: Optional[str] = None
    evaluate: Optional[bool] = False

class QueryResponse(BaseModel):
    answer: str
    context: List[str]
    latency_seconds: float
    evaluation_score: Optional[float] = None

@app.on_event("startup")
async def startup_event():
    logger.info("Initializing Normative Query Service")
    try:
        await vector_store.initialize()
        logger.info("Vector store initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize vector store: {str(e)}")
        raise

@app.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    start_time = time.time()

    if not request.question or len(request.question.strip()) == 0:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        # Recuperar contexto relevante
        context = await context_retriever.retrieve_context(request.question)

        # Generar respuesta estructurada
        answer = await normative_chain.generate_answer(
            question=request.question,
            context=context
        )

        # Calcular latencia
        latency = time.time() - start_time

        # Validar latencia contra configuración
        if latency > settings.max_latency_seconds:
            logger.warning(f"Latency exceeded threshold: {latency}s")

        response = QueryResponse(
            answer=answer,
            context=context,
            latency_seconds=latency
        )

        # Evaluar si está habilitado
        if request.evaluate:
            score = evaluation_metrics.calculate_precision(
                question=request.question,
                answer=answer,
                context=context
            )
            response.evaluation_score = score

        return response

    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        )

@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "healthy"})

// === ARCHIVO: app/config/settings.py ===
from pydantic import BaseSettings, Field
from typing import Optional
import os

class Settings(BaseSettings):
    # Configuración general de la aplicación
    app_name: str = "Normative Query Service"
    environment: str = Field(default="development", env="ENVIRONMENT")

    # Configuración de latencia y volumen
    max_latency_seconds: float = Field(default=2.0, env="MAX_LATENCY_SECONDS")
    max_queries_per_hour: int = Field(default=100, env="MAX_QUERIES_PER_HOUR")
    max_tokens_per_query: int = Field(default=1000, env="MAX_TOKENS_PER_QUERY")

    # Configuración de AWS Bedrock
    bedrock_model_id: str = Field(default="anthropic.claude-v2", env="BEDROCK_MODEL_ID")
    bedrock_region: str = Field(default="us-east-1", env="AWS_REGION")

    # Configuración de recuperación de contexto
    context_retrieval_top_k: int = Field(default=5, env="CONTEXT_RETRIEVAL_TOP_K")
    context_retrieval_threshold: float = Field(default=0.7, env="CONTEXT_RETRIEVAL_THRESHOLD")

    # Configuración de evaluación
    evaluation_dataset_path: str = Field(
        default="app/eval/evaluation_dataset.json",
        env="EVALUATION_DATASET_PATH"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Validaciones adicionales
        if self.max_latency_seconds <= 0:
            raise ValueError("max_latency_seconds must be positive")
        if self.max_queries_per_hour <= 0:
            raise ValueError("max_queries_per_hour must be positive")
        if self.max_tokens_per_query <= 0:
            raise ValueError("max_tokens_per_query must be positive")
        if not self.bedrock_model_id:
            raise ValueError("bedrock_model_id cannot be empty")
        if not self.bedrock_region:
            raise ValueError("bedrock_region cannot be empty")

// === ARCHIVO: app/models/normative_response.py ===
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from datetime import datetime
from enum import Enum

class NormativeSource(str, Enum):
    """Enumeración de posibles fuentes normativas."""
    REGULATION = "REGULATION"
    POLICY = "POLICY"
    PROCEDURE = "PROCEDURE"
    GUIDELINE = "GUIDELINE"
    LEGAL_FRAMEWORK = "LEGAL_FRAMEWORK"

class Reference(BaseModel):
    """Modelo que representa una referencia normativa específica."""
    document_id: str = Field(..., description="Identificador único del documento normativo")
    section: str = Field(..., description="Sección específica dentro del documento")
    paragraph: Optional[str] = Field(None, description="Párrafo específico dentro de la sección")
    source_type: NormativeSource = Field(..., description="Tipo de fuente normativa")
    last_updated: datetime = Field(..., description="Fecha de última actualización del documento")

    @validator('document_id')
    def validate_document_id(cls, v):
        if not v.strip():
            raise ValueError('document_id no puede estar vacío')
        return v

    @validator('section')
    def validate_section(cls, v):
        if not v.strip():
            raise ValueError('section no puede estar vacío')
        return v

class NormativeResponse(BaseModel):
    """Modelo para estructurar la respuesta generada por el modelo a consultas normativas."""
    query_id: str = Field(..., description="Identificador único de la consulta")
    response_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Identificador único de la respuesta")
    query_text: str = Field(..., description="Texto original de la consulta realizada")
    generated_response: str = Field(..., description="Respuesta generada por el modelo")
    references: List[Reference] = Field(default_factory=list, description="Listado de referencias normativas utilizadas")
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="Puntuación de confianza en la respuesta (0-1)")
    processing_time_ms: float = Field(..., ge=0, description="Tiempo de procesamiento en milisegundos")
    model_version: str = Field(..., description="Versión del modelo utilizado para generar la respuesta")
    timestamp: datetime = Field(default_factory=datetime.now, description="Momento en que se generó la respuesta")

    @validator('query_text')
    def validate_query_text(cls, v):
        if not v.strip():
            raise ValueError('query_text no puede estar vacío')
        if len(v) > 1000:
            raise ValueError('query_text no puede exceder 1000 caracteres')
        return v

    @validator('generated_response')
    def validate_generated_response(cls, v):
        if not v.strip():
            raise ValueError('generated_response no puede estar vacía')
        if len(v) > 2000:
            raise ValueError('generated_response no puede exceder 2000 caracteres')
        return v

    @validator('confidence_score')
    def validate_confidence_score(cls, v):
        if not (0.0 <= v <= 1.0):
            raise ValueError('confidence_score debe estar entre 0.0 y 1.0')
        return v

    def add_reference(self, document_id: str, section: str, source_type: NormativeSource,
                     last_updated: datetime, paragraph: Optional[str] = None) -> None:
        """Añade una referencia normativa a la respuesta."""
        self.references.append(
            Reference(
                document_id=document_id,
                section=section,
                paragraph=paragraph,
                source_type=source_type,
                last_updated=last_updated
            )
        )

    def to_dict(self) -> dict:
        """Convierte el modelo a un diccionario para serialización."""
        return self.model_dump()

import uuid

// === ARCHIVO: app/schemas/query_schema.py ===
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, validator, root_validator
from enum import Enum

class QueryType(str, Enum):
    """Enumeración de tipos de consultas soportadas."""
    DEFINITION = "DEFINITION"
    PROCEDURE = "PROCEDURE"
    COMPLIANCE = "COMPLIANCE"
    EXAMPLE = "EXAMPLE"
    COMPARISON = "COMPARISON"

class QueryMetadata(BaseModel):
    """Metadatos asociados a la consulta."""
    department: str = Field(..., description="Departamento que realiza la consulta")
    urgency_level: int = Field(..., ge=1, le=5, description="Nivel de urgencia (1-5)")
    requester_id: str = Field(..., description="Identificador del solicitante")
    related_topics: List[str] = Field(default_factory=list, description="Temas relacionados con la consulta")

    @validator('department')
    def validate_department(cls, v):
        if not v.strip():
            raise ValueError('department no puede estar vacío')
        return v

    @validator('requester_id')
    def validate_requester_id(cls, v):
        if not v.strip():
            raise ValueError('requester_id no puede estar vacío')
        return v

class QuerySchema(BaseModel):
    """Esquema para validar las consultas de entrada."""
    query_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Identificador único de la consulta")
    query_text: str = Field(..., min_length=10, max_length=1000, description="Texto de la consulta")
    query_type: QueryType = Field(..., description="Tipo de consulta")
    metadata: QueryMetadata = Field(..., description="Metadatos asociados a la consulta")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Parámetros adicionales para la consulta")
    max_tokens: int = Field(default=500, ge=50, le=2000, description="Máximo número de tokens para la respuesta")
    temperature: float = Field(default=0.3, ge=0.0, le=1.0, description="Temperatura para el sampling de la respuesta")
    top_k: int = Field(default=50, ge=1, le=100, description="Número de documentos a considerar para recuperación")

    @validator('query_text')
    def validate_query_text(cls, v):
        if not v.strip():
            raise ValueError('query_text no puede estar vacío')
        return v

    @root_validator
    def check_parameters_consistency(cls, values):
        query_type = values.get('query_type')
        parameters = values.get('parameters', {})

        required_params = {
            QueryType.DEFINITION: [],
            QueryType.PROCEDURE: ['context_scope'],
            QueryType.COMPLIANCE: ['regulation_id'],
            QueryType.EXAMPLE: ['example_type'],
            QueryType.COMPARISON: ['item_a', 'item_b']
        }

        if query_type in required_params:
            for param in required_params[query_type]:
                if param not in parameters:
                    raise ValueError(f'Parámetro requerido para {query_type}: {param}')

        return values

    def to_langchain_kwargs(self) -> dict:
        """Convierte el esquema a kwargs compatibles con LangChain."""
        return {
            "input": self.query_text,
            "metadata": self.metadata.model_dump(),
            "query_type": self.query_type.value,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "top_k": self.top_k
        }

    def update_parameters(self, **kwargs) -> None:
        """Actualiza los parámetros de la consulta."""
        self.parameters.update(kwargs)

import uuid

// === ARCHIVO: infra/terraform/variables.tf ===
variable "region" {
  description = "The AWS region to deploy the resources"
  type        = string
  default     = "us-east-1"
}

variable "lambda_function_name" {
  description = "The name of the Lambda function"
  type        = string
  default     = "normative-query-lambda"
}

variable "api_gateway_name" {
  description = "The name of the API Gateway"
  type        = string
  default     = "normative-query-api"
}

variable "stage_name" {
  description = "The stage name for the API Gateway"
  type        = string
  default     = "prod"
}

variable "lambda_memory_size" {
  description = "The amount of memory allocated to the Lambda function in MB"
  type        = number
  default     = 128
}

variable "lambda_timeout" {
  description = "The maximum execution time of the Lambda function in seconds"
  type        = number
  default     = 30
}

variable "lambda_role" {
  description = "The ARN of the IAM role that the Lambda function assumes"
  type        = string
}

variable "lambda_handler" {
  description = "The handler for the Lambda function"
  type        = string
  default     = "app.main.lambda_handler"
}

// === ARCHIVO: infra/terraform/main.tf ===
provider "aws" {
  region = var.region
}

resource "aws_lambda_function" "normative_query" {
  function_name = var.lambda_function_name
  role         = var.lambda_role
  handler      = var.lambda_handler
  runtime      = "python3.13"
  memory_size  = var.lambda_memory_size
  timeout      = var.lambda_timeout
  
  environment {
    variables = {
      REGION = var.region
    }
  }
  
  source_code_hash = filebase64sha256("./app/main.py")
  filename         = "app/main.py"
  
  depends_on = [
    module.iam_role
  ]
}

resource "aws_api_gateway_rest_api" "normative_query" {
  name        = var.api_gateway_name
  description = "API Gateway for normative queries"
}

resource "aws_api_gateway_resource" "query" {
  rest_api_id = aws_api_gateway_rest_api.normative_query.id
  parent_id  = aws_api_gateway_rest_api.normative_query.root_resource_id
  path_part  = "query"
}

resource "aws_api_gateway_method" "post" {
  rest_api_id   = aws_api_gateway_rest_api.normative_query.id
  resource_id   = aws_api_gateway_resource.query.id
  http_method   = "POST"
  authorization = "NONE"
  
  request_parameters = {
    "method.request.header.Content-Type" = true
  }
}

resource "aws_api_gateway_integration" "lambda" {
  rest_api_id = aws_api_gateway_rest_api.normative_query.id
  resource_id = aws_api_gateway_resource.query.id
  http_method = aws_api_gateway_method.post.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.normative_query.invoke_arn
  
  request_templates = {
    "application/json" = "$input.json('$')"
  }
}

resource "aws_api_gateway_deployment" "normative_query" {
  depends_on = [
    aws_api_gateway_integration.lambda
  ]
  
  rest_api_id = aws_api_gateway_rest_api.normative_query.id
  stage_name  = var.stage_name
}

output "api_gateway_url" {
  value = aws_api_gateway_deployment.normative_query.invoke_url
}

// === ARCHIVO: app/prompts/normative_query_template.txt ===
You are an expert in financial regulations and compliance. Given the context below, generate a structured response to the query. Ensure the response is clear, concise, and accurate.

Context:
{{ context }}

Query:
{{ query }}

Structured Response:
- Relevant Section:
- Explanation:
- Source:

// === ARCHIVO: app/retrieval/context_retriever.py ===
from typing import List
import numpy as np
from langchain.vectorstores import VectorStore
from app.models.normative_response import NormativeResponse
from app.config.settings import Settings

class ContextRetriever:
    def __init__(self, vector_store: VectorStore, settings: Settings):
        self.vector_store = vector_store
        self.settings = settings

    def retrieve_context(self, query: str) -> List[NormativeResponse]:
        try:
            embeddings = self.vector_store.get_embeddings(query)
            if not embeddings:
                raise ValueError('No embeddings found for the query')
            context = self.vector_store.search(embeddings)
            return self._process_context(context)
        except Exception as e:
            self.settings.logger.error(f'Error retrieving context: {e}')
            raise

    def _process_context(self, context: List[str]) -> List[NormativeResponse]:
        responses = []
        for doc in context:
            response = NormativeResponse(text=doc)
            responses.append(response)
        return responses

// === ARCHIVO: app/retrieval/vector_store.py ===
from typing import List
import numpy as np
from langchain.vectorstores import VectorStore
from app.config.settings import Settings

class VectorStore:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.store = {}

    def add_embeddings(self, documents: List[str], embeddings: np.ndarray):
        if len(documents)!= len(embeddings):
            raise ValueError('Number of documents and embeddings must match')
        for doc, embedding in zip(documents, embeddings):
            self.store[doc] = embedding

    def get_embeddings(self, query: str) -> np.ndarray:
        if query not in self.store:
            raise ValueError('No embeddings found for the query')
        return self.store[query]

    def search(self, embeddings: np.ndarray) -> List[str]:
        results = []
        for doc, embedding in self.store.items():
            similarity = np.dot(embedding, embeddings)
            if similarity > self.settings.similarity_threshold:
                results.append(doc)
        return results

// === ARCHIVO: app/chains/normative_chain.py ===
from typing import List
from app.retrieval.context_retriever import ContextRetriever
from app.models.normative_response import NormativeResponse
from app.config.settings import Settings

class NormativeChain:
    def __init__(self, context_retriever: ContextRetriever, settings: Settings):
        self.context_retriever = context_retriever
        self.settings = settings

    def execute(self, query: str) -> List[NormativeResponse]:
        context = self.context_retriever.retrieve_context(query)
        responses = []
        for response in context:
            responses.append(response)
        return responses

// === ARCHIVO: app/eval/evaluation_metrics.py ===
from typing import List
import json

from app.models.normative_response import NormativeResponse


def calculate_precision(responses: List[NormativeResponse], ground_truth: List[str]) -> float:
    """Calculate the precision of the responses.

    Args:
        responses (List[NormativeResponse]): The list of responses to evaluate.
        ground_truth (List[str]): The list of ground truth values.

    Returns:
        float: The precision of the responses.
    """    true_positives = 0
    total_responses = len(responses)

    for response in responses:
        if response.generated_response in ground_truth:
            true_positives += 1

    if total_responses == 0:
        return 0.0

    return true_positives / total_responses


def calculate_latency(responses: List[NormativeResponse]) -> float:
    """Calculate the average latency of the responses.

    Args:
        responses (List[NormativeResponse]): The list of responses to evaluate.

    Returns:
        float: The average latency of the responses.
    """    total_latency = sum(response.latency for response in responses)
    total_responses = len(responses)

    if total_responses == 0:
        return 0.0

    return total_latency / total_responses

// === ARCHIVO: app/eval/evaluation_dataset.json ===
[
    {
        "query": "¿Cuáles son las políticas de privacidad?",
        "ground_truth": [
            "Las políticas de privacidad se encuentran en el documento de políticas y procedimientos."
        ]
    },
    {
        "query": "¿Cuáles son los requisitos para abrir una cuenta?",
        "ground_truth": [
            "Los requisitos para abrir una cuenta se encuentran en el documento de apertura de cuentas."
        ]
    },
    {
        "query": "¿Cuáles son los términos y condiciones del préstamo?",
        "ground_truth": [
            "Los términos y condiciones del préstamo se encuentran en el documento de préstamo."
        ]
    }
]

// === ARCHIVO: app/config/aws_config.py ===
import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def get_aws_credentials() -> dict:
    """Retrieve AWS credentials from environment variables.

    Returns:
        dict: A dictionary containing the AWS access key ID and secret access key.
    """    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    if not aws_access_key_id or not aws_secret_access_key:
        raise NoCredentialsError('AWS credentials not found in environment variables.')

    return {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key
    }


def get_aws_session() -> boto3.session.Session:
    """Create an AWS session using the retrieved credentials.

    Returns:
        boto3.session.Session: An AWS session object.
    """    credentials = get_aws_credentials()

    try:
        session = boto3.Session(
            aws_access_key_id=credentials['aws_access_key_id'],
            aws_secret_access_key=credentials['aws_secret_access_key']
        )
    except (NoCredentialsError, PartialCredentialsError) as e:
        raise e

    return session


def get_bedrock_client() -> boto3.client:
    """Create a Bedrock client using the AWS session.

    Returns:
        boto3.client: A Bedrock client object.
    """    session = get_aws_session()
    return session.client('bedrock')

// === ARCHIVO: tests/test_context_retrieval.py ===
import pytest
from app.retrieval.context_retriever import ContextRetriever
from app.models.normative_response import NormativeResponse, Reference

@pytest.fixture
def context_retriever() -> ContextRetriever:
    return ContextRetriever()

def test_retrieve_relevant_context(context_retriever: ContextRetriever):
    query = 'sample query'
    expected_references = [Reference(document_id='doc1', section='section1', source_type=NormativeSource.INTERNAL)]
    response = context_retriever.retrieve_context(query)
    assert isinstance(response, NormativeResponse)
    assert response.references == expected_references

def test_retrieve_context_error_handling(context_retriever: ContextRetriever):
    with pytest.raises(Exception):
        context_retriever.retrieve_context('error query')

// === ARCHIVO: tests/test_chain_execution.py ===
import pytest
from app.chains.normative_chain import NormativeChain
from app.models.normative_response import NormativeResponse

@pytest.fixture
def normative_chain() -> NormativeChain:
    return NormativeChain()

def test_execute_chain(normative_chain: NormativeChain):
    query = 'sample query'
    expected_response = NormativeResponse(query_text='sample query', generated_response='sample response', confidence_score=0.9)
    response = normative_chain.execute(query)
    assert isinstance(response, NormativeResponse)
    assert response == expected_response

def test_execute_chain_error_handling(normative_chain: NormativeChain):
    with pytest.raises(Exception):
        normative_chain.execute('error query')

// === ARCHIVO: tests/test_evaluation_metrics.py ===
import pytest
from app.eval.evaluation_metrics import EvaluationMetrics
from app.models.normative_response import NormativeResponse

@pytest.fixture
def evaluation_metrics() -> EvaluationMetrics:
    return EvaluationMetrics()

def test_calculate_precision(evaluation_metrics: EvaluationMetrics):
    responses = [NormativeResponse(query_text='query1', generated_response='response1', confidence_score=0.9)]
    expected_precision = 1.0
    precision = evaluation_metrics.calculate_precision(responses)
    assert precision == expected_precision

def test_calculate_latency(evaluation_metrics: EvaluationMetrics):
    responses = [NormativeResponse(query_text='query1', generated_response='response1', confidence_score=0.9)]
    expected_latency = 0.5
    latency = evaluation_metrics.calculate_latency(responses)
    assert latency == expected_latency

def test_evaluation_metrics_error_handling(evaluation_metrics: EvaluationMetrics):
    with pytest.raises(Exception):
        evaluation_metrics.calculate_precision([])

// === ARCHIVO: README.md ===
# Proyecto de IA Generativa para Consultas Normativas

## Descripción
Este proyecto implementa una solución basada en modelos generativos para responder consultas sobre la normativa interna de una institución financiera. La solución recupera contexto relevante, genera una salida estructurada y es medible en términos de precisión y latencia.

## Instalación
1. Clona el repositorio.
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución
1. Configura las variables de entorno en `.env`.
2. Inicia la aplicación:
   ```bash
   uvicorn app.main:app --reload
   ```

## Estructura de Carpetas
- `app/`: Código fuente de la aplicación.
- `tests/`: Casos de prueba.
- `docs/`: Documentación adicional.
- `infra/`: Infraestructura como código (Terraform).

## Contribuyendo
Por favor, lee el archivo `CONTRIBUTING.md` para detalles sobre nuestro código de conducta, y el proceso para enviarnos tu trabajo (pull requests).

## Licencia
Este proyecto está bajo la Licencia MIT - mira el archivo `LICENSE` para detalles.
```
