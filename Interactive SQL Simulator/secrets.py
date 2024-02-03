from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    USER: str
    PASSWORD: str
    HOST: str
    DATABASE: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


secret = Settings()
