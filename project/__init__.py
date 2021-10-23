from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
from project.views import *

class Api():
    url='https://rest.coinapi.io/v1/exchangerate/{}/{}'
    apikey="A58F5EDA-00BC-4E43-B2C2-979F9A48884E"
    cabecera = {"X-CoinAPI-Key": "A58F5EDA-00BC-4E43-B2C2-979F9A48884E"}

