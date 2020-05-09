import time

from presentation.views.view import View


class DateView(View):
    DATE_FORMAT = "%a, %-d %b '%y"

    def __init__(self, display, global_color):
        super(DateView, self).__init__(display, global_color)

    def show(self):
        formatted = time.strftime(self.DATE_FORMAT)
        self._log(formatted)
        self.display.show_text(formatted, self.global_color)
