import sqlite3
DATABASE_FILE = "App_Stock/baseDatos.db"

def create_table():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entryproducts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE,
            code INTEGER,
            name TEXT,
            um TEXT,
            quantity REAL,
            warehouse INTEGER,
            supplier TEXT,
            invoice TEXT,
            comment TEXT
        )
    ''')
    connection.commit()
    connection.close()

create_table()