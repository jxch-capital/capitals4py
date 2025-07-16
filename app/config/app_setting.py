from pydantic import BaseModel, ConfigDict

class Settings(BaseModel):
    http_proxy_addr: str = ""
    http_proxy_port: int = 10808
    http_proxy_enable: bool = False
    dir_qlib_data: str = ""
    dir_project: str = ""

    model_config = ConfigDict(frozen=True)

