from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from datetime import datetime

def stockActualInsumo(codigo):
    conexion = sql.connect('Soft_Veneziana2/venezianaDB.db')
    cursor = conexion.cursor()
    consulta = "SELECT cantidad FROM insumos WHERE codigo = ?"
    cursor.execute(consulta, (codigo,))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        return resultado[0]# El resultado es una tupla, tomamos el primer elemento
    else:
        return 0  # Código no encontrado

