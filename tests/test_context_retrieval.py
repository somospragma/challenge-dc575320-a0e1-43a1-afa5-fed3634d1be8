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