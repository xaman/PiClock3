import schedule
from data.network.weather_request import WeatherRequest
from data.respository.repository import Repository
from domain.weather.temperature_unit import TemperatureUnit


class WeatherRepository(Repository):
    _SCHEDULE_MINUTES = 15

    def __init__(self, location_name, temperature_unit=TemperatureUnit.CELSIUS):
        super(WeatherRepository, self).__init__()
        self.location_name = location_name
        self.temperature_unit = temperature_unit

    def initialize(self):
        self._request_data()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_data)

    def _request_data(self):
        request = WeatherRequest(self.location_name)
        request.execute(self.on_data)

