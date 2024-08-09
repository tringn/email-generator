import secrets

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    OPENAI_API_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str
    API_V1_STR: str = "/api/v1"
    LLM_CHAT_MODEL: str = "gpt-4o-mini"
    LLM_CHAT_MODEL_TEMPERATURE: float = 0.7


settings = Settings()  # type: ignore
