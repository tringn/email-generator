"""Logger module for the app."""

import logging

__all__ = ["get_logger"]


formatter = "%(asctime)s - %(funcName)s - %(filename)s - %(levelname)s - %(message)s"


def get_logger(name: str):
    """
    Get logger instance.

    Args:
        name: logger name
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    ch_format = logging.Formatter(formatter)
    console_handler.setFormatter(ch_format)

    logger.addHandler(console_handler)

    return logger
