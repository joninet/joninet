from models.producto import Producto
class Ingreso(Producto):
    def __init__(self, codigo: str, nombre: str, cantidad: int):
        super().__init__(codigo, nombre)
        self.cantidad = cantidad

    def __repr__(self):
        return f"Ingreso(codigo={self.codigo}, nombre={self.nombre}, cantidad={self.cantidad})"
