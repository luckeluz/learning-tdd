from money import Money
from bank import Bank


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys: Money):
        self.moneys.extend(moneys)

    def evaluate(self, bank: Bank, currency: str):
        total = Money(0, currency)
        failures = ''
        for m in self.moneys:
            c, k = bank.convert(m, currency)
            if k is None:
                total += c
            else:
                failures += k if not failures else ',' + k

        if not failures:
            return total

        raise Exception('Missing exchange rate(s):[' + failures + ']')
