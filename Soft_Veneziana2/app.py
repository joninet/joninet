from flask import Flask, render_template, request, session, redirect, url_for
import config
import sqlite3 as sql
from datetime import datetime
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = sql.connect("Soft_Veneziana2/usuarios.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()

    conn.close()

    if user is not None:
        session['email'] = email
        session['name'] = user[1]
        session['surnames'] = user[2]

        return redirect(url_for('tasks'))
    else:
        return render_template('index.html', message="Las credenciales no son correctas")