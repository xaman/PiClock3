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
    BLACK = Color(0, 0, 0)
    GREY = Color(20, 20, 20)
    WHITE = Color(255, 255, 255)
    RED = Color(255, 0, 0)
    PINK = Color(255, 51, 153)
    YELLOW = Color(255, 255, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)
