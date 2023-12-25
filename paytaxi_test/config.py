from typing import Literal
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf8")

    mode: Literal["DEV", "TEST"]

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    test_postgres_user: str
    test_postgres_password: str
    test_postgres_db: str
    test_postgres_host: str
    test_postgres_port: int

    @property
    def db_url(self) -> PostgresDsn:
        return PostgresDsn(
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@"
            f"{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def test_db_url(self) -> PostgresDsn:
        return PostgresDsn(
            f"postgresql+asyncpg://"
            f"{self.test_postgres_user}:{self.test_postgres_password}@"
            f"{self.test_postgres_host}:{self.test_postgres_port}/"
            f"{self.test_postgres_db}"
        )


settings = Settings()  # type: ignore
