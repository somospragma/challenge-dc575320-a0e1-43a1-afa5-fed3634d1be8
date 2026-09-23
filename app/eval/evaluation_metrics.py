from typing import List
import json

from app.models.normative_response import NormativeResponse


def calculate_precision(responses: List[NormativeResponse], ground_truth: List[str]) -> float:
    """Calculate the precision of the responses.

    Args:
        responses (List[NormativeResponse]): The list of responses to evaluate.
        ground_truth (List[str]): The list of ground truth values.

    Returns:
        float: The precision of the responses.
    """    true_positives = 0
    total_responses = len(responses)

    for response in responses:
        if response.generated_response in ground_truth:
            true_positives += 1

    if total_responses == 0:
        return 0.0

    return true_positives / total_responses


def calculate_latency(responses: List[NormativeResponse]) -> float:
    """Calculate the average latency of the responses.

    Args:
        responses (List[NormativeResponse]): The list of responses to evaluate.

    Returns:
        float: The average latency of the responses.
    """    total_latency = sum(response.latency for response in responses)
    total_responses = len(responses)

    if total_responses == 0:
        return 0.0

    return total_latency / total_responses