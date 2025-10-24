import sqlite3

def consultar_clientes(conn: sqlite3.Connection):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Cliente')
        datos = cursor.fetchall()
        print("Clientes:")
        for i, registros in enumerate(datos):
            if i + 1 < len(datos):
                print(registros[0], end=', ')
            else:
                print(registros[0])

    except Exception as e:
        print("No se ha podido realizar la consulta: ", e)

    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")

    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")


def consultar_empleados(conn: sqlite3.Connection):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Empleado')
        datos = cursor.fetchall()
        print("Empleados:")
        for i, registros in enumerate(datos):
            if i + 1 < len(datos):
                print(registros[0], end=', ')
            else:
                print(registros[0])

    except Exception as e:
        print("No se ha podido realizar la consulta: ", e)

    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")

    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")


def consultar_proyectos(conn: sqlite3.Connection):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Proyecto')
        datos = cursor.fetchall()
        print("Proyectos:")
        for i, registros in enumerate(datos):
            if i + 1 < len(datos):
                print(registros[0], end=', ')
            else:
                print(registros[0])

    except Exception as e:
        print("No se ha podido realizar la consulta: ", e)

    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")

    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")


def consultar_todo(conn: sqlite3.Connection):
    try:
        cursor = conn.cursor()

        # 1. Ver todos los registros de Cliente
        cursor.execute('SELECT * FROM Cliente')
        print("Clientes:")
        print(cursor.fetchall())

        # 2. Ver todos los registros de Empleado
        cursor.execute('SELECT * FROM Empleado')
        print("\nEmpleados:")
        print(cursor.fetchall())

        # 3. Ver todos los registros de Proyecto
        cursor.execute('SELECT * FROM Proyecto')
        print("\nProyectos:")
        print(cursor.fetchall())

        cursor.execute('SELECT * FROM EmpleadosProyecto')
        print("\nEmpleados por proyecto:")
        print(cursor.fetchall())
    
    except Exception as e:
        print("No se han podido realizar las consultas: ", e)

    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")

    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
        