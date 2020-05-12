from random import choice


class Color(object):

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class RandomColor(Color):

    def __init__(self):
        r = choice(range(0, 255))
        g = choice(range(0, 255))
        b = choice(range(0, 255))
        super(RandomColor, self).__init__(r, g, b)


class Colors:
    """
    Palette of RGB colors: https://coolors.co/
    """
    WHITE = Color(255, 255, 255)
    BLACK = Color(0, 0, 0)
    ULTRAMARINE_BLUE = Color(0, 100, 255)
    DODGER_BLUE = Color(0, 150, 255)
    ELECTRIC_GREEN = Color(0, 255, 0)
    KELLY_GREEN = Color(100, 200, 0)
    MIKADO_YELLOW = Color(255, 200, 0)
    SAFETY_ORANGE = Color(255, 100, 0)
    COQUELICOT = Color(255, 50, 0)
    CANDY_APPLE_RED = Color(255, 25, 0)
    IMPERIAL_RED = Color(255, 0, 50)
    RED = Color(255, 0, 0)
    FUCHSIA = Color(255, 0, 255)
