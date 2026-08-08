from app.models.feedback import FeedbackResponse
from app.memory.interview_memory import interview_memory


class FeedbackService:

    def generate_feedback(
        self,
        candidate_id: str
    ) -> FeedbackResponse:

        # Use shared interview memory
        answers = interview_memory.get_answers(candidate_id)

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

        total_answers = len(answers)

        # Basic MVP scoring
        technical_score = min(100, total_answers * 20)

        communication_score = 70

        overall_score = round(
            (technical_score + communication_score) / 2
        )

        strengths = [
            "Candidate attempted the interview questions.",
            "Candidate demonstrated knowledge of the discussed topics."
        ]

        weaknesses = [
            "Some answers may require more depth.",
            "Technical explanations can be improved with practical examples."
        ]

        recommendations = [
            "Practice explaining technical concepts clearly.",
            "Use practical examples when answering technical questions.",
            "Review topics where answers were incomplete."
        ]

        return FeedbackResponse(
            candidate_id=candidate_id,
            overall_score=overall_score,
            technical_score=technical_score,
            communication_score=communication_score,
            strengths=strengths,
            weaknesses=weaknesses,
            recommendations=recommendations
        )