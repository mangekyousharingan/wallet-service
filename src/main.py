from src.config.models import HttpServerConfig
from src.controllers.http import create_http_controller
from src.http_server import HttpServer


def start_http_server_app() -> None:
    http_server_config = HttpServerConfig(host="0.0.0.0", port=8080)  # TODO: read host and port from config
    http_controller = create_http_controller()
    http_server = HttpServer(http_controller, http_server_config)
    http_server.start()


def main():
    start_http_server_app()


if __name__ == "__main__":
    main()
