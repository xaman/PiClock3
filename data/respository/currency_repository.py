import schedule
from data.network.currency_request import CurrencyRequest
from data.respository.repository import Repository


class CurrencyRepository(Repository):
    _SCHEDULE_MINUTES = 60

    def __init__(self, base_currency):
        super(CurrencyRepository, self).__init__()
        self.base_currency = base_currency

    def initialize(self):
        self._request_data()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_data)

    def _request_data(self):
        request = CurrencyRequest(self.base_currency)
        request.execute(self.on_data)
