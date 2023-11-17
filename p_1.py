import sqlite3 as sql

def createDB():
    conn=sql.connect("streamers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
            name text,
            followers integer,
            subs integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre,followers,subs):
    conn = sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO streamers VALUES ('{nombre}',{followers},{subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()  

def readRows():
    conn = sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()  
    print(datos)

def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * FROM streamers ORDER BY {field} DESC"#AL DESC SI LO SACAS TE ORDENA AL REVEZ
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()  
    print(datos)

def search():
    conn = sql.connect("streamers.db")
    cursor=conn.cursor()
    #para buscar sin importar mayusculas y minusculas poner - WHERE name like 'joni'
    instruccion=f"SELECT * FROM streamers WHERE name='joni'" 
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()  
    print(datos)

def updateFields():
    conn = sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"UPDATE streamers SET followers=15 WHERE name like 'joni'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

def delete():
    conn = sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"DELETE FROM streamers WHERE name='joni'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow("ibai", 700000, 25000)
    #insertRow("joni", 400000, 200)
    #readRows()
    #readOrdered("name")
    #search()
    #updateFields()
    delete()