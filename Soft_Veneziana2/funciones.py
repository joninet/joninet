import sqlite3 as sql
def getNombreUsuario(idUsuario):
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM usuario WHERE id = ?", (idUsuario,))
    result = cursor.fetchone()
    nombreUsuario = None  # Establecer valor predeterminado
    if result:  # Verificar si se encontró una fila
        nombreUsuario = result[0]
    conn.close()
    return nombreUsuario
