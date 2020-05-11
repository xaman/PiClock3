from domain.weather.temperature_unit import TemperatureUnit
from presentation.views.view import View


class WeatherView(View):

    def __init__(self, display, repository):
        super(WeatherView, self).__init__(display)
        self.repository = repository

    def show(self):
        """
        Shows the name of the city, the temperature and the list of conditions
        :return: London, 22C, overcast
        """
        if self.repository.data:
            weather = self.repository.data
            city = weather.name
            temperature = int(weather.temperature.value)
            unit = self._get_temperature_unit()
            conditions = ""
            for condition in weather.conditions:
                conditions += ", " + condition.description
            forecast = "%s, %s%s%s" % (city, temperature, unit, conditions)
            self._log(forecast)
            self.display.show_text(forecast)

    def _get_temperature_unit(self):
        return "C" if self.repository.temperature_unit == TemperatureUnit.CELSIUS else "F"
