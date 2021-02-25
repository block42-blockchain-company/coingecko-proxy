from pycoingecko import CoinGeckoAPI
from flask import Flask
app = Flask(__name__)

@app.route('/')
def fetch():
	cg = CoinGeckoAPI()
	markets = cg.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page='250', page='1')

	return markets




