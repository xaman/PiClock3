import logging

from presentation.views.clock import Clock


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
        return Clock(self.display)
