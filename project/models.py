import sqlite3

from project.__init__ import *
from project.views import *
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
        
        conexion = sqlite3.connect(self.route_database)

        cur = conexion.cursor()

        cur.execute(consulta, params)
        conexion.commit()
        conexion.close()

    def BalanceSQL(self, consulta, params=[]):
        conexion = sqlite3.connect(self.route_database)

        cur= conexion.cursor()

        cur.execute(consulta, params)
        total= cur.fetchone()[0]

        if total == None:
            total = 0
        conexion.close()
        return total
    def coin():
         
        MONEDAFROM=[]
        #ETH

        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'ETH' "
        monedadisp= dbManager.consultaSQL(consulta)
        if monedadisp != None:
            MONEDAFROM.append('ETH')
        #LTC
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'LTC' "
        monedadisp1= dbManager.consultaSQL(consulta)
        if monedadisp1 != None:
            MONEDAFROM.append('LTC')
        #BNB
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'BNB' "
        monedadisp2= dbManager.consultaSQL(consulta)
        if monedadisp2 != None:
            MONEDAFROM.append('BNB')
        #EOS
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'EOS' "
        monedadisp3= dbManager.consultaSQL(consulta)
        if monedadisp3 != None:
            MONEDAFROM.append('EOS')
        #XLM
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'XLM' "
        monedadisp4= dbManager.consultaSQL(consulta)
        if monedadisp4 != None:
            MONEDAFROM.append('XLM')
        #TRX
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'TRX' "
        monedadisp5= dbManager.consultaSQL(consulta)
        if monedadisp5 != None:
            MONEDAFROM.append('TRX')
        #BTC
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'BTC' "
        monedadisp6= dbManager.consultaSQL(consulta)
        if monedadisp6 != None:
            MONEDAFROM.append('BTC')
        #XRP
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'XRP' "
        monedadisp7= dbManager.consultaSQL(consulta)
        if monedadisp7 != None:
            MONEDAFROM.append('XRP')
        #BCH
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'BCH' "
        monedadisp8= dbManager.consultaSQL(consulta)
        if monedadisp8 != None:
            MONEDAFROM.append('BCH')
        #USDT
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'USDT' "   
        monedadisp9= dbManager.consultaSQL(consulta)
        if monedadisp9 != None:
            MONEDAFROM.append('USDT')
        #ADA
        consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'ADA' "   
        monedadisp10= dbManager.consultaSQL(consulta)
        if monedadisp10 != None:
            MONEDAFROM.append('ADA')





