from data.network.weather_request import WeatherRequest
from presentation.views.view import View


class WeatherView(View):

    def __init__(self, display, global_color, location):
        super(WeatherView, self).__init__(display, global_color)
        self.location_name = location

    def prepare(self):
        request = WeatherRequest(self.location_name)
        request.execute(self._on_weather)

    def _on_weather(self, weather):
        self.weather = weather

    def show(self):
        self.display.show_text("London, sunny as fuck!", self.global_color)
