import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.alpha_vantage import AlphaVantageClient
from indicators.indicator_engine import IndicatorEngine
from backtesting.backtest_engine import BacktestEngine

print("Downloading Data...\n")

client = AlphaVantageClient()
df = client.get_daily_data("AAPL")

print("Calculating Indicators...\n")

engine = IndicatorEngine()
df = engine.calculate_all(df)

print("Running Backtest...\n")

backtest = BacktestEngine()

portfolio = backtest.run(df)

print(portfolio.stats())