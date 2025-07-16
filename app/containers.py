from dependency_injector import containers, providers
from config.app_setting import Settings


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app"])

    app_settings = providers.Singleton(Settings)
