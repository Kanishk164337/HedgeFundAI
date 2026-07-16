import yfinance as yf
import pandas as pd


class YahooFinanceClient:

    def get_daily_data(self, symbol: str):

        ticker = yf.Ticker(symbol)

        df = ticker.history(
            period="1y",
            interval="1d"
        )

        if df.empty:
            raise Exception(f"No data found for {symbol}")

        df = df[["Open", "High", "Low", "Close", "Volume"]]

        df = df.dropna()

        return df