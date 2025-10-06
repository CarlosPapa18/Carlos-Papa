# main.py
import os
import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
from gestion_productos_gui import abrir_ventana_gestion

# Ruta base del proyecto (donde está este archivo)
BASE_DIR = os.path.dirname(__file__)

def cargar_imagen_segura(nombre_archivo, tamaño=None):
    """
    Carga imagen con Pillow desde la carpeta del script.
    nombre_archivo: string (ej. "g.png" o "FONDO-1.jpeg")
    tamaño: (ancho, alto) opcional -> redimensiona
    Devuelve ImageTk.PhotoImage o None si falla.
    """
    ruta = os.path.join(BASE_DIR, nombre_archivo)
    try:
        img = Image.open(ruta)
        if tamaño:
            img = img.resize(tamaño, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error cargando imagen {nombre_archivo}: {e}")
        return None

def abrir_gestion():
    abrir_ventana_gestion(root)

# === Ventana principal ===
root = tk.Tk()
root.title("Sistema de Inventario - POO")
root.geometry("900x650")
root.resizable(False, False)

# === Fondo principal (usa g.png si existe) ===
bg_img = cargar_imagen_segura("FONDO-1.jpeg", tamaño=(900,650))
if bg_img:
    label_bg = tk.Label(root, image=bg_img)
    label_bg.image = bg_img
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)
else:
    # fondo plano si no carga imagen
    root.configure(bg="#e9eef6")

# === Recuadro de información del estudiante (centrado) ===
info_frame = tk.Frame(root, bg="white", bd=2, relief="solid")
# Centrar el frame
info_frame.place(relx=0.5, rely=0.4, anchor="center", width=600)

# Tipografías
titulo_font = font.Font(family="Arial", size=12, weight="bold")
texto_font = font.Font(family="Arial", size=10)

# Texto que viste en la captura (adáptalo si quieres)
texto_informacion = (
    "UNIVERSIDAD ESTATAL AMAZÓNICA\n"
    "INGENIERÍA EN TECNOLOGÍAS DE LA INFORMACIÓN\n\n"
    "ASIGNATURA:\n"
    "PROGRAMACIÓN ORIENTADA A OBJETOS (A)\n\n"
    "TEMA:\n"
    "Sistema de Gestión de Inventario\n\n"
    "INTEGRANTE:\n"
    "Carlos Jamil Papa Tanguila\n\n"
    "DOCENTE:\n"
    "Mgs. SANTIAGO ISRAEL NOGALES GUERRERO\n\n"
    "SEMESTRE:\n"
    "Segundo Nivel\n\n"
    "FECHA:\n"
    "domingo, 5 de octubre de 2025\n\n"
    "#UEAEsExcelencia    #UEAEenLinea"
)

lbl_info = tk.Label(info_frame, text=texto_informacion, justify="left",
                    font=texto_font, bg="white")
lbl_info.pack(padx=15, pady=15)

# === Botones debajo del recuadro ===
btn_abrir = tk.Button(root, text="Gestión de Productos", font=("Arial", 12, "bold"),
                      bg="#1f6feb", fg="white", command=abrir_gestion)
btn_abrir.place(relx=0.5, rely=0.72, anchor="center", width=280, height=45)

btn_salir = tk.Button(root, text="Salir (Esc)", font=("Arial", 10),
                      bg="#c94c4c", fg="white", command=root.quit)
btn_salir.place(relx=0.5, rely=0.82, anchor="center", width=140, height=36)

# Atajo de teclado Escape para salir
root.bind("<Escape>", lambda e: root.quit())

# Mensaje instructivo (arriba o debajo)
lbl_instr = tk.Label(root, text="Presiona Escape para salir de la aplicación", bg=root.cget("bg"))
lbl_instr.place(relx=0.5, rely=0.88, anchor="center")

# Ejecutar
root.mainloop()








