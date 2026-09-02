import tkinter as tk
from DsProgramacionURQ.cuatrimestre_dos.conexion import conectar

ventana = tk.Tk()
ventana.title("SGDC")
ventana.geometry("500x600")
ventana.configure(bg="#2c3e50")
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)


#compruebo la conexion
conexion = conectar()

#if conexion:
    #tk.Label(ventana, text="Se conecto correctamente a la base de datos " + conexion.database +".").pack()

# Interfaz gráfica
tk.Label(ventana,text="SISTEMA DE GESTIÓN DE CURSOS", font="Arial 14 bold",fg="pink", bg="#2c3e50").grid(row=0, column=0, columnspan=2, pady=20)

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


boton_agregar = tk.Button(ventana,text="Registrar", width=11)
boton_agregar.grid(row=5, column=0, padx=5, pady=20)

boton_modificar = tk.Button(ventana,text="Modificar", width=11)
boton_modificar.grid(row=5, column=1, padx=5, pady=20)

boton_eliminar = tk.Button(ventana,text="Eliminar", width=11)
boton_eliminar.grid(row=5, column=2, padx=5, pady=20)

ventana.mainloop()


