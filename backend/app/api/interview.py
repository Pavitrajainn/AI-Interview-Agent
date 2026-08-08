from fastapi import APIRouter, HTTPException

from app.models.interview import (
    InterviewQuestion,
    InterviewSession,
    AnswerSubmission,
    AnswerResponse
)

from app.services.interview_service import InterviewService

router = APIRouter(
    prefix="/api/interview",
    tags=["Interview"],
)


interview_service = InterviewService()


@router.get(
    "/question/{question_number}",
    response_model=InterviewQuestion
)
def get_interview_question(question_number: int):
    try:
        return interview_service.get_question(question_number)
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail="Question number out of range"
        )


@router.post(
    "/start",
    response_model=InterviewSession
)
def start_interview(candidate_id: str):
    return interview_service.start_interview(candidate_id)

@router.post(
    "/answer",
    response_model=AnswerResponse
)
def submit_answer(submission: AnswerSubmission):
    try:
        return interview_service.submit_answer(
            candidate_id=submission.candidate_id,
            question_id=submission.question_id,
            answer=submission.answer
        )
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )
        
@router.get("/memory/{candidate_id}")
def get_interview_memory(candidate_id: str):
    return interview_service.get_interview_memory(candidate_id)