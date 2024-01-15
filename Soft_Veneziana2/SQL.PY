import sqlite3 as sql
from datetime import datetime

def nuevaTabla():
    conn = sql.connect("App_Notascopy/usuarios.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE ingresosInsumos (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surnames TEXT,
            email TEXT,
            password TEXT
        )"""
    )
    conn.commit()
    conn.close()

def nuevaTabla2():
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE ingresos (
            id INTEGER PRIMARY KEY,
            fecha DATETIME,
            codigo INTEGER,
            descripcion TEXT,
            cantidad REAL,
            proveedor TEXT,
            oc INTEGER,
            lote TEXT,
            vto DATE,
            estado TEXT,
            eliminado BOOLEAN)"""
    )
    conn.commit()
    conn.close()

nuevaTabla2()

def agregoIngreso(id, name, surnames, email, password):
    conn = sql.connect("App_Notascopy/usuarios.db")
    cursor = conn.cursor()
    fechaActual = datetime.now()

    instruccion = "INSERT INTO usuario (id, name, surnames, email, password) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(instruccion, (id, name, surnames, email, password))
    
    conn.commit()
    conn.close()

#agregoIngreso(1, "Jonathan", "Desplats", "joninet@msn.com", "fordfiesta")

def eliminarTabla():
    try:
        conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS ingresos")
    except Exception as e:
        print("Error al eliminar la tabla:", e)

#eliminarTabla()






