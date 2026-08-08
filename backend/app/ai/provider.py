from abc import ABC, abstractmethod
from typing import Any


class AIProvider(ABC):
    """Base interface for all AI providers."""

    @abstractmethod
    def generate_question(self, context: dict[str, Any]) -> str:
        pass

    @abstractmethod
    def generate_followup(self, context: dict[str, Any]) -> str:
        pass

    @abstractmethod
    def evaluate_answer(self, context: dict[str, Any]) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_feedback(self, context: dict[str, Any]) -> dict[str, Any]:
        pass