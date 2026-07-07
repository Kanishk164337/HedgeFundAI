import pandas_ta as ta


class VolumeIndicators:

    def calculate(self, df):

        # ==========================
        # VWAP
        # ==========================

        df["VWAP"] = ta.vwap(
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            volume=df["Volume"]
        )

        # ==========================
        # On Balance Volume
        # ==========================

        df["OBV"] = ta.obv(
            close=df["Close"],
            volume=df["Volume"]
        )

        # ==========================
        # Money Flow Index
        # ==========================

        df["MFI"] = ta.mfi(
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            volume=df["Volume"],
            length=14
        )

        # ==========================
        # Chaikin Money Flow
        # ==========================

        df["CMF"] = ta.cmf(
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            volume=df["Volume"],
            length=20
        )

        return df