import sqlite3
DATABASE_FILE = "App_Stock/baseDatos.db"

def create_table():
    # Crea la tabla si no existe
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            code INTEGER,
            stock REAL,
            typeProduct TEXT,
            um TEXT
        )
    ''')
    connection.commit()
    connection.close()

create_table()