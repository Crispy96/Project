from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")

from project.views import *

MONEDAS= ['EUR-Euros',
        'ETH-Ethereum',
        'LTC-Litecoin',
        'BNB-Binance',
        'EOS',
        'XLM-Stellar',
        'TRX-Trom',
        'BTC-Bitcoin',
        'XRP',
        'BCH-Bitcoin Cash',
        'USDT-Tether',
        'BSV',
        'ADA-Cardano']
