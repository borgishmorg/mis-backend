from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST = '0.0.0.0'
    PORT = 4000
    WORKERS = 1

    ENABLE_AUTORELOAD = True
    ENABLE_DEVELOP_MOD = True

    POSTGRES_DSN = 'postgresql://root:example@localhost:5432/mis'


settings = Settings()
