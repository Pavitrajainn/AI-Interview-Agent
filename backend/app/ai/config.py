import os
from dotenv import load_dotenv

# Load environment variables from backend/.env
load_dotenv()


class Settings:
    """
    Application configuration.

    Values are loaded from environment variables so
    sensitive credentials are not hardcoded in source code.
    """

    APP_NAME: str = os.getenv(
        "APP_NAME",
        "AI Interview Agent"
    )

    AI_PROVIDER: str = os.getenv(
        "AI_PROVIDER",
        "mock"
    )

    AI_API_KEY: str | None = os.getenv(
        "AI_API_KEY"
    )

    AI_MODEL: str = os.getenv(
        "AI_MODEL",
        "mock-model"
    )


settings = Settings()

# Backward-compatible module-level exports
APP_NAME = settings.APP_NAME
AI_PROVIDER = settings.AI_PROVIDER
AI_API_KEY = settings.AI_API_KEY
AI_MODEL = settings.AI_MODEL
