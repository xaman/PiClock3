import logging


class View(object):
    display = None
    logger = logging.getLogger('presentation')

    def __init__(self, display):
        self.display = display

    def show(self):
        raise NotImplementedError("Class %s does not implement show()" % self.__class__.__name__)

    def clean(self):
        self._log("Cleaning...")

    def _log(self, message):
        self.logger.debug(self.__class__.__name__ + " - " + message)
