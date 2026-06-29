from market.alpha_vantage import AlphaVantageClient
from indicators.momentum import MomentumIndicators

print("Downloading historical data...\n")

client = AlphaVantageClient()

df = client.get_daily_data("AAPL")

print(df.tail())

print("\nCalculating Momentum Indicators...\n")

momentum = MomentumIndicators(df)

result = momentum.calculate()

print(
    result[
        [
            "Close",
            "RSI",
            "MACD",
            "MACD_SIGNAL",
            "MACD_HIST",
            "STOCH_K",
            "STOCH_D",
            "CCI",
            "ROC"
        ]
    ].tail()
)