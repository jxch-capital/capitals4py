from dependency_injector import containers, providers
from app.config.app_setting import Settings
from app.services.qlib_service import QLibService
from app.services.qlib_protocol import QLibProtocol


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=[
        "app.services",
    ])

    app_settings: Settings = providers.Singleton(Settings)
    qlib_service: QLibProtocol = providers.Singleton(QLibService, settings=app_settings)
