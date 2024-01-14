import sys
from typing import Any

import yaml

from src.config.configs import Configs
from src.config.factories.adapters_factory import AdaptersFactory
from src.controllers.http import create_http_controller
from src.http_server import HttpServer


def config_path(config_file: str) -> str:
    return f"src/config/files/{config_file}.yaml"


def read_config(path: str) -> Any:
    with open(path) as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit()
        else:
            return config


def start_http_server_app(configs: Configs) -> None:
    adapters_factory = AdaptersFactory(configs)
    http_controller = create_http_controller()
    http_server = HttpServer(http_controller, configs.http_server, adapters_factory.logger)
    http_server.start()


def main() -> None:
    path = config_path("localhost")
    config = Configs(read_config(path))

    start_http_server_app(config)


if __name__ == "__main__":
    main()
