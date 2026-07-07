import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.alpha_vantage import AlphaVantageClient
from indicators.trend import TrendIndicators

print("Downloading historical data...\n")

client = AlphaVantageClient()

df = client.get_daily_data("AAPL")

print(df.tail())

print("\nCalculating Trend Indicators...\n")

trend = TrendIndicators(df)
result = trend.calculate()

print(
    result[
        [
            "Close",
            "EMA20",
            "EMA50",
            "EMA200",
            "SMA20",
            "SMA50",
            "ADX",
        ]
    ].tail()
)