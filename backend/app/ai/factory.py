from .config import AI_PROVIDER
from .mock_provider import MockAIProvider
from .provider import AIProvider


def get_ai_provider() -> AIProvider:
    """
    Return the configured AI provider.

    Currently the project supports the mock provider.
    Additional providers can be added later without
    changing the application services.
    """

    if AI_PROVIDER == "mock":
        return MockAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )