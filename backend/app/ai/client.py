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
        Generate a response from the AI provider.
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

