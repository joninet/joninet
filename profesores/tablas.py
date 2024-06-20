import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('profesordb.db')

# Crear un cursor
cursor = conexion.cursor()

# Obtener la lista de tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

# Mostrar las tablas
print("Tablas en la base de datos:")
for tabla in tablas:
    print(tabla[0])

# Obtener la estructura de cada tabla
for tabla in tablas:
    nombre_tabla = tabla[0]
    print(f"\nEstructura de la tabla {nombre_tabla}:")
    cursor.execute(f"PRAGMA table_info({nombre_tabla});")
    columnas = cursor.fetchall()
    for columna in columnas:
        print(columna)

# Obtener las claves foráneas de cada tabla
for tabla in tablas:
    nombre_tabla = tabla[0]
    print(f"\nClaves foráneas de la tabla {nombre_tabla}:")
    cursor.execute(f"PRAGMA foreign_key_list({nombre_tabla});")
    claves_foraneas = cursor.fetchall()
    for clave in claves_foraneas:
        print(clave)

# Cerrar la conexión
conexion.close()
