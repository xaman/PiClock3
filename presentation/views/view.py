import logging


class View(object):
    display = None
    global_color = None
    logger = logging.getLogger("views")

    def __init__(self, display, global_color):
        self.display = display
        self.global_color = global_color

    def prepare(self):
        self._log("Preparing...")

    def show(self):
        raise NotImplementedError("Class %s does not implement show()" % self.__class__.__name__)

    def clean(self):
        self._log("Cleaning...")

    def _log(self, message):
        self.logger.debug(self.__class__.__name__ + " - " + message)
