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
            Colors.WHITE,
            Colors.ULTRAMARINE_BLUE,
            Colors.DODGER_BLUE,
            Colors.ELECTRIC_GREEN,
            Colors.KELLY_GREEN,
            Colors.MIKADO_YELLOW,
            Colors.SAFETY_ORANGE,
            Colors.COQUELICOT,
            Colors.CANDY_APPLE_RED,
            Colors.IMPERIAL_RED,
            Colors.FUCHSIA
        ]

    def get_color(self):
        new_pos = self.index % len(self.palette)
        self.index += 1
        return self.palette[new_pos]
