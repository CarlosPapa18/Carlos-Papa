import os
import subprocess

#  Muestra el contenido del script seleccionado
def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(" El archivo no se encontró.")
        return None
    except Exception as e:
        print(f" Ocurrió un error al leer el archivo: {e}")
        return None

#  Ejecuta el script seleccionado en una terminal nueva
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux/Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f" Error al ejecutar el código: {e}")

#  Menú principal - Muestra las semanas disponibles (02 a 07)
def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    semanas = {
        '2': 'semana02',
        '3': 'semana03',
        '4': 'semana04',
        '5': 'semana05',
        '6': 'semana06',
        '7': 'semana07'
    }

    while True:
        print("\n===== DASHBOARD DE CARLOS PAPA - PROGRAMACIÓN ORIENTADA A OBJETOS =====")
        for key in semanas:
            print(f"{key} - {semanas[key]}")
        print("0 - Salir")

        eleccion = input("Selecciona una semana o '0' para salir: ")
        if eleccion == '0':
            print(" Gracias por usar el dashboard.")
            break
        elif eleccion in semanas:
            ruta_semana = os.path.join(ruta_base, semanas[eleccion])
            if os.path.isdir(ruta_semana):
                mostrar_scripts(ruta_semana)
            else:
                print(" La carpeta de esa semana no existe aún.")
        else:
            print(" Opción no válida. Intenta nuevamente.")

#  Muestra scripts disponibles dentro de una semana específica
def mostrar_scripts(ruta_carpeta):
    scripts = [f.name for f in os.scandir(ruta_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\n Contenido de: {os.path.basename(ruta_carpeta)}")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Volver al menú principal")

        eleccion = input("Selecciona un script o '0' para volver: ")
        if eleccion == '0':
            break
        else:
            try:
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(scripts):
                    ruta_script = os.path.join(ruta_carpeta, scripts[eleccion])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Deseas ejecutarlo? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        else:
                            print(" No se ejecutó el script.")
                        input("Presiona Enter para continuar...")
                else:
                    print(" Opción fuera de rango.")
            except ValueError:
                print(" Entrada no válida. Usa solo números.")

#  Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
