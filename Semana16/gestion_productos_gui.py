# gestion_productos_gui.py
import tkinter as tk
from interfaz_productos import InterfazProductos
from inventario import Inventario
from PIL import Image, ImageTk

def abrir_ventana_gestion(root_principal):
    ventana_gestion = tk.Toplevel(root_principal)
    ventana_gestion.title("Gestión de Productos")
    ventana_gestion.geometry("600x400")

    inventario = Inventario()
    inventario.cargar_desde_archivo()

    # Fondo
    img_fondo = Image.open("FONDO-1.jpeg")
    fondo_img = ImageTk.PhotoImage(img_fondo)
    label_fondo = tk.Label(ventana_gestion, image=fondo_img)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    # Imagen decorativa
    img_poke = Image.open("R.png")
    poke_img = ImageTk.PhotoImage(img_poke)
    label_poke = tk.Label(ventana_gestion, image=poke_img, bd=0)
    label_poke.place(x=450, y=50)

    interfaz = InterfazProductos(ventana_gestion, inventario)
    ventana_gestion.mainloop()

