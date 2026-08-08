from pydantic import BaseModel


class InterviewQuestion(BaseModel):
    id: str
    question: str
    topic: str
    difficulty: str


class InterviewSession(BaseModel):
    candidate_id: str
    current_question: InterviewQuestion | None = None
    question_number: int = 0
    total_questions: int = 5


class AnswerSubmission(BaseModel):
    candidate_id: str
    question_id: str
    answer: str


class AnswerResponse(BaseModel):
    candidate_id: str
    question_id: str
    answer: str
    next_question: InterviewQuestion | None = None
    completed: bool