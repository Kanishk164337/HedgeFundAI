class TrendAnalysis:

    def analyze(self, df):

        latest = df.iloc[-1]

        score = 0
        reasons = []

        # Price vs EMA20
        if latest["Close"] > latest["EMA20"]:
            score += 20
            reasons.append("Price above EMA20")
        else:
            reasons.append("Price below EMA20")

        # EMA20 vs EMA50
        if latest["EMA20"] > latest["EMA50"]:
            score += 20
            reasons.append("EMA20 above EMA50")

        # EMA50 vs EMA200
        if latest["EMA50"] > latest["EMA200"]:
            score += 20
            reasons.append("EMA50 above EMA200")

        # Price vs SMA50
        if latest["Close"] > latest["SMA50"]:
            score += 20
            reasons.append("Price above SMA50")

        # ADX
        if latest["ADX"] > 25:
            score += 20
            reasons.append("Strong trend (ADX > 25)")
        else:
            reasons.append("Weak trend")

        return {
            "score": score,
            "reasons": reasons
        }