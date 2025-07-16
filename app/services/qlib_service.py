from app.services.qlib_protocol import QLibProtocol
from app.config.app_setting import Settings
from qlib.tests.data import GetData
import qlib


class QLibService(QLibProtocol):
    def __init__(self, settings: Settings):
        self.settings = settings

    def qlib_data(self, region: str) -> str:
        target_dir = self.settings.get_qlib_data_path() / region
        GetData().qlib_data(target_dir=target_dir, region=region, exists_skip=True)
        return target_dir

    def qlib_init(self, region: str):
        target_dir = self.settings.get_qlib_data_path() / region
        qlib.init(provider_uri=target_dir, region=region, exists_skip=True)
