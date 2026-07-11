from indicators.trend import TrendIndicators
from indicators.momentum import MomentumIndicators
from indicators.volatility import VolatilityIndicators
from indicators.volume import VolumeIndicators


class IndicatorEngine:

    def __init__(self):
        self.trend = TrendIndicators()
        self.momentum = MomentumIndicators()
        self.volatility = VolatilityIndicators()
        self.volume = VolumeIndicators()

    def calculate_all(self, df):

        print("Calculating Trend Indicators...")
        df = self.trend.calculate(df)

        print("Calculating Momentum Indicators...")
        df = self.momentum.calculate(df)

        print("Calculating Volatility Indicators...")
        df = self.volatility.calculate(df)

        print("Calculating Volume Indicators...")
        df = self.volume.calculate(df)

        return df