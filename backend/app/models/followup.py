from pydantic import BaseModel


class FollowUpRequest(BaseModel):
    candidate_id: str
    question_id: str
    answer: str


class FollowUpResponse(BaseModel):
    candidate_id: str
    previous_question_id: str
    follow_up_question: str