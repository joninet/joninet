import sqlite3 as sql
from datetime import datetime

import sqlite3 as sql
from datetime import datetime

def tabla_existe(cursor, nombre_tabla):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{nombre_tabla}'")
    return cursor.fetchone() is not None

def nueva_tabla():
    conn = sql.connect("Soft_Veneziana2/baseDatos.db")
    cursor = conn.cursor()
    
    nombre_tabla = "insumos"
    
    if not tabla_existe(cursor, nombre_tabla):
        cursor.execute(
            f"""CREATE TABLE {nombre_tabla} (
                id INTEGER PRIMARY KEY,
                codigo INTEGER,
                nombre TEXT,
                cantidad REAL,
                tipo TEXT,
                um TEXT)"""
        )
        conn.commit()
        print(f"Tabla '{nombre_tabla}' creada exitosamente.")
    else:
        print(f"La tabla '{nombre_tabla}' ya existe.")
    
    conn.close()

#nueva_tabla()


def nuevaTabla2():
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE ingresos (
            id INTEGER PRIMARY KEY,
            fecha DATETIME,
            codigo INTEGER,
            descripcion TEXT,
            cantidad REAL,
            proveedor TEXT,
            oc INTEGER,
            lote TEXT,
            vto DATE,
            estado TEXT,
            eliminado BOOLEAN)"""
    )
    conn.commit()
    conn.close()

#nuevaTabla2()

"""def agregoIngreso(id, name, surnames, email, password, nombreUsuario):
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()
    fechaActual = datetime.now()

    instruccion = "INSERT INTO usuario (id, name, surnames, email, password, nombreUsuario) VALUES (?, ?, ?, ?, ?,?)"
    cursor.execute(instruccion, (id, name, surnames, email, password, nombreUsuario))
    
    conn.commit()
    conn.close()

agregoIngreso(2, "Jonathan", "Desplats", "joninet@msn.com", "fordfiesta", "joninet")

def eliminarTabla():
    try:
        conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS ingresos")
    except Exception as e:
        print("Error al eliminar la tabla:", e)

#eliminarTabla()"""
        

def agregarColumnaIdUsuario():
    conn = sql.connect("Soft_Veneziana2/baseDatos.db")
    cursor = conn.cursor()

    try:
        # Agrega la nueva columna 'idusuario' a la tabla 'ingresos'
        cursor.execute("ALTER TABLE ingresos ADD COLUMN remito TEXT")

        # Guarda los cambios en la base de datos
        conn.commit()
        print("Columna 'remito' agregada correctamente.")

    except sql.Error as e:
        print(f"Error al agregar la columna 'remito': {e}")

    finally:
        conn.close()

agregarColumnaIdUsuario()
        
def modificarColumnaIdUsuario():
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()

    try:
        # Modifica el nombre de la columna a 'usuarioIngreso'
        cursor.execute("ALTER TABLE ingresos RENAME COLUMN idusuario TO usuarioIngreso")

        # Modifica el tipo de la columna a 'TEXT'
        cursor.execute("ALTER TABLE ingresos ALTER COLUMN usuarioIngreso TYPE TEXT")

        # Guarda los cambios en la base de datos
        conn.commit()
        print("Columna 'idusuario' modificada correctamente.")

    except sql.Error as e:
        print(f"Error al modificar la columna 'idusuario': {e}")

    finally:
        conn.close()

#modificarColumnaIdUsuario()

def eliminar_usuario_por_id(id_usuario):
    try:
        # Conectar a la base de datos
        conexion = sql.connect("Soft_Veneziana2/venezianaDB.db")  # Asegúrate de proporcionar el nombre correcto de tu base de datos

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar la sentencia SQL para eliminar la fila
        cursor.execute('DELETE FROM usuario WHERE id = ?', (id_usuario,))

        # Confirmar la operación
        conexion.commit()

        print(f'Usuario con ID {id_usuario} eliminado correctamente.')

    except sqlite3.Error as error:
        print(f'Error al eliminar el usuario: {error}')

    finally:
        # Cerrar la conexión
        if conexion:
            conexion.close()

# Usar la función para eliminar el usuario con ID 1
#eliminar_usuario_por_id(1)

def eliminar_filas_por_ids(database, table, id_column, ids_to_delete):
    try:
        # Conectar a la base de datos
        conn = sql.connect(database)
        cursor = conn.cursor()

        # Construir la consulta SQL para eliminar las filas con los IDs especificados
        query = f"DELETE FROM {table} WHERE {id_column} IN ({','.join('?' for _ in ids_to_delete)})"

        # Imprimir la consulta para depuración
        print("Query:", query)

        # Ejecutar la consulta con la lista de IDs
        cursor.execute(query, ids_to_delete)

        # Imprimir el número de filas afectadas
        print("Filas afectadas:", cursor.rowcount)

        # Confirmar los cambios en la base de datos
        conn.commit()

    except sqlite3.Error as e:
        # Imprimir el error en caso de excepción
        print("Error al eliminar filas:", e)

    finally:
        # Cerrar la conexión
        conn.close()

# Uso de la función para eliminar filas con IDs 1, 2, 3, 4, 5
#eliminar_filas_por_ids("Soft_Veneziana2/venezianaDB.db", "insumos", "id", [1, 2, 3, 4, 5])









