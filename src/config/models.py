from dataclasses import dataclass


@dataclass
class HttpServerConfig:
    host: str
    port: int
