# producto.py
class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.codigo} - {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"
