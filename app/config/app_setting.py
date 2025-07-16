from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    proxy_addr: str = ""
    proxy_port: int = 10808
    proxy_enable: bool = False
    dir_qlib_data: str = ""
    dir_project: str = ""

    model_config = ConfigDict(frozen=True)

    def get_qlib_data_path(self):
        return Path(self.dir_qlib_data)

