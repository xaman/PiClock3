from presentation.views.view import View
import time


class Clock(View):
    DURATION_SECONDS = 4
    WAIT_SECONDS = 1
    FORMAT_HOUR = "%H"
    FORMAT_MINUTES = "%M"

    def show(self):
        hour = time.strftime(self.FORMAT_HOUR)
        minutes = time.strftime(self.FORMAT_HOUR)
        for i in range(0, self.DURATION_SECONDS):
            # Changes dots blink every second
            dots = ":" if (i % 2 == 0) else " "
            print(hour + dots + minutes)
            time.sleep(self.WAIT_SECONDS)
