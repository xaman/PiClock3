from presentation.views.view import View


class WeatherView(View):

    def __init__(self, display, global_color, repository):
        super(WeatherView, self).__init__(display, global_color)
        self.repository = repository

    def show(self):
        if not self.repository.is_empty():
            weather = self.repository.data
            if len(weather.locations) > 0:
                location = weather.locations[0]
                self.display.show_text(location.name, self.global_color)
