from fastapi import APIRouter

from app.models.curriculum import Curriculum
from app.services.curriculum_service import CurriculumService


router = APIRouter(
    prefix="/api/curriculum",
    tags=["Curriculum"],
)

curriculum_service = CurriculumService()


@router.get("", response_model=Curriculum)
def get_curriculum():
    return curriculum_service.get_curriculum()