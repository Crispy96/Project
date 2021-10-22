
from project import app
from flask import render_template, request, redirect, url_for, flash
from project.__init__ import Api
from project.forms import Formulary
from project.models import DBManager
import requests
from datetime import datetime


route_database = app.config.get("ROUTE_DATA_BASE")
dbManager = DBManager(route_database)

@app.route("/")
def begin():
    consulta = """ SELECT * FROM movimientos ORDER by date """
    movimientos = dbManager.consultaSQL(consulta)

    return render_template("begin.html", items=movimientos)

@app.route("/purchase", methods=['GET', 'POST'])
def purchase():
    formulario= Formulary()
    
    if request.method == 'GET':
        formulario.cantidad_toH.data = 0
        formulario.puH.data = 0
        return render_template("purchase.html", form = formulario)
    else:
        if formulario.validate():
            if formulario.calculator.data: 
                api=Api()
                
                mf = formulario.moneda_from.data
                mt = formulario.moneda_to.data
                qf = formulario.cantidad_from.data
                sol= requests.get ((api.url).format(mf, mt), headers = api.cabecera)    
                dic = sol.json()
                formulario.cantidad_toH.data= qf * dic['rate']
                formulario.puH.data = dic['rate']
                formulario.date = datetime.today().strftime('%Y-%m-%d')
                formulario.time = datetime.today().strftime('%H:%M:%S')
                return render_template("purchase.html", form=formulario)
           
            if formulario.submit.data:
                
                consulta = """ INSERT INTO movimientos (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, pu)
                VALUES (:date, :time, :moneda_from, :cantidad_from, :moneda_to, :cantidad_to, :pu)   
                """
                try:
                    dbManager.insertSQL(consulta, formulario.data)
                except Exception as e:
                    print("Se ha producido un error de acceso a base de datos:", e)
                    flash("Se ha producido un error en la base de datos. Consulte con su administrador")

                    return render_template("purchase.html", form=formulario)

                return redirect(url_for("begin.html"))
            else: 
                return render_template("purchase.html", form = formulario)
        
        
      
@app.route("/status")
def status():
    
    return render_template("status.html")
