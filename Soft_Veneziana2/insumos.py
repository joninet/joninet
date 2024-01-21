from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from datetime import datetime
from funciones import codAleatorio

def nuevoInsumoDB():
    codigo = codAleatorio()
    nombre = request.form['nombre']
    tipo = request.form['tipo']
    um = request.form['um']

    if not (codigo and nombre and tipo and um):
        return render_template('nuevoInsumo.html', errorIngresoInsumo="Las credenciales no son correctas o existen campos vacíos")

    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()

    # Verificar si el nombre ya existe en la base de datos
    cursor.execute("SELECT COUNT(*) FROM insumos WHERE nombre = ?", (nombre,))
    count = cursor.fetchone()[0]

    if count > 0:
        conn.close()
        return render_template('nuevoInsumo.html', errorIngresoInsumo="El nombre ya existe en la base de datos")

    # Insertar datos en la tabla 'insumos'
    cursor.execute("INSERT INTO insumos (codigo, nombre, cantidad, tipo, um) VALUES (?, ?, ?, ?, ?)", (codigo, nombre, 0, tipo, um))

    # Commit para aplicar cambios
    conn.commit()

    # Cerrar la conexión
    conn.close()

    return redirect(url_for('main'))


