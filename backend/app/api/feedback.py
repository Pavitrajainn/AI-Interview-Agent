from fastapi import APIRouter

from app.models.feedback import (
    FeedbackRequest,
    FeedbackResponse
)

from app.services.feedback_service import FeedbackService


router = APIRouter(
    prefix="/api/feedback",
    tags=["Feedback"]
)

feedback_service = FeedbackService()


@router.post(
    "/generate",
    response_model=FeedbackResponse
)
def generate_feedback(request: FeedbackRequest):

    return feedback_service.generate_feedback(
        candidate_id=request.candidate_id
    )