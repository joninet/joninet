import sqlite3

conn = sqlite3.connect('Base_de_Datos/base_datos.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE Ingresos (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 fecha DATE NOT NULL,
                 cantidad REAL NOT NULL,
                 oc TEXT,
                 lotes TEXT,
                 vtos TEXT,
                 remito TEXT,
                 proveedor_id INTEGER NOT NULL,
                 producto_id INTEGER NOT NULL,
                 estado_id INTEGER NOT NULL,
                 usuario_id INTEGER NOT NULL,
                 FOREIGN KEY (proveedor_id) REFERENCES Proveedor(id),
                 FOREIGN KEY (producto_id) REFERENCES Producto(id),
                 FOREIGN KEY (estado_id) REFERENCES Estado(id),
                 FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
                 
               )
               """)


conn.commit()
conn.close()
