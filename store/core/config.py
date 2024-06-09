from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "store fastapi"
    ROOT_PATH: str = ""
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
