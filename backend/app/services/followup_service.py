from app.models.followup import FollowUpResponse
from app.ai.client import AIClient, MockAIClient


class FollowUpService:

    def __init__(self):

        # Use the shared AI abstraction
        self.ai_client: AIClient = MockAIClient()

    def generate_follow_up(
        self,
        candidate_id: str,
        question_id: str,
        answer: str
    ) -> FollowUpResponse:
        """
        Generate a contextual follow-up question using the AI client.
        """

        from app.ai.prompts import FOLLOW_UP_PROMPT

        prompt = FOLLOW_UP_PROMPT.format(
            previous_question=question_id,
            candidate_answer=answer
        )

        follow_up_question = self.ai_client.generate(prompt)

        return FollowUpResponse(
            candidate_id=candidate_id,
            previous_question_id=question_id,
            follow_up_question=follow_up_question
        )