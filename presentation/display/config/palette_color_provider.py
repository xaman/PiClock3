from domain.colors import Colors, Color
from presentation.display.config.color_provider import ColorProvider


class PaletteColorProvider(ColorProvider):
    index = 0

    def __init__(self):
        """
        https://coolors.co/0096ff-00ff00-ffc800-ff6400-ff3200
        """
        super(PaletteColorProvider, self).__init__()
        self.palette = [
            Colors.ELECTRIC_GREEN,
            Colors.SAFETY_ORANGE,
            Colors.COQUELICOT,
            Colors.RED,
        ]

    def get_color(self):
        new_pos = self.index % len(self.palette)
        self.index += 1
        return self.palette[new_pos]
