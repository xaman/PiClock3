#!/usr/bin/env python3
import logging.config
import config
from presentation.display.config.hourly_color_provider import HourlyColorProvider
from presentation.display.display import Display
from presentation.display.display_presenter import DisplayPresenter

logger = logging.getLogger()
display = Display(color_provider=HourlyColorProvider())
displayPresenter = DisplayPresenter(display)


def _main():
    try:
        _setup_logging()
        displayPresenter.start()
    except KeyboardInterrupt:
        pass


def _setup_logging():
    try:
        logging.config.fileConfig(config.LOGGING_CONFIG)
    except AttributeError:
        pass


if __name__ == '__main__':
    _main()
