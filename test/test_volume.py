import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.alpha_vantage import AlphaVantageClient
from indicators.volume import VolumeIndicators

print("Downloading historical data...\n")

client = AlphaVantageClient()

df = client.get_daily_data("AAPL")

print(df.tail())

print("\nCalculating Volume Indicators...\n")

volume = VolumeIndicators()

df = volume.calculate(df)

print("\nColumns after calculation:\n")
print(df.columns)

print("\nLast 5 rows:\n")
print(df.tail())