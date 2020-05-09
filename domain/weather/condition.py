class Condition(object):

    def __init__(self, json):
        self.id = json["id"]
        self.name = json["main"]
        self.description = json["description"]

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
