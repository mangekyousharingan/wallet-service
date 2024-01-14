from abc import abstractmethod

from src.core.ports.abstract_logger import AbstractLogger


class AbstractAdaptersFactory:
    @abstractmethod
    def logger(self, name: str) -> AbstractLogger:
        raise NotImplemented
