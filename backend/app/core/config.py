from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str = "mongodb://mongo:27017"  # Provide your default MongoDB URI here
    DB_NAME: str = "auth_db"
    SECRET_KEY: str = "your_secret_key_here"  # Provide your default secret key here
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
