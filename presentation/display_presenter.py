import logging
import schedule

from data.respository.currency_repository import CurrencyRepository
from data.respository.weather_repository import WeatherRepository
from domain.colors import Colors
from domain.currency.currencies import Currencies
from presentation.views.clock_view import ClockView
from presentation.views.currency_view import CurrencyView
from presentation.views.date_view import DateView
from presentation.views.weather_view import WeatherView


class DisplayPresenter(object):
    GLOBAL_COLOR = Colors.DARK_MAGENTA
    GLOBAL_BRIGHTNESS = 1.0
    LOCATION = "London,uk"
    CURRENCY = Currencies.GBP

    index = 0
    logger = logging.getLogger()
    weather_repository = WeatherRepository(LOCATION)
    currency_repository = CurrencyRepository(CURRENCY)

    def __init__(self, display):
        display.set_brightness(self.GLOBAL_BRIGHTNESS)
        self.display = display

    def start(self):
        self._initialize_repositories()
        self._loop()

    def _initialize_repositories(self):
        self.weather_repository.initialize()
        self.currency_repository.initialize()

    def _loop(self):
        current_view = self.create_view(self.index)
        while True:
            next_view = self.create_view(self.index + 1)
            current_view.show()
            current_view.clean()
            self.index += 1
            current_view = next_view
            self._scheduler_run_pending()

    def _scheduler_run_pending(self):
        self.logger.debug("Running pending tasks...")
        schedule.run_pending()

    def create_view(self, position):
        view_type = position % 6
        if position % 2 == 0:
            return ClockView(self.display, self.GLOBAL_COLOR)
        elif view_type == 1:
            return DateView(self.display, self.GLOBAL_COLOR)
        elif view_type == 3:
            return WeatherView(self.display, self.GLOBAL_COLOR, self.weather_repository)
        elif view_type == 5:
            return CurrencyView(self.display, self.GLOBAL_COLOR, self.currency_repository, self.CURRENCY,
                                Currencies.EUR)
