from conexion import conectar

def agregarAlumno(nombre, apellido, dni):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(" INSERT INTO alumnos (nombre, apellido, dni) VALUES (?, ?, ?)",
                    (nombre, apellido, dni))

    conexion.commit()

    cursor.close()
    conexion.close()


def listarAlumnos():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, apellido, dni FROM alumnos")

    alumnos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return alumnos

#print(listarAlumnos())

def modificarAlumno(idAlumno, nombre, apellido, dni):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("UPDATE alumnos SET nombre = ?, apellido = ?, dni = ? WHERE id = ?",
                    (nombre, apellido, dni, idAlumno))

    conexion.commit()

    cursor.close()
    conexion.close()

#modificarAlumno(1, "Ana", "Gonzalez", "12345678")


def eliminarAlumno(idAlumno):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("DELETE FROM alumnos WHERE id = ?", (idAlumno,))

    conexion.commit()

    cursor.close()
    conexion.close()

eliminarAlumno(1)