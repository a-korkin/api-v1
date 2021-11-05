from pydantic import BaseSettings
from functools import lru_cache

class GlobalConfig(BaseSettings):
    DATABASE_URL: str
    API_V1: str = "/api/v1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_configuration() -> GlobalConfig:
    return GlobalConfig()

settings = get_configuration()    
