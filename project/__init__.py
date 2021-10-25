from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
from project.views import *
from config import *

MONEDAS= ['',
        'EUR',
        'ETH',
        'LTC',
        'BNB',
        'EOS',
        'XLM',
        'TRX',
        'BTC',
        'XRP',
        'BCH',
        'USDT',
        'ADA']


class Api():
    url='https://rest.coinapi.io/v1/exchangerate/{}/{}'
    apikey = apikey
    cabecera = {"X-CoinAPI-Key": apikey}
