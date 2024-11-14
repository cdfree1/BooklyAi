#builtin

#external
from pydantic_settings import BaseSettings, SettingsConfigDict

#internal

class Environment(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(env_file=".env")
    OPENAPI_KEY:str