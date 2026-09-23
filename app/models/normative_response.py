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