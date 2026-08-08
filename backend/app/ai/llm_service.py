from typing import Any

from .factory import get_ai_provider
from .provider import AIProvider


class LLMService:
    """Application-level service for AI operations."""

    def __init__(self, provider: AIProvider | None = None):
        self.provider = provider or get_ai_provider()

    def generate_question(self, context: dict[str, Any]) -> str:
        return self.provider.generate_question(context)

    def generate_followup(self, context: dict[str, Any]) -> str:
        return self.provider.generate_followup(context)

    def evaluate_answer(
        self,
        context: dict[str, Any],
    ) -> dict[str, Any]:
        return self.provider.evaluate_answer(context)

    def generate_feedback(
        self,
        context: dict[str, Any],
    ) -> dict[str, Any]:
        return self.provider.generate_feedback(context)