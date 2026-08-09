from app.models.followup import FollowUpResponse
from app.ai.llm_service import LLMService


class FollowUpService:

    def __init__(self):
        # Use the centralized AI service.
        # This allows MockAIProvider now and
        # real LLM providers later.
        self.llm_service = LLMService()

    def generate_follow_up(
        self,
        candidate_id: str,
        question_id: str,
        answer: str
    ) -> FollowUpResponse:
        """
        Generate a contextual follow-up question
        using the configured AI provider.
        """

        context = {
            "question_id": question_id,
            "answer": answer,
        }

        follow_up_question = self.llm_service.generate_followup(
            context
        )

        return FollowUpResponse(
            candidate_id=candidate_id,
            previous_question_id=question_id,
            follow_up_question=follow_up_question
        )
