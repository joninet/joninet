import sqlite3 as sql

def insertData(dbconn, table, column, values):
    conn = None
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        query = f"INSERT INTO {table} ({', '.join(column)}) VALUES ({', '.join(['?' for _ in values])})"
        cursor.execute(query, values)
        conn.commit()
        
    except sql.Error as e:
        print(f"Error al insertar datos: {e}")
        
    finally:
        if conn:
            conn.close()
