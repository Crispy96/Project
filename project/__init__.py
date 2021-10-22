from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")

from project.views import *

class Api():
    url='https://rest.coinapi.io/v1/exchangerate/{}/{}'
    apikey="9A55ADFB-B569-458B-BFA9-77AE8D360889"
    cabecera = {"X-CoinAPI-Key": "9A55ADFB-B569-458B-BFA9-77AE8D360889"}

