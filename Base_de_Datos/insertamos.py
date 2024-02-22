import sqlite3

"""# Conectar a la base de datos (si no existe, se creará)
conexion = sqlite3.connect('Base_de_Datos/base_datos.db')

# Crear un cursor para ejecutar sentencias SQL
cursor = conexion.cursor()

# Sentencia SQL para insertar datos en la tabla Categoria
sql_insert = "INSERT INTO Categoria (nombre) VALUES (?)"

# Datos que deseas insertar
nombres_categorias = ['Electrónica', 'Ropa', 'Hogar', 'Deportes']

# Iterar sobre los nombres de las categorías y ejecutar la sentencia SQL
for nombre_categoria in nombres_categorias:
    cursor.execute(sql_insert, (nombre_categoria,))

# Confirmar la transacción
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()"""

# Conectar a la base de datos
conexion = sqlite3.connect('Base_de_Datos/base_datos.db')

# Crear un cursor para ejecutar sentencias SQL
cursor = conexion.cursor()

# Sentencia SQL para insertar datos en la tabla Producto
sql_insert_producto = "INSERT INTO Producto (nombre, um, descripcion, categoria_id) VALUES (?, ?, ?, ?)"

# Datos de ejemplo para productos (nombre, um, descripcion, categoria_id)
datos_productos = [
    ('Producto1', 'kg', 'Descripción del Producto1', 1),  # Asociado a la categoría con id 1
    ('Producto2', 'uni', 'Descripción del Producto2', 2),  # Asociado a la categoría con id 2
    ('Producto3', 'lts', 'Descripción del Producto3', 1),  # Asociado a la categoría con id 1
    # Puedes agregar más datos aquí
]

"""# Iterar sobre los datos de ejemplo y ejecutar la sentencia SQL para cada uno
for producto in datos_productos:
    cursor.execute(sql_insert_producto, producto)

# Confirmar la transacción
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()"""

import sqlite3

conexion = sqlite3.connect('Base_de_Datos/base_datos.db')
cursor = conexion.cursor()

# Consulta SQL para seleccionar todos los productos con su categoría correspondiente
sql_select = """
SELECT Producto.nombre, Producto.um, Producto.descripcion, Categoria.nombre AS categoria
FROM Producto
JOIN Categoria ON Producto.categoria_id = Categoria.id
"""

cursor.execute(sql_select)
resultados = cursor.fetchall()

for producto in resultados:
    print("Nombre:", producto[0])
    print("UM:", producto[1])
    print("Descripción:", producto[2])
    print("Categoría:", producto[3])
    print("-------------------------")

conexion.close()


