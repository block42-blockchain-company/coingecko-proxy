from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
markets = cg.get_coins_markets(vs_currency='usd')

print("# of markets = ", len(markets))



