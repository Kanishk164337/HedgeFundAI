import pandas as pd


class EMACrossoverStrategy:

    def generate_signals(self, df: pd.DataFrame):

        df = df.copy()

        df["Buy"] = (
            (df["EMA20"] > df["EMA50"]) &
            (df["EMA20"].shift(1) <= df["EMA50"].shift(1))
        )

        df["Sell"] = (
            (df["EMA20"] < df["EMA50"]) &
            (df["EMA20"].shift(1) >= df["EMA50"].shift(1))
        )

        print("\n========== DEBUG ==========")
        print("Buy Signals :", df["Buy"].sum())
        print("Sell Signals:", df["Sell"].sum())
        print("===========================\n")

        return df