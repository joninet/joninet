from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from datetime import datetime
from config import dbconn
from models.stock import stockActualInsumo
from helpers.funciones import editarStock

def borrarIngresos():
    try:
        conn = sql.connect(dbconn)
        id = request.form['id']
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM ingresos WHERE id = ?", (id,))

        conn.commit()
        conn.close()

        return redirect(url_for('main'))

    except Exception as e:
        return f"Error al borrar el ingreso: {str(e)}"

def editarIngreso():
    id = request.form.get('id') 
    conn = sql.connect(dbconn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingresos WHERE id = ?", (id,))
    editar = cursor.fetchall()

    conn.close()
    return render_template('editarIngresos2.html', registro=editar)

def editarDb():
    id = request.form.get('id')
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    proveedor = request.form['proveedor']
    oc = request.form['oc']
    lote = request.form['lote']
    vto = request.form['vto']
    estado = request.form['estado']

    conn = sql.connect(dbconn)
    cursor = conn.cursor()

    query = """UPDATE ingresos
                SET codigo = ?, descripcion = ?, cantidad = ?, 
                    proveedor = ?, oc = ?, lote = ?, vto = ?, estado = ?
                WHERE id = ?"""
    params = (codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, id)

    cursor.execute(query, params)
    conn.commit()
    conn.close()

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
        conn = sql.connect(dbconn)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ingresos (fecha, codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, eliminado, usuarioIngreso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (dateIngreso, codigo, descripcion, cantidad, proveedor, oc, lote, vto, 'En Revision', False, usuarioIngreso))
        conn.commit()
        conn.close()

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