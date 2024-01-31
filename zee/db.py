import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("ingresos.db")

# Crear el cursor
cursor = conexion.cursor()

# Crear la tabla
cursor.execute("""
CREATE TABLE ingresos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    nombre TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATETIME NOT NULL
);
""")

# Cerrar la conexión
conexion.commit()
conexion.close()