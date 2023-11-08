import unittest
from io import StringIO

from PortfolioAnalyzer.portfolioanalyzer import PortfoliosAnalyzer


class TestPortfolioAnalyzer(unittest.TestCase):
    def setUp(self):
        self.portfolio_2021 = StringIO("""InstrumentId,Name,Date,Price
                                    A123,BondA,2021-10-29,100.0
                                    A456,BondB,2021-10-29,200.0
                                    A456,BondD,2021-10-29,200.0
                                    A789,BondC,2021-10-29,300.1""")

        self.portfolio_2022 = StringIO("""InstrumentId,Name,Date,Price
                                    A123,BondE,2022-10-29,100.0
                                    A456,BondB,2022-10-29,200.5
                                    A789,BondC,2022-10-29,300.2""")

    def test_count_lost_bonds_between_portfolios(self):
        self.assertFalse()

    def test_find_max_increased_bond(self):
        self.assertFalse()


if __name__ == '__main__':
    unittest.main()
