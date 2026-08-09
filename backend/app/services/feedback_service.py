from app.models.feedback import FeedbackResponse
from app.memory.interview_memory import interview_memory
from app.ai.llm_service import LLMService


class FeedbackService:

    def __init__(self):
        # Use the centralized AI service.
        # This supports MockAIProvider now and
        # real LLM providers later.
        self.llm_service = LLMService()

    def generate_feedback(
        self,
        candidate_id: str
    ) -> FeedbackResponse:

        # Get candidate interview answers
        answers = interview_memory.get_answers(candidate_id)

        # Handle missing interview data
        if not answers:
            return FeedbackResponse(
                candidate_id=candidate_id,
                overall_score=0,
                technical_score=0,
                communication_score=0,
                strengths=[
                    "No interview answers available."
                ],
                weaknesses=[
                    "Interview data is missing."
                ],
                recommendations=[
                    "Complete the interview before generating feedback."
                ]
            )

        # Build interview context for the AI provider
        context = {
            "answers": answers
        }

        # Generate structured AI feedback
        ai_feedback = self.llm_service.generate_feedback(
            context
        )

        return FeedbackResponse(
            candidate_id=candidate_id,
            overall_score=ai_feedback["overall_score"],
            technical_score=ai_feedback["technical_score"],
            communication_score=ai_feedback["communication_score"],
            strengths=ai_feedback["strengths"],
            weaknesses=ai_feedback["weaknesses"],
            recommendations=ai_feedback["recommendations"]
        )
