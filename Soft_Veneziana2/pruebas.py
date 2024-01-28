import sqlite3 as sql
from flask import Flask, render_template
from config import dbconn

def imprimirDatos(dbconn, valorBuscar, columnaMostrar, tabla, columnaBuscar):
    conn = sql.connect(dbconn)
    cursor = conn.cursor()

    cursor.execute(f"SELECT {columnaMostrar} FROM {tabla} WHERE {columnaBuscar} = ?", (valorBuscar,))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado:
        # Devuelve el código si se encontró el ID
        return resultado[0]
    
codigo = imprimirDatos("Soft_Veneziana2/baseDatos.db", 46949, "cantidad", "ingresos", "codigo")
print(codigo)
