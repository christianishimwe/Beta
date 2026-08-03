from pydantic_settings import BaseSettings, SettingsConfigDict


_basesettings = model_config = SettingsConfigDict(
    env_file=".env",
    env_ignore_empty=True,
    extra="ignore"
)


class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = _basesettings


class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str

    model_config = _basesettings

    @property
    def POSTGRES_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


database_settings = DatabaseSettings()
redis_settings = RedisSettings()
