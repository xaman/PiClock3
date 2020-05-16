import logging
import schedule

from data.respository.currency_repository import CurrencyRepository
from data.respository.trending_repository import TrendingRepository
from data.respository.weather_repository import WeatherRepository
from domain.currency.currencies import Currencies
from presentation.display.config.hourly_brightness_provider import HourlyBrightnessProvider
from presentation.formatter.text_formatter import TextFormatter
from presentation.views.clock_view import ClockView
from presentation.views.currency_view import CurrencyView
from presentation.views.date_view import DateView
from presentation.views.trending_view import TrendingView
from presentation.views.weather_view import WeatherView


class DisplayPresenter(object):
    LOCATION = "London,uk"
    CURRENCY = Currencies.GBP
    WOEID = "23424950"

    index = 0
    logger = logging.getLogger('presentation')
    weather_repository = WeatherRepository(LOCATION)
    currency_repository = CurrencyRepository(CURRENCY)
    trending_repository = TrendingRepository(WOEID)

    def __init__(self, display):
        self.display = display
        self.brightness_provider = HourlyBrightnessProvider(display)

    def start(self):
        self._initialize_repositories()
        self._loop()

    def _initialize_repositories(self):
        self.weather_repository.initialize()
        self.currency_repository.initialize()
        self.trending_repository.initialize()

    def _loop(self):
        current_view = self.create_view(self.index)
        while True:
            self.brightness_provider.update_brightness()
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
        view_type = position % 8
        if position % 2 == 0:
            return ClockView(self.display)
        elif view_type == 1:
            return DateView(self.display)
        elif view_type == 3:
            return WeatherView(self.display, self.weather_repository)
        elif view_type == 5:
            return CurrencyView(self.display, self.currency_repository, self.CURRENCY, Currencies.EUR)
        elif view_type == 7:
            return TrendingView(self.display, self.trending_repository, TextFormatter())
