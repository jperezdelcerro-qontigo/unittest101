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
        # GIVEN
        fip = PortfoliosAnalyzer(self.portfolio_2021, self.portfolio_2022)

        # WHEN
        actual_number_of_bonds = fip.count_lost_bonds()

        # THEN
        expected_number_of_bonds = 2
        self.assertEqual(expected_number_of_bonds, actual_number_of_bonds, msg="Should be 2 bonds")

    def test_find_max_increased_bond(self):
        # GIVEN
        fip = PortfoliosAnalyzer(self.portfolio_2021, self.portfolio_2022)

        # WHEN
        actual_most_increased_bond = fip.find_max_increased_bond()

        # THEN
        expected_most_increased_bond = "BondB"
        self.assertEqual(expected_most_increased_bond, actual_most_increased_bond, msg="Should be BondB")


if __name__ == '__main__':
    unittest.main()
