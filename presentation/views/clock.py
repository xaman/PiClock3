from presentation.views.view import View
import time


class Clock(View):
    DURATION_SECONDS = 4
    WAIT_SECONDS = 1
    FORMAT_HOUR = "%H"
    FORMAT_MINUTES = "%M"

    def __init__(self, display):
        super(Clock, self).__init__(display)

    def show(self):
        hour = time.strftime(self.FORMAT_HOUR)
        minutes = time.strftime(self.FORMAT_HOUR)
        for i in range(0, self.DURATION_SECONDS):
            # Changes dots blink every second
            dots = ":" if (i % 2 == 0) else " "
            formatted_time = hour + dots + minutes
            print(formatted_time)
            self._show_time(formatted_time)
            time.sleep(self.WAIT_SECONDS)

    @staticmethod
    def _show_time(formatted_time):
        formatted_time = "10:01"
        digit0 = int(formatted_time[0])
        digit1 = int(formatted_time[1])
        dots = formatted_time[2]
        digit2 = int(formatted_time[3])
        digit3 = int(formatted_time[4])
