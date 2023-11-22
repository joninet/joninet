import sqlite3 as sql

def nuevaTabla():
    conn = sql.connect("Soft_Veneziana/ingresos_db.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE ingresos_db (
            id INTEGER PRIMARY KEY,
            codigo INTEGER,
            descripcion TEXT,
            cantidad REAL,
            proveedor TEXT,
            oc INTEGER,
            lote TEXT,
            vto DATE,
            estado TEXT,
            eliminado BOOLEAN
        )"""
    )
    conn.commit()
    conn.close()

def agregoIngreso(codigo,descripcion,cantidad,proveedor,oc,lote,vto,estado,eliminado):
    #agregoIngreso(3900001,"Harina 000",28800,"Molino chabas",61950,"1305","2023-11-18","En Revision",FALSE)
    estado="En Revisión"
    eliminado=False
    conn = sql.connect("Soft_Veneziana/ingresos_db.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO ingresos_db VALUES ('{codigo}',{descripcion},{cantidad},{proveedor},{oc},{lote},{vto},{estado},{eliminado})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def eliminarIngreso(id):
    conn = sql.connect("Soft_Veneziana/ingresos_db.db")
    cursor = conn.cursor()
    instruccion = "UPDATE ingresos_db SET eliminado=True WHERE id = ?"
    cursor.execute(instruccion, (id,))
    conn.commit()
    conn.close()

agregoIngreso(3900001,"Harina 000",28800,"Molino chabas",61950,"1305","2023-11-18","En Revision","False")