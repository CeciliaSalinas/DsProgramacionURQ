from conexion import conectar


def agregarCurso(nombre, duracion, profesor, cupo):
 
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO cursos (nombre, duracion, profesor, cupo) VALUES (?, ?, ?, ?)",
                   (nombre, duracion, profesor, cupo))

    conexion.commit()
    conexion.close()

def listarCursos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM cursos")

    cursos = cursor.fetchall()
    conexion.close()

    return cursos

def modificarCurso(id, nombre, duracion,profesor, cupo):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("UPDATE cursos SET nombre = ?, duracion = ?, profesor = ?, cupo = ? WHERE id = ?",
                   (nombre, duracion, profesor, cupo, id))

    conexion.commit()
    conexion.close()

def eliminarCurso(idCurso):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM cursos WHERE id = ?",(idCurso,))    

    conexion.commit()
    conexion.close()

