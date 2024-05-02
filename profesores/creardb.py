import sqlite3

def conectar_db(nombre_db):
  """Crea una conexión a la base de datos SQLite con el nombre especificado."""
  conexion = sqlite3.connect(nombre_db)
  return conexion

conexion = conectar_db("profesordb.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE notas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fecha DATE NOT NULL,
  nota FLOAT NOT NULL,
  rec1 FLOAT,
  rec2 FLOAT,
  rec3 FLOAT,
  id_alumno INTEGER NOT NULL,
  id_parcial INTEGER NOT NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id),
  FOREIGN KEY (id_parcial) REFERENCES parciales(id)
);
""")

conexion.commit()
conexion.close()
