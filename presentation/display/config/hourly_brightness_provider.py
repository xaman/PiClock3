from datetime import datetime

from presentation.display.config.brigthness_provider import BrightnessProvider
from presentation.display.display import Display


class HourlyBrightnessProvider(BrightnessProvider):

    def __init__(self, display):
        super(HourlyBrightnessProvider, self).__init__(display)
        self.configs = {
            0: Display.MINIMUM_BRIGHTNESS,
            1: Display.MINIMUM_BRIGHTNESS,
            2: Display.MINIMUM_BRIGHTNESS,
            3: Display.MINIMUM_BRIGHTNESS,
            4: Display.MINIMUM_BRIGHTNESS,
            5: Display.MINIMUM_BRIGHTNESS,
            6: Display.MINIMUM_BRIGHTNESS,
            7: Display.MINIMUM_BRIGHTNESS,
            8: 0.2,
            9: 0.2,
            10: 0.2,
            11: 0.2,
            12: 0.2,
            13: 0.2,
            14: 0.2,
            15: 0.2,
            16: 0.2,
            17: 0.2,
            18: 0.2,
            19: 0.2,
            20: 0.2,
            21: Display.MINIMUM_BRIGHTNESS,
            22: Display.MINIMUM_BRIGHTNESS,
            23: Display.MINIMUM_BRIGHTNESS
        }

    def get_brightness(self):
        hour = datetime.now().hour
        return self.configs[hour]

    def update_brightness(self):
        new_brightness = self.get_brightness()
        if new_brightness != self.current_brightness:
            self.display.set_brightness(new_brightness)
            self.current_brightness = new_brightness
