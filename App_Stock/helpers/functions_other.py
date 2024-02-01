import sqlite3 as sql
from config import dbconn
import random

def randomCode():
    validate=False

    while not validate:
        code = random.randint(11111, 99999)
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM products WHERE code =? ", (code,))
        count = cursor.fetchone()[0]

        if count == 0:
            conn.commit()
            conn.close()
            validate=True
            return code