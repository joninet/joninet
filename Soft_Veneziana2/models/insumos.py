from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from datetime import datetime
from config import dbconn
from helpers.funciones import codAleatorio
from helpers.funcionesDb import insertarDatos, borrarFila, actualizarDatos

def borrarInsumos():
    idBorrar = request.form['idInsumo']
    borrarFila(dbconn, 'insumos', idBorrar)

    return render_template('datosActualizados.html')

def nuevoInsumoDB():
    codigo = codAleatorio()
    nombre = request.form['nombre']
    tipo = request.form['tipo']
    um = request.form['um']

    if not (codigo and nombre and tipo and um):
        return render_template('nuevoInsumo.html', errorIngresoInsumo="Las credenciales no son correctas o existen campos vacíos")

    conn = sql.connect(dbconn)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM insumos WHERE nombre = ?", (nombre,))
    count = cursor.fetchone()[0]

    if count > 0:
        conn.close()
        return render_template('nuevoInsumo.html', errorIngresoInsumo="El nombre ya existe en la base de datos")

    cursor.execute("INSERT INTO insumos (codigo, nombre, cantidad, tipo, um) VALUES (?, ?, ?, ?, ?)", (codigo, nombre, 0, tipo, um))

    conn.commit()

    conn.close()

    return render_template('datosActualizados.html')

def editarInsumo():
    id = request.form.get('id') 
    conn = sql.connect(dbconn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM insumos WHERE id = ?", (id,))
    editar = cursor.fetchall()

    conn.close()
    return render_template('editarInsumo.html', registro=editar)

def editarDbInsumo(id_fila):
    nombre = request.form['nombre']
    tipo = request.form['tipo']
    um = request.form['um']

    columnas = ["nombre", "tipo", "um"]
    valores = [nombre, tipo, um]

    actualizarDatos(dbconn, "insumos", columnas, valores, f"id = ?", (id_fila,))
    return render_template('datosActualizados.html')


