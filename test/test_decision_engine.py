import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from market.alpha_vantage import AlphaVantageClient
from indicators.indicator_engine import IndicatorEngine
from analysis.analysis_engine import AnalysisEngine
from ai.decision_engine import DecisionEngine

print("Downloading Data...\n")

client = AlphaVantageClient()

df = client.get_daily_data("AAPL")

print("Calculating Indicators...\n")

indicator_engine = IndicatorEngine()

df = indicator_engine.calculate_all(df)

print("\nRunning Analysis Engine...\n")

analysis_engine = AnalysisEngine()

analysis = analysis_engine.analyze(df)

print("Analysis Complete.\n")

print("Generating AI Investment Report...\n")

decision_engine = DecisionEngine()

report = decision_engine.analyze("AAPL", analysis)

print(report)