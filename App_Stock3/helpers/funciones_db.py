import sqlite3 as sql
import json
from fastapi import HTTPException

class FuncionesDB():
  def __init__(self):
    self._con = sql.connect("./base_datos.db")
    self._cur = self._con.cursor()

  #funcion para insertar datos en una tabla
  #column: nombres de las columnas en formato lista column = ["name", "code"]
  #values: valores de la columna en formato lista values = ["valorName", "valorCode"]
  def insertarDatos(self, tabla, column, values):
    try:
      query = f"INSERT INTO {tabla} ({', '.join(column)}) VALUES ({', '.join(['?' for _ in values])})"
      self._cur.execute(query, values)
      self._con.commit()
    except sql.Error as e:
      print(f"error: {e}")

  def seleccionarDatos(self, valorBuscar, columnaMostrar, tabla, columnaBuscar):
    try:
      self._cur.execute(f"SELECT {columnaMostrar} FROM {tabla} WHERE {columnaBuscar} = ?", (valorBuscar,))
      result = self._cur.fetchone()

      return result[0] if result else None
    except sql.Error as e:
      print(f"Error al consultar datos: {e}")
      return None  
    
  def borrarDatos(self, tabla, id):
    checkId = self.seleccionarDatos(id, "id", tabla, "id")
    if checkId is None:
      return {"message": "No existe el Id"}
    else:
      try:
        self._cur.execute(f"DELETE FROM {tabla} WHERE id = ?", (id,))
        self._con.commit()
        return {"message": "Borrado correctamente"}
      except Exception as e:
        return {"message": "Error al borrar:"}

  def __del__(self):
    self._con.close()