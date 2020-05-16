import logging
import time
import config
from unicornhatmini import UnicornHATMini
from PIL import Image, ImageDraw, ImageFont


class Display(object):
    MINIMUM_BRIGHTNESS = 0.02
    MAXIMUM_BRIGHTNESS = 1.0
    DEFAULT_ROTATION = 180
    DEFAULT_BRIGHTNESS = 0.2
    TEXT_DELAY = 0.03

    logger = logging.getLogger()
    unicornhatmini = None
    font_path = str(config.PROJECT_ROOT / 'resources/ttf/5x7.ttf')
    font = ImageFont.truetype(font_path, 8)

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
        text_color = color if color is not None else self.get_color()
        # Measure the size of our text, we only really care about the width for the moment
        # but we could do line-by-line scroll if we used the height
        text_width, text_height = self.font.getsize(text)
        # Create a new PIL image big enough to fit the text
        image = Image.new('P', (text_width + self.display_width + self.display_width, self.display_height), 0)
        draw = ImageDraw.Draw(image)
        # Draw the text into the image
        draw.text((self.display_width, -1), text, font=self.font, fill=255)
        offset_x = 0
        while True:
            for y in range(self.display_height):
                for x in range(self.display_width):
                    if image.getpixel((x + offset_x, y)) == 255:
                        self.unicornhatmini.set_pixel(x, y, text_color.r, text_color.g, text_color.b)
                    else:
                        self.unicornhatmini.set_pixel(x, y, 0, 0, 0)
            offset_x += 1
            if offset_x + self.display_width > image.size[0]:
                break
            self.unicornhatmini.show()
            time.sleep(self.TEXT_DELAY)

    def refresh(self):
        self.unicornhatmini.show()
