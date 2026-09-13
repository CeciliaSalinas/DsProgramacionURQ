import tkinter as tk
from tkinter import ttk

#"Una interfaz que después puedo configurar para distintas entidades.
#la clase  recibe una lista , no necesita saber que pametroen particular
class Interfaz:
                #la clase interfaz recibe estos parametros
    def __init__(self, ventana, titulo, campos, columnas):
        self.ventana = ventana
        self.titulo = titulo
        #aca guardamso los campos que tendra cada entidad(nombre, duracion, profe...)
        self.campos = campos
        self.columnas = columnas
        #creamos un diccionario vacio, donde guardamos las referencias de los entry
        self.entries = {}
        self.idSeleccionado = None


    def crearFormulario(self):
        #for crea todos los label y entry automaticamente , va recorriendo 1 x 1 de lso campos
        for i, campo in enumerate(self.campos):

            label = tk.Label(self.ventana, text=campo.capitalize())

            label.grid(row=i, column=0)

            entry = tk.Entry(self.ventana)

            entry.grid(row=i, column=1)
            #los entry quedan guardados aca dentro del diccionario
            self.entries[campo] = entry

    
    def obtenerDatos(self):
        #creamos un diccionario vacio
        datos = {}
        #recorremso el diccionario 
        for campo in self.campos:
                        # y apara cada uno buscamos su Entry 
                                          #obtenemos lo que escribio el usuario
            #y los guardamos
            datos[campo] = self.entries[campo].get()

        return datos


    def limpiarFormulario(self):
        #recorre todos los campos y busca el Entry correspondiente y elimina su contenido
        for campo in self.campos:
            self.entries[campo].delete(0, tk.END)


    def crearTabla(self):
        self.tabla = ttk.Treeview(self.ventana, columns=self.columnas, show="headings")

        #se van a crear automaticamente las columnas que indiquemos
        for columna in self.columnas:
            self.tabla.heading( columna, text=columna.capitalize())

            self.tabla.column(columna, anchor="center", width=110)

        self.tabla.grid( row=len(self.campos) + 3, column=0, columnspan=4, padx=10, pady=20)


    def cargarDatos(self, datos):
        #borra todos los datos que ya estabn en la tabla
        self.tabla.delete(*self.tabla.get_children())
        #recorremos todos los datos que recibimos
        for fila in datos:
            #se agerga la fila al treeview
            self.tabla.insert("", tk.END, values=fila)


    def obtenerSeleccion(self):
        #pregunta que fila esta seleccionada
        seleccion = self.tabla.selection()

        if not seleccion:
            return None
        #si ahay una tomamos esa fila
        item = seleccion[0]
        #obtenemos sus valores
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