import tkinter as tk
from interfaz import Interfaz
from curso import listarCursos,agregarCurso, modificarCurso, eliminarCurso
from alumno import listarAlumnos, agregarAlumno, modificarAlumno, eliminarAlumno
from tkinter import messagebox

ventana = tk.Tk()

ventana.title("Sistema de gestión")
ventana.geometry("570x520")


camposCurso = ["nombre", "duracion", "profesor","cupo"]
columnasCurso = ["id", "nombre", "cantidad de meses","profesor", "cupo"]

crudCursos = Interfaz(ventana,"Cursos",camposCurso, columnasCurso)


camposAlumno = ["nombre", "apellido", "dni"]
columnasAlumno = ["id", "nombre", "apellido", "dni"]

crudAlumnos = Interfaz( ventana, "Alumnos",camposAlumno,columnasAlumno)

def mostrarDatos():
    datos = crudCursos.obtenerDatos()
    print(datos)


def limpiar():
    crudCursos.limpiarFormulario()

boton_limpiar = tk.Button(ventana,text="Limpiar",command=limpiar)
boton_limpiar.grid(row=6, column=3, padx=5, pady=10)


def mostrarCursos():
    cursos = listarCursos()
    crudCursos.cargarDatos(cursos)

def agregar():

    datos = crudCursos.obtenerDatos()

    nombre = datos["nombre"]
    duracion = datos["duracion"]
    profesor = datos["profesor"]
    cupo = datos["cupo"]

    if nombre == "" or duracion == "" or profesor == "" or cupo == "":
        messagebox.showwarning( "Validación", "Debe completar todos los campos.")
        return

    agregarCurso( nombre, int(duracion), profesor, int(cupo))

    try:
        duracion = int(duracion)
        cupo = int(cupo)

    except ValueError:
        messagebox.showwarning( "Validación","La duración y el cupo deben ser números enteros.")
        return

    crudCursos.cargarDatos(listarCursos())
    crudCursos.limpiarFormulario()

    messagebox.showinfo( "Registro", "El curso se registró correctamente.")

boton_agregar = tk.Button( ventana, text="Registrar", command=agregar)
boton_agregar.grid( row=6, column=0, padx=5, pady=10)


def mostrarSeleccion():
    crudCursos.cargarSeleccion()


def modificar():

    if crudCursos.idSeleccionado is None:
        messagebox.showwarning( "Validación", "Debe seleccionar un curso.")
        return

    datos = crudCursos.obtenerDatos()

    nombre = datos["nombre"]
    duracion = datos["duracion"]
    profesor = datos["profesor"]
    cupo = datos["cupo"]

    if nombre == "" or duracion == "" or profesor == "" or cupo == "":
        messagebox.showwarning("Validación","Debe completar todos los campos.")
        return

    try:
        duracion = int(duracion)
        cupo = int(cupo)

    except ValueError:
        messagebox.showwarning( "Validación","La duración y el cupo deben ser números enteros.")
        return

    modificarCurso( crudCursos.idSeleccionado, nombre, int(duracion), profesor,int(cupo))

    crudCursos.cargarDatos(listarCursos())
    crudCursos.limpiarFormulario()
    crudCursos.idSeleccionado = None

    messagebox.showinfo("Modificación", "El curso se modificó correctamente.")

boton_modificar = tk.Button(ventana,text="Modificar",command=modificar)
boton_modificar.grid( row=6, column=1, padx=5, pady=10)


def eliminar():

    if crudCursos.idSeleccionado is None:
            messagebox.showwarning( "Validación","Debe seleccionar un curso.")
            return

    respuesta = messagebox.askquestion(
        "Confirmar eliminación",
        "¿Está seguro de eliminar el curso?"
    )

    if respuesta == "yes":

        eliminarCurso(crudCursos.idSeleccionado)

        crudCursos.cargarDatos(listarCursos())
        crudCursos.limpiarFormulario()
        crudCursos.idSeleccionado = None

        messagebox.showinfo("Eliminación","El curso se eliminó correctamente.")

boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar)
boton_eliminar.grid(row=6, column=2, padx=5, pady=10)


