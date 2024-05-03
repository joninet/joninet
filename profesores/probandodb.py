import sqlite3 as sql

def eliminarTabla():
    try:
        conn = sql.connect("profesordb.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS notas")
    except Exception as e:
        print("Error al eliminar la tabla:", e)

eliminarTabla()