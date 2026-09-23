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