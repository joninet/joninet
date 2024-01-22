import sqlite3 as sql
def insertar_datos_generico(dbconn, tabla, columnas, valores):
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        # Construir la consulta SQL dinámicamente
        query = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({', '.join(['?' for _ in valores])})"
        cursor.execute(query, valores)

        conn.commit()
    except sql.Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        if conn:
            conn.close()
