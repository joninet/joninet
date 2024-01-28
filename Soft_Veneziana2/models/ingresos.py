from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from datetime import datetime
from config import dbconn
from models.stock import stockActualInsumo
from helpers.funciones import editarStock
from helpers.funcionesDb import insertarDatos, borrarFila, actualizarDatos, imprimirDatos

def mostrarIngreso(id_fila):
  db = sql.connect(dbconn)
  ingreso = db.execute("SELECT * FROM ingresos WHERE id = {}".format(id_fila)).fetchone()

  return render_template("mostrarIngreso.html", ingreso=ingreso)

def borrarIngresos():
    idBorrar = request.form['id']
    codigo = imprimirDatos(dbconn, idBorrar, "codigo", "ingresos", "id")
    cantidadIngreso= imprimirDatos(dbconn, codigo, "cantidad", "ingresos", "codigo")
    stockNuevo = int(stockActualInsumo(codigo)) - int(cantidadIngreso)
    editarStock(stockNuevo, codigo)

    borrarFila(dbconn, 'ingresos', idBorrar)

    return render_template('datosActualizados.html')

def editarIngreso():
    id = request.form.get('id') 
    conn = sql.connect(dbconn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingresos WHERE id = ?", (id,))
    editar = cursor.fetchall()

    conn.close()
    return render_template('editarIngresos2.html', registro=editar)

def editarDb(id_fila):
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    proveedor = request.form['proveedor']
    oc = request.form['oc']
    lote = request.form['lote']
    vto = request.form['vto']
    estado = request.form['estado']
    remito = request.form['remito']

    columnas = ["codigo", "descripcion", "cantidad", "proveedor", "oc", "lote", "vto", "estado", "remito"]
    valores = [codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, remito]

    actualizarDatos(dbconn, "ingresos", columnas, valores, f"id = ?", (id_fila,))
    return render_template('datosActualizados.html')

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
    remito=request.form['remito']

    if codigo and descripcion != "Codigo Incorrecto" and cantidad and proveedor and oc:
        columnas = ["fecha", "codigo", "descripcion", "cantidad", "proveedor", "oc", "lote", "vto", "estado", "eliminado", "usuarioIngreso", "remito"]
        valores = [dateIngreso, codigo, descripcion, cantidad, proveedor, oc, lote, vto, 'En Revision', False, usuarioIngreso, remito]

        insertarDatos(dbconn, "ingresos", columnas, valores)

        stockNuevo = int(cantidad) + int(stockActualInsumo(codigo))

        editarStock(stockNuevo, codigo)
        
        return render_template('datosActualizados.html')
    else:
        return render_template('nuevoIngresos.html', errorIngresoInsumo="Las credenciales no son correctas o existen campos vacios")
    


