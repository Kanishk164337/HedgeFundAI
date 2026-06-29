import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


class AlphaVantageClient:
    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self):
        self.api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

        if not self.api_key:
            raise ValueError("Alpha Vantage API Key not found!")

    def get_company_overview(self, symbol: str):

        params = {
            "function": "OVERVIEW",
            "symbol": symbol.upper(),
            "apikey": self.api_key
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        return response.json()

    def get_daily_data(self, symbol: str):

        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol.upper(),
            "outputsize": "compact",      # Free plan supports compact
            "apikey": self.api_key
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        if "Time Series (Daily)" not in data:
            raise Exception(data)

        df = pd.DataFrame.from_dict(
            data["Time Series (Daily)"],
            orient="index"
        )

        df.rename(columns={
            "1. open": "Open",
            "2. high": "High",
            "3. low": "Low",
            "4. close": "Close",
            "5. volume": "Volume"
        }, inplace=True)

        df = df.astype(float)

        df.index = pd.to_datetime(df.index)

        df.sort_index(inplace=True)

        return df