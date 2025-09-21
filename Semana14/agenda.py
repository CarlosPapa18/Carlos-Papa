# ==============================
# AGENDA PERSONAL - TAREA
# ==============================
# Esta aplicación usa Tkinter (para la interfaz gráfica) y tkcalendar (para elegir fechas).
# Funcionalidades:
# - Agregar eventos con fecha, hora y descripción.
# - Mostrar los eventos en una lista (Treeview).
# - Eliminar eventos seleccionados.
# - Botón para salir de la aplicación.
# ==============================

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry   # Widget para elegir fecha
from datetime import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal - Tkinter")  # Título de la ventana
        self.root.geometry("700x500")  # Tamaño de la ventana

        # ===== FRAME 1: Lista de eventos =====
        frame_lista = ttk.Frame(self.root)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview para mostrar los eventos (como una tabla)
        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=200)
        self.tree.pack(fill="both", expand=True)

        # ===== FRAME 2: Entrada de datos =====
        frame_form = ttk.Frame(self.root)
        frame_form.pack(fill="x", padx=10, pady=10)

        # Campo Fecha (usa DateEntry de tkcalendar)
        ttk.Label(frame_form, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = DateEntry(frame_form, date_pattern="dd/mm/yyyy")
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Campo Hora
        ttk.Label(frame_form, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_hora = ttk.Entry(frame_form)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5)

        # Campo Descripción
        ttk.Label(frame_form, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_desc = ttk.Entry(frame_form, width=50)
        self.entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # ===== FRAME 3: Botones =====
        frame_botones = ttk.Frame(self.root)
        frame_botones.pack(fill="x", padx=10, pady=10)

        ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Salir", command=self.root.quit).pack(side="right", padx=5)

    # Método para agregar un evento a la lista
    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get().strip()
        desc = self.entry_desc.get().strip()

        # Validación simple: que no esté vacío
        if not fecha or not hora or not desc:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        # Validar formato de hora (HH:MM)
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Formato inválido", "La hora debe estar en formato HH:MM (24 horas).")
            return

        # Insertar en el Treeview
        self.tree.insert("", "end", values=(fecha, hora, desc))

        # Limpiar los campos
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    # Método para eliminar un evento seleccionado
    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Sin selección", "Seleccione un evento para eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmar:
            for item in seleccionado:
                self.tree.delete(item)

# ==========================
# Ejecutar la aplicación
# ==========================
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()



