from pycoingecko import CoinGeckoAPI

def fetch():
	cg = CoinGeckoAPI()
	markets = cg.get_coins_markets(vs_currency='usd')

	return markets

fetch()
