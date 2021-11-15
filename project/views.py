
from project import app
from flask import render_template, request, redirect, url_for, flash
from project.models import Api
from project.forms import Formulary, Formulary2
from project.models import DBManager
import requests
from datetime import datetime
from config import *
from collections import Counter

route_database = app.config.get("ROUTE_DATA_BASE")
dbManager = DBManager(route_database)

@app.route("/")
def begin():
    try:
        consulta = """ SELECT * FROM movimientos ORDER by date """
        movimientos = dbManager.consultaSQL(consulta)
    except:

        flash("Hay un error al conectar con su base de datos")
        return render_template("begin.html", disableInicio=True)

   
    return render_template("begin.html", items=movimientos, disableInicio=True)

@app.route("/purchase", methods=['GET', 'POST'])   

def purchase():
    formulario= Formulary()
    
    if request.method == 'GET':
        formulario.cantidad_toH.data = 0
        formulario.puH.data = 0
        
       
        return render_template("purchase.html", form = formulario, disablePurchase=True, block=True)
    else:
          
        if formulario.validate():
           
            if formulario.calculator.data:
                
                
                mf = formulario.moneda_from.data
                mt = formulario.moneda_to.data
                qf = formulario.cantidad_from.data
                
                d= datetime.today().strftime('%Y-%m-%d')
                t =datetime.today().strftime('%H:%M:%S')
                
                
                formulario.date.data = d
                formulario.time.data = t
                if mf == mt:
                    flash("Las monedas no pueden ser iguales") 
                    return render_template("purchase.html", form=formulario, disablePurchase=True)  
                if mf != 'EUR':
                    consulta= "SELECT SUM(cantidad_from) FROM movimientos WHERE moneda_from= '{}' "
                    sumFrom= dbManager.consultaSQL(consulta.format(mf), formulario.data)
                    consulta= "SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to= '{}' "
                    sumTo= dbManager.consultaSQL(consulta.format(mf), formulario.data)
                    
                    if sumFrom[0]['SUM(cantidad_from)'] == None:
                        sumFrom[0]['SUM(cantidad_from)'] = 0
                    if sumTo[0]['SUM(cantidad_to)'] == None:
                        sumTo[0]['SUM(cantidad_to)'] = 0
                    dispocoin= sumTo[0]['SUM(cantidad_to)'] - sumFrom[0]['SUM(cantidad_from)']
                   
                    if dispocoin - float(qf) <-0:
                        flash("No dispones de suficientes monedas para comprar. Consulta movimientos. ")
                        print(dispocoin-float(qf))
                        return render_template("purchase.html", form=formulario, disablePurchase=True)
                    
                api=Api()
                sol= requests.get ((api.url).format(mf, mt), headers = api.cabecera)   
                dic = sol.json()
                try:
                    formulario.cantidad_toH.data= round(qf * dic['rate'],6)
                except Exception as e:
                    print("Se ha producido un error ", e)
                    flash("Hay un error con tu APIKEY. Comprueba que esta escrita correctamente. Si es así, has consumido el número total de consulta de esta. Puedes obtener otra en CoinAPI.")
                    return render_template("purchase.html", form=formulario, disablePurchase=True)
              
                formulario.puH.data = round(dic['rate'],6 )

                
                
                return render_template("purchase.html", form = formulario, disablePurchase=True, block=False)
            elif formulario.submit.data:
                consulta = """ INSERT INTO movimientos (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, pu)
                                        VALUES (:date, :time, :moneda_from, :cantidad_from, :moneda_to, :cantidad_toH, :puH)   
                                    """
                try:
                    dbManager.insertSQL(consulta, formulario.data)
                    print("*******AQUI*****")
                except Exception as e:
                    print("Se ha producido un error de acceso a base de datos:", e)
                    flash("Se ha producido un error en la base de datos. Consulte con su administrador")

                    return render_template("purchase.html", form=formulario, disablePurchase=True)

            return redirect(url_for("begin"))
        else: 
            return render_template("purchase.html", form = formulario, disablePurchase=True)
        

           
      
