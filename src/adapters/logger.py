import logging
from typing import Any, Callable

from src.core.ports.abstract_logger import AbstractLogger


class Logger(AbstractLogger):
    def __init__(self, name: str):
        self._logger = logging.getLogger(name)

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.DEBUG, msg, *args, **kwargs)

    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.INFO, msg, *args, **kwargs)

    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.ERROR, msg, *args, **kwargs)

    def exception(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.ERROR, msg, *args, exc_info=True, **kwargs)

    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.CRITICAL, msg, *args, **kwargs)

    def log(self, level: int, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(level, msg, *args, **kwargs)

    def _log(self, level: int, msg: str, *args: Any, **kwargs: Any) -> None:
        stacklevel = kwargs.get("stacklevel", 1) + 2  # incremented to show real source of error
        kwargs["stacklevel"] = stacklevel
        self._logger.log(level, msg, *args, **kwargs)


LoggerFactory = Callable[[str], AbstractLogger]

