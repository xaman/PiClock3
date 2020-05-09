import logging

from presentation.views.clock_view import ClockView
from presentation.views.date_view import DateView


class DisplayPresenter(object):
    views_count = 0
    logger = logging.getLogger()

    def __init__(self, display):
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
            return ClockView(self.display)
        elif pos == 1:
            return DateView(self.display)
