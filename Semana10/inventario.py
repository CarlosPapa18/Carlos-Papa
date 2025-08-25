# inventario.py
# Manejo del inventario y persistencia en archivo inventario.txt

from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self._cargar_desde_archivo()

    # ================== CARGAR ==================
    def _cargar_desde_archivo(self):
        """
        Lee inventario.txt (UTF-8 o UTF-8 con BOM).
        Formato esperado por línea: ID;Nombre;Cantidad;Precio
        """
        try:
            with open(self.archivo, "r", encoding="utf-8-sig") as f:
                for i, linea in enumerate(f, start=1):
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(";")
                    if len(partes) != 4:
                        print(f"[WARN] Línea {i} ignorada (formato incorrecto): {linea}")
                        continue
                    id_producto, nombre, cantidad, precio = partes
                    try:
                        cantidad = int(cantidad)
                        precio = float(precio)
                    except ValueError:
                        print(f"[WARN] Línea {i} con datos inválidos: {linea}")
                        continue
                    self.productos.append(Producto(id_producto, nombre, cantidad, precio))
        except FileNotFoundError:
            open(self.archivo, "w", encoding="utf-8").close()
        except PermissionError:
            print("[ERROR] No tienes permisos para leer el archivo de inventario.")
        except Exception as e:
            print(f"[ERROR] Error inesperado al cargar: {e}")

    # ================== GUARDAR ==================
    def _guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()};{p.get_nombre()};{p.get_cantidad()};{p.get_precio()}\n")
        except PermissionError:
            print("[ERROR] No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"[ERROR] Error inesperado al guardar: {e}")

    # ================== CRUD ==================
    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("El ID ya existe.")
            return
        self.productos.append(producto)
        self._guardar_en_archivo()
        print("Producto añadido y guardado.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self._guardar_en_archivo()
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None: p.set_cantidad(cantidad)
                if precio is not None: p.set_precio(precio)
                self._guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("Resultados:")
            for p in encontrados: print(p)
        else:
            print("No se encontraron productos.")

    def mostrar_todos(self):
        if not self.productos:
            print("[INFO] No hay productos en el inventario.")
            return
        print("Inventario actual:")
        for p in self.productos:
            print(p)
