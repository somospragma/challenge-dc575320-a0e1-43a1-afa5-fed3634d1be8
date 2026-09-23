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