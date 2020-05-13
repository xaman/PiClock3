from presentation.display.display import Display


class BrightnessProvider(object):

    current_brightness = Display.DEFAULT_BRIGHTNESS

    def __init__(self, display):
        super(BrightnessProvider, self).__init__()
        self.display = display

    def get_brightness(self):
        raise NotImplementedError("Class %s doesn't implement get_brightness()" % self.__class__.__name__)

    def update_brightness(self):
        raise NotImplementedError("Class %s doesn't implement update_brightness()" % self.__class__.__name__)
