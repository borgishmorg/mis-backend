from pydantic import BaseSettings
from secrets import token_bytes


class Settings(BaseSettings):
    HOST = '0.0.0.0'
    PORT = 4000
    WORKERS = 1

    JWT_SECRET = 'secret'
    JWT_ALGORITHM = 'HS256'
    JWT_ACCESS_TOKEN_LIFETIME = 15 * 60  # seconds
    JWT_REFRESH_TOKEN_LIFETIME = 6 * 60 * 60  # seconds

    ENABLE_AUTORELOAD = True
    ENABLE_DEVELOP_MOD = True
    ENABLE_RANDOM_JWT_SECRET = False

    POSTGRES_DSN = 'postgresql://root:example@localhost:5432/mis'


settings = Settings()

if settings.ENABLE_RANDOM_JWT_SECRET:
    settings.JWT_SECRET = token_bytes(32)
