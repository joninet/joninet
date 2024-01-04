"""import sqlite3

# Conectar a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect('App_Notas/users.db')

# Crear un cursor
cursor = conn.cursor()

# Ejecutar la consulta SQL
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        surnames TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()"""

import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('App_Notas/users.db')

# Crear un cursor
cursor = conn.cursor()

# Datos del usuario a insertar
nuevo_usuario = ('Jonathan', 'Desplats', 'joninet@msn.com', 'fordfiesta')

# Ejecutar la consulta SQL para insertar un nuevo usuario
cursor.execute('''
    INSERT INTO users (name, surnames, email, password)
    VALUES (?, ?, ?, ?)
''', nuevo_usuario)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()


