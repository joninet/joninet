import sqlite3 as sql

def insertData(dbconn, table, column, values):
    conn = None
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        query = f"INSERT INTO {table} ({', '.join(column)}) VALUES ({', '.join(['?' for _ in values])})"
        cursor.execute(query, values)
        conn.commit()
        
    except sql.Error as e:
        print(f"Failed to insert data: {e}")
        
    finally:
        if conn:
            conn.close()

import json

def viewRow(dbconn, id, table):
    db = sql.connect(dbconn)
    cursor = db.cursor()
    view = cursor.execute(f"SELECT * FROM {table} WHERE id = ?", (id,)).fetchone()
    db.close()

    if view:
        view_dict = dict(zip([desc[0] for desc in cursor.description], view))
        return json.dumps(view_dict)
    else:
        return None 
