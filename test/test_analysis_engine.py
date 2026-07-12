import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.alpha_vantage import AlphaVantageClient
from indicators.indicator_engine import IndicatorEngine
from analysis.analysis_engine import AnalysisEngine

print("Downloading Data...\n")

client = AlphaVantageClient()

df = client.get_daily_data("AAPL")

indicator_engine = IndicatorEngine()

df = indicator_engine.calculate_all(df)

print("\nRunning Analysis Engine...\n")

analysis_engine = AnalysisEngine()

result = analysis_engine.analyze(df)

print(result)