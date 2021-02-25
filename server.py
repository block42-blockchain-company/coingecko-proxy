import os
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

    if None in [currency, limit, page]:
        return "Error: Missing params!", 403

    response = coingecko.get_coins_markets(vs_currency=currency, order='market_cap_desc', per_page=limit, page=page, sparkline=False)
    return json.dumps(response)


@app.route('/coin/<ticker>')
def coin(ticker):
    response = coingecko.get_coin_by_id(id=ticker)
    return json.dumps(response)


# Run app
app.run(host="0.0.0.0", port=os.environ["PORT"])