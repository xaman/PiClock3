from domain.weather.condition import Condition
from domain.weather.location import Location
from domain.weather.temperature_unit import TemperatureUnit


class Weather(object):
    def __init__(self, json):
        self.temperature_unit = TemperatureUnit(json["units"]["temperature"])
        self.condition = Condition(json["item"]["condition"])
        self.location = Location(json["location"])

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
