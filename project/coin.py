import requests

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


url='https://rest.coinapi.io/v1/exchangerate/{}/{}'
apikey="9A55ADFB-B569-458B-BFA9-77AE8D360889"
cabecera = {"X-CoinAPI-Key": apikey}


