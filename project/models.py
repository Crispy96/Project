import sqlite3
from project.coin import *
import requests
from project.forms import Formulary



class DBManager():
    def __init__(self, route_database):
        self.route_database = route_database

    def consultaSQL(self, consulta, params=[]):
    
        conexion = sqlite3.connect(self.route_database)

        cur = conexion.cursor()
        cur.execute(consulta, params)

        keys = []
        for item in cur.description:
            keys.append(item[0])        

        registros = []
        for registro in cur.fetchall():
            ix_clave = 0
            d = {}
            for columna in keys:
                d[columna] = registro[ix_clave]
                ix_clave += 1
            registros.append(d)

        conexion.close()
        return registros

def insertSQL(self, consulta, params):
        conexion = sqlite3.connect(self.routa_database)

        cur = conexion.cursor()

        cur.execute(consulta, params)
        conexion.commit()
        conexion.close()

def BalanceSQL():
    conexion = sqlite3.connect(self.routa_database)

    cur= conexion.cursor()

    cur.execute(consulta, params)
    total= cur.fetchone()[0]

    if total == None:
        total = 0
    conexion.close()
    return total

class request_API():
    def __init__(self, url):
        self.url= URL

    def request(self, moneda_to, moneda_from):
        headers= {"X-CoinAPI-Key": apikey}
        self.moneda_from = moneda_from
        self.moneda_to = moneda_to
        answer = request.get((self.url).format(self.moneda_from, self.moneda_to), headers=cabecera)
        pu = 1/answer.json()['rate']

    def calculo():
        mt = 1/answer
        

        
    

       

        
