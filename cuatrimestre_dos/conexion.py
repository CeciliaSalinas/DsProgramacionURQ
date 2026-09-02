import mariadb

def conectar():
    try:
        conexion = mariadb.connect(
            user="root",
            password="",
            host="127.0.0.1",
            port=3306,
            database="gestion_cursos"
        )

        return conexion

    except mariadb.Error as error:
        print(f"Error al conectar con la base de datos:{error}")

