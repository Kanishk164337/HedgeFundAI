class MomentumAnalysis:

    def analyze(self, df):

        latest = df.iloc[-1]

        score = 0
        reasons = []

        # RSI
        if 50 <= latest["RSI"] <= 70:
            score += 20
            reasons.append("Healthy RSI")

        elif latest["RSI"] > 70:
            reasons.append("Overbought RSI")

        else:
            reasons.append("Weak RSI")

        # MACD
        if latest["MACD"] > latest["MACD_SIGNAL"]:
            score += 20
            reasons.append("Bullish MACD")

        else:
            reasons.append("Bearish MACD")

        # Stochastic
        if latest["STOCH_K"] > latest["STOCH_D"]:
            score += 20
            reasons.append("Bullish Stochastic")

        # ROC
        if latest["ROC"] > 0:
            score += 20
            reasons.append("Positive ROC")

        # CCI
        if latest["CCI"] > 0:
            score += 20
            reasons.append("Positive CCI")

        return {
            "score": score,
            "reasons": reasons
        }