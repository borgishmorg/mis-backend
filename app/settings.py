from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST = '0.0.0.0'
    PORT = 4000
    WORKERS = 1

    ENABLE_AUTORELOAD = True


settings = Settings()
