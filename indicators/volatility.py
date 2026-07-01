import pandas_ta as ta


class VolatilityIndicators:

    def calculate(self, df):

        # ==========================
        # ATR
        # ==========================

        df["ATR"] = ta.atr(
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            length=14
        )

        # ==========================
        # Bollinger Bands
        # ==========================

        bb = ta.bbands(
            close=df["Close"],
            length=20
        )

        # Use iloc so it works across pandas_ta versions
        df["BB_Lower"] = bb.iloc[:, 0]
        df["BB_Middle"] = bb.iloc[:, 1]
        df["BB_Upper"] = bb.iloc[:, 2]

        # ==========================
        # Donchian Channel
        # ==========================

        dc = ta.donchian(
            high=df["High"],
            low=df["Low"],
            lower_length=20,
            upper_length=20
        )

        df["Donchian_Lower"] = dc.iloc[:, 0]
        df["Donchian_Middle"] = dc.iloc[:, 1]
        df["Donchian_Upper"] = dc.iloc[:, 2]

        # ==========================
        # Historical Volatility
        # ==========================

        returns = df["Close"].pct_change()

        df["Historical_Volatility"] = (
            returns.rolling(20).std() * (252 ** 0.5)
        )

        return df