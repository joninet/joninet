from flask import Flask, render_template, request, session, redirect, url_for, jsonify 
import sqlite3 as sql
from datetime import datetime
from config import dbconn
from models.login import login, impLogout
from models.ingresos import borrarIngresos, editarIngreso, editarDb, nuevoIngreso, mostrarIngreso
from models.insumos import nuevoInsumoDB, borrarInsumos, borrarFila, editarInsumo, editarDbInsumo
from helpers.funcionesDb import mostrarUltimasFilas
from models.stock import nuevoDescuento


app = Flask(__name__)

app.secret_key = 'd5fb8c4fa8bd46638dadc4e751e0d68d'

@app.route("/mostrarIng/<id_fila>")
def impMostrarIngreso(id_fila):
    return mostrarIngreso(id_fila)


@app.route("/editarIng/<id_fila>", methods=['POST'])
def impEditarIng(id_fila):
    return editarDb(id_fila)

@app.route("/editarIns/<id_fila>", methods=['POST'])
def impEditarIns(id_fila):
    return editarDbInsumo(id_fila)

@app.route('/main', methods=['GET'])
def main():
    ultmiosIngresos = mostrarUltimasFilas(dbconn, "ingresos", 5)
    ultimosInsumos = mostrarUltimasFilas(dbconn, "insumos", 5)
    return render_template('main.html', ingreso=ultmiosIngresos, insumos=ultimosInsumos)

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

@app.route('/generarDesc', methods=['GET'])
def generarDesc():
    return render_template('descuentos.html')

@app.route('/verStock')
def verStock():
    stockInsumo = mostrarUltimasFilas(dbconn, "insumos", 99995)
    return render_template('verStock.html', insumo=stockInsumo)

@app.route('/nuevoInsumo', methods=['GET'])
def nuevoInsumo():
    return render_template('nuevoInsumo.html')

@app.route('/borrarIngresos', methods=['POST'])
def impBorrarIngresos():
    return borrarIngresos()

@app.route('/borrarInsumos/<id_fila>')
def impBorrarInsumos(id_fila):
    borrarFila(dbconn, 'insumos', id_fila)
    return render_template('datosActualizados.html')

@app.route('/nuevoUsuario', methods=['GET'])
def nuevoUsuario():
    return render_template('nuevoUsuario.html')

@app.route('/borrarUsuario', methods=['GET'])
def borrarUsuario():
    return render_template('borrarUsuario.html')

@app.route('/editar-ingreso', methods=['POST'])
def impEditarIngresos():
    return editarIngreso()

@app.route('/editar-insumo', methods=['POST'])
def impEditarInsumo():
    return editarInsumo()

@app.route('/nuevo-ingreso', methods=['POST'])
def impNuevoIngreso():
    return nuevoIngreso()

@app.route('/nuevo-insumo', methods=['POST'])
def impNuevoInsumo():
    return nuevoInsumoDB()

@app.route('/nuevo-descuento', methods=['GET', 'POST'])
def impNuevoDescuento():
    return nuevoDescuento()

@app.route('/buscar-codigo/<int:codigo>', methods=['GET'])
def buscarCodigo(codigo):
    try:
        conn = sql.connect(dbconn)
        cursor = conn.cursor()

        cursor.execute("SELECT nombre, um FROM insumos WHERE codigo = ?", (codigo,))
        resultado = cursor.fetchone()

        conn.close()

        if resultado:
            return jsonify({'nombre': resultado[0], 'um': resultado[1]})
        else:
            return jsonify({'error': 'Código incorrecto'})

    except Exception as e:
        return jsonify({'error': str(e)})

  
if __name__ == '__main__':
    app.run(debug=True)