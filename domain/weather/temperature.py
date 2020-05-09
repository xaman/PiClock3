class Temperature(object):

    def __init__(self, json):
        self.value = json["temp"]
        self.temp_min = json["temp_min"]
        self.temp_max = json["temp_max"]
        self.humidity = json["humidity"]
        self.pressure = json["pressure"]
