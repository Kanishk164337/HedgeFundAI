import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from portfolio.portfolio_engine import PortfolioEngine


portfolio = PortfolioEngine()

symbols = [
    "AAPL",
    "MSFT",
    "NVDA"
]

results = portfolio.analyze(symbols)

print("\n========== PORTFOLIO ==========\n")

for stock in results:

    print(stock)