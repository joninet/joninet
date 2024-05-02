import sqlite3

def agregar_columna_division():
    # Establecer conexión con la base de datos
    try:
        conexion = sqlite3.connect('profesordb.db')
        cursor = conexion.cursor()
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return

    # Verificar si la columna ya existe
    try:
        cursor.execute("SELECT division FROM grados")
    except sqlite3.OperationalError:
        # La columna no existe, agregarla
        consulta = """
        ALTER TABLE grados
        ADD COLUMN division TEXT;
        """
        cursor.execute(consulta)
        conexion.commit()
        print("Columna 'division' agregada exitosamente")
    else:
        # La columna ya existe, informar al usuario
        print("La columna 'division' ya existe en la tabla 'grados'")

    # Cerrar la conexión a la base de datos
    finally:
        if conexion:
            conexion.close()

if __name__ == "__main__":
    agregar_columna_division()

