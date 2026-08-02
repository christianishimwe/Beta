from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    REDIS_SERVER: str
    REDIS_PORT: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )
