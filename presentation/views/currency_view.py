from presentation.views.view import View


class CurrencyView(View):

    def __init__(self, display, global_color, repository, from_currency, to_currency):
        super(CurrencyView, self).__init__(display, global_color)
        self.repository = repository
        self.from_currency = from_currency
        self.to_currency = to_currency

    def show(self):
        exchange = self.repository.data
        if exchange:
            conversion = exchange.rates[self.to_currency]
            text = "%s-%s: %.3f" % (self.from_currency, self.to_currency, conversion)
            self._log(text)
            self.display.show_text(text, self.global_color)
