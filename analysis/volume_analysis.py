class VolumeAnalysis:

    def analyze(self, df):

        latest = df.iloc[-1]

        score = 0
        reasons = []

        # Money Flow Index
        if 40 <= latest["MFI"] <= 80:
            score += 25
            reasons.append("Healthy Money Flow")

        elif latest["MFI"] > 80:
            reasons.append("Overbought Volume")

        else:
            reasons.append("Weak Money Flow")

        # Chaikin Money Flow
        if latest["CMF"] > 0:
            score += 25
            reasons.append("Positive Money Flow")

        else:
            reasons.append("Negative Money Flow")

        # On Balance Volume
        if latest["OBV"] > df["OBV"].iloc[-2]:
            score += 25
            reasons.append("OBV Rising")

        else:
            reasons.append("OBV Falling")

        # VWAP
        if latest["Close"] > latest["VWAP"]:
            score += 25
            reasons.append("Price above VWAP")

        else:
            reasons.append("Price below VWAP")

        return {
            "score": score,
            "reasons": reasons
        }