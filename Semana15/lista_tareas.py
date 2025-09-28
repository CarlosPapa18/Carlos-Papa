import tkinter as tk
from tkinter import messagebox

def añadir_tarea(event=None):
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

def completar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(indice, f"{tarea} ")
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para completar.")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)

lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.pack(pady=10)

btn_añadir = tk.Button(ventana, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Eventos extra
entrada_tarea.bind("<Return>", añadir_tarea)
lista_tareas.bind("<Double-1>", lambda e: completar_tarea())

ventana.mainloop()
