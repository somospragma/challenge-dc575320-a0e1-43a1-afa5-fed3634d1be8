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