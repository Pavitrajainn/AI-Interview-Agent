from abc import ABC, abstractmethod


class AIClient(ABC):
    """
    Abstract interface for AI providers.

    Future LLM providers can implement this interface
    without changing the business logic.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a text response from the AI provider.
        """
        pass

    @abstractmethod
    def generate_feedback(self, prompt: str) -> dict:
        """
        Generate structured interview feedback.
        """
        pass


class MockAIClient(AIClient):
    """
    Mock AI provider used during development.

    This allows the application to work without
    an external API key.
    """

    def generate(self, prompt: str) -> str:
        return (
            "This is a mock AI response. "
            "An actual LLM provider can be integrated later."
        )

    def generate_feedback(self, prompt: str) -> dict:
        """
        Return structured mock feedback.

        Later this method can be replaced with
        a real LLM structured-output implementation.
        """

        return {
            "overall_score": 75,
            "technical_score": 80,
            "communication_score": 70,
            "strengths": [
                "Candidate demonstrated understanding of Python concepts.",
                "Candidate provided a technically relevant answer."
            ],
            "weaknesses": [
                "Some explanations could be more detailed.",
                "Practical examples could improve the answer."
            ],
            "recommendations": [
                "Practice explaining technical concepts in depth.",
                "Use practical examples when answering interview questions."
            ]
        }