import logging

formatter = logging.Formatter("[{asctime:<23}] [{levelname:<8}] [{threadName}][{module}.{funcName}] {message}", style="{")

# init one normal filehandler and a stream-handler for stdout
file_logger = logging.FileHandler("events.log")
file_logger.setLevel(logging.DEBUG)
file_logger.setFormatter(formatter)

console_logger = logging.StreamHandler()
console_logger.setLevel(logging.WARNING)
console_logger.setFormatter(formatter)

logger = logging.getLogger("my_logger")
# set logger to lowest, the handlers can then decide on their own
logger.setLevel(logging.DEBUG)

logger.addHandler(console_logger)
logger.addHandler(file_logger)


if __name__ == '__main__':
    logger.debug("Debug")
    logger.info("Info")
    logger.warning("Warning!")
    logger.error("Error!")
    logger.critical("CRITICAL")
    print(len("2024-09-12 00:18:26,775"))