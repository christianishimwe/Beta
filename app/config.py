from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )


redis_settings = RedisSettings()
