import json

from flask import Flask, request
from pycoingecko import CoinGeckoAPI

app = Flask(__name__)

coingecko = CoinGeckoAPI()


@app.route('/')
def root():
    return "ttfm 🚀"


@app.route('/markets')
def markets():
    currency = request.args.get('currency')
    limit = request.args.get('limit')
    page = request.args.get('page')

    response = coingecko.get_coins_markets(vs_currency=currency, order='market_cap_desc', per_page=limit, page=page)
    return json.dumps(response)


@app.route('/coin/<ticker>')
def coin(ticker):
    response = coingecko.get_coin_by_id(id=ticker)
    return json.dumps(response)


# Run app
app.run()