crudCursos.crearFormulario()
crudCursos.crearTabla()
crudCursos.tabla.bind("<<TreeviewSelect>>",lambda event: crudCursos.cargarSeleccion())


mostrarCursos()


def abrirAlumnos():

    ventanaAlumnos = tk.Toplevel(ventana)

    ventanaAlumnos.title("Gestión de alumnos")
    ventanaAlumnos.geometry("600x500")

    ventanaAlumnos.lift()
    ventanaAlumnos.focus_force()

    crudAlumnos = Interfaz(ventanaAlumnos,"Alumnos", camposAlumno, columnasAlumno)

    crudAlumnos.crearFormulario()
    crudAlumnos.crearTabla()
    crudAlumnos.cargarDatos(listarAlumnos())

    crudAlumnos.tabla.bind("<<TreeviewSelect>>",lambda event: crudAlumnos.cargarSeleccion())



    def agregar():
        datos = crudAlumnos.obtenerDatos()

        nombre = datos["nombre"]
        apellido = datos["apellido"]
        dni = datos["dni"]

        if nombre == "" or apellido == "" or dni == "" :
            messagebox.showwarning( "Validación", "Debe completar todos los campos.", parent=ventanaAlumnos)
            return

        try:
            dni = int(dni)

        except ValueError:
            messagebox.showwarning( "Validación","El dni debe ser número entero.", parent=ventanaAlumnos)
        return


    boton_agregar = tk.Button(ventanaAlumnos, text="Registrar", command=agregar)
    boton_agregar.grid( row=5, column=0, padx=5,pady=10)


    def modificar():

        if crudAlumnos.idSeleccionado is None:
                messagebox.showwarning("Validación","Debe seleccionar un alumno.", parent=ventanaAlumnos)
                return

        datos = crudAlumnos.obtenerDatos()

        nombre = datos["nombre"]
        apellido = datos["apellido"]
        dni = datos["dni"]

        if nombre == "" or apellido == "" or dni == "":
            messagebox.showwarning("Validación","Debe completar todos los campos.", parent=ventanaAlumnos)
            return

        try:
            dni = int(dni)

        except ValueError:
            messagebox.showwarning( "Validación","El dni debe ser número entero.", parent=ventanaAlumnos)
            return

        modificarAlumno(crudAlumnos.idSeleccionado, nombre, apellido, dni)

        crudAlumnos.cargarDatos(listarAlumnos())
        crudAlumnos.limpiarFormulario()
        crudAlumnos.idSeleccionado = None

        messagebox.showinfo("Modificación", "El alumno se modificó correctamente.",parent=ventanaAlumnos)

    boton_modificar = tk.Button(ventanaAlumnos, text="Modificar",command=modificar)
    boton_modificar.grid(row=5,column=1, padx=5,pady=10)


    def eliminar():

        if crudAlumnos.idSeleccionado is None:
            messagebox.showwarning( "Validación","Debe seleccionar un alumno.", parent=ventanaAlumnos)
            return

        respuesta = messagebox.askquestion( "Confirmar eliminación", "¿Está seguro de eliminar el alumno?",parent=ventanaAlumnos)

        if respuesta == "yes":

            eliminarAlumno(crudAlumnos.idSeleccionado)

            crudAlumnos.cargarDatos(listarAlumnos())
            crudAlumnos.limpiarFormulario()

            crudAlumnos.idSeleccionado = None

            messagebox.showinfo( "Eliminación", "El alumno se eliminó correctamente.", parent=ventanaAlumnos)

    boton_eliminar = tk.Button( ventanaAlumnos, text="Eliminar", command=eliminar)
    boton_eliminar.grid( row=5, column=2, padx=5,pady=10)

    def limpiar():
        crudAlumnos.limpiarFormulario()

    boton_limpiar = tk.Button( ventanaAlumnos, text="Limpiar",command=limpiar)
    boton_limpiar.grid( row=5, column=3, padx=5, pady=10)

boton_alumnos = tk.Button(ventana, text="Gestionar Alumnos", command=abrirAlumnos)
boton_alumnos.grid(row=8, column=0, padx=5, pady=10)

ventana.mainloop()



