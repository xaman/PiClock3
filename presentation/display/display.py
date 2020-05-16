import logging
import time
import config
import numpy
from unicornhatmini import UnicornHATMini
from PIL import Image, ImageDraw, ImageFont

from resources.fonts import font5x7


class Display(object):
    MINIMUM_BRIGHTNESS = 0.02
    MAXIMUM_BRIGHTNESS = 1.0
    DEFAULT_ROTATION = 180
    DEFAULT_BRIGHTNESS = 0.2
    TEXT_DELAY = 0.03

    logger = logging.getLogger('presentation')
    unicornhatmini = None
    font_path = str(config.PROJECT_ROOT / 'resources/ttf/5x7.ttf')
    font = ImageFont.truetype(font_path, 8)
    font_array = font5x7

    def __init__(self, color_provider):
        hat = UnicornHATMini()
        hat.set_rotation(self.DEFAULT_ROTATION)
        hat.set_brightness(self.DEFAULT_BRIGHTNESS)
        self.display_width, self.display_height = hat.get_shape()
        self.unicornhatmini = hat
        self.color_provider = color_provider

    def get_color(self):
        return self.color_provider.get_color()

    def set_brightness(self, brightness):
        if self.MINIMUM_BRIGHTNESS <= brightness <= self.MAXIMUM_BRIGHTNESS:
            self.unicornhatmini.set_brightness(brightness)

    def set_pixel(self, x, y, color=None):
        pixel_color = color if color is not None else self.get_color()
        if 0 <= x < self.display_width and 0 <= y < self.display_height:
            self.unicornhatmini.set_pixel(x, y, pixel_color.r, pixel_color.g, pixel_color.b)

    def show_text(self, text, color=None):
        """
        This method comes from the Unicorn Mini Hat examples.
        It uses the PIL library to convert a text into an image
        with an specific TTF font.
        """
        # Measure the size of our text, we only really care about the width for the moment
        # but we could do line-by-line scroll if we used the height
        text_width, text_height = self.font.getsize(text)
        # Create a new PIL image big enough to fit the text
        image = Image.new('P', (text_width + self.display_width + self.display_width, self.display_height), 0)
        draw = ImageDraw.Draw(image)
        # Draw the text into the image
        draw.text((self.display_width, -1), text, font=self.font, fill=255)
        self._scroll_array(lambda x, y: image.getpixel((x, y)), image.size[0], color)

    def show_text2(self, text, color=None):
        """
        Converts every character of the text into an array
        from the font included in the Scroll pHat library.
        It looks worse than the TTF solution but it is more
        flexible.
        """
        array = self._char_array(text[0])
        for pos in range(1, len(text)):
            char_arr = self._char_array(text[pos])
            if char_arr:
                array = numpy.concatenate((array, char_arr), axis=1)
        self._scroll_array(lambda x, y: array[y][x], len(array[0]), color)

    def _char_array(self, char):
        """
        Converts the char into a two dimensions array
        """
        font = self.font_array.data
        if char in font:
            char_arr = font[char]
        elif type(char) is not int and ord(char) in font:
            char_arr = font[ord(char)]
        else:
            char_arr = None
        if char_arr:
            return self._char_array_fix_rows(char_arr)

    def _char_array_fix_rows(self, char_arr):
        """
        Adds rows filled with zeros to the char arrays with less
        rows than the display height
        """
        num_rows = len(char_arr)
        num_cols = len(char_arr[0])
        if num_rows != self.display_height:
            for n in range(num_rows, self.display_height):
                char_arr.append([0 for i in range(num_cols)])
        return char_arr

    def _scroll_array(self, array_values, array_width, color=None):
        text_color = color if color is not None else self.get_color()
        offset_x = 0
        while True:
            for y in range(self.display_height):
                for x in range(self.display_width):
                    if array_values(x + offset_x, y) == 255:
                        self.unicornhatmini.set_pixel(x, y, text_color.r, text_color.g, text_color.b)
                    else:
                        self.unicornhatmini.set_pixel(x, y, 0, 0, 0)
            offset_x += 1
            if offset_x + self.display_width > array_width:
                break
            self.unicornhatmini.show()
            time.sleep(self.TEXT_DELAY)

    def refresh(self):
        self.unicornhatmini.show()

    def _log(self, message):
        self.logger.debug(message)
