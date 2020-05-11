from domain.colors import Colors
from presentation.views.view import View
import time

from resources.fonts.rounded_numbers import ROUNDED_NUMBERS


class ClockView(View):
    DURATION_SECONDS = 4
    WAIT_SECONDS = 1
    FORMAT_HOUR = "%H"
    FORMAT_MINUTES = "%M"
    DOTS_NO = [[0], [0], [0], [0], [0], [0], [0]]
    DOTS_YES = [[0], [0], [1], [0], [1], [0], [0]]

    def __init__(self, display):
        super(ClockView, self).__init__(display)

    def show(self):
        pixel_color = self.display.get_color()
        hour = time.strftime(self.FORMAT_HOUR)
        minutes = time.strftime(self.FORMAT_MINUTES)
        for i in range(0, self.DURATION_SECONDS):
            # Changes dots blink every second
            dots = ":" if (i % 2 == 0) else " "
            formatted_time = hour + dots + minutes
            self._log(formatted_time)
            self._show_time(formatted_time, pixel_color)
            time.sleep(self.WAIT_SECONDS)

    def _show_time(self, formatted_time, pixel_color):
        h1, h2, dots, m1, m2 = formatted_time
        digit1 = self._convert_to_digit(h1)
        digit2 = self._convert_to_digit(h2)
        digit3 = self._convert_to_digit(m1)
        digit4 = self._convert_to_digit(m2)
        self._show_digit(0, 0, digit1, pixel_color)
        self._show_digit(4, 0, digit2, pixel_color)
        self._show_digit(9, 0, digit3, pixel_color)
        self._show_digit(13, 0, digit4, pixel_color)
        # Dots
        dots_value = self.DOTS_YES if dots == ":" else self.DOTS_NO
        self._show_digit(8, 0, dots_value, pixel_color)
        # Refreshes the display only once
        self.display.refresh()

    @staticmethod
    def _convert_to_digit(number):
        return ROUNDED_NUMBERS[int(number)]

    def _show_digit(self, x, y, digit, pixel_color):
        for row in range(0, len(digit)):
            for col in range(0, len(digit[0])):
                color = Colors.BLACK if digit[row][col] == 0 else pixel_color
                self.display.set_pixel(x + col, y + row, color)
