class ColorProvider(object):

    def __init__(self):
        super(ColorProvider, self).__init__()

    def get_color(self):
        raise NotImplementedError("Class %s doesn't implement get_color()" % self.__class__.__name__)
