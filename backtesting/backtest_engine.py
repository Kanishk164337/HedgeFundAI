import vectorbt as vbt

from backtesting.strategy import EMACrossoverStrategy


class BacktestEngine:

    def __init__(self):

        self.strategy = EMACrossoverStrategy()

    def run(self, df):

        df = self.strategy.generate_signals(df)

        portfolio = vbt.Portfolio.from_signals(
            close=df["Close"],
            entries=df["Buy"],
            exits=df["Sell"],
            init_cash=10000,
            fees=0.001
        )

        return portfolio