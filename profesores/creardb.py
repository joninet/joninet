import sqlite3

def conectar_db(nombre_db):
  """Crea una conexión a la base de datos SQLite con el nombre especificado."""
  conexion = sqlite3.connect(nombre_db)
  return conexion

conexion = conectar_db("profesordb.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE parciales (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tema VARCHAR(255) NOT NULL,
  id_materias INTEGER NOT NULL,
  FOREIGN KEY (id_materias) REFERENCES materias(id)
);
""")

conexion.commit()
conexion.close()
