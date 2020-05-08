import logging

from unicornhatmini import UnicornHATMini


class Display(object):
    DEFAULT_BRIGHTNESS = 0.02
    DEFAULT_ROTATION = 0

    logger = logging.getLogger()

    unicornhatmini = None

    def __init__(self):
        hat = UnicornHATMini()
        hat.set_rotation(self.DEFAULT_ROTATION)
        hat.set_brightness(self.DEFAULT_BRIGHTNESS)
        self.display_width, self.display_height = hat.get_shape()
        self.unicornhatmini = hat

    def set_pixel(self, x, y, color):
        # self.logger.debug("Setting pixel %d,%d to %d,%d,%d" % (x, y, color.r, color.g, color.b))
        if 0 <= x < self.display_width and 0 <= y < self.display_height:
            self.unicornhatmini.set_pixel(x, y, color.r, color.g, color.b)

    def refresh(self):
        self.unicornhatmini.show()
