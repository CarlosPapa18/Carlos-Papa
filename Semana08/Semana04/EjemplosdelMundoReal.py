from abc import ABC, abstractmethod
from datetime import date

# Clase base abstracta que representa un producto genérico
class Producto(ABC):
    def __init__(self, nombre, precio_base):
        self._nombre = nombre              # Nombre del producto
        self._precio_base = precio_base    # Precio sin impuestos ni descuentos

    @abstractmethod
    def calcular_precio_final(self):
        # Método abstracto que será implementado por las clases hijas
        pass

    def __str__(self):
        # Representación del producto en texto
        return f"{self.__class__.__name__}: {self._nombre}"

# Clase que representa un producto electrónico
class Electronico(Producto):
    def calcular_precio_final(self):
        impuesto = self._precio_base * 0.12  # Aplica 12% de IVA
        return self._precio_base + impuesto  # Precio final con impuesto

# Clase que representa ropa, que puede tener descuento
class Ropa(Producto):
    def __init__(self, nombre, precio_base, descuento):
        super().__init__(nombre, precio_base)
        self._descuento = descuento  # Descuento en porcentaje

    def calcular_precio_final(self):
        # Calcula el precio con descuento
        return self._precio_base - (self._precio_base * self._descuento / 100)

# Clase que representa alimentos, con posible descuento por cercanía a la fecha de caducidad
class Alimento(Producto):
    def __init__(self, nombre, precio_base, fecha_caducidad):
        super().__init__(nombre, precio_base)
        self._fecha_caducidad = fecha_caducidad  # Fecha de caducidad del producto

    def calcular_precio_final(self):
        # Calcula los días restantes hasta la fecha de caducidad
        dias_restantes = (self._fecha_caducidad - date.today()).days
        if dias_restantes <= 3:
            return self._precio_base * 0.5  # Aplica 50% de descuento si está próximo a vencerse
        return self._precio_base  # Si no, retorna el precio completo

# Bloque principal de ejecución
if __name__ == "__main__":
    # Lista de productos de diferentes tipos (demostración de polimorfismo)
    productos = [
        Electronico("Laptop Lenovo", 800),
        Ropa("Camisa deportiva", 35, 20),  # 20% de descuento
        Alimento("Yogur natural", 1.50, date(2025, 6, 24))  # Producto próximo a caducar
    ]

    print("Resumen de precios en tienda virtual:\n")
    for producto in productos:
        # Se llama al mismo método, pero cada clase aplica su propia lógica (polimorfismo)
        print(f"{producto} - Precio final: ${producto.calcular_precio_final():.2f}")