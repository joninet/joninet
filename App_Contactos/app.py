from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/addContact', methods=['POST'])
def addContact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        
        return 'Enviado correctamente'

@app.route('/edit')
def editContact():
    return 'Edit Contact'

@app.route('/delete')
def deleteContact():
    return 'Delete Contact'


if __name__ == '__main__':
    app.run(port=3000, debug=True)
