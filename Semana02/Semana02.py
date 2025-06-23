from abc import ABC, abstractmethod

# === 1. ABSTRACCIÓN ===
class Vehiculo(ABC):
    @abstractmethod
    def encender(self):
        pass

class Auto(Vehiculo):
    def encender(self):
        print("🚗 El auto ha sido encendido.")

# === 2. ENCAPSULACIÓN ===
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

# === 3. HERENCIA ===
class Animal:
    def hablar(self):
        print("🐾 El animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print(" El perro dice: Guau!")

# === 4. POLIMORFISMO ===
class Gato:
    def hablar(self):
        print(" El gato dice: Miau")

class Pato:
    def hablar(self):
        print(" El pato dice: Cuac")

def hacer_hablar(animal):
    animal.hablar()


# ==============================
#  EJECUCIÓN DE TODOS LOS EJEMPLOS
# ==============================

print("\n=== ABSTRACCIÓN ===")
auto = Auto()
auto.encender()

print("\n=== ENCAPSULACIÓN ===")
cuenta = Cuenta(100)
cuenta.depositar(50)
cuenta.mostrar_saldo()

print("\n=== HERENCIA ===")
perro = Perro()
perro.hablar()

print("\n=== POLIMORFISMO ===")
gato = Gato()
pato = Pato()
hacer_hablar(gato)
hacer_hablar(pato)
