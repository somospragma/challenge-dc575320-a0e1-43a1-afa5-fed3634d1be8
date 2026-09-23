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