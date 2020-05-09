import logging

from domain.colors import Colors
from presentation.views.clock_view import ClockView
from presentation.views.date_view import DateView


class DisplayPresenter(object):
    GLOBAL_COLOR = Colors.YELLOW
    GLOBAL_BRIGHTNESS = 0.05
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
            self.index += 1
            current_view = next_view

    def create_view(self, position):
        type = position % 2
        if type == 0:
            return ClockView(self.display, self.GLOBAL_COLOR)
        elif type == 1:
            return DateView(self.display, self.GLOBAL_COLOR)
