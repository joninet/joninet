import sqlite3 as sql

def eliminarRegistros():
    try:
        conn = sql.connect("profesordb.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notas")
            conn.commit()
            print("Todos los registros han sido eliminados.")
    except Exception as e:
        print("Error al eliminar los registros:", e)

eliminarRegistros()
