import logging
from logging import Logger


def get_logger() -> Logger:
    # Defines configuration variables
    level = logging.DEBUG
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Initiate Logger instance
    logger = logging.getLogger(__file__)
    logger.setLevel(level=level)

    # Initiate handlers
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt=formatter)

    # Add handlers to initiated Logger instance
    logger.addHandler(hdlr=stream_handler)

    return logger
