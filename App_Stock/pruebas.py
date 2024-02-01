import sqlite3 as sql
import json
from fastapi import HTTPException

dbconn = "baseDatos.db"
def printData(dbconn, valueSearch, columnView, table, columnSearch):
    conn = sql.connect(dbconn)
    cursor = conn.cursor()

    cursor.execute(f"SELECT {columnView} FROM {table} WHERE {columnSearch} = ?", (valueSearch,))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado:
        return resultado[0]
    
print()