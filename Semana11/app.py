# main.py
# Menú interactivo para usar el sistema de inventario

from inventario import Inventario
from producto import Producto

def menu():
    # Crear objeto Inventario y cargar datos desde archivo
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        # Mostrar menú de opciones
        print("\n=== MENÚ INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Guardar inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar un nuevo producto
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(codigo, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            # Mostrar todos los productos
            inventario.mostrar_inventario()
        elif opcion == "3":
            # Buscar producto por código o nombre
            criterio = input("Ingrese código o nombre del producto: ")
            encontrados = inventario.buscar_producto(criterio)
            if encontrados:
                for p in encontrados:
                    print(p)
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            # Actualizar cantidad de un producto
            codigo = input("Código del producto: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(codigo, nueva_cantidad)
        elif opcion == "5":
            # Eliminar un producto
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "6":
            # Guardar inventario en archivo CSV
            inventario.guardar_en_archivo()
        elif opcion == "7":
            # Guardar y salir del programa
            inventario.guardar_en_archivo()
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
