import sqlite3 as sql
from datetime import datetime

def nuevaTabla():
    conn = sql.connect("Soft_Veneziana/ingresos_db.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE ingresos_db (
            id INTEGER PRIMARY KEY,
            fecha TEXT,
            codigo INTEGER,
            descripcion TEXT,
            cantidad REAL,
            proveedor TEXT,
            oc INTEGER,
            lote TEXT,
            vto DATE,
            estado TEXT,
            eliminado BOOLEAN
        )"""
    )
    conn.commit()
    conn.close()

def agregoIngreso(codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, eliminado):
    conn = sql.connect("Soft_Veneziana/ingresos_db.db")
    cursor = conn.cursor()
    fechaActual= datetime.now()
    instruccion = f"INSERT INTO ingresos_db (fecha,codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, eliminado) VALUES ('{fechaActual}',{codigo}, '{descripcion}', {cantidad}, '{proveedor}', {oc}, '{lote}', '{vto}', '{estado}', {eliminado})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

agregoIngreso(3900001, "Harina 000", 28800, "Molino Chabas", 61950, "1305", "2024-11-20", "En Revision", False)


def eliminarIngreso(id):
    conn = sql.connect("Soft_Veneziana/ingresos_db.db")
    cursor = conn.cursor()
    instruccion = "UPDATE ingresos_db SET eliminado=True WHERE id = ?"
    cursor.execute(instruccion, (id,))
    conn.commit()
    conn.close()

def buscarId(numeroId):
    conn = sql.connect("Soft_Veneziana/ingresos_db.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM ingresos_db WHERE id = {numeroId}"
    cursor.execute(instruccion)
    fila = cursor.fetchone()
    conn.close()
    return fila

def modificoIngreso(id, codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, eliminado):
    conn = sql.connect("Soft_Veneziana/ingresos_db.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE ingresos_db SET codigo={codigo}, descripcion='{descripcion}', cantidad={cantidad}, proveedor='{proveedor}', oc={oc}, lote='{lote}', vto='{vto}', estado='{estado}', eliminado={eliminado} WHERE id={id}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

#modificoIngreso(6, 3900002, "Harina 0000", 28801, "Molino Minetti", 61951, "1306", "2023-11-19", "En Proceso", False)
#nuevaTabla()