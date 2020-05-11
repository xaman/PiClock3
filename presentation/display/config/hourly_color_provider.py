from datetime import datetime

from domain.colors import Colors
from presentation.display.config.color_provider import ColorProvider


class HourlyColorProvider(ColorProvider):
    position = 0

    def __init__(self):
        super(HourlyColorProvider, self).__init__()

        self.configs = {
            0: Colors.FUCHSIA,
            1: Colors.FUCHSIA,
            2: Colors.FUCHSIA,
            3: Colors.WHITE,
            4: Colors.WHITE,
            5: Colors.WHITE,
            6: Colors.WHITE,
            7: Colors.ULTRAMARINE_BLUE,
            8: Colors.ULTRAMARINE_BLUE,
            9: Colors.DODGER_BLUE,
            10: Colors.DODGER_BLUE,
            11: Colors.ELECTRIC_GREEN,
            12: Colors.ELECTRIC_GREEN,
            13: Colors.KELLY_GREEN,
            14: Colors.MIKADO_YELLOW,
            15: Colors.SAFETY_ORANGE,
            16: Colors.COQUELICOT,
            17: Colors.IMPERIAL_RED,
            18: Colors.RED,
            19: Colors.RED,
            20: Colors.FUCHSIA,
            21: Colors.FUCHSIA,
            22: Colors.FUCHSIA,
            23: Colors.FUCHSIA
        }

    def get_color(self):
        hour = datetime.now().hour
        return self.configs[hour]
