from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from config import dbconn
from datetime import datetime
from helpers.funciones import editarStock

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
    
def nuevoDescuento():
    if request.method == 'POST':
        # Procesar los datos del formulario
        descuentos = {}
        for i in range(10):
            codigo = request.form['codigo']
            cantidad = request.form['cantidad']
            if codigo and cantidad:
                stockNuevo = int(stockActualInsumo(codigo)) - int(cantidad)
                editarStock(stockNuevo, codigo)

        # Aquí deberías aplicar los descuentos a tu base de datos SQL

    return render_template('datosActualizados.html')

