import uvicorn
from fastapi import FastAPI

from src.config.models import HttpServerConfig


class HttpServer:
    def __init__(self, http_controller: FastAPI, http_server_config: HttpServerConfig):
        self.http_controller = http_controller
        self.http_server_config = http_server_config

    def start(self):
        print(f"Starting http service on host: {self.http_server_config.host} & port: {self.http_server_config.port}")
        uvicorn.run(self.http_controller, host=self.http_server_config.host, port=self.http_server_config.port)
        print("Stopping http service...")
