from domain.weather.location import Location


class Weather(object):

    def __init__(self, json):
        self.message = json["message"]
        self.code = json["cod"]
        self.locations = []
        for location in json["list"]:
            self.locations.append(Location(location))

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
