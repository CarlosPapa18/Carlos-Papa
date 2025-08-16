from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("El ID ya existe.")
                return
        self.productos.append(producto)
        print("Producto añadido.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos.")

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        print("Listado de productos:")
        for p in self.productos:
            print(p)
