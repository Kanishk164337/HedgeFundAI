import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.alpha_vantage import AlphaVantageClient
from indicators.indicator_engine import IndicatorEngine
from analysis.volatility_analysis import VolatilityAnalysis

print("Downloading Data...\n")

client = AlphaVantageClient()

df = client.get_daily_data("AAPL")

engine = IndicatorEngine()

df = engine.calculate_all(df)

analysis = VolatilityAnalysis()

result = analysis.analyze(df)

print(result)
