class Condition(object):
    def __init__(self, json):
        self.temp = json["temp"]
        self.date = json["date"]
        self.text = json["text"]

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
