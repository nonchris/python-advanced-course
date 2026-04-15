"""
Sets up a logger for you python project.
Logs by to console and file, also hooks exceptions.

Logfile is by default: data/<logger_name>_<startup time>.log
If log-folder doesn't exist it will be created

Usage options:
from <this module> import logger
logger.info("hello there")

or

from <this module> import LOGGER_NAME
logger = logging.getLogger(LOGGER_NAME)
logger.info("hello there")

or

from <this module> import logger as _logger
logger = _logger.getChild(__name__)
logger.info("hello there")
"""

import logging
import sys
import types
from datetime import datetime
from pathlib import Path

LOGGER_NAME: str = "my_logger"

LOG_FOLDER: str = "data/"

STARTUP_TIME: datetime = datetime.now()

# full list of things you can access: https://docs.python.org/3/library/logging.html#logrecord-attributes
# e.g. processName could be a useful addition...
formatter = logging.Formatter("[{asctime}] [{levelname}] [{threadName}][{module}.{funcName}] {message}", style="{")

log_folder = Path(LOG_FOLDER)  # this could also be an env variable...
log_folder.mkdir(parents=True, exist_ok=True)

# init one normal filehandler and a stream-handler for stdout
# log file shall contain date
_startup_time = STARTUP_TIME.strftime("%Y-%m-%d_%H-%M-%S")
file_logger = logging.FileHandler(f"{log_folder}/{LOGGER_NAME}_{_startup_time}.log")
file_logger.setLevel(logging.DEBUG)
file_logger.setFormatter(formatter)

console_logger = logging.StreamHandler()
console_logger.setLevel(logging.WARNING)
console_logger.setFormatter(formatter)

logger = logging.getLogger(LOGGER_NAME)
# set logger to lowest, the handlers can then decide on their own
logger.setLevel(logging.DEBUG)

logger.addHandler(console_logger)
logger.addHandler(file_logger)


def exc_handler(exc_type: type[BaseException], value: BaseException, tb: types.TracebackType | None) -> None:
    """
    include exceptions in the logger
    https://docs.python.org/3/library/sys.html#sys.excepthook
    """
    logger.critical(value, exc_info=(exc_type, value, tb))
    # original hook value is stored here
    # https://docs.python.org/3/library/sys.html#sys.__excepthook__
    sys.__excepthook__(exc_type, value, tb)


sys.excepthook = exc_handler
