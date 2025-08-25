# app.py
# Menú principal de la aplicación

from producto import Producto
from inventario import Inventario

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Mostrar todos los productos")
    print("2. Añadir producto")
    print("3. Eliminar producto")
    print("4. Actualizar producto")
    print("5. Buscar producto")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.mostrar_todos()
        elif opcion == "2":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.añadir_producto(Producto(id_producto, nombre, cantidad, precio))
            except ValueError:
                print("Error: cantidad debe ser entero y precio decimal.")
        elif opcion == "3":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "4":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter = no cambiar): ")
            precio = input("Nuevo precio (Enter = no cambiar): ")
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )
        elif opcion == "5":
            nombre = input("nombre a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
