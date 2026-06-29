import pandas as pd
from ta.trend import EMAIndicator, SMAIndicator, ADXIndicator


class TrendIndicators:

    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()

    def calculate(self):

        df = self.data

        # EMA
        df["EMA20"] = EMAIndicator(
            close=df["Close"],
            window=20
        ).ema_indicator()

        df["EMA50"] = EMAIndicator(
            close=df["Close"],
            window=50
        ).ema_indicator()

        df["EMA200"] = EMAIndicator(
            close=df["Close"],
            window=200
        ).ema_indicator()

        # SMA
        df["SMA20"] = SMAIndicator(
            close=df["Close"],
            window=20
        ).sma_indicator()

        df["SMA50"] = SMAIndicator(
            close=df["Close"],
            window=50
        ).sma_indicator()

        # ADX
        adx = ADXIndicator(
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            window=14
        )

        df["ADX"] = adx.adx()

        return df