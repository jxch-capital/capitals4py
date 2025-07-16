from dependency_injector import containers, providers
from capitals4py.config.app_setting import Settings
from capitals4py.services.qlib_service import QLibService
from capitals4py.services.qlib_protocol import QLibProtocol


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["capitals4py.api"])

    app_settings: Settings = providers.Singleton(Settings)
    qlib_service: QLibProtocol = providers.Singleton(QLibService, settings=app_settings)
