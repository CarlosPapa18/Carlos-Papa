# producto.py
# Clase que representa un producto en el inventario

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        # Código del producto (ID único)
        self.codigo = codigo
        # Nombre del producto
        self.nombre = nombre
        # Cantidad disponible en inventario
        self.cantidad = cantidad
        # Precio unitario del producto
        self.precio = precio

    def __str__(self):
        # Retorna una representación en texto del producto
        return f"{self.codigo} - {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"
