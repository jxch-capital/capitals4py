from dependency_injector import containers, providers
import os


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".api"])

