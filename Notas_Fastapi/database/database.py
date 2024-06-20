import sqlite3

# Crear la base de datos y las tablas necesarias
def crear_base_de_datos():
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()

    # Crear tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')

    # Crear tabla de notas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            contenido TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    ''')

    conexion.commit()
    conexion.close()

crear_base_de_datos()
