from presentation.views.view import View


class WeatherView(View):

    def __init__(self, display, global_color):
        super(WeatherView, self).__init__(display, global_color)

    def prepare(self):
        self._log("Getting weather")

    def show(self):
        self.display.show_text("London, sunny as fuck!", self.global_color)
