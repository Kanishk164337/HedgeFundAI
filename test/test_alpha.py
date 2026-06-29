from market.alpha_vantage import AlphaVantageClient

client = AlphaVantageClient()

print("Downloading Company Data...\n")

company = client.get_company_overview("AAPL")

print(company["Name"])
print(company["Sector"])
print(company["Industry"])
print(company["MarketCapitalization"])