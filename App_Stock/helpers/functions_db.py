import sqlite3 as sql
import json
from fastapi import HTTPException

def insertData(dbconn, table, column, values):
    conn = None
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        query = f"INSERT INTO {table} ({', '.join(column)}) VALUES ({', '.join(['?' for _ in values])})"
        cursor.execute(query, values)
        conn.commit()
        
    except sql.Error as e:
        print(f"Failed to insert data: {e}")
        
    finally:
        if conn:
            conn.close()

def viewRow(dbconn, id, table):
    try:
        db = sql.connect(dbconn)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {table} WHERE id = ?", (id,))
        row = cursor.fetchone()
        db.close()

        if row:
            #cursor.description (me muestra la descripcion de cada columna)
            columns = [desc[0] for desc in cursor.description]
            #zip convina column y row, y despues con dict las convierte en diccionario a las 2 parejas
            result = dict(zip(columns, row))
            return result
        else:
            raise HTTPException(status_code=404, detail=f"Row with ID {id} not found in table {table}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def editRow(dbconn, tabla, columnas, valores, condicion, condicion_valores):
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        set_clause = ', '.join([f"{columna} = ?" for columna in columnas])
        query = f"UPDATE {tabla} SET {set_clause} WHERE {condicion}"

        # Añadimos los valores de la condición al final de la lista de valores
        valores.extend(condicion_valores)

        cursor.execute(query, tuple(valores))
        conn.commit()
        conn.close()
        return "corrrecto"

    except sql.Error as e:
        print(f"Error al actualizar datos: {e}")
        if conn:
            conn.close()

def printData(dbconn, valueSearch, columnView, table, columnSearch):
    conn = sql.connect(dbconn)
    cursor = conn.cursor()

    cursor.execute(f"SELECT {columnView} FROM {table} WHERE {columnSearch} = ?", (valueSearch,))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado:
        return resultado[0]
    else:
        return None
    
def deleteRow(dbconn, table, id):
    checkId=printData(dbconn, id, "id", "products", "id")
    if checkId is None:
        return {"message": "ID not found"}
    else:
        try:
            conn = sql.connect(dbconn)
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {table} WHERE id = ?", (id,))

            conn.commit()
            conn.close()
            return {"message": "Delet Product successfully"}

        except Exception as e:
            return {"message": "Error deleting row:"}
