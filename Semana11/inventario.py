# inventario.py
# Clase que maneja el inventario completo utilizando un diccionario para optimización de búsquedas

import csv
from producto import Producto

class Inventario:
    def __init__(self):
        # Diccionario con código del producto como clave y objeto Producto como valor
        # Permite búsquedas rápidas, actualizaciones y eliminaciones
        self.productos = {}

    def agregar_producto(self, producto):
        # Agrega un producto al inventario
        # Verifica si el código ya existe para evitar duplicados
        if producto.codigo in self.productos:
            print(f"El producto {producto.codigo} ya existe. Actualiza la cantidad si es necesario.")
        else:
            self.productos[producto.codigo] = producto
            print(f"Producto {producto.nombre} agregado correctamente.")

    def mostrar_inventario(self):
        # Muestra todos los productos del inventario
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("=== Inventario ===")
            for p in self.productos.values():
                print(p)

    def buscar_producto(self, criterio):
        # Busca un producto por código o nombre
        # Retorna una lista de productos encontrados
        if criterio in self.productos:  # Buscar por código
            return [self.productos[criterio]]
        # Buscar por nombre (insensible a mayúsculas)
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == criterio.lower()]
        return encontrados

    def actualizar_cantidad(self, codigo, nueva_cantidad):
        # Actualiza la cantidad de un producto específico
        producto = self.productos.get(codigo)
        if producto:
            producto.cantidad = nueva_cantidad
            print(f"Cantidad de {producto.nombre} actualizada a {nueva_cantidad}.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        # Elimina un producto del inventario por su código
        if codigo in self.productos:
            nombre = self.productos[codigo].nombre
            del self.productos[codigo]
            print(f"Producto {nombre} eliminado del inventario.")
        else:
            print("Producto no encontrado.")

    def guardar_en_archivo(self, nombre_archivo="inventario.csv"):
        # Guarda el inventario completo en un archivo CSV
        with open(nombre_archivo, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Escribir encabezados
            writer.writerow(["Codigo", "Nombre", "Cantidad", "Precio"])
            # Escribir cada producto
            for p in self.productos.values():
                writer.writerow([p.codigo, p.nombre, p.cantidad, p.precio])
        print("Inventario guardado correctamente.")

    def cargar_desde_archivo(self, nombre_archivo="inventario.csv"):
        # Carga los productos desde un archivo CSV
        try:
            with open(nombre_archivo, mode="r") as file:
                reader = csv.DictReader(file)
                self.productos = {}
                for row in reader:
                    p = Producto(row["Codigo"], row["Nombre"], int(row["Cantidad"]), float(row["Precio"]))
                    self.productos[p.codigo] = p
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se iniciará con inventario vacío.")
