from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3 as sql
from datetime import datetime

app = Flask(__name__)

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
        session['id'] = user[0]
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

    cursor.execute("SELECT * FROM ingresos WHERE eliminado = False")
    ingreso = cursor.fetchall()

    conn.close()

    return render_template('main.html', ingreso=ingreso)

@app.route('/nuevoIngresos', methods=['GET'])
def nuevoIngresos():
    return render_template('nuevoIngresos.html')

@app.route('/editarIngresos', methods=['GET'])
def editarIngresos():
    return render_template('editarIngresos.html')

@app.route('/borrarIngresos', methods=['POST'])
def borrarIngresos():
    try:
        conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
        id = request.form['id']
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM ingresos WHERE id = ?", (id,))

        conn.commit()
        conn.close()

        return redirect(url_for('main'))

    except Exception as e:
        return f"Error al borrar el ingreso: {str(e)}"


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

@app.route('/editar-ingreso', methods=['POST'])
def editarIngreso():
    id = request.form.get('id')  # Obtén el valor de 'id' del formulario
    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingresos WHERE id = ?", (id,))
    editar = cursor.fetchall()

    conn.close()
    return render_template('editarIngresos2.html', registro=editar)

@app.route('/editar-db', methods=['POST'])
def editarDb():
    id = request.form.get('id')
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    proveedor = request.form['proveedor']
    oc = request.form['oc']
    lote = request.form['lote']
    vto = request.form['vto']
    estado = request.form['estado']

    conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
    cursor = conn.cursor()

    query = """UPDATE ingresos
                SET codigo = ?, descripcion = ?, cantidad = ?, 
                    proveedor = ?, oc = ?, lote = ?, vto = ?, estado = ?
                WHERE id = ?"""
    params = (codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, id)
            # Ejecutar la consulta de actualización
    cursor.execute(query, params)
            # Commit para aplicar los cambios
    conn.commit()
            # Cerrar la conexión
    conn.close()

    return redirect(url_for('main'))



@app.route('/nuevo-ingreso', methods=['POST'])
def nuevoIngreso():
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    proveedor = request.form['proveedor']
    oc = request.form['oc']
    lote = request.form['lote']
    vto = request.form['vto']
    usuarioIngreso = request.form['usuarioIngreso']
    d = datetime.now()
    dateIngreso=d.strftime("%Y-%m-%d %H:%M:%S")

    if codigo and descripcion and cantidad and proveedor and oc :
        conn = sql.connect("Soft_Veneziana2/venezianaDB.db")
        cursor = conn.cursor()
        # Insertar datos en la tabla 'ingresos'
        cursor.execute("INSERT INTO ingresos (fecha, codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado, eliminado, usuarioIngreso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (dateIngreso, codigo, descripcion, cantidad, proveedor, oc, lote, vto, 'En Revision', False, usuarioIngreso))
        # Commit para aplicar cambios
        conn.commit()
        # Cerrar la conexión
        conn.close()
        return redirect(url_for('main'))
    else:
        return render_template('nuevoIngresos.html', errorIngresoInsumo="Las credenciales no son correctas o existen campos vacios")
    
        
if __name__ == '__main__':
    app.run(debug=True)