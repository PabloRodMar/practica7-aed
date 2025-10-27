import sqlite3
import conexion, utilidades

######################## Funciones internas ########################
def pedir_cliente(conn: sqlite3.Connection) -> str:
    cliente = input("Introduzca el ID del cliente que solicita el proyecto: ")
    cli_encontrado = utilidades.buscar_cliente(conn, cliente)
    return cliente, cli_encontrado

def pedir_empleado(conn: sqlite3.Connection) -> str:
    empleado = input("Introduzca el ID del empleado jefe del proyecto: ")
    emp_encontrado = utilidades.buscar_empleado(conn, empleado)
    return empleado, emp_encontrado

def pedir_proyecto(conn: sqlite3.Connection) -> str:
    nombre_proyecto = input("Introduzca el nombre del proyecto: ")
    nombre_encontrado = utilidades.proyecto_repetido(conn, nombre_proyecto)
    return nombre_proyecto, nombre_encontrado

def pedir_fecha() -> str:
    fecha = input("Introduzca la fecha de inicio de el proyecto: ")
    fecha_valida = utilidades.validar_fecha(fecha)
    return fecha, fecha_valida

######################### Operaciones CRUD #########################

def registrar_proyecto(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()

    cliente, cli_encontrado = pedir_cliente(conn)
    while not cli_encontrado:
        print("Error: El cliente no ha sido encontrado. Inténtelo de nuevo.")
        cliente, cli_encontrado = pedir_cliente(conn)

    empleado, emp_encontrado = pedir_empleado(conn)
    while not emp_encontrado:
        print("Error: El empleado no ha sido encontrado. Inténtelo de nuevo.")
        empleado, emp_encontrado = pedir_empleado(conn)
    
    nombre_proyecto, nombre_encontrado = pedir_proyecto(conn)
    while not nombre_encontrado:
        print("Error: El nombre del proyecto ya está en uso. Introduzca otro.")
        nombre_proyecto, nombre_encontrado = pedir_proyecto(conn)

    desc = input("Introduzca una descripción para el proyecto: ")

    fecha_inicio, fecha_valida = pedir_fecha()
    while not fecha_valida:
        print("Error: Fecha inválida. Inténtelo de nuevo.")
        fecha_inicio, fecha_valida = pedir_fecha()

    fecha_fin, fecha_valida = pedir_fecha()
    while not fecha_valida:
        print("Error: Fecha inválida. Inténtelo de nuevo.")
        fecha_fin, fecha_valida = pedir_fecha()