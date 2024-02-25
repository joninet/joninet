import sqlite3

conn = sqlite3.connect('App_Stock3/base_datos.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE Producto (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nombre TEXT NOT NULL,
                 um TEXT NOT NULL,
                 descripcion TEXT,
                 categoria_id INTEGER NOT NULL,
                 FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
                 
               )
               """)


conn.commit()
conn.close()