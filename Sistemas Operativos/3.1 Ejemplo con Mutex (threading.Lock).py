import threading

# Variable global compartida
contador_global = 0

# Creamos un mutex
mutex = threading.Lock()

# Función que incrementa el contador de manera segura
def incrementar():
    global contador_global
    mutex.acquire()  # Adquirimos el mutex
    try:
        contador_global += 1  # Sección crítica
    finally:
        mutex.release()  # Liberamos el mutex

# Función que ejecuta la tarea varias veces
def tarea():
    for _ in range(100000):
        incrementar()

# Creamos dos hilos
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperamos que los hilos terminen
hilo1.join()
hilo2.join()

print("El valor final del contador global es:", contador_global)
