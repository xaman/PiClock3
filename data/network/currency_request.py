import json

from data.network.request import Request
from domain.currency.exchange import Exchange


class CurrencyRequest(Request):
    _URL = "https://api.exchangeratesapi.io/latest?base={currency}"

    def __init__(self, base_currency):
        url = self._URL.format(currency=base_currency)
        super(CurrencyRequest, self).__init__(url)

    def execute(self, callback):
        response = self.get().response()
        if response:
            json_response = json.loads(response)
            exchange = Exchange(json_response)
            callback(exchange)
        else:
            callback(None)
