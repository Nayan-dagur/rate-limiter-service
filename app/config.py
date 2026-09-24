from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Distributed Rate Limiter Service"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    RATE_LIMIT_REQUESTS: int = 10     # Max requests allowed
    RATE_LIMIT_WINDOW_SECONDS: int = 60 # In this time window

    class Config:
        env_file = ".env"

settings = Settings()

