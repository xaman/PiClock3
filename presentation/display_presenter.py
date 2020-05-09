import logging

from domain.colors import Colors
from presentation.views.clock_view import ClockView
from presentation.views.date_view import DateView
from presentation.views.weather_view import WeatherView


class DisplayPresenter(object):
    GLOBAL_COLOR = Colors.BROWN
    GLOBAL_BRIGHTNESS = 0.1
    LOCATION = "London"

    index = 0
    logger = logging.getLogger()

    def __init__(self, display):
        display.set_brightness(self.GLOBAL_BRIGHTNESS)
        self.display = display

    def start(self):
        self.loop()

    def loop(self):
        current_view = self.create_view(self.index)
        while True:
            next_view = self.create_view(self.index + 1)
            next_view.prepare()
            current_view.show()
            current_view.clean()
            self.index += 1
            current_view = next_view

    def create_view(self, position):
        view_type = position % 4
        if view_type in [0, 2]:
            return ClockView(self.display, self.GLOBAL_COLOR)
        elif view_type == 3:
            return DateView(self.display, self.GLOBAL_COLOR)
        elif view_type == 1:
            return WeatherView(self.display, self.GLOBAL_COLOR, self.LOCATION)
