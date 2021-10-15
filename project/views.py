from project import app
from flask import render_template, request
from project.models import DBManager
from project.forms import MovimientosFormulario

route_database = app.config.get("ROUTE_DATA_BASE")
dbManager = DBManager(route_database)

@app.route("/")
def begin():
    consulta = """ SELECT * FROM movimientos ORDER BY date """
    movimientos = dbManager.consultaSQL(consulta)

    return render_template("begin.html", items=movimientos)

@app.route("/purchase", methods=['GET', 'POST'])
def purchase():
    formulario= MovimientosFormulario()
    if request.method == 'GET':
        return render_template("purchase.html", el_formulario = formulario)
    else:
        pass      
