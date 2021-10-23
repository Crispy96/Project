from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
from project.views import *

class Api():
    url='https://rest.coinapi.io/v1/exchangerate/{}/{}'
    apikey="8C0131C4-430B-4CB8-A373-B76252A39275"
    cabecera = {"X-CoinAPI-Key": "8C0131C4-430B-4CB8-A373-B76252A39275"}

