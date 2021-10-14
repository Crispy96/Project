import sqlite3

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