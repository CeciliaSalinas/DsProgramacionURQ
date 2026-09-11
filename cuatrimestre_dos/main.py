import tkinter as tk
from conexion import conectar
from curso import agregarCurso, listarCursos, modificarCurso, eliminarCurso
from tkinter import messagebox
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Sistema de gestion de cursos")
ventana.geometry("600x700")
ventana.configure(bg="#2c3e50")
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

conexion = conectar()

def registrarCurso():
    nombre = nombreCurso.get()
    duracion = duracionCurso.get()
    profesor = nombreProfesor.get()
    cupo = cupoEstudiantes.get()

    if nombre == "":
        messagebox.showwarning("Validación","Debe ingresar el nombre del curso.")
        return

    if duracion == "":
        messagebox.showwarning("Validación","Debe ingresar la duración del curso.")
        return

    try:
        duracion = int(duracionCurso.get())
    except ValueError:
        messagebox.showwarning("Validación","La duración debe ser en números.")
        return

    if profesor == "":
        messagebox.showwarning("Validación","Debe ingresar el nombre del profesor.")
        return

    if cupo == "":
        messagebox.showwarning("Validación","Debe ingresar el cupo de estudiantes del curso.")
        return
    try:
        cupo = int(cupoEstudiantes.get())
    except ValueError:
        messagebox.showwarning("Validación","Debe ingresar números en el cupo de estudiantes.")
        return
    
    agregarCurso(nombre, duracion, profesor, cupo)

    messagebox.showinfo("Registro exitoso", "El curso se registró correctamente.")

    mostrarCursos()

    nombreCurso.delete(0, tk.END)
    duracionCurso.delete(0, tk.END)
    nombreProfesor.delete(0, tk.END)
    cupoEstudiantes.delete(0, tk.END)

def mostrarCursos():
    cursos = listarCursos()

    listaCursos.delete(*listaCursos.get_children())

    for curso in cursos:
        id, nombre, duracion,profesor, cupo = curso
        listaCursos.insert("", tk.END, values=(id, nombre,duracion,profesor,cupo))


idCursoSeleccionado = None

def seleccionarCurso(event):
    global idCursoSeleccionado

    seleccion = listaCursos.selection()

    if seleccion:
        item = seleccion[0]

        datos = listaCursos.item(item, "values")

        idCursoSeleccionado = datos[0]
        nombre = datos[1]
        duracion = datos[2]
        profesor = datos[3]
        cupo = datos[4]

        nombreCurso.delete(0, tk.END)
        nombreCurso.insert(0, nombre)

        duracionCurso.delete(0, tk.END)
        duracionCurso.insert(0, duracion)

        nombreProfesor.delete(0, tk.END)
        nombreProfesor.insert(0, profesor)

        cupoEstudiantes.delete(0, tk.END)
        cupoEstudiantes.insert(0, cupo)

        print("ID del curso:", idCursoSeleccionado)

def modificarCursoInterfaz():
    global idCursoSeleccionado 

    if idCursoSeleccionado is None:
        messagebox.showwarning("Validación","Debe seleccionar un curso para modificar.")
        return

    nombre = nombreCurso.get()
    duracion = duracionCurso.get()
    profesor = nombreProfesor.get()
    cupo = cupoEstudiantes.get()  

    if nombre == "":
        messagebox.showwarning("Validación","Debe ingresar el nombre del curso.")
        return 

    try:
        duracion = int(duracionCurso.get())
    except ValueError:
        messagebox.showwarning("Validación","La duración debe ser en números.")
        return


    if profesor == "":
        messagebox.showwarning("Validación", "Debe ingresar el nombre del profesor.")
        return

    try:
        cupo = int(cupoEstudiantes.get())
    except ValueError:
        messagebox.showwarning("Validación","Debe ingresar números en el cupo de estudiantes.")
        return

    modificarCurso(idCursoSeleccionado, nombre, duracion, profesor, cupo)

    messagebox.showinfo("Modificación exitosa","El curso se modificó correctamente.")

    mostrarCursos()  

    nombreCurso.delete(0, tk.END)
    duracionCurso.delete(0, tk.END)
    nombreProfesor.delete(0, tk.END)
    cupoEstudiantes.delete(0, tk.END)  

    idCursoSeleccionado = None
            
