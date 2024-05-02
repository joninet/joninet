import sqlite3 as sql
import json
from fastapi import HTTPException
import math

class FuncionesDB():
  def __init__(self):
    self._con = sql.connect("./profesordb.db")
    self._cur = self._con.cursor()

  #funcion para insertar datos en una tabla
  #column: nombres de las columnas en formato lista column = ["name", "code"]
  #values: valores de la columna en formato lista values = ["valorName", "valorCode"]
  def insertarDatos(self, tabla, column, values):
    try:
      query = f"INSERT INTO {tabla} ({', '.join(column)}) VALUES ({', '.join(['?' for _ in values])})"
      self._cur.execute(query, values)
      self._con.commit()
      id_ = self._cur.lastrowid
      return id_
    except sql.Error as e:
      print(f"error: {e}")

  def __del__(self):
    self._con.close()