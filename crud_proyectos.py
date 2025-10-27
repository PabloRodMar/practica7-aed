import sqlite3
import conexion, utilidades

######################## Funciones internas ########################

def pedir_cliente(conn: sqlite3.Connection, accion: str) -> str:
    if accion == 'solicitar':
        cliente = input("Introduzca el ID del cliente que solicita el proyecto: ")
    else:
        cliente = input("Introduzca el ID del cliente al que se va a transferir el proyecto: ")
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

def pedir_fecha(inicio_fin: str) -> str:
    if inicio_fin == "inicio":
        fecha = input("Introduzca la fecha de inicio de el proyecto: ")
    else:
        fecha = input("Introduzca la fecha de fin de el proyecto: ")
    fecha_valida = utilidades.validar_fecha(fecha)
    return fecha, fecha_valida

def pedir_presupuesto() -> float:
    while True:
        try:
            presupuesto = float(input("Introduzca el presupuesto del proyecto: "))
            break
        except Exception as e:
            print("Error: El valor introducido debe ser un número: ", e)
    return presupuesto

def agregar_empleados(conn: sqlite3.Connection) -> list:
    empleados = []
    while True:
        empleado = input("Introduzca el ID del empleado que se agregará al nuevo proyecto: (pulse enter para salir): ")
        if not empleado:
            break
        else:
            if utilidades.buscar_empleado(conn, empleado): # Si se encuentra
                empleados.append(empleado)
            else:
                print("Empleado no encontrado en la base de datos, vuelva a intentarlo.\n")
    return empleados

def permitir_proyecto(accion: str) -> int:
    while True:
        try:
            if accion == "eliminar":
                proyecto = input("Introduzca el proyecto que se va a eliminar: ")
            else:
                proyecto = input("Introduzca el proyecto que será transferido a otro cliente: ")
            if not proyecto:
                return
            proyecto = int(proyecto)
            break
        except ValueError:
            print("Error: El ID debe ser un número, de los mostrados anteriormente.")
    return proyecto

######################### Operaciones CRUD #########################

def registrar_proyecto(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()

    cliente, cli_encontrado = pedir_cliente(conn, 'solicitar')
    while not cli_encontrado:
        print("Error: El cliente no ha sido encontrado. Inténtelo de nuevo.")
        cliente, cli_encontrado = pedir_cliente(conn, 'solicitar')

    empleado, emp_encontrado = pedir_empleado(conn)
    while not emp_encontrado:
        print("Error: El empleado no ha sido encontrado. Inténtelo de nuevo.")
        empleado, emp_encontrado = pedir_empleado(conn)
    
    nombre_proyecto, nombre_encontrado = pedir_proyecto(conn)
    while not nombre_encontrado:
        print("Error: El nombre del proyecto ya está en uso. Introduzca otro.")
        nombre_proyecto, nombre_encontrado = pedir_proyecto(conn)

    desc = input("Introduzca una descripción para el proyecto: ")

    fecha_inicio, fecha_valida = pedir_fecha("inicio")
    while not fecha_valida:
        print("Error: Fecha inválida. Inténtelo de nuevo.")
        fecha_inicio, fecha_valida = pedir_fecha("inicio")

    fecha_fin, fecha_valida = pedir_fecha("fin")
    while not fecha_valida:
        print("Error: Fecha inválida. Inténtelo de nuevo.")
        fecha_fin, fecha_valida = pedir_fecha("fin")
    
    presupuesto = pedir_presupuesto()

    try:
        # No estoy seguro si es cursor o connection
        cursor.execute("BEGIN TRANSACTION;")

        # Ahora lo hago así porque Cristo me dijo que era más seguro
        cursor.execute(f'''INSERT INTO Proyecto (id_cliente, id_jefe_proyecto, titulo_proyecto, descripcion, fecha_inicio, fecha_fin, presupuesto) 
                           VALUES (?, ?, ?, ?, ?, ?, ?)''', (cliente, empleado, nombre_proyecto, desc, fecha_inicio, fecha_fin, presupuesto))
        
        conn.commit()
        print("Proyecto registrado correctamente.")

    except Exception as e:
        conn.rollback()
        print("Error: La transacción no se ha llevado acabo: ", e)
    
    empleados = agregar_empleados(conn)

    cursor.execute("SELECT MAX(id_proyecto) FROM Proyecto")
    ultimo_id = cursor.fetchone()[0]

    try:
        cursor.execute("BEGIN TRANSACTION;")

        for empleado in empleados:
            cursor.execute(f'''INSERT INTO EmpleadosProyecto (id_empleado, id_proyecto) VALUES (?, ?);''', (empleado, ultimo_id))
        
        conn.commit()
        print("Asignaciones de empleados registradas correctamente.")

    except Exception as e:
        conn.rollback()
        print("Error: La transacción no se ha llevado acabo: ", e)

###################### ELIMINAR ######################

def eliminar_proyecto(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()

    cursor.execute("SELECT id_proyecto FROM Proyecto")
    lista_proyectos = cursor.fetchall()
    # ¡¡FOR IMPLÍCITO!!
    # Explicación: Recorre todos los proyectos y guarda sólo las ids
    ids = [fila[0] for fila in lista_proyectos]

    print(f"Proyectos disponibles para ser eliminados: ", ids)

    proyecto = permitir_proyecto('eliminar')

    while True:
        if proyecto not in ids:
            print("ID inválida: Introduzca una ID válida de las mostradas.")
            proyecto = permitir_proyecto('eliminar')
        break

    try:
        cursor.execute("BEGIN TRANSACTION;")

        cursor.execute(f"DELETE FROM Proyecto WHERE id_proyecto = {proyecto};")
        cursor.execute(f"DELETE FROM EmpleadosProyecto WHERE id_proyecto = {proyecto};")

        conn.commit()
        print("Proyecto y empleados de este eliminados correctamente.")
    
    except Exception as e:
        conn.rollback()
        print("Error: La transacción no se ha llevado acabo: ", e)

###################### TRANSFERIR ######################

def transferir_proyecto(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()

    cursor.execute("SELECT id_proyecto FROM Proyecto")
    lista_proyectos = cursor.fetchall()
    ids = [fila[0] for fila in lista_proyectos]

    print(f"Proyectos disponibles: ", ids)

    proyecto = permitir_proyecto('actualizar')

    while True:
        if proyecto not in ids:
            print("ID inválida: Introduzca una ID válida de las mostradas.")
            proyecto = permitir_proyecto('actualizar')
        break

    cliente, cli_encontrado = pedir_cliente(conn, 'transferir')
    while not cli_encontrado:
        print("Error: El cliente no ha sido encontrado. Inténtelo de nuevo.")
        cliente, cli_encontrado = pedir_cliente(conn, 'transferir')
    
    try:
        cursor.execute("BEGIN TRANSACTION;")

        cursor.execute(f'''UPDATE Proyecto SET id_cliente = '{cliente}' WHERE id_proyecto = {proyecto};''')

        conn.commit()
        print(f"Proyecto transferido al cliente '{cliente}' de manera correcta.")
    
    except Exception as e:
        conn.rollback()
        print("Error: La transacción no se ha llevado acabo: ", e)