import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.yahoo_finance import YahooFinanceClient

client = YahooFinanceClient()

print("Downloading BIT COIN...\n")

df = client.get_daily_data("BTC-USD")

print(df.tail())