from typing import Any

from .provider import AIProvider


class MockAIProvider(AIProvider):
    """
    Local fallback AI provider.

    This provider allows the application to work without
    an external LLM API key.
    """

    def generate_question(self, context: dict[str, Any]) -> str:
        topic = context.get("topic", "Python")

        return (
            f"Can you explain {topic} and give a practical "
            "example from your experience?"
        )

    def generate_followup(self, context: dict[str, Any]) -> str:
        answer = context.get("answer", "")

        if "list" in answer.lower():
            return "What is the difference between a Python list and a tuple?"

        if "function" in answer.lower():
            return "What is the difference between parameters and arguments?"

        if "oop" in answer.lower() or "object" in answer.lower():
            return "Can you explain the main principles of OOP?"

        return (
            "Can you explain your answer in more detail "
            "and provide a practical example?"
        )

    def evaluate_answer(
        self,
        context: dict[str, Any],
    ) -> dict[str, Any]:

        answer = context.get("answer", "").strip()

        if not answer:
            return {
                "score": 0,
                "technical_score": 0,
                "communication_score": 0,
                "strengths": [],
                "weaknesses": ["No answer was provided."],
            }

        word_count = len(answer.split())

        if word_count >= 30:
            score = 8
        elif word_count >= 15:
            score = 7
        elif word_count >= 5:
            score = 5
        else:
            score = 3

        return {
            "score": score,
            "technical_score": score,
            "communication_score": min(score + 1, 10),
            "strengths": [
                "Candidate attempted to explain the concept.",
            ],
            "weaknesses": [
                "The answer could include more technical detail "
                "and practical examples."
            ],
        }

    def generate_feedback(
        self,
        context: dict[str, Any],
    ) -> dict[str, Any]:

        answers = context.get("answers", [])

        if not answers:
            return {
                "overall_score": 0,
                "technical_score": 0,
                "communication_score": 0,
                "strengths": [],
                "weaknesses": [
                    "No interview answers were available."
                ],
                "recommendations": [
                    "Complete the interview before requesting feedback."
                ],
            }

        total_answers = len(answers)

        return {
            "overall_score": 7,
            "technical_score": 7,
            "communication_score": 7,
            "strengths": [
                f"Completed {total_answers} interview questions.",
                "Demonstrated understanding of technical concepts.",
            ],
            "weaknesses": [
                "Some answers could be more detailed.",
            ],
            "recommendations": [
                "Practice explaining concepts with practical examples.",
                "Improve technical depth in interview answers.",
            ],
        }