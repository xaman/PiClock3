from domain.weather.condition import Condition
from domain.weather.temperature import Temperature


class Location(object):

    def __init__(self, json):
        self.id = json["id"]
        self.name = json["name"]
        self.temperature = Temperature(json["main"])
        self.conditions = []
        for condition in json["weather"]:
            self.conditions.append(Condition(condition))

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
