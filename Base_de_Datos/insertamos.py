import sqlite3 as sql
import json
from fastapi import HTTPException
import datetime

class HandleDB():
    def __init__(self):
        self._con = sql.connect("Base_de_Datos/base_datos.db")
        self._cur = self._con.cursor()

    def insertData(self, tabla, columna, valores):
        try:
            query = f"INSERT INTO {tabla} ({', '.join(columna)}) VALUES ({', '.join(['?' for _ in valores])})"
            self._cur.execute(query, valores)
            self._con.commit()
        except sql.Error as e:
            print(f"error al insertar: {e}")


    def deleteRow(self, tabla, id):
        self._cur.execute(f"DELETE FROM {tabla} WHERE id = ?", (id,))
        self._con.commit()
        return {"message": "Delet Product successfully"}
            
    def __del__(self):
        self._con.close()

#funcion para insertar datos en una tabla
#column: nombres de las columnas en formato lista column = ["name", "code"]
#values: valores de la columna en formato lista values = ["valorName", "valorCode"]
fecha=datetime.datetime.now()
fechaHoy=fecha.strftime('%Y-%m-%d %H:%M:%S')
columna = ["fecha", "cantidad", "oc", "lotes", "vtos", "remito", "proveedor_id", "producto_id", "estado_id", "usuario_id"]
valores = [fecha, 96000, "456666", "198234", "", "2-9567", 2, 2, 1, 1]

inserto=HandleDB()
inserto.insertData("Ingresos", columna, valores)
      