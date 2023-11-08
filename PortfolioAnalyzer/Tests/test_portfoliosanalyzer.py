from io import StringIO

from PortfolioAnalyzer.portfolioanalyzer import PortfoliosAnalyzer


class TestPortfolioAnalyzer:
    def test_count_lost_bonds_between_portfolios(self):
        # GIVEN
        portfolio_2021 = "PortfolioAnalyzer/Tests/Data/portfolio_2021.csv"
        portfolio_2022 = "PortfolioAnalyzer/Tests/Data/portfolio_2022.csv"
        pa = PortfoliosAnalyzer(portfolio_2021, portfolio_2022)

        # WHEN
        actual_number_of_bonds = pa.count_lost_bonds()

        # THEN
        assert False

    def test_find_max_increased_bond(self):
        # GIVEN
        portfolio_2021 = "PortfolioAnalyzer/Tests/Data/portfolio_2021.csv"
        portfolio_2022 = "PortfolioAnalyzer/Tests/Data/portfolio_2022.csv"
        pa = PortfoliosAnalyzer(portfolio_2021, portfolio_2022)

        # WHEN


        # THEN
        assert False
