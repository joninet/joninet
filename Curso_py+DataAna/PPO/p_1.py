productos = [
    {'cod':'10001', 'Nombre':'Jabón Harmony', 'Categoría':'Higiene personal', 'pvp':0.9},
    {'cod':'10002', 'Nombre':'Cereal Nestlé', 'Categoría':'Cereal', 'pvp':1.5},
    {'cod':'10003', 'Nombre':'Limones', 'Categoría':'Fruta', 'pvp':.7}
]

def mostrarProducto(productos, cod):
    for p in productos:
        if (cod == p['cod']):
                    return print('{} {}'.format(p['Nombre'],p['pvp']))
    print('Producto no encontrado')

mostrarProducto(productos,"10002")

def eliminarProducto(productos,cod):
    for i,p in enumerate(productos):
        if (cod == p['cod']):
            del (productos[i])
            print(str(p)"eliminado")
    print(productos)
eliminarProducto(productos,"10003")
