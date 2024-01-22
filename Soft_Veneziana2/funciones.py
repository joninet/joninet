from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql
from config import dbconn
import random
def codAleatorio():
    paso=False

    while not paso:
        codigo = random.randint(11111, 99999)
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM insumos WHERE codigo =? ", (codigo,))
        count = cursor.fetchone()[0]

        if count == 0:
            conn.commit()
            conn.close()
            paso=True
            return codigo

        
