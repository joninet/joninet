from flask import request, session, redirect, url_for, render_template
import sqlite3 as sql

def impLogout():
    session.clear()
    return redirect(url_for('home'))

def login():
    email = request.form['email']
    password = request.form['password']

    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuario WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()

    conn.close()

    if user is not None:
        session['nombreUsuario'] = user[5]
        session['email'] = email
        session['name'] = user[1]
        session['surnames'] = user[2]

        return redirect(url_for('main'))
    else:
        return render_template('index.html', message="Las credenciales no son correctas")