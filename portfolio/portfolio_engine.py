from core.pipeline import HedgeFundPipeline


class PortfolioEngine:

    def __init__(self):
        self.pipeline = HedgeFundPipeline()

    def analyze(self, symbols):

        results = []

        for symbol in symbols:

            print(f"\nAnalyzing {symbol}...")

            try:

                report = self.pipeline.analyze(symbol)

                results.append({

                    "symbol": symbol,

                    "signal": report["analysis"]["signal"],

                    "score": report["analysis"]["overall_score"],

                    "confidence": report["analysis"]["confidence"]

                })

            except Exception as e:

                print(f"{symbol}: {e}")

        results = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )

        return results