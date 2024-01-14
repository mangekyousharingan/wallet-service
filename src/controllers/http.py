from fastapi import FastAPI
from starlette.responses import JSONResponse


def create_http_controller() -> FastAPI:
    controller = FastAPI()

    @controller.get("/healthz")
    def _healthz() -> JSONResponse:
        return JSONResponse("OK")

    return controller
