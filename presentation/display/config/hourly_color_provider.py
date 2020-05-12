from datetime import datetime

from domain.colors import Colors
from presentation.display.config.color_provider import ColorProvider


class HourlyColorProvider(ColorProvider):
    position = 0

    def __init__(self):
        super(HourlyColorProvider, self).__init__()

        self.configs = {
            0: Colors.WHITE,
            1: Colors.WHITE,
            2: Colors.WHITE,
            3: Colors.WHITE,
            4: Colors.WHITE,
            5: Colors.WHITE,
            6: Colors.WHITE,
            7: Colors.WHITE,
            8: Colors.WHITE,
            9: Colors.ELECTRIC_GREEN,
            10: Colors.ELECTRIC_GREEN,
            11: Colors.ELECTRIC_GREEN,
            12: Colors.SAFETY_ORANGE,
            13: Colors.SAFETY_ORANGE,
            14: Colors.SAFETY_ORANGE,
            15: Colors.COQUELICOT,
            16: Colors.COQUELICOT,
            17: Colors.COQUELICOT,
            18: Colors.RED,
            19: Colors.RED,
            20: Colors.RED,
            21: Colors.WHITE,
            22: Colors.WHITE,
            23: Colors.WHITE
        }

    def get_color(self):
        hour = datetime.now().hour
        return self.configs[hour]
