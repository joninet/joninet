import sqlite3

def conectar_db(nombre_db):
  """Crea una conexión a la base de datos SQLite con el nombre especificado."""
  conexion = sqlite3.connect(nombre_db)
  return conexion

conexion = conectar_db("profesordb.db")
cursor = conexion.cursor()

# Crear la tabla "alumnos"
cursor.execute("""
CREATE TABLE alumnos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(255) NOT NULL,
  apellidos VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  id_colegio INTEGER NOT NULL,
  FOREIGN KEY (id_colegio) REFERENCES colegios(id)
);
""")

# Crear la tabla "colegios"
cursor.execute("""
CREATE TABLE colegios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(255) NOT NULL
);
""")

# Crear la tabla "grados"
cursor.execute("""
CREATE TABLE grados (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(255) NOT NULL
);
""")

# Crear la tabla "materias"
cursor.execute("""
CREATE TABLE materias (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(255) NOT NULL,
  id_colegio INTEGER NOT NULL,
  id_grado INTEGER NOT NULL,
  FOREIGN KEY (id_colegio) REFERENCES colegios(id),
  FOREIGN KEY (id_grado) REFERENCES grados(id)
);
""")

# Crear la tabla "parciales"
cursor.execute("""
CREATE TABLE parciales (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tema VARCHAR(255) NOT NULL,
  id_materia INTEGER NOT NULL,
  id_colegio INTEGER NOT NULL,
  FOREIGN KEY (id_materia) REFERENCES materias(id),
  FOREIGN KEY (id_colegio) REFERENCES colegios(id)
);
""")

# Crear la tabla "notas"
cursor.execute("""
CREATE TABLE notas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fecha DATE NOT NULL,
  nota FLOAT NOT NULL,
  id_alumno INTEGER NOT NULL,
  id_parcial INTEGER NOT NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id),
  FOREIGN KEY (id_parcial) REFERENCES parciales(id)
);
""")

conexion.commit()
conexion.close()
