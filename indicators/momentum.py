import pandas as pd

from ta.momentum import (
    RSIIndicator,
    StochasticOscillator,
    ROCIndicator
)

from ta.trend import (
    MACD,
    CCIIndicator
)


class MomentumIndicators:

    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()

    def calculate(self):

        df = self.data

        # ==========================
        # RSI
        # ==========================

        df["RSI"] = RSIIndicator(
            close=df["Close"],
            window=14
        ).rsi()

        # ==========================
        # MACD
        # ==========================

        macd = MACD(
            close=df["Close"]
        )

        df["MACD"] = macd.macd()
        df["MACD_SIGNAL"] = macd.macd_signal()
        df["MACD_HIST"] = macd.macd_diff()

        # ==========================
        # STOCHASTIC
        # ==========================

        stoch = StochasticOscillator(
            high=df["High"],
            low=df["Low"],
            close=df["Close"]
        )

        df["STOCH_K"] = stoch.stoch()
        df["STOCH_D"] = stoch.stoch_signal()

        # ==========================
        # CCI
        # ==========================

        df["CCI"] = CCIIndicator(
            high=df["High"],
            low=df["Low"],
            close=df["Close"]
        ).cci()

        # ==========================
        # ROC
        # ==========================

        df["ROC"] = ROCIndicator(
            close=df["Close"]
        ).roc()

        return df