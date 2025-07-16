from typing import Protocol

class QLibProtocol(Protocol):
    def qlib_data(self, region: str) -> str: ...
    def qlib_init(self, region: str): ...


