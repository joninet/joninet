import sqlite3 as sql
from datetime import datetime

def nuevaTabla():
    conn = sql.connect("App_Notascopy/venezianaDB.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE insumos (
            id INTEGER PRIMARY KEY,
            codigo INTEGER,
            nombre TEXT,
            cantidad REAL,
            tipo TEXT,
            um TEXT)"""
    )
    conn.commit()
    conn.close()

nuevaTabla()

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
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()

    try:
        # Agrega la nueva columna 'idusuario' a la tabla 'ingresos'
        cursor.execute("ALTER TABLE usuario ADD COLUMN nombreUsuario TEXT")

        # Guarda los cambios en la base de datos
        conn.commit()
        print("Columna 'nombreusuario' agregada correctamente.")

    except sql.Error as e:
        print(f"Error al agregar la columna 'idusuario': {e}")

    finally:
        conn.close()

#agregarColumnaIdUsuario()
        
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







