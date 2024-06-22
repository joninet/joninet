import psycopg2
from psycopg2 import sql as psql
import json
import math

class FuncionesDB():
    def __init__(self):
        self._con = psycopg2.connect(
            dbname="profesor_db",
            user="profesor_db_user",
            password="koOaedgIMCvjcAxHOld1F0Jd5ytWkIeM",  # Reemplaza 'your_password' con tu contraseña real
            host="dpg-cpabeiv109ks73alrtj0-a.oregon-postgres.render.com",
            port="5432"
        )
        self._cur = self._con.cursor()

    def insertarDatos(self, tabla, column, values):
        try:
            query = psql.SQL("INSERT INTO {table} ({fields}) VALUES ({values}) RETURNING id").format(
                table=psql.Identifier(tabla),
                fields=psql.SQL(', ').join(map(psql.Identifier, column)),
                values=psql.SQL(', ').join(psql.Placeholder() * len(values))
            )
            self._cur.execute(query, values)
            self._con.commit()
            id_ = self._cur.fetchone()[0]
            return id_
        except psycopg2.Error as e:
            print(f"error: {e}")
      
    def editarRegistro(self, tabla, column, values, condition, conditionValues):
        try:
            setClause = ', '.join([f"{col} = %s" for col in column])
            query = f"UPDATE {tabla} SET {setClause} WHERE {condition}"

            values.extend(conditionValues)

            self._cur.execute(query, tuple(values))
            self._con.commit()
            return "correcto"
        except psycopg2.Error as e:
            print(f"Error al actualizar datos: {e}")

    def mostrarTabla(self, tabla):
        try:
            self._cur.execute(psql.SQL("SELECT * FROM {table}").format(table=psql.Identifier(tabla)))
            result = self._cur.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"Error al consultar datos: {e}")
            return None

    def borrarRegistro(self, tabla, id):
        try:
            self._cur.execute(psql.SQL("DELETE FROM {table} WHERE id = %s").format(table=psql.Identifier(tabla)), (id,))
            self._con.commit()
            return {"message": "Borrado correctamente"}
        except psycopg2.Error as e:
            return {"message": f"Error al borrar: {e}"}
    
    def mostrarTablaPaginada(self, tabla, pagina, por_pagina):
        try:
            offset = (pagina - 1) * por_pagina
            self._cur.execute(psql.SQL("SELECT * FROM {table} LIMIT %s OFFSET %s").format(table=psql.Identifier(tabla)), (por_pagina, offset))
            result = self._cur.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"Error al consultar datos paginados: {e}")
            return None
    
    def contarFilas(self, tabla):
        try:
            self._cur.execute(psql.SQL("SELECT COUNT(*) FROM {table}").format(table=psql.Identifier(tabla)))
            result = self._cur.fetchone()
            return result[0]
        except psycopg2.Error as e:
            print(f"Error al contar filas: {e}")
            return 0
    
    def __del__(self):
        self._con.close()
