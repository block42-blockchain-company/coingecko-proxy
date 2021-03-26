import os
import json

from flask import Flask, request, Response, abort, send_from_directory
from pycoingecko import CoinGeckoAPI

app = Flask(__name__)

coingecko = CoinGeckoAPI()


@app.route('/')
def root():
    return "ttfm 🚀"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route('/markets')
def markets():
    currency = request.args.get('currency')
    limit = request.args.get('limit')
    page = request.args.get('page')

    if None in [currency, limit, page]:
        abort(Response("Invalid request: Params missing", status=400))

    response = coingecko.get_coins_markets(vs_currency=currency, order='market_cap_desc', per_page=limit, page=page, sparkline=False)
    return json.dumps(response)


@app.route('/coins/<ticker>')
def coins(ticker):
    response = coingecko.get_coin_by_id(id=ticker)
    return json.dumps(response)


@app.route('/coins/<ticker>/history')
def history(ticker):
    date = request.args.get('date')

    if date is None:
        abort(Response("Invalid request: Params missing", status=400))

    response = coingecko.get_coin_history_by_id(id=ticker, date=date)
    return json.dumps(response)


# Run app
app.run(host="0.0.0.0", port=os.environ["PORT"])
