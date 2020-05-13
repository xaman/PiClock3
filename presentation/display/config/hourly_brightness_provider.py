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
            8: 0.5,
            9: 0.5,
            10: 0.5,
            11: 0.5,
            12: 0.5,
            13: 0.5,
            14: 0.4,
            15: 0.4,
            16: 0.4,
            17: 0.4,
            18: 0.4,
            19: 0.05,
            20: 0.05,
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