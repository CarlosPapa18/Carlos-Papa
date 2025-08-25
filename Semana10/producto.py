# producto.py
# Modelo de datos para un producto

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self): return self.id
    def get_nombre(self): return self.nombre
    def get_cantidad(self): return self.cantidad
    def get_precio(self): return self.precio

    # Setters
    def set_cantidad(self, cantidad): self.cantidad = cantidad
    def set_precio(self, precio): self.precio = precio

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: {self.precio:.2f}"
