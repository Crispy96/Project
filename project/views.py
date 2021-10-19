from project import app
from flask import render_template, request
from project.models import *
from project.forms import Formulary


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
    calculator_pushed= False
    if request.method == 'GET':
        formulario.cantidad_to.data = 0
        return render_template("purchase.html", form = formulario)
    else:
        if formulario.validate():
            if formulario.calculator.data:    
                #formulario.pu.data = pu
                #formulario.puH.data= formulario.pu.data
                formulario.cantidad_to.data= 23
                #formulario.cantitdadtoH.data = formulario.cantidad_to.data
          
                return render_template("purchase.html", form=formulario)
        else:
            return render_template("purchase.html", form = formulario)    
            """
            if form.sumbit.data:
               consulta = 
                INSERT INTO movimientos (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, put)
                VALUES (:date, :concepto, :ingreso_gasto, :cantidad)
               

                try:
                    dbManager.modificaSQL(consulta, formulario.data)
                except Exception as e:
                    print("Se ha producido un error de acceso a base de datos:", e)
                    flash("Se ha producido un error en la base de datos. Consulte con su administrador")
                return render_template("nuevo_movimiento.html", form=formulario)

                return redirect(url_for("begin.html"))
            else: 
            return render_template("purchase.html", form = formulario)

"""
@app.route("/status")
def status():
    return render_template("status.html")
