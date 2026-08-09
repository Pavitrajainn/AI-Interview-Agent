import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv(
        "APP_NAME",
        "AI Interview Agent"
    )

    AI_PROVIDER: str = os.getenv(
        "AI_PROVIDER",
        "mock"
    )

    OPENAI_API_KEY: str | None = os.getenv(
        "OPENAI_API_KEY"
    )


settings = Settings()
