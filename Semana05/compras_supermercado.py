# Programa: Calculadora de Compras de Supermercado
# Este programa solicita el nombre, precio unitario y cantidad de un producto,
# calcula el precio total de la compra y verifica si supera un límite de gasto.

# Solicita al usuario el nombre del producto (tipo string)
nombre_producto = input("Ingresa el nombre del producto: ")

# Solicita el precio unitario del producto (tipo float)
precio_unitario = float(input("Ingresa el precio unitario del producto ($): "))

# Solicita la cantidad que se va a comprar (tipo entero)
cantidad_comprada = int(input("Ingresa la cantidad comprada: "))

# Calcula el precio total multiplicando el precio por la cantidad
precio_total = precio_unitario * cantidad_comprada  # tipo float

# Define una constante que representa el límite de gasto permitido (tipo float)
LIMITE_GASTO = 100.00

# Verifica si el precio total supera el límite (tipo booleano)
supera_limite = precio_total > LIMITE_GASTO  # Devuelve True o False

# Muestra un resumen con todos los datos
print("\n--- RESUMEN DE COMPRA ---")  # Línea en blanco + título
print(f"Producto: {nombre_producto}")  # Muestra el nombre del producto
print(f"Cantidad: {cantidad_comprada}")  # Muestra cuántas unidades se compraron
print(f"Precio unitario: ${precio_unitario}")  # Muestra el precio por unidad
print(f"Precio total: ${precio_total:.2f}")  # Muestra el precio total con 2 decimales
print(f"¿Supera el límite de gasto ($100)? {supera_limite}")  # True o False
