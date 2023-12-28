#minuto 19:35
from flask import Flask, render_template, request
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


if __name__ == '__main__':# Comprobar si el script está siendo ejecutado directamente (no importado como módulo)
    app.run(debug=True)#Esto facilita la detección y depuración de errores durante el desarrollo.