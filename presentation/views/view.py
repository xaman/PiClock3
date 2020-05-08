class View(object):

    listener = None

    def prepare(self):
        pass

    def show(self):
        raise NotImplementedError("Class %s does not implement show()" % self.__class__.__name__)

    def clean(self):
        pass