def eliminarCursoInterfaz():
    global idCursoSeleccionado

    if idCursoSeleccionado is None:
        messagebox.showwarning( "Validación","Debe seleccionar un curso para eliminar.")
        return

    respuesta = messagebox.askquestion("Confirmar eliminación","¿Está seguro de que desea eliminar este curso?")

    if respuesta == "yes":
        eliminarCurso(idCursoSeleccionado)

        messagebox.showinfo("Eliminación exitosa","El curso se eliminó correctamente.")
        
        mostrarCursos()

        nombreCurso.delete(0, tk.END)
        duracionCurso.delete(0, tk.END)
        nombreProfesor.delete(0, tk.END)
        cupoEstudiantes.delete(0, tk.END)

        idCursoSeleccionado = None

        
tk.Label(ventana,text="REGISTRAR CURSO", font="Arial 14 bold",fg="pink", bg="#2c3e50").grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(ventana,text="Nombre curso:", fg="white", font="Arial 12", bg="#2c3e50").grid(row=1, column=0, padx=10, pady=10, sticky="e")
nombreCurso = tk.Entry(ventana)
nombreCurso.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana,text="Duración:" ,fg="white", font="Arial 12", bg="#2c3e50").grid(row=2, column=0, padx=10, pady=10, sticky="e")
duracionCurso = tk.Entry(ventana)
duracionCurso.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana,text="Profesor/a:",fg="white", font="Arial 12", bg="#2c3e50").grid(row=3, column=0, padx=10, pady=10, sticky="e")
nombreProfesor = tk.Entry(ventana)
nombreProfesor.grid(row=3, column=1, padx=10, pady=10)

tk.Label(ventana,text="Cupo:",fg="white", font="Arial 12", bg="#2c3e50").grid(row=4, column=0, padx=10, pady=10, sticky="e")
cupoEstudiantes = tk.Entry(ventana)
cupoEstudiantes.grid(row=4, column=1, padx=10, pady=10)


boton_agregar = tk.Button(ventana,text="Registrar", width=11, command=registrarCurso)
boton_agregar.grid(row=5, column=0, padx=5, pady=20)

boton_modificar = tk.Button(ventana,text="Modificar", width=11, command=modificarCursoInterfaz)
boton_modificar.grid(row=5, column=1, padx=5, pady=20)

boton_eliminar = tk.Button(ventana,text="Eliminar", width=11, command=eliminarCursoInterfaz)
boton_eliminar.grid(row=5, column=2, padx=5, pady=20)



tk.Label(ventana, text="CURSOS REGISTRADOS", font="Arial 14 bold", fg="pink", bg="#2c3e50").grid(row=7, column=0, columnspan=3, pady=20)
#listaCursos = tk.Listbox(ventana, width=60, height=10)
listaCursos = ttk.Treeview(ventana,columns=("id", "nombre", "duracion", "profesor", "cupo"), show="headings",height=10)

listaCursos.heading("id", text="ID", anchor="center")
listaCursos.heading("nombre", text="Nombre", anchor="center")
listaCursos.heading("duracion", text="Duración en meses", anchor="center")
listaCursos.heading("profesor", text="Profesor", anchor="center")
listaCursos.heading("cupo", text="Cupo alumnos", anchor="center")

listaCursos.column("id", width=50, anchor="center")
listaCursos.column("nombre", width=120, anchor="center")
listaCursos.column("duracion", width=120, anchor="center")
listaCursos.column("profesor", width=150, anchor="center")
listaCursos.column("cupo", width=120, anchor="center")

listaCursos.grid(row=8, column=0, columnspan=3,padx=20, pady=10)
#listaCursos.bind("<<ListboxSelect>>", seleccionarCurso)
listaCursos.bind("<<TreeviewSelect>>", seleccionarCurso)

mostrarCursos()
ventana.mainloop()


