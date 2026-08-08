from fastapi import APIRouter

from app.models.candidate import Candidate
from app.services.candidate_service import CandidateService


router = APIRouter(
    prefix="/api/candidate",
    tags=["Candidate"],
)

candidate_service = CandidateService()


@router.get("", response_model=Candidate)
def get_candidate():
    return candidate_service.get_candidate()