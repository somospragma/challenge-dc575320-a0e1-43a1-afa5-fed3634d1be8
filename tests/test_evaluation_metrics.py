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