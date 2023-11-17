class Producto:
    def __init__(self, cod, nombre, categoria, pvp):
        self.cod=cod
        self.nombre=nombre
        self.categoria=categoria
        self.pvp=pvp
        self.productos = [{'cod':'10001', 'Nombre':'Jabón Harmony', 'Categoría':'Higiene personal', 'pvp':0.9},
                    {'cod':'10002', 'Nombre':'Cereal Nestlé', 'Categoría':'Cereal', 'pvp':1.5},
                    {'cod':'10003', 'Nombre':'Limones', 'Categoría':'Fruta', 'pvp':.7}]
    def mostarLista(self):
        return self.productos

class Negocio:
    def __init__(self):
        #self.cod=cod
        self.productos = Producto.productos
    def mostrarProductos(self):
        productoLista = self.productos
        return productoLista
mostrar=Negocio()
print(mostrar.mostrarProductos())
    

