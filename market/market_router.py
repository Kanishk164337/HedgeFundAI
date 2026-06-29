from market.alpha_vantage import AlphaVantageClient
from market.binance import BinanceClient


class MarketRouter:

    def __init__(self):
        self.alpha = AlphaVantageClient()
        self.binance = BinanceClient()

    def get_data(self, symbol: str):

        symbol = symbol.upper()

        crypto_suffixes = (
            "USDT",
            "BTC",
            "ETH",
            "BNB",
            "FDUSD",
            "USDC",
        )

        if symbol.endswith(crypto_suffixes):
            return self.binance.get_24hr_stats(symbol)

        return self.alpha.get_company_overview(symbol)