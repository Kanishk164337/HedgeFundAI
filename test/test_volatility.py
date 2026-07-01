import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.alpha_vantage import AlphaVantageClient
from indicators.volatility import VolatilityIndicators

print("Downloading historical data...\n")

client = AlphaVantageClient()

df = client.get_daily_data("AAPL")

print(df.tail())

print("\nCalculating Volatility Indicators...\n")

volatility = VolatilityIndicators()

df = volatility.calculate(df)

print(
    df[
        [
            "Close",
            "ATR",
            "BB_Lower",
            "BB_Middle",
            "BB_Upper",
            "Donchian_Lower",
            "Donchian_Upper",
            "Historical_Volatility",
        ]
    ].tail()
)