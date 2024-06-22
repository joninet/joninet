import sqlite3

# Conéctate a la base de datos (o crea una nueva base de datos si no existe)
conn = sqlite3.connect('profesordb.db')

# Crea un cursor
cursor = conn.cursor()

# Agrega la nueva columna 'fecha' a la tabla 'condiciones'
cursor.execute('''
    ALTER TABLE parciales
    ADD COLUMN fecha DATE
''')

# Confirma los cambios
conn.commit()

# Cierra la conexión
conn.close()

