import requests


class BinanceClient:

    BASE_URL = "https://api.binance.com"

    def get_price(self, symbol="BTCUSDT"):

        endpoint = "/api/v3/ticker/price"

        response = requests.get(
            self.BASE_URL + endpoint,
            params={"symbol": symbol.upper()},
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    def get_24hr_stats(self, symbol="BTCUSDT"):

        endpoint = "/api/v3/ticker/24hr"

        response = requests.get(
            self.BASE_URL + endpoint,
            params={"symbol": symbol.upper()},
            timeout=10,
        )

        response.raise_for_status()

        return response.json()