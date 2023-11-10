import logging

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    try:
        model_config = SettingsConfigDict(
            env_file='.env', env_file_encoding='utf-8'
        )
    except ValidationError:
        logger.info('.env file not find')

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    SENTRY_DSN: str

    SMTP_TLS: bool
    SMTP_PORT: int
    SMTP_HOST: str
    SMTP_USER: str
    SMTP_PASSWORD: str
    EMAILS_FROM_EMAIL: str
