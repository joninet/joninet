from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
import random
def codAleatorio():
    paso=False

    while not paso:
        codigo = random.randint(11111, 99999)
        conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM insumos WHERE codigo =? ", (codigo,))
        count = cursor.fetchone()[0]

        if count == 0:
            conn.commit()
            conn.close()
            paso=True
            return codigo

        
