import random
import time

# Simulación de memoria con bloques fijos
class Memoria:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.memoria = [None] * tamanio  # Representa los bloques de memoria

    # Método para asignar memoria
    def asignar(self, proceso, tamanio_requerido):
        for i in range(self.tamanio - tamanio_requerido + 1):
            # Buscar bloque contiguo libre
            if all(self.memoria[i + j] is None for j in range(tamanio_requerido)):
                for j in range(tamanio_requerido):
                    self.memoria[i + j] = proceso
                print(f"{proceso} asignó {tamanio_requerido} bloques.")
                return True
        print(f"{proceso} no pudo asignar memoria. No hay espacio contiguo.")
        return False

    # Método para liberar memoria
    def liberar(self, proceso):
        for i in range(self.tamanio):
            if self.memoria[i] == proceso:
                self.memoria[i] = None
        print(f"{proceso} liberó su memoria.")

    # Mostrar estado de la memoria
    def mostrar_memoria(self):
        print("Estado actual de la memoria:")
        print(self.memoria)

# Simulación de proceso
def proceso(nombre, memoria):
    tamanio_requerido = random.randint(1, 5)
    print(f"{nombre} pide {tamanio_requerido} bloques.")
    if memoria.asignar(nombre, tamanio_requerido):
        time.sleep(random.randint(1, 3))
        memoria.liberar(nombre)
    time.sleep(random.randint(1, 2))

# Función principal
def gestionar_memoria():
    memoria = Memoria(10)
    procesos = ['Proceso-A', 'Proceso-B', 'Proceso-C', 'Proceso-D', 'Proceso-E']
    for i in range(5):
        proceso_nombre = random.choice(procesos)
        proceso(proceso_nombre, memoria)
    memoria.mostrar_memoria()

if __name__ == "__main__":
    gestionar_memoria()


