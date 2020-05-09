import schedule
from data.network.weather_request import WeatherRequest
from data.respository.repository import Repository


class WeatherRepository(Repository):
    _SCHEDULE_MINUTES = 15

    def __init__(self, location_name):
        super(WeatherRepository, self).__init__()
        self.location_name = location_name

    def initialize(self):
        self._request_data()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_data)

    def _request_data(self):
        request = WeatherRequest(self.location_name)
        request.execute(self._on_result)

    def _on_result(self, data):
        self.data = data
        self.logger.debug("Data: " + str(data))
