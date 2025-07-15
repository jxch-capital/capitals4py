import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(dotenv_path='.env', override=True)
env = os.environ.get('ENV', 'dev')
env_file = f'.env.{env}'
load_dotenv(env_file, override=True)


class Settings(BaseSettings):
    http_proxy_addr: str = ""
    http_proxy_port: int = 10808
    http_proxy_enable: bool = False

    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding='utf-8')
