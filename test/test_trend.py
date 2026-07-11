import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.alpha_vantage import AlphaVantageClient
from indicators.trend import TrendIndicators

print("Downloading historical data...\n")

# Download market data
client = AlphaVantageClient()

df = client.get_daily_data("AAPL")

print(df.tail())

print("\nCalculating Trend Indicators...\n")

# Calculate indicators
trend = TrendIndicators()

df = trend.calculate(df)

# Display results
print(
    df[
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