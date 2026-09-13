import tkinter as tk
from tkinter import ttk

class Interfaz:
                
    def __init__(self, ventana, titulo, campos, columnas):
        self.ventana = ventana
        self.titulo = titulo
        self.campos = campos
        self.columnas = columnas
        self.entries = {}
        self.idSeleccionado = None


    def crearFormulario(self):
        for i, campo in enumerate(self.campos):

            label = tk.Label(self.ventana, text=campo.capitalize())
            label.grid(row=i, column=0)

            entry = tk.Entry(self.ventana)
            entry.grid(row=i, column=1)
            self.entries[campo] = entry

    
    def obtenerDatos(self):
        datos = {}
        
        for campo in self.campos:
            datos[campo] = self.entries[campo].get()
        return datos


    def limpiarFormulario(self):
        for campo in self.campos:
            self.entries[campo].delete(0, tk.END)


    def crearTabla(self):
        self.tabla = ttk.Treeview(self.ventana, columns=self.columnas, show="headings")

        for columna in self.columnas:
            self.tabla.heading( columna, text=columna.capitalize())

            self.tabla.column(columna, anchor="center", width=110)

        self.tabla.grid( row=len(self.campos) + 3, column=0, columnspan=4, padx=10, pady=20)


    def cargarDatos(self, datos):

        self.tabla.delete(*self.tabla.get_children())
   
        for fila in datos:
            self.tabla.insert("", tk.END, values=fila)


    def obtenerSeleccion(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            return None
        
        item = seleccion[0]
        datos = self.tabla.item(item, "values")

        return datos

    def cargarSeleccion(self):

        datos = self.obtenerSeleccion()

        if datos is None:
            return

        self.idSeleccionado = datos[0]

        for i, campo in enumerate(self.campos):

            self.entries[campo].delete(0, tk.END)

            self.entries[campo].insert(0, datos[i +1])