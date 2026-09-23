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