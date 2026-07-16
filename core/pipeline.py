from market.market_router import MarketRouter
from indicators.indicator_engine import IndicatorEngine
from analysis.analysis_engine import AnalysisEngine
from ai.decision_engine import DecisionEngine


class HedgeFundPipeline:

    def __init__(self):

        self.market = MarketRouter()
        self.indicators = IndicatorEngine()
        self.analysis = AnalysisEngine()
        self.ai = DecisionEngine()

    def analyze(self, symbol: str):

        symbol = symbol.upper()

        print("Downloading Market Data...")

        df = self.market.get_data(symbol)

        print("Calculating Indicators...")

        df = self.indicators.calculate_all(df)

        print("Running Analysis...")

        analysis = self.analysis.analyze(df)

        print("Generating AI Report...")

        report = self.ai.analyze(symbol, analysis)

        return {
            "symbol": symbol,
            "analysis": analysis,
            "report": report,
            "data": df,
        }