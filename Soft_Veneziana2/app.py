from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3 as sql
from datetime import datetime

app = Flask(__name__)

# Configuración de la clave secreta
app.secret_key = 'd5fb8c4fa8bd46638dadc4e751e0d68d'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuario WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()

    conn.close()

    if user is not None:
        session['email'] = email
        session['name'] = user[1]
        session['surnames'] = user[2]

        return redirect(url_for('main'))
    else:
        return render_template('index.html', message="Las credenciales no son correctas")
    
@app.route('/main', methods=['GET'])
def main():
    """email = request.form['email']
    conn = sql.connect("Soft_Veneziana2/usuarios.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE email = ?", (email))
    tasks = cursor.fetchone()

    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in tasks:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()"""

    return render_template('main.html')#, tasks = insertObject)

@app.route('/nuevoIngresos', methods=['GET'])
def nuevoIngresos():
    return render_template('nuevoIngresos.html')

@app.route('/editarIngresos', methods=['GET'])
def editarIngresos():
    return render_template('editarIngresos.html')

@app.route('/borrarIngresos', methods=['GET'])
def borrarIngresos():
    return render_template('borrarIngresos.html')

@app.route('/nuevoUsuario', methods=['GET'])
def nuevoUsuario():
    return render_template('nuevoUsuario.html')

@app.route('/borrarUsuario', methods=['GET'])
def borrarUsuario():
    return render_template('borrarUsuario.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True)