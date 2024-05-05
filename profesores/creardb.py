import sqlite3

def conectar_db(nombre_db):
  """Crea una conexión a la base de datos SQLite con el nombre especificado."""
  conexion = sqlite3.connect(nombre_db)
  return conexion

conexion = conectar_db("profesordb.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE alumnos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombres VARCHAR(255) NOT NULL,
  apellidos VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  id_colegios INTEGER NOT NULL,
  id_grados INTEGER NOT NULL,
  FOREIGN KEY (id_colegios) REFERENCES colegios(id),
  FOREIGN KEY (id_grados) REFERENCES grados(id)
);
""")

conexion.commit()
conexion.close()
