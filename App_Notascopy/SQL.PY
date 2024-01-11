import sqlite3 as sql
from datetime import datetime

def nuevaTabla():
    conn = sql.connect("App_Notascopy/usuarios.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE usuario (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surnames TEXT,
            email TEXT,
            password TEXT
        )"""
    )
    conn.commit()
    conn.close()

def agregoIngreso(id, name, surnames, email, password):
    conn = sql.connect("App_Notascopy/usuarios.db")
    cursor = conn.cursor()
    fechaActual = datetime.now()

    instruccion = f"INSERT INTO usuario (id, name, surnames, email, password) VALUES ({id}, '{name}', '{surnames}', '{email}', '{password}')"
    
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

agregoIngreso(1, "Jonathan", "Desplats", "joninet@msn.com", "fordfiesta")





