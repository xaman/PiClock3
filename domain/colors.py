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
    WHITE = Color(255, 255, 255)
