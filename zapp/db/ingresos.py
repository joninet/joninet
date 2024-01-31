import sqlite3

def conectar_base_datos():
    connection = sqlite3.connect("ingresos.db")
    return connection

def cerrar_base_datos(connection):
    connection.close()

def crear_tabla_ingresos(connection):
    connection.execute(
        """
        CREATE TABLE ingresos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo VARCHAR(255),
            nombre VARCHAR(255),
            cantidad INTEGER,
            fecha DATE
        );
        """
    )

def insertar_ingreso(connection, ingreso):
    connection.execute(
        """
        INSERT INTO ingresos (
            codigo,
            nombre,
            cantidad,
            fecha
        ) VALUES (
            ?,
            ?,
            ?,
            CURRENT_DATE
        );
        """,
        (ingreso.codigo, ingreso.nombre, ingreso.cantidad),
    )
    connection.commit()

def obtener_ingresos(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ingresos")
    return cursor.fetchall()

def cerrar_cursor(cursor):
    cursor.close()