from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf8")

    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: int

    @property
    def db_url(self) -> PostgresDsn:
        return PostgresDsn(
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )
    

settings = Settings()  # type: ignore
