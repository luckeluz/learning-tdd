from money import Money
from portfolio import Portfolio

import unittest


class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = tenEuros.times(2)
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision, actualMoneyAfterDivision)

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, 'USD')
        fifteenDollars = Money(15, 'USD')
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate('USD'))

    def testAdditionofDollarsAndEuros(self):
        fiveDollars = Money(5, 'USD')
        tenEuros = Money(10, 'EUR')
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, 'USD')
        actualValue = portfolio.evaluate('USD')
        self.assertEqual(expectedValue, actualValue, f'{expectedValue} != {actualValue}')

    def testAdditionofdollarsAndWons(self):
        oneDollar = Money(1, 'USD')
        elevenHundredWon = Money(1100, 'KRW')
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundredWon)
        expectedValue = Money(2200, 'KRW')
        actualValue = portfolio.evaluate('KRW')
        self.assertEqual(expectedValue, actualValue, f'{expectedValue} != {actualValue}')


if __name__ == '__main__':
    unittest.main()
