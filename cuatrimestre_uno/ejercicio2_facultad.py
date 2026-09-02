class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    def agregarEstudiante(self, nombre, apellido, matricula, carrera):

        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                print("La matrícula ya existe")
                return
            
        estudiante = Estudiante(nombre, apellido, matricula, carrera)
        self.estudiantes.append(estudiante)

    def agregarCurso(self, nombreCurso, codigoCurso, profesorEncargado, capacidadMaxima):

        for curso in self.cursos:
            if curso.codigoCurso == codigoCurso:
                print("El código del curso ya existe")
                return
    
        curso = Curso(nombreCurso, codigoCurso, profesorEncargado, capacidadMaxima)
        self.cursos.append(curso)
    
    def inscribirEstudianteCurso(self, matricula, codigoCurso):
        estudiante_localizado = None
        curso_localizado = None

        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                estudiante_localizado = estudiante
        
        for curso in self.cursos:
            if curso.codigoCurso == codigoCurso:
                curso_localizado = curso
        
        if estudiante_localizado == None:
            print("Estudiante no encontrado")
        
        elif curso_localizado == None:
            print("Curso no encontrado")
        
        else:
            curso_localizado.inscribirEstudiante(estudiante_localizado)
    
    def bajaEstudianteCurso(self, matricula, codigoCurso):
        estudiante_localizado = None
        curso_localizado = None

        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                estudiante_localizado = estudiante
        
        for curso in self.cursos:
            if curso.codigoCurso == codigoCurso:
                curso_localizado = curso

        if estudiante_localizado == None:
            print("Estudiante no encontrado")
        
        elif curso_localizado == None:
            print("Curso no encontrado")
        
        else:
            curso_localizado.bajaEstudianteCurso(estudiante_localizado)
    
    def consultarEstadoEstudiante(self):
        try:
            print(self.estudiantes[0])
        
        except IndexError:
            print("No hay estudiantes registrados")
            return

        for estudiante in self.estudiantes:
            estudiante.consultarEstadoEstudiante()
    
    def consultarEstadoCurso(self):
        try:
            print(self.cursos[0])
        
        except IndexError:
            print("No hay cursos registrados")
            return
        
        for curso in self.cursos:
            curso.consultarEstadoCurso()

class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera

        self.cursosInscriptos = []
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.matricula} - {self.carrera} "

    def consultarEstadoEstudiante(self):
        print("Nombre:", self.nombre)
        print("Apellido:" , self.apellido)

        for curso in self.cursosInscriptos:
            print("Cursos inscriptos:", curso.nombreCurso)


class Curso:
    def __init__(self, nombreCurso, codigoCurso, profesorEncargado, capacidadMaxima):
        self.nombreCurso = nombreCurso
        self.codigoCurso = codigoCurso
        self.profesorEncargado = profesorEncargado
        self.capacidadMaxima = capacidadMaxima
        self.estudiantesInscriptos = []

    def __str__(self):
        return f"{self.nombreCurso} - {self.codigoCurso} - {self.profesorEncargado}"

    def inscribirEstudiante(self, estudiante):
        if estudiante in self.estudiantesInscriptos:
            print("El estudiante ya está inscripto en el curso")

        if len(self.estudiantesInscriptos) < self.capacidadMaxima:
            self.estudiantesInscriptos.append(estudiante)

            estudiante.cursosInscriptos.append(self)

            print("Se inscribió al estudiante con éxito")
        
        else:
            print("No hay cupos disponibles de inscripción")
    
    def bajaEstudianteCurso(self, estudiante):
        if estudiante in self.estudiantesInscriptos:
            self.estudiantesInscriptos.remove(estudiante)
            estudiante.cursosInscriptos.remove(self)

            print("Se dio de baja al estudiante del curso.")
        
        else:
            print("No hay estudiante inscripto en el curso.")

    def consultarEstadoCurso(self):
        print("Curso:", self.nombreCurso)

        print("Estudiantes inscriptos:", len (self.estudiantesInscriptos))

        print("Cupos disponibles:" , self.capacidadMaxima - len(self.estudiantesInscriptos))
            

def main():

    facultad = Facultad()

    while True:
            print('0 Salir')
            print('1 - Agregar estudiante')
            print('2 - Agregar curso')
            print('3 - Inscribir estudiante a curso')
            print('4 - Baja estudiante de curso')
            print('5 - Consultar estado de cursos')
            print('6 - Consultar estado de los estudiantes')

            opcionMenu = input("Ingresar una opción de menú:")
    
            if opcionMenu == "0":
                print("Salir del sistema")
                break

            elif opcionMenu == "1":
                nombre = input("Ingresar nombre: ")
                apellido = input("Ingresar apellido: ")
                matricula = input("Ingresar matrícula: ")
                carrera = input("Ingresar carrera: ")

                facultad.agregarEstudiante(nombre, apellido, matricula, carrera)
                print("Se agregó estudiante")

            elif opcionMenu == "2":
                nombreCurso = input("Ingresar nombre curso: ")
                codigoCurso = input("Ingresar codigo de curso: ")
                profesorEncargado = input("Ingresar profesor encargado: ")

                try:
                    capacidadMaxima = int(input("Ingresar capacidad máxima del curso: "))
                
                except ValueError:
                    print("Ingresar un valor numérico para la capacidad máxima del curso: ")
                    continue

                facultad.agregarCurso(nombreCurso, codigoCurso, profesorEncargado, capacidadMaxima)
                print("Curso agregado")
            
            elif opcionMenu == "3":
                matricula = input("Ingresar matrícula: ")
                codigoCurso = input ("Ingresar codigo de curso: ")

                facultad.inscribirEstudianteCurso(matricula, codigoCurso)
            
            elif opcionMenu == "4":
                matricula = input("Ingresar matrícula: ")
                codigoCurso = input ("Ingresar codigo de curso: ")

                facultad.bajaEstudianteCurso(matricula, codigoCurso)
            
            elif opcionMenu == "5":
                facultad.consultarEstadoCurso()
            
            elif opcionMenu == "6":
                facultad.consultarEstadoEstudiante()
            
            else:
                print("Opción incorrecta!, igresar una nueva opción.")
main()