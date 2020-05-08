#!/usr/bin/env python3
import logging.config
import config

logger = logging.getLogger()


def _main():
    try:
        _setup_logging()
        logger.debug("Hello world!")
    except KeyboardInterrupt:
        pass


def _setup_logging():
    try:
        logging.config.fileConfig(config.LOGGING_CONFIG)
    except AttributeError:
        pass


if __name__ == '__main__':
    _main()
