import logging


class Repository(object):
    logger = logging.getLogger("data")

    def __init__(self):
        self.data = None

    def initialize(self):
        raise NotImplementedError("Class %s doesn't implement initialize()" % self.__class__.__name__)

    def is_empty(self):
        return self.data is None
