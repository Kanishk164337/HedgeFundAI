import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.alpha_vantage import AlphaVantageClient
from indicators.indicator_engine import IndicatorEngine

print("Downloading historical data...\n")

client = AlphaVantageClient()

df = client.get_daily_data("AAPL")

print(df.tail())

print("\nRunning Indicator Engine...\n")

engine = IndicatorEngine()

df = engine.calculate_all(df)

print("\nFinal DataFrame Columns:\n")

print(df.columns.tolist())

print("\nLast 5 Rows:\n")

print(df.tail())