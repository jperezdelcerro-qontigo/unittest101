import pandas as pd


class PortfoliosAnalyzer(object):
    NAME = "Name"
    PRICE = "Price"
    ID = "InstrumentId"
    DATE = "Date"

    def __init__(self, portfolio_a_path: str, portfolio_b_path: str) -> None:
        self.portfolio_a = pd.read_csv(portfolio_a_path)
        self.portfolio_b = pd.read_csv(portfolio_b_path)

    def count_lost_bonds(self) -> int:
        """
        Count the lost bond between them
        :return lost bonds:
        """
        return len(set(self.portfolio_a[self.NAME]) - set(self.portfolio_b[self.NAME]))

    def find_max_increased_bond(self) -> str:
        """
        Finds the bond whose price has increased the most between portfolios
        :return bond name:
        """
        merged_df = pd.merge(self.portfolio_a, self.portfolio_b, on=self.NAME,
                             suffixes=("portfolio_a", "portfolio_b"))
        merged_df["Price_difference"] = merged_df[self.PRICE + "portfolio_b"] - merged_df[self.PRICE + "portfolio_a"]
        return merged_df.loc[merged_df["Price_difference"].idxmax()][self.NAME]