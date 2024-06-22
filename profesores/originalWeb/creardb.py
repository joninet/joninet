import psycopg2

# Define tu script SQL como un string
sql_script = """
-- Crear tabla colegios
CREATE TABLE colegios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Crear tabla grados
CREATE TABLE grados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    division TEXT
);

-- Crear tabla materias
CREATE TABLE materias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    id_colegio INTEGER NOT NULL,
    id_grado INTEGER NOT NULL,
    FOREIGN KEY (id_colegio) REFERENCES colegios(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (id_grado) REFERENCES grados(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Crear tabla alumnos
CREATE TABLE alumnos (
    id SERIAL PRIMARY KEY,
    nombres VARCHAR(255) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    id_colegios INTEGER NOT NULL,
    id_grados INTEGER NOT NULL,
    FOREIGN KEY (id_colegios) REFERENCES colegios(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (id_grados) REFERENCES grados(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Crear tabla parciales
CREATE TABLE parciales (
    id SERIAL PRIMARY KEY,
    tema VARCHAR(255) NOT NULL,
    id_materias INTEGER NOT NULL,
    FOREIGN KEY (id_materias) REFERENCES materias(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Crear tabla notas
CREATE TABLE notas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    nota FLOAT NOT NULL,
    rec1 FLOAT,
    rec2 FLOAT,
    rec3 FLOAT,
    id_alumno INTEGER NOT NULL,
    id_parcial INTEGER NOT NULL,
    FOREIGN KEY (id_alumno) REFERENCES alumnos(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (id_parcial) REFERENCES parciales(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);
"""

# Conecta a tu base de datos PostgreSQL y ejecuta el script
try:
    # Conectar a la base de datos
    conn = psycopg2.connect(
        dbname="profesor_db",
        user="profesor_db_user",
        password="koOaedgIMCvjcAxHOld1F0Jd5ytWkIeM",  # Reemplaza 'your_password' con tu contraseña real
        host="dpg-cpabeiv109ks73alrtj0-a.oregon-postgres.render.com",
        port="5432"
    )
    cur = conn.cursor()
    
    # Ejecutar el script SQL
    cur.execute(sql_script)
    
    # Confirmar los cambios
    conn.commit()
    
    # Cerrar la conexión
    cur.close()
    conn.close()

    print("Tablas y relaciones creadas exitosamente")
except Exception as e:
    print(f"Error al crear las tablas: {e}")
