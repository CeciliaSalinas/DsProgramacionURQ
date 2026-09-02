class Biblioteca:
    def __init__(self):
        self.miembros = []
        self.libros = []
    
    def agregarMiembro(self, nombre, dni):
        miembro = Miembro(nombre, dni)
        self.miembros.append(miembro)
    
    def agregarLibro(self, titulo, autor, isbn):
        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)
    
    def prestarLibro(self, dni, isbn):
        libro_localizado = None
        miembro_localizado = None

        #recorrer lista libros hasta que coincida con el isnbn
        for libro in self.libros:
            if libro.isbn == isbn:
                libro_localizado = libro
        
        #recorrer lista de liembro hasta que coincida con el dni
        for miembro in self.miembros:
            if miembro.dni == dni:
                miembro_localizado = miembro

        if libro_localizado == None:
            print("Libro no encontrado")

        elif miembro_localizado == None:
            print("Miembro no encontrado")
           
        else :
            miembro_localizado.tomarPrestado(libro_localizado)

    def devolverLibro(self, dni, isbn):
        libro_localizado = None
        miembro_localizado = None

        for libro in self.libros:
            if libro.isbn == isbn:
                libro_localizado = libro

        for miembro in self.miembros:
            if miembro.dni == dni:
                miembro_localizado = miembro
        
        if libro_localizado == None:
            print("Libro no encontrado")

        elif miembro_localizado == None:
            print("Miembro no encontrado")
           
        else :
            miembro_localizado.devolverLibro(libro_localizado)
        
    def consultarEstadoLibro(self):
        #valido
        try:
            print(self.libros[0])
        
        except IndexError:
            print("** No hay libros cargados **")
            return
        
        #recorrer la lista de libros
        for libro in self.libros:
            print("Título:", libro.titulo)
            print("Estado:", libro.estado)

            if libro.liPrestado != None:
                print("Prestado a miembro:", libro.liprestado.nombre)

    def consultarEstadoMiembro(self):
        #valido
        try:
            print(self.miembros[0])
        
        except IndexError:
            print("** No hay miembros registrados **")
            return
        
        for miembro in self.miembros:
            print("Nombre:", miembro.nombre)
            print("Dni:", miembro.dni)

            for libro in miembro.librosPrestados:
                print("Libros prestados:", libro.titulo)

            
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = "Disponible"
        self.liPrestado = None
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.isbn} - {self.estado}"
    
    def prestar_libro(self):
        self.estado = "Prestado"
    
    def devolverLibro(self):
        self.estado = "Disponible"


class Miembro:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.librosPrestados = [] 

    def __str__(self):
        return f"{self.nombre} - Dni: {self.dni}"
    
    def tomarPrestado(self, libro):
        if libro.estado == "Disponible":
            libro.prestar_libro()
            libro.liPrestado = self
            self.librosPrestados.append(libro)

            print("LIBRO PRESTADO")
        else:
            print("LIBRO NO DISPONIBLE")
    
    def devolverLibro(self, libro):
        if libro in self.librosPrestados:

            libro.devolverLibro()
            libro.liPrestado = None

            self.librosPrestados.remove(libro)

            print("LIBRO DEVUELTO")
        else:
            print("EL LIBRO NO FUE PRESTADO")

def main():

    biblioteca = Biblioteca()

    while True:
            print('0 Salir')
            print('1 - Agregar libro')
            print('2 - Agregar miembro')
            print('3 - Prestar libros')
            print('4 - Devolver libros')
            print('5 - Consultar estado de los libros')
            print('6 - Consultar estado de los miembros')

            #valido
            try:
                opcionMenu = int(input("Ingresar una opción:"))

            except ValueError:
                print("** Ingresar un valor numérico para el menú **")
                continue

            if opcionMenu == 0:
                    print("Salir del sistema")
                    break

            elif opcionMenu == 1:
                titulo = input("Ingresar titulo:")
                autor = input("Ingresar autor:")
                isbn = input("Ingresar ISBN:")

                biblioteca.agregarLibro(titulo, autor, isbn)
                print("Libro agregado")

            elif opcionMenu == 2:
                 nombre = input("Ingresar nombre:")
                #valido
                 try:
                     dni = int(input("Ingresar dni:"))

                 except ValueError:
                    print("** Ingresar un valor numérico para el dni **")
                    continue
            
                 biblioteca.agregarMiembro(nombre, dni)
                 print("Miembro agregado")

           
            elif opcionMenu == 3:
                dni = input("Ingrese DNI del miembro: ")
                isbn = input("Ingrese ISBN del libro: ")

                biblioteca.prestarLibro(dni, isbn)

            elif opcionMenu == 4:
                dni = input("Ingrese DNI del miembro: ")
                isbn = input("Ingrese ISBN del libro: ")

                biblioteca.devolverLibro(dni, isbn)
            
            elif opcionMenu == 5:

                biblioteca.consultarEstadoLibro()

            elif opcionMenu == 6:

                biblioteca.consultarEstadoMiembro()
            
            else:
                print("Opción incorrecta!, igresar una nueva opción.")
main()


    




        
