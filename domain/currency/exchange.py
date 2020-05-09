class Exchange(object):

    def __init__(self, json):
        self.rates = json["rates"]

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
