#!/usr/bin/env python3
import logging.config
import config
from presentation.display import Display

logger = logging.getLogger()
display = Display()


def _main():
    try:
        _setup_logging()
        display.start()
    except KeyboardInterrupt:
        pass


def _setup_logging():
    try:
        logging.config.fileConfig(config.LOGGING_CONFIG)
    except AttributeError:
        pass


if __name__ == '__main__':
    _main()
