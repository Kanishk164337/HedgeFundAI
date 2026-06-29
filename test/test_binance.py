from market.binance import BinanceClient

client = BinanceClient()

price = client.get_price("BTCUSDT")

print("BTC Price")
print(price)

stats = client.get_24hr_stats("BTCUSDT")

print("\n24 Hour Change")
print(stats["priceChangePercent"] + "%")