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