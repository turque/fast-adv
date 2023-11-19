import secrets
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, EmailStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file='.env')

    API_V1_STR: str = '/api/v1'
    SERVER_HOST: AnyHttpUrl
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days  int = 60 * 24 * 8
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = 'HS256'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @field_validator('BACKEND_CORS_ORIGINS')
    def assemble_cors_origins(
        cls, v: Union[str, List[str]]
    ) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = 'fast-adv'
    SENTRY_DSN: str

    @field_validator('SENTRY_DSN')
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if len(v) == 0:
            return None
        return v

    DATABASE_URL: Optional[str] = None

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAILS_ENABLED: bool = False

    EMAIL_TEST_USER: EmailStr = 'test@example.com'  # type: ignore
    USERS_OPEN_REGISTRATION: bool = False
    BREVO_API_KEY: str = None

    TEMPLATE_TEST: str = 'email/test_email.j2'
    TEMPLATE_INVITE: str = 'email/invite.j2'


settings = Settings()
