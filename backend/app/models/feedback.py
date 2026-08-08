from pydantic import BaseModel
from typing import List


class FeedbackRequest(BaseModel):
    candidate_id: str


class FeedbackResponse(BaseModel):
    candidate_id: str
    overall_score: int
    technical_score: int
    communication_score: int
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]