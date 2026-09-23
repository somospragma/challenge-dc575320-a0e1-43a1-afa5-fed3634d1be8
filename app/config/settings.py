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