import sqlite3

conn=sqlite3.connect('Base_de_Datos/base_datos.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE Categoria (
    id INTEGER PRIMARY KEY,
    nombre TEXT
               )
               """)

conn.commit()
conn.close()