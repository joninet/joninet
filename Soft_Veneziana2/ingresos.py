from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from datetime import datetime
from stock import stockActualInsumo

def borrarIngresos():
    try:
        conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
        id = request.form['id']
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM ingresos WHERE id = ?", (id,))

        conn.commit()
        conn.close()

        return redirect(url_for('main'))

    except Exception as e:
        return f"Error al borrar el ingreso: {str(e)}"

def editarIngreso():
    id = request.form.get('id')  # Obtén el valor de 'id' del formulario
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
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

    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()

    query = """UPDATE ingresos
                SET codigo = ?, descripcion = ?, cantidad = ?, 
                    proveedor = ?, oc = ?, lote = ?, vto = ?, estado = ?
                WHERE id = ?"""
    params = (codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, id)
            # Ejecutar la consulta de actualización
    cursor.execute(query, params)
            # Commit para aplicar los cambios
    conn.commit()
            # Cerrar la conexión
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
        conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
        cursor = conn.cursor()
        # Insertar datos en la tabla 'ingresos'
        cursor.execute("INSERT INTO ingresos (fecha, codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, eliminado, usuarioIngreso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (dateIngreso, codigo, descripcion, cantidad, proveedor, oc, lote, vto, 'En Revision', False, usuarioIngreso))
        # Commit para aplicar cambios
        conn.commit()
        # Cerrar la conexión
        conn.close()

        #agregamos al stock
        stockNuevo = int(cantidad) + int(stockActualInsumo(codigo))

        conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
        cursor = conn.cursor()
        consulta_busqueda = "SELECT * FROM insumos WHERE codigo = ?"
        cursor.execute(consulta_busqueda, (codigo,))
        resultado = cursor.fetchone()

        if resultado:
            consulta_actualizacion = "UPDATE insumos SET cantidad = ? WHERE codigo = ?"
            cursor.execute(consulta_actualizacion, (stockNuevo, codigo))
            conn.commit()
            conn.close()

        return redirect(url_for('main'))
    

    else:
        return render_template('nuevoIngresos.html', errorIngresoInsumo="Las credenciales no son correctas o existen campos vacios")
    

def main():
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()  

    cursor.execute("SELECT * FROM ingresos WHERE eliminado = False")
    ingreso = cursor.fetchall()

    conn.close()

    return render_template('main.html', ingreso=ingreso)