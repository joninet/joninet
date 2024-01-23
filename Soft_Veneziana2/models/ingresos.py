from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from datetime import datetime
from config import dbconn
from models.stock import stockActualInsumo
from helpers.funciones import editarStock
from helpers.funcionesDb import insertarDatos, borrarFila, actualizarDatos

def borrarIngresos():
    idBorrar = request.form['id']
    borrarFila(dbconn, 'ingresos', idBorrar)

    return redirect(url_for('main'))

def editarIngreso():
    id = request.form.get('id') 
    conn = sql.connect(dbconn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingresos WHERE id = ?", (id,))
    editar = cursor.fetchall()

    conn.close()
    return render_template('editarIngresos2.html', registro=editar)

def editarDb():
    idEditar = f"id = {request.form.get('id')}"
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    proveedor = request.form['proveedor']
    oc = request.form['oc']
    lote = request.form['lote']
    vto = request.form['vto']
    estado = request.form['estado']

    columnas = ["codigo", "descripcion", "cantidad", "proveedor", "oc", "lote", "vto", "estado", "eliminado"]
    valores = [codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, False]

    actualizarDatos(dbconn, "insumos", columnas, valores, idEditar)

    return redirect(url_for('main'))

def nuevoIngreso():
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    proveedor = request.form['proveedor']
    oc = request.form['oc']
    lote = request.form['lote']
    vto = request.form['vto']
    usuarioIngreso = request.form['usuarioIngreso']
    d = datetime.now()
    dateIngreso=d.strftime("%Y-%m-%d %H:%M:%S")

    if codigo and descripcion != "Codigo Incorrecto" and cantidad and proveedor and oc:
        columnas = ["fecha", "codigo", "descripcion", "cantidad", "proveedor", "oc", "lote", "vto", "estado", "eliminado", "usuarioIngreso"]
        valores = [dateIngreso, codigo, descripcion, cantidad, proveedor, oc, lote, vto, 'En Revision', False, usuarioIngreso]

        insertarDatos(dbconn, "ingresos", columnas, valores)

        stockNuevo = int(cantidad) + int(stockActualInsumo(codigo))

        editarStock(stockNuevo, codigo)
        
        return redirect(url_for('main'))
    else:
        return render_template('nuevoIngresos.html', errorIngresoInsumo="Las credenciales no son correctas o existen campos vacios")
    

def main():
    conn = sql.connect(dbconn)
    cursor = conn.cursor()  

    cursor.execute("SELECT * FROM ingresos WHERE eliminado = False")
    ingreso = cursor.fetchall()

    conn.close()

    return render_template('main.html', ingreso=ingreso)