from io import StringIO

from PortfolioAnalyzer.portfolioanalyzer import PortfoliosAnalyzer


class TestPortfolioAnalyzer:
    def setup_method(self):
        self.portfolio_2021 = "PortfolioAnalyzer/Tests/Data/portfolio_2021.csv"
        self.portfolio_2022 = "PortfolioAnalyzer/Tests/Data/portfolio_2022.csv"

    def test_count_lost_bonds_between_portfolios(self):
        # GIVEN
        pa = PortfoliosAnalyzer(self.portfolio_2021, self.portfolio_2022)

        # WHEN
        actual_number_of_bonds = pa.count_lost_bonds()

        # THEN
        expected_number_of_bonds = 2
        assert expected_number_of_bonds == actual_number_of_bonds, "Should be 2 bonds"

    def test_find_max_increased_bond(self):
        # GIVEN
        pa = PortfoliosAnalyzer(self.portfolio_2021, self.portfolio_2022)

        # WHEN
        actual_most_increased_bond = pa.find_max_increased_bond()

        # THEN
        expected_most_increased_bond = "BondB"
        assert expected_most_increased_bond == actual_most_increased_bond, "Should be BondB"
