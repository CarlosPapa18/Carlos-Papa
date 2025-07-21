# ------------------------------
# Ejemplo de POO en Python
# Sistema simple de Vehículos
# ------------------------------

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.__velocidad_maxima = velocidad_maxima  # Encapsulación

    # Getter para velocidad máxima
    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

    # Método genérico que será sobrescrito (polimorfismo)
    def describir(self):
        print(f"Vehículo {self.marca} {self.modelo} con velocidad máxima de {self.__velocidad_maxima} km/h")

# Clase derivada: Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, num_puertas):
        super().__init__(marca, modelo, velocidad_maxima)
        self.num_puertas = num_puertas

    def describir(self):
        print(f"Auto {self.marca} {self.modelo}, {self.num_puertas} puertas, velocidad máx: {self.get_velocidad_maxima()} km/h")

# Clase derivada: Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, tipo):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo = tipo  # ej: deportiva, scooter

    def describir(self):
        print(f"Motocicleta {self.marca} {self.modelo} ({self.tipo}), velocidad máx: {self.get_velocidad_maxima()} km/h")

# Programa principal
if __name__ == "__main__":
    # Crear instancias
    auto1 = Auto("Toyota", "Corolla", 180, 4)
    moto1 = Motocicleta("Yamaha", "YZF-R3", 190, "deportiva")

    # Encapsulación: acceder a velocidad máxima con getter
    print(f"La velocidad máxima del auto es: {auto1.get_velocidad_maxima()} km/h")

    # Demostración de polimorfismo
    vehiculos = [auto1, moto1]
    for vehiculo in vehiculos:
        vehiculo.describir()
