import logging

from domain.colors import Colors
from presentation.views.clock_view import ClockView
from presentation.views.date_view import DateView


class DisplayPresenter(object):
    GLOBAL_COLOR = Colors.YELLOW
    GLOBAL_BRIGHTNESS = 0.05
    views_count = 0
    logger = logging.getLogger()

    def __init__(self, display):
        display.set_brightness(self.GLOBAL_BRIGHTNESS)
        self.display = display

    def start(self):
        self.loop()

    def loop(self):
        view = self.next_view()
        while True:
            view.show()
            self.views_count += 1
            view = self.next_view()

    def next_view(self):
        pos = self.views_count % 2
        if pos == 0:
            return ClockView(self.display, self.GLOBAL_COLOR)
        elif pos == 1:
            return DateView(self.display, self.GLOBAL_COLOR)
