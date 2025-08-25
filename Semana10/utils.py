# utils.py
# Funciones auxiliares para manejo de archivos y validaciones

def leer_archivo(ruta):
    """Lee todas las líneas de un archivo con UTF-8.
    Si no existe, lo crea vacío."""
    try:
        with open(ruta, "r", encoding="utf-8-sig") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"[WARN] Archivo {ruta} no encontrado. Se creará uno nuevo.")
        return []
    except PermissionError:
        print(f"[ERROR] No tienes permisos para leer el archivo {ruta}.")
        return []
    except Exception as e:
        print(f"[ERROR] Error inesperado al leer el archivo: {e}")
        return []


def escribir_archivo(ruta, lineas):
    """Escribe todas las líneas en un archivo con UTF-8."""
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            f.writelines(lineas)
        print("[INFO] Archivo guardado correctamente.")
    except PermissionError:
        print(f"[ERROR] No tienes permisos para escribir en {ruta}.")
    except Exception as e:
        print(f"[ERROR] Error inesperado al escribir el archivo: {e}")


def validar_entero(valor, nombre_campo="valor"):
    """Valida si el valor es un número entero."""
    try:
        return int(valor)
    except ValueError:
        print(f"[WARN] {nombre_campo} inválido, debe ser un número entero.")
        return None


def validar_float(valor, nombre_campo="valor"):
    """Valida si el valor es un número decimal."""
    try:
        return float(valor)
    except ValueError:
        print(f"[WARN] {nombre_campo} inválido, debe ser un número decimal.")
        return None
