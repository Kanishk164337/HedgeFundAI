from analysis.trend_analysis import TrendAnalysis
from analysis.momentum_analysis import MomentumAnalysis
from analysis.volatility_analysis import VolatilityAnalysis
from analysis.volume_analysis import VolumeAnalysis


class AnalysisEngine:

    def __init__(self):
        self.trend = TrendAnalysis()
        self.momentum = MomentumAnalysis()
        self.volatility = VolatilityAnalysis()
        self.volume = VolumeAnalysis()

    def analyze(self, df):

        trend = self.trend.analyze(df)
        momentum = self.momentum.analyze(df)
        volatility = self.volatility.analyze(df)
        volume = self.volume.analyze(df)

        overall_score = (
            trend["score"]
            + momentum["score"]
            + volatility["score"]
            + volume["score"]
        ) / 4

        if overall_score >= 80:
            signal = "STRONG BUY"
        elif overall_score >= 65:
            signal = "BUY"
        elif overall_score >= 50:
            signal = "HOLD"
        elif overall_score >= 35:
            signal = "SELL"
        else:
            signal = "STRONG SELL"

        confidence = round(overall_score)

        return {
            "trend": trend,
            "momentum": momentum,
            "volatility": volatility,
            "volume": volume,
            "overall_score": round(overall_score, 2),
            "signal": signal,
            "confidence": confidence,
        }