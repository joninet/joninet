from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3 as sql
from datetime import datetime
from config import dbconn
from login import login, impLogout
from ingresos import borrarIngresos, editarIngreso, editarDb, nuevoIngreso
from insumos import nuevoInsumoDB

app = Flask(__name__)

app.secret_key = 'd5fb8c4fa8bd46638dadc4e751e0d68d'

@app.route('/main', methods=['GET'])
def main():
    conn = sql.connect(dbconn)
    cursor = conn.cursor()  

    cursor.execute("SELECT * FROM ingresos WHERE eliminado = False")
    ingreso = cursor.fetchall()

    conn.close()

    return render_template('main.html', ingreso=ingreso)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/logout')
def logout():
    return impLogout()

@app.route('/login', methods=['POST'])
def impLogin():
    return login()

@app.route('/nuevoIngresos', methods=['GET'])
def nuevoIngresos():
    return render_template('nuevoIngresos.html')

@app.route('/verStock', methods=['GET'])
def verStock():
    return render_template('verStock.html')

@app.route('/nuevoInsumo', methods=['GET'])
def nuevoInsumo():
    return render_template('nuevoInsumo.html')

@app.route('/editarIngresos', methods=['GET'])
def editarIngresos():
    return render_template('editarIngresos.html')

@app.route('/borrarIngresos', methods=['POST'])
def impBorrarIngresos():
    return borrarIngresos()

@app.route('/nuevoUsuario', methods=['GET'])
def nuevoUsuario():
    return render_template('nuevoUsuario.html')

@app.route('/borrarUsuario', methods=['GET'])
def borrarUsuario():
    return render_template('borrarUsuario.html')

@app.route('/editar-ingreso', methods=['POST'])
def impEditarIngresos():
    return editarIngreso()

@app.route('/editar-db', methods=['POST'])
def impEditarDB():
    return editarDb()

@app.route('/nuevo-ingreso', methods=['POST'])
def impNuevoIngreso():
    return nuevoIngreso()

@app.route('/nuevo-insumo', methods=['POST'])
def impNuevoInsumo():
    return nuevoInsumoDB()

@app.route('/buscar-codigo/<int:codigo>', methods=['GET'])
def buscarCodigo(codigo):
    try:
        # Conéctate a la base de datos
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        # Realiza la consulta para obtener el nombre asociado al código
        cursor.execute("SELECT nombre FROM insumos WHERE codigo = ?", (codigo,))
        nombre = cursor.fetchone()

        # Cierra la conexión a la base de datos
        conn.close()

        if nombre:
            return nombre[0]  # Devuelve el nombre como respuesta
        else:
            return 'Codigo Incorrecto'  # Devuelve una cadena vacía si no se encuentra el código

    except Exception as e:
        return str("Descripcion")

  
if __name__ == '__main__':
    app.run(debug=True)