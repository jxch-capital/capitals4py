from capitals4py.api import router
from fastapi import Depends
from dependency_injector.wiring import inject, Provide
from capitals4py.containers import Container
from capitals4py.services.qlib_protocol import QLibProtocol


@router.get("/qlib/day/{region}/{code}/{start_date}/{end_date}")
@inject
def get_user(
        region: str,
        code: str,
        start_date: str,
        end_date: str,
        qlib_service: QLibProtocol = Depends(Provide[Container.qlib_service]),
):
