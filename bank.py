from money import Money


class Bank:
    def __init__(self):
        self.exchangeRates = dict()

    def add_exchange_rate(self, currency_from: str, currency_to: str, rate: float):
        key = currency_from + '->' + currency_to
        self.exchangeRates[key] = rate

    def convert(self, a_money: Money, a_currency: str):
        if a_money.currency == a_currency:
            return Money(a_money.amount, a_currency), None

        key = a_money.currency + '->' + a_currency
        if key in self.exchangeRates:
            return Money(a_money.amount * self.exchangeRates[key], a_currency), None

        return None, key
