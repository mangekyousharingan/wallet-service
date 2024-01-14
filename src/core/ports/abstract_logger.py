from abc import ABC, abstractmethod
from typing import Any


class AbstractLogger(ABC):
    @abstractmethod
    def __init__(self, name: str):
        raise NotImplementedError

    @abstractmethod
    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def exception(self, msg: str, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def log(self, level: int, msg: str, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError
