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
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()  

    cursor.execute("SELECT * FROM ingresos")
    tasks = cursor.fetchall()

    conn.close()

    return render_template('main.html', tasks=tasks)

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

@app.route('/buscar-id', methods=['GET', 'POST'])
def buscarId():
    if request.method == 'POST':
        id = request.form['id']
        if id:
            conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ingresos WHERE id = ?", (id,))
            registros = cursor.fetchall()
            if registros:
                return redirect(url_for('editar-ingreso', id=registros[0][0]))
                # Aquí asumo que el ID está en la primera posición de la tupla. Ajusta según tu esquema de base de datos.
            else:
                return 'No se encontró el registro'
        else:
            return 'El campo "id" es obligatorio'
    else:
        return 'El método de solicitud debe ser POST'

@app.route('/editar-ingreso/<int:id>', methods=['GET'])
def editarIngreso(id):
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingresos WHERE id = {}".format(id))
    registro = cursor.fetchone()
    return render_template('editaringresos2.html', registro=registro)




@app.route('/nuevo-ingreso', methods=['POST'])
def nuevoIngreso():
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    proveedor = request.form['proveedor']
    oc = request.form['oc']
    lote = request.form['lote']
    vto = request.form['vto']
    d = datetime.now()
    dateIngreso=d.strftime("%Y-%m-%d %H:%M:%S")

    if codigo and descripcion and cantidad and proveedor and oc and lote and vto:
        conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
        cursor = conn.cursor()
        # Insertar datos en la tabla 'ingresos'
        cursor.execute("INSERT INTO ingresos (fecha, codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, eliminado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (dateIngreso, codigo, descripcion, cantidad, proveedor, oc, lote, vto, 'En Revision', False))
        # Commit para aplicar cambios
        conn.commit()
        # Cerrar la conexión
        conn.close()
        return redirect(url_for('main'))
    else:
        return render_template('nuevoIngresos.html', errorIngresoInsumo="Las credenciales no son correctas o existen campos vacios")
    
        
if __name__ == '__main__':
    app.run(debug=True)