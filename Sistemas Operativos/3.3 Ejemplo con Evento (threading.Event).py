import threading
import time

# Creamos un evento
evento = threading.Event()

# Hilo que espera al evento
def esperar_evento():
    print("Esperando al evento...")
    evento.wait()  # Bloquea hasta que se active el evento
    print("El evento ha sido activado!")

# Hilo que activa el evento
def activar_evento():
    print("Esperando 5 segundos antes de activar el evento...")
    time.sleep(5)
    evento.set()  # Activa el evento
    print("El evento ha sido activado después de 5 segundos")

# Creamos los hilos
hilo1 = threading.Thread(target=esperar_evento)
hilo2 = threading.Thread(target=activar_evento)

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperamos que terminen
hilo1.join()
hilo2.join()

print("Programa terminado")
