from market.alpha_vantage import AlphaVantageClient
from market.yahoo_finance import YahooFinanceClient


class MarketRouter:

    def __init__(self):

        self.alpha = AlphaVantageClient()
        self.yahoo = YahooFinanceClient()

    def get_data(self, symbol: str):

        symbol = symbol.upper()

        # Indian Stocks
        if symbol.endswith(".NS") or symbol.endswith(".BO"):

            print("Using Yahoo Finance (Indian Stock)")
            return self.yahoo.get_daily_data(symbol)

        # Commodities
        if symbol.endswith("=F"):

            print("Using Yahoo Finance (Commodity)")
            return self.yahoo.get_daily_data(symbol)

        # Crypto
        if symbol.endswith("-USD"):

            print("Using Yahoo Finance (Crypto)")
            return self.yahoo.get_daily_data(symbol)

        # Index
        if symbol.startswith("^"):

            print("Using Yahoo Finance (Index)")
            return self.yahoo.get_daily_data(symbol)

        # Default US Stock
        print("Using Alpha Vantage (US Stock)")
        return self.alpha.get_daily_data(symbol)