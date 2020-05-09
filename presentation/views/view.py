class View(object):

    display = None
    global_color = None

    def __init__(self, display, global_color):
        self.display = display
        self.global_color = global_color

    def prepare(self):
        pass

    def show(self):
        raise NotImplementedError("Class %s does not implement show()" % self.__class__.__name__)

    def clean(self):
        pass
