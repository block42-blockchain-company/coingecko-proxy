import os
import http.server
import socketserver
import json

from http import HTTPStatus

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        msg = cg.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page='250', page='1')
        j = json.dumps(msg)
        self.wfile.write(j.encode())

port = int(os.getenv('PORT', 6543))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()







