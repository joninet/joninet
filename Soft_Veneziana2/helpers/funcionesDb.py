import sqlite3 as sql
def insertarDatos(dbconn, tabla, columnas, valores):
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        query = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({', '.join(['?' for _ in valores])})"
        cursor.execute(query, valores)
        conn.commit()
        conn.close()
        
    except sql.Error as e:
        print(f"Error al insertar datos: {e}")
        if conn:
            conn.close()

def actualizarDatos(dbconn, tabla, columnas, valores, condicion):
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        set_clause = ', '.join([f"{columna} = ?" for columna in columnas])
        query = f"UPDATE {tabla} SET {set_clause} WHERE {condicion}"
        
        cursor.execute(query, valores)
        conn.commit()
        conn.close()
        
    except sql.Error as e:
        print(f"Error al actualizar datos: {e}")
        if conn:
            conn.close()


def borrarFila(dbconn, tabla, id):
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {tabla} WHERE id = ?", (id,))

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error al borrar la fila: {e}")