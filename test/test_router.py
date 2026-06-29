from market.market_router import MarketRouter

router = MarketRouter()

print("========== STOCK ==========\n")

stock = router.get_data("AAPL")

print(stock["Name"])
print(stock["Sector"])

print("\n========== CRYPTO ==========\n")

crypto = router.get_data("BTCUSDT")

print("Symbol:", crypto["symbol"])
print("Price:", crypto["lastPrice"])
print("24h Change:", crypto["priceChangePercent"] + "%")