import uvicorn
from fastapi import FastAPI

from src.adapters.logger import LoggerFactory
from src.config.models import HttpServerConfig


class HttpServer:
    def __init__(
        self,
        http_controller: FastAPI,
        http_server_config: HttpServerConfig,
        logger_factory: LoggerFactory,
    ):
        self.http_controller = http_controller
        self.http_server_config = http_server_config
        self.logger = logger_factory(__name__)

    def start(self) -> None:
        self.logger.info(
            f"Starting http service on host: "
            f"{self.http_server_config.host} & "
            f"port: {self.http_server_config.port}"
        )
        print(self.http_server_config.port, self.http_server_config.host)
        uvicorn.run(
            self.http_controller,
            host=self.http_server_config.host,
            port=self.http_server_config.port,
        )
        self.logger.info("Stopping http service...")
