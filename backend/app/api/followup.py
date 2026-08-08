from fastapi import APIRouter

from app.models.followup import (
    FollowUpRequest,
    FollowUpResponse
)

from app.services.followup_service import FollowUpService


router = APIRouter(
    prefix="/api/followup",
    tags=["Follow-up"]
)


followup_service = FollowUpService()


@router.post(
    "/generate",
    response_model=FollowUpResponse
)
def generate_follow_up(request: FollowUpRequest):

    return followup_service.generate_follow_up(
        candidate_id=request.candidate_id,
        question_id=request.question_id,
        answer=request.answer
    )