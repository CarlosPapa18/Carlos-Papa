import threading

# Creamos una barrera para 2 hilos
barrera = threading.Barrier(2)

# Función que imprime un mensaje y espera en la barrera
def tarea():
    print("Hilo iniciado")
    barrera.wait()  # Espera que ambos hilos lleguen
    print("Hilo continuando")

# Creamos dos hilos
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperamos que terminen
hilo1.join()
hilo2.join()

print("Programa terminado")
