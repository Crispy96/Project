
from project.models import DBManager
from project import app

route_database = app.config.get("ROUTE_DATA_BASE")
dbManager = DBManager(route_database)

class coin():
    dbManager= DBManager("data/movimientos.db")
    MONEDAFROM=['EUR']
    MONEDAS=[]
    MON=['EUR']
    consulta = "SELECT moneda_to FROM movimientos"
    proba= dbManager.consultaSQL(consulta)
    
    MON.extend(proba)

    #ETH
    eth="ETH"
    consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= '{}' "
    monedadisp= dbManager.consultaSQL(consulta.format(eth))
    if monedadisp != None:
        MONEDAS.append('ETH')
    
    #LTC
    ltc='LTC'
    consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= '{}' "
    monedadisp1= dbManager.consultaSQL(consulta.format(ltc))
    if monedadisp1 != None:
        MONEDAS.append('LTC')
    #BNB
    consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'BNB' "
    monedadisp2= dbManager.consultaSQL(consulta)
    if monedadisp2 == None:
        MONEDAFROM.append('pepe')
    #EOS
    consulta = "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= 'EOS' "
    monedadisp3= dbManager.consultaSQL(consulta)
    if monedadisp3 == None:
        pass
    else:
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

   
    """
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
            print(MONEDAFROM)
    """