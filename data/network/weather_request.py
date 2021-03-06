import json

from data.network.request import Request
from domain.weather.temperature_unit import TemperatureUnit
from domain.weather.weather import Weather


class WeatherRequest(Request):
    _ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
    _PARAMS = "?q={location}&units={unit}"
    _TOKEN = "&APPID=73d340307ca960288fcd451e50891737"

    def __init__(self, location_name, temperature_unit=TemperatureUnit.CELSIUS):
        url = self._ENDPOINT + self._get_params(location_name, temperature_unit) + self._TOKEN
        super(WeatherRequest, self).__init__(url)

    def _get_params(self, location_name, temperature_unit):
        return self._PARAMS.format(location=location_name, unit=temperature_unit)

    def execute(self, callback):
        response = self.get().response()
        if response:
            json_response = json.loads(response)
            weather = Weather(json_response)
            callback(weather)
        else:
            callback(None)
