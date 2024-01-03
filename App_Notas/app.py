#minuto 19:35
from flask import Flask, render_template, request, session, redirect, url_for
import config 
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = config.HEX_SEC_KEY
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql=MySQL(app)

@app.route('/', methods=['GET']) # Ruta principal, se maneja con el método GET
def home():
    return render_template('index.html')# Genera y muestra 'index.html' al acceder a la ruta principal


@app.route('/login', methods=['POST']) #se relaciona típicamente con el manejo de formularios de inicio de sesión.
def login():
    email = request.form['email'] # Obtiene el valor del campo 'email' desde el formulario enviado
    password = request.form['password']# Obtiene el valor del campo 'password' desde el formulario enviado

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user=cur.fetchone()
    cur.close()

    if user is not None:
        session['email'] = email
        session['name'] = user[1]
        session['surnames'] = user[2]
        return redirect(url_for('task'))
    else:
        return render_template('index.html', message="las credenciales no son validas")
    
@app.route('/task', methods=['GET'])
def task():
    return render_template('task.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':# Comprobar si el script está siendo ejecutado directamente (no importado como módulo)
    app.run(debug=True)#Esto facilita la detección y depuración de errores durante el desarrollo.