"""
Aplicación GUI Básica
Autor: [Tu Nombre]
Curso: Programación Orientada a Objetos
Semana 13

Descripción:
Esta aplicación permite al usuario ingresar información
en un campo de texto y agregarla a una lista.
También incluye un botón para limpiar el texto ingresado
o eliminar un elemento seleccionado de la lista.
"""

# Importamos la biblioteca tkinter para crear la GUI
import tkinter as tk
# Importamos messagebox para mostrar mensajes de alerta o información
from tkinter import messagebox

# Función para agregar texto a la lista
def agregar():
    """Agrega el texto del campo de entrada a la lista."""
    texto = entrada.get()  # Obtiene el texto que escribió el usuario
    if texto.strip():  # Verifica que no esté vacío
        lista.insert(tk.END, texto)  # Inserta el texto al final de la lista
        entrada.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        # Muestra un mensaje de advertencia si el campo está vacío
        messagebox.showwarning("Entrada vacía", "Debe escribir algo antes de agregar.")

# Función para limpiar la entrada o eliminar un elemento seleccionado
def limpiar():
    """Elimina el elemento seleccionado o limpia la entrada."""
    seleccion = lista.curselection()  # Obtiene la posición del elemento seleccionado
    if seleccion:
        lista.delete(seleccion)  # Elimina el elemento seleccionado de la lista
    elif entrada.get():  # Si no hay selección pero hay texto en la entrada
        entrada.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        # Muestra un mensaje si no hay nada que limpiar
        messagebox.showinfo("Nada que limpiar", "No hay texto ni selección para limpiar.")

# Creamos la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica - Deber")  # Título de la ventana
ventana.geometry("400x300")  # Tamaño inicial de la ventana (ancho x alto)

# Etiqueta para indicar al usuario dónde escribir
tk.Label(ventana, text="Ingrese información:").pack(pady=5)

# Campo de entrada de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón para agregar el texto ingresado a la lista
tk.Button(ventana, text="Agregar", command=agregar).pack(pady=5)
# Botón para limpiar el texto o eliminar selección
tk.Button(ventana, text="Limpiar", command=limpiar).pack(pady=5)

# Lista donde se mostrarán los elementos agregados
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Mantiene la ventana abierta y a la espera de acciones del usuario
ventana.mainloop()
