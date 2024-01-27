import sqlite3 as sql
from flask import Flask, render_template
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

def actualizarDatos(dbconn, tabla, columnas, valores, condicion, condicion_valores):
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        set_clause = ', '.join([f"{columna} = ?" for columna in columnas])
        query = f"UPDATE {tabla} SET {set_clause} WHERE {condicion}"

        # Añadimos los valores de la condición al final de la lista de valores
        valores.extend(condicion_valores)

        cursor.execute(query, tuple(valores))
        conn.commit()
        conn.close()

    except sql.Error as e:
        print(f"Error al actualizar datos: {e}")
        if conn:
            conn.close()


def borrarFila(dbconn, tabla, id_fila):
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {tabla} WHERE id = ?", (id_fila,))

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error al borrar la fila: {e}")

def mostrarUltimasFilas(dbconn, tabla, limite):
    conn = sql.connect(dbconn)
    cursor = conn.cursor()  

    cursor.execute(f"SELECT * FROM {tabla} LIMIT {limite}")
    ingreso = cursor.fetchall()

    conn.close()
    return ingreso
