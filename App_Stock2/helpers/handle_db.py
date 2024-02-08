import sqlite3 as sql
import json
from fastapi import HTTPException

class HandleDB():
  def __init__(self):
    self._con = sql.connect("./baseDatos.db")
    self._cur = self._con.cursor()

  #funcion para insertar datos en una tabla
  #column: nombres de las columnas en formato lista column = ["name", "code"]
  #values: valores de la columna en formato lista values = ["valorName", "valorCode"]
  def insertData(self, table, column, values):
    try:
      query = f"INSERT INTO {table} ({', '.join(column)}) VALUES ({', '.join(['?' for _ in values])})"
      self._cur.execute(query, values)
      self._con.commit()
    except sql.Error as e:
      print(f"Failed to insert data: {e}")

  #funcion para ver ver un registro segun el id
  #id: id del cual queremos la informacion
  #table: nombre de la tabla
  def viewRow(self, id, table):
    #Verificamos si existe el id
    checkId=self.printData(id, "id", table, "id")
    if checkId is None:
      return {"message": "ID not found"}
    else:
      try:
        self._cur.execute(f"SELECT * FROM {table} WHERE id = ?", (id,))
        row = self._cur.fetchone()

        if row:
          #cursor.description (me muestra la descripcion de cada columna)
          columns = [desc[0] for desc in self._cur.description]
          #zip convina column y row, y despues con dict las convierte en diccionario a las 2 parejas
          result = dict(zip(columns, row))
          return result
        else:
          raise HTTPException(status_code=404, detail=f"Row with ID {id} not found in table {table}")
      except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
      

  #fundion para editar un registro
  #tabla: nombre de la tabla 
  #column: nombres de las columnas en formato lista column = ["name", "code"]
  #values: valores de la columna en formato lista values = ["valorName", "valorCode"]
  #condition en formato f"id = ?"
  #conditionValues en formato (id,)
  
  def editRow(self, tabla, column, values, condition, conditionValues):
    try:
      setClause = ', '.join([f"{column} = ?" for column in column])
      query = f"UPDATE {tabla} SET {setClause} WHERE {condition}"

      values.extend(conditionValues)

      self._cur.execute(query, tuple(values))
      self._con.commit()
      return "corrrecto"
    
    except sql.Error as e:
        print(f"Error al actualizar datos: {e}")

  def printData(self, valueSearch, columnView, table, columnSearch):
     try:
        self._cur.execute(f"SELECT {columnView} FROM {table} WHERE {columnSearch} = ?", (valueSearch,))
        result = self._cur.fetchone()

        return result[0] if result else None
     except sql.Error as e:
      print(f"Error al consultar datos: {e}")
      return None
     
  def deleteRow(self, table, id):
    checkId = self.printData(id, "id", table, "id")
    if checkId is None:
      return {"message": "ID not found"}
    else:
      try:
        self._cur.execute(f"DELETE FROM {table} WHERE id = ?", (id,))
        self._con.commit()
        return {"message": "Delet Product successfully"}
      except Exception as e:
        return {"message": "Error deleting row:"}
  
  def viewRowLimit(self, table, limit):
    try:
      self._cur.execute(f"SELECT * FROM {table} LIMIT {limit}")
      rows = self._cur.fetchall()

      # Convertir las filas a una lista de diccionarios
      columns = [column[0] for column in self._cur.description]
      result = [dict(zip(columns, row)) for row in rows]
      return result
    
    except sql.Error as e:
      print(f"Error al consultar datos: {e}")
      return None
        

  def __del__(self):
    self._con.close()