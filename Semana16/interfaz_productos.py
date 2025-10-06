# interfaz_productos.py
import tkinter as tk
from tkinter import messagebox, ttk
from producto import Producto

class InterfazProductos:
    def __init__(self, root, inventario):
        self.root = root
        self.inventario = inventario

        # Frame principal dentro del root (permite colocar sobre un panel blanco si tienes fondo)
        self.frame = tk.Frame(root, bg="white")
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Campos de entrada
        tk.Label(self.frame, text="Código").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Label(self.frame, text="Nombre").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Label(self.frame, text="Cantidad").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        tk.Label(self.frame, text="Precio").grid(row=3, column=0, padx=5, pady=5, sticky="e")

        self.entry_codigo = tk.Entry(self.frame)
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_cantidad = tk.Entry(self.frame)
        self.entry_precio = tk.Entry(self.frame)

        self.entry_codigo.grid(row=0, column=1, padx=5, pady=5)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)
        self.entry_cantidad.grid(row=2, column=1, padx=5, pady=5)
        self.entry_precio.grid(row=3, column=1, padx=5, pady=5)

        # Botones
        tk.Button(self.frame, text="Agregar", command=self.agregar).grid(row=4, column=0, padx=5, pady=8)
        tk.Button(self.frame, text="Eliminar", command=self.eliminar).grid(row=4, column=1, padx=5, pady=8)
        tk.Button(self.frame, text="Mostrar", command=self.mostrar).grid(row=5, column=0, columnspan=2, pady=8)

        # Treeview para mostrar productos (mejor que Text)
        self.tree = ttk.Treeview(self.frame, columns=("Codigo","Nombre","Cantidad","Precio"), show="headings", height=8)
        self.tree.heading("Codigo", text="Código")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio", text="Precio")
        self.tree.grid(row=6, column=0, columnspan=2, pady=5, sticky="nsew")

        # Permitir expandir el tree
        self.frame.grid_rowconfigure(6, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        # Bind para seleccionar fila y cargar en campos (útil para modificar/eliminar)
        self.tree.bind("<<TreeviewSelect>>", self._cargar_seleccion_en_campos)

        # Inicializar vista con los productos actuales
        self.actualizar_vista()

    def agregar(self):
        codigo = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        try:
            cantidad = int(self.entry_cantidad.get().strip())
            precio = float(self.entry_precio.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser entero y Precio debe ser numérico.")
            return

        if not codigo or not nombre:
            messagebox.showwarning("Atención", "Complete los campos Código y Nombre.")
            return

        p = Producto(codigo, nombre, cantidad, precio)
        self.inventario.agregar_producto(p)
        messagebox.showinfo("Éxito", f"Producto {nombre} agregado.")
        self.limpiar_campos()
        self.actualizar_vista()

    def eliminar(self):
        # Eliminar por selección en TreeView si existe
        sel = self.tree.selection()
        if sel:
            codigo = self.tree.item(sel[0])["values"][0]
            self.inventario.eliminar_producto(codigo)
            messagebox.showinfo("Éxito", f"Producto {codigo} eliminado.")
            self.actualizar_vista()
            self.limpiar_campos()
        else:
            # También permitimos eliminar por código escrito
            codigo = self.entry_codigo.get().strip()
            if codigo:
                self.inventario.eliminar_producto(codigo)
                messagebox.showinfo("Éxito", f"Producto {codigo} eliminado.")
                self.actualizar_vista()
                self.limpiar_campos()
            else:
                messagebox.showwarning("Atención", "Seleccione un producto o escriba un código para eliminar.")

    def mostrar(self):
        # Mostrar reusa la misma vista del tree: simplemente actualizar
        self.actualizar_vista()
        messagebox.showinfo("Inventario", "Lista actualizada.")

    def actualizar_vista(self):
        # Limpia y carga la información desde inventario.productos
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Si tu inventario almacena en diccionario:
        if hasattr(self.inventario, "productos"):
            for p in self.inventario.productos.values():
                self.tree.insert("", "end", values=(p.codigo, p.nombre, p.cantidad, p.precio))
        else:
            # Fallback: si inventario tiene método listar() que devuelve objetos
            if hasattr(self.inventario, "listar"):
                for p in self.inventario.listar():
                    self.tree.insert("", "end", values=(p.codigo, p.nombre, p.cantidad, p.precio))

    def _cargar_seleccion_en_campos(self, event=None):
        sel = self.tree.selection()
        if sel:
            vals = self.tree.item(sel[0])["values"]
            # vals = (codigo, nombre, cantidad, precio)
            self.entry_codigo.delete(0, tk.END); self.entry_codigo.insert(0, vals[0])
            self.entry_nombre.delete(0, tk.END); self.entry_nombre.insert(0, vals[1])
            self.entry_cantidad.delete(0, tk.END); self.entry_cantidad.insert(0, vals[2])
            self.entry_precio.delete(0, tk.END); self.entry_precio.insert(0, vals[3])

    def limpiar_campos(self):
        self.entry_codigo.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)


