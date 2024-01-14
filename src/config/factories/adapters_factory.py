from src.adapters.abstract_adapters_factory import AbstractAdaptersFactory
from src.adapters.logger import Logger
from src.config.configs import Configs
from src.core.ports.abstract_logger import AbstractLogger


class AdaptersFactory(AbstractAdaptersFactory):
    def __init__(self, configs: Configs):
        self.configs = configs

    def logger(self, name: str) -> AbstractLogger:
        return Logger(name)
