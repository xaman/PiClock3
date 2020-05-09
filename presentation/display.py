import logging
import time

from unicornhatmini import UnicornHATMini
from PIL import Image, ImageDraw, ImageFont


class Display(object):
    DEFAULT_BRIGHTNESS = 0.02
    DEFAULT_ROTATION = 0

    logger = logging.getLogger()
    unicornhatmini = None
    font = ImageFont.truetype("resources/ttf/5x7.ttf", 8)

    def __init__(self):
        hat = UnicornHATMini()
        hat.set_rotation(self.DEFAULT_ROTATION)
        hat.set_brightness(self.DEFAULT_BRIGHTNESS)
        self.display_width, self.display_height = hat.get_shape()
        self.unicornhatmini = hat

    def set_pixel(self, x, y, color):
        if 0 <= x < self.display_width and 0 <= y < self.display_height:
            self.unicornhatmini.set_pixel(x, y, color.r, color.g, color.b)

    def show_text(self, text, color):
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
                        self.unicornhatmini.set_pixel(x, y, color.r, color.g, color.b)
                    else:
                        self.unicornhatmini.set_pixel(x, y, 0, 0, 0)
            offset_x += 1
            if offset_x + self.display_width > image.size[0]:
                break
            self.unicornhatmini.show()
            time.sleep(0.05)

    def refresh(self):
        self.unicornhatmini.show()