@app.route("/status", )
def status():
    
    api=Api()
    formulario = Formulary2()
    consultaFROM = """SELECT SUM(cantidad_from) FROM movimientos WHERE moneda_from='{}' """
    consultaTO= """SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to='{}' """ 
   
  
  
   #EUROS
    try:
        EURfrom=dbManager.BalanceSQL(consultaFROM.format('EUR'))
        EURto=dbManager.BalanceSQL(consultaTO.format('EUR'))
        if EURfrom== None:
            EURfrom = 0
        if EURto== None:
            EURto==0
        inversion=EURfrom-EURto
    
    
        #ETH
        ETHfrom=float(dbManager.BalanceSQL(consultaFROM.format('ETH')))
        ETHto =  dbManager.BalanceSQL(consultaTO.format('ETH'))
        if ETHfrom== None:
            ETHfrom = 0
        if ETHto== None:
            ETHto==0
        ETHsol=ETHto-ETHfrom
        meth='ETH'
        e='EUR'
        if ETHsol == 0:
            ETHeur=0
        else:
            sol= requests.get ((api.url).format(e, meth), headers = api.cabecera)
            dic = sol.json()
            try:
                ETHrate=dic['rate']
            except  Exception as e:
                print("Se ha producido un error ", e)
                flash("Hay un error con tu APIKEY. Comprueba que esta escrita correctamente. Si es así, has consumido el número total de consulta de esta. Puedes obtener otra en CoinAPI.")
                return render_template("status.html", form=formulario, disableStatus=True)
            ETHeur=ETHrate/ETHsol
        
        #LTC
        LTCfrom=float(dbManager.BalanceSQL(consultaFROM.format('LTC')))
        LTCto =  dbManager.BalanceSQL(consultaTO.format('LTC'))
        if LTCfrom== None:
            LTCfrom = 0
        if LTCto== None:
            LTCto==0
        LTCsol=LTCto-LTCfrom
        mltc='LTC'
        if LTCsol == 0:
            LTCeur=0
        else:
            sol= requests.get ((api.url).format(e, mltc), headers = api.cabecera)    
            dic2 = sol.json()
            
            LTCrate=dic2['rate']
            LTCeur=LTCrate/LTCsol
        
        #BNB
        BNBfrom=float(dbManager.BalanceSQL(consultaFROM.format('BNB')))
        BNBto =  dbManager.BalanceSQL(consultaTO.format('BNB'))
        if BNBfrom== None:
            BNBfrom = 0
        if BNBto== None:
            BNBto==0
        BNBsol=BNBto-BNBfrom
        mbnb='BNB'
        if BNBsol==0:
            BNBeur=0
        else:
            sol= requests.get ((api.url).format(e, mbnb), headers = api.cabecera)    
            dic3 = sol.json()
            BNBrate=dic3['rate']
            BNBeur=BNBrate/BNBsol
            
        #EOS
        EOSfrom=float(dbManager.BalanceSQL(consultaFROM.format('EOS')))
        EOSto =  dbManager.BalanceSQL(consultaTO.format('EOS'))
        if EOSfrom== None:
            EOSfrom = 0
        if EOSto== None:
            EOSto==0
        EOSsol=EOSto-EOSfrom
        meos='EOS'
        if EOSsol == 0:
            EOSeur=0
        else:
            sol= requests.get ((api.url).format(e, meos), headers = api.cabecera)    
            dic4 = sol.json()
            EOSrate=dic4['rate']
            EOSeur=EOSrate/EOSsol
        
        #XLM
        XLMfrom=float(dbManager.BalanceSQL(consultaFROM.format('XLM')))
        XLMto =  dbManager.BalanceSQL(consultaTO.format('XLM'))
        if XLMfrom== None:
            XLMfrom = 0
        if XLMto== None:
            XLMto==0
        XLMsol=XLMto-XLMfrom
        mxlm='XLM'
        if XLMsol==0:
            XLMeur=0
        else:
            sol= requests.get ((api.url).format(e, mxlm), headers = api.cabecera)    
            dic5 = sol.json()
            XLMrate=dic5['rate']
            XLMeur=XLMrate/XLMsol
        
        #TRX
        TRXfrom=float(dbManager.BalanceSQL(consultaFROM.format('TRX')))
        TRXto =  dbManager.BalanceSQL(consultaTO.format('TRX'))
        if TRXfrom== None:
            TRXfrom = 0
        if TRXto== None:
            TRXto==0
        TRXsol=TRXto-TRXfrom
        mtrx='TRX'
        if TRXsol==0:
            TRXeur=0
        else:
            sol= requests.get ((api.url).format(e, mtrx), headers = api.cabecera)    
            dic6 = sol.json()
            TRXrate=dic6['rate']
            TRXeur=TRXrate/TRXsol
        
        #BTC
        BTCfrom=float(dbManager.BalanceSQL(consultaFROM.format('BTC')))
        BTCto =  dbManager.BalanceSQL(consultaTO.format('BTC'))
        if BTCfrom== None:
            BTCfrom = 0
        if BTCto== None:
            BTCto==0
        BTCsol=BTCto-BTCfrom
        mbtc='BTC'
        if BTCsol == 0:
            BTCeur=0
        else:
            sol= requests.get ((api.url).format(e, mbtc), headers = api.cabecera)    
            dic7 = sol.json()
            BTCrate=dic7['rate']
            BTCeur=BTCrate/BTCsol
        
        #XRP
        XRPfrom=float(dbManager.BalanceSQL(consultaFROM.format('XRP')))
        XRPto =  dbManager.BalanceSQL(consultaTO.format('XRP'))
        if XRPfrom== None:
            XRPfrom = 0
        if XRPto== None:
            XRPto==0
        XRPsol=XRPto-XRPfrom
        mxrp='XRP'
        if XLMsol==0:
            XRPeur=0
        else:
            sol= requests.get ((api.url).format(e, mxrp), headers = api.cabecera)    
            dic8 = sol.json()
            XRPrate=dic8['rate']
            XRPeur= XRPrate/XRPsol
            
        #BCH
        BCHfrom=float(dbManager.BalanceSQL(consultaFROM.format('BCH')))
        BCHto =  dbManager.BalanceSQL(consultaTO.format('BCH'))
        if BCHfrom== None:
            BCHfrom = 0
        if BCHto== None:
            BCHto==0
        BCHsol=BCHto-BCHfrom
        mbch='BCH'
        if BCHsol==0:
            BCHeur=0
        else:
            sol= requests.get ((api.url).format(e, mbch), headers = api.cabecera)    
            dic9 = sol.json()
            BCHrate=dic9['rate']
            BCHeur= BCHrate/BCHsol
        
        #USDT
        USDTfrom=float(dbManager.BalanceSQL(consultaFROM.format('USDT')))
        USDTto =  dbManager.BalanceSQL(consultaTO.format('USDT'))
        if USDTfrom== None:
            USDTfrom = 0
        if USDTto== None:
            USDTto==0
        USDTsol=USDTto-USDTfrom
        musdt='USDT'
        if USDTsol==0:
            USDTeur=0
        else:
            sol= requests.get ((api.url).format(e, musdt), headers = api.cabecera)    
            dic10 = sol.json()
            USDTrate=dic10['rate']
            USDTeur= USDTrate/USDTsol
        
        #ADA
        ADAfrom=float(dbManager.BalanceSQL(consultaFROM.format('ADA')))
        ADAto =  dbManager.BalanceSQL(consultaTO.format('ADA'))
        if ADAfrom== None:
            ADAfrom = 0
        if ADAto== None:
            ADAto==0
        ADAsol=ADAto-ADAfrom
        mada='ADA'
        if ADAsol==0:
            ADAeur=0
        else:
            sol= requests.get ((api.url).format(e, mada), headers = api.cabecera)    
            dic12 = sol.json()
            ADArate=dic12['rate']
            ADAeur=ADArate / ADAsol
        
        
        sumCOIN= ETHeur+LTCeur+BNBeur+EOSeur+XLMeur+TRXeur+BTCeur+XRPeur+BCHeur+USDTeur+ADAeur
        estado =sumCOIN-inversion
        if request.method == 'GET':
            formulario.investH.data = inversion
            formulario.estadoH.data = estado
            if estado <0:
                flash("Prueba hacer mejores inversiones")    
    except:
        flash("No es posible conectarse a su base de datos, deberá combrobarla.")
    return render_template("status.html", form=formulario, disableStatus=True )

