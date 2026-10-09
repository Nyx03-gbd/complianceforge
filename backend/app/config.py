from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg2://complianceforge:CHANGE_ME@db:5432/complianceforge"
    secret_key: str
    environment: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
