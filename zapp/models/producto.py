class Producto:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre

    def __repr__(self):
        return f"Producto(codigo={self.codigo}, nombre={self.nombre})"
