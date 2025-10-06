# inventario.py
# Clase que maneja el inventario completo utilizando un diccionario para optimización de búsquedas

from producto import Producto

class Inventario:
    def __init__(self):
        # Diccionario con código del producto como clave y objeto Producto como valor
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print(f"El producto {producto.codigo} ya existe. Actualiza la cantidad si es necesario.")
        else:
            self.productos[producto.codigo] = producto
            print(f"Producto {producto.nombre} agregado correctamente.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("=== Inventario ===")
            for p in self.productos.values():
                print(p)

    def buscar_producto(self, criterio):
        if criterio in self.productos:
            return [self.productos[criterio]]
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == criterio.lower()]
        return encontrados

    def actualizar_cantidad(self, codigo, nueva_cantidad):
        producto = self.productos.get(codigo)
        if producto:
            producto.cantidad = nueva_cantidad
            print(f"Cantidad de {producto.nombre} actualizada a {nueva_cantidad}.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            nombre = self.productos[codigo].nombre
            del self.productos[codigo]
            print(f"Producto {nombre} eliminado del inventario.")
        else:
            print("Producto no encontrado.")

    def guardar_en_archivo(self, nombre_archivo="inventario.txt"):
        with open(nombre_archivo, "w") as f:
            # Escribimos encabezado
            f.write("Codigo,Nombre,Cantidad,Precio\n")
            for p in self.productos.values():
                f.write(f"{p.codigo},{p.nombre},{p.cantidad},{p.precio}\n")
        print("Inventario guardado correctamente.")

    def cargar_desde_archivo(self, nombre_archivo="inventario.txt"):
        try:
            with open(nombre_archivo, "r") as f:
                self.productos = {}
                lineas = f.readlines()
                for linea in lineas:
                    # Ignorar encabezado
                    if "Codigo" in linea or "Nombre" in linea:
                        continue
                    codigo, nombre, cantidad, precio = linea.strip().split(",")
                    self.productos[codigo] = Producto(codigo, nombre, int(cantidad), float(precio))
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            self.productos = {}
            print("Archivo no encontrado. Inventario vacío.")
        except ValueError as e:
            print(f"Error al cargar archivo: {e}")






