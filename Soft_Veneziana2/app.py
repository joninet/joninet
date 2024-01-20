from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3 as sql
from datetime import datetime
from login import login, impLogout
from ingresos import borrarIngresos, editarIngreso, editarDb, nuevoIngreso
from insumos import nuevoInsumoDB

app = Flask(__name__)

app.secret_key = 'd5fb8c4fa8bd46638dadc4e751e0d68d'

@app.route('/main', methods=['GET'])
def main():
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
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
  
if __name__ == '__main__':
    app.run(debug=True)