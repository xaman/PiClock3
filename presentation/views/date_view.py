import logging
import time

from domain.colors import Colors
from presentation.views.view import View


class DateView(View):
    DATE_FORMAT = "%a, %-d %b '%y"

    logger = logging.getLogger("views")

    def __init__(self, display):
        super(DateView, self).__init__(display)

    def show(self):
        formatted = time.strftime(self.DATE_FORMAT)
        self.logger.debug(self.__class__.__name__ + " - " + formatted)
        self.display.show_text(formatted, Colors.GREY)
