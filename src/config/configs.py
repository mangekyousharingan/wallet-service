from src.config.models import HttpServerConfig


class Configs:
    def __init__(self, config_yaml: dict) -> None:
        self.config = config_yaml

    @property
    def http_server(self) -> HttpServerConfig:
        return HttpServerConfig(self.config["http_server"]["host"], port=self.config["http_server"]["port"])
