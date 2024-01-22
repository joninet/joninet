from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from config import dbconn
from datetime import datetime

def stockActualInsumo(codigo):
    conexion = sql.connect(dbconn)
    cursor = conexion.cursor()
    consulta = "SELECT cantidad FROM insumos WHERE codigo = ?"
    cursor.execute(consulta, (codigo,))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        return resultado[0]
    else:
        return 0 

