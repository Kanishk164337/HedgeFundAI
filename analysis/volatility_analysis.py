class VolatilityAnalysis:

    def analyze(self, df):

        latest = df.iloc[-1]

        score = 0
        reasons = []

        # ATR
        if latest["ATR"] < latest["Close"] * 0.03:
            score += 25
            reasons.append("Low ATR (controlled volatility)")
        else:
            reasons.append("High ATR (volatile market)")

        # Bollinger Band Position
        if latest["Close"] < latest["BB_Upper"]:
            score += 25
            reasons.append("Price below upper Bollinger Band")
        else:
            reasons.append("Price touching upper Bollinger Band")

        # Historical Volatility
        if latest["Historical_Volatility"] < 0.40:
            score += 25
            reasons.append("Moderate historical volatility")
        else:
            reasons.append("High historical volatility")

        # Donchian Channel
        if latest["Close"] < latest["Donchian_Upper"]:
            score += 25
            reasons.append("Below Donchian resistance")
        else:
            reasons.append("Testing Donchian breakout")

        return {
            "score": score,
            "reasons": reasons
        }