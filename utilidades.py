import sqlite3

############################ Validaciones ############################

def validar_tlf() -> int:
    while True:
        try:
            nuevo_tlf = input("Introduzca el nuevo telefono de el cliente: ")
            if len(nuevo_tlf) != 9 and nuevo_tlf != "":
                print("Número inválido: Debe tener 9 dígitos, sin prefijo.")
            elif len(nuevo_tlf) == 9:
                nuevo_tlf = int(nuevo_tlf)
                break
            elif nuevo_tlf == "":
                break
        except ValueError:
            print("Error: El número de teléfono sólo debe contener números.")
        except Exception as e:
            print("Error inesperado: ", e)
    return nuevo_tlf


def validar_email() -> bool:
    while True:
        esta_bien = True
        email = input("Introduzca el nuevo email de el cliente: ")
        if "@" not in email:
            esta_bien = False
            print("Error: Falta un arroba (@) en el correo.")

        usuario, dominio = email.split("@", 1)
        if "." not in dominio:
            esta_bien = False
            print("Error: Falta un punto (.) en el correo.")

        if not usuario or not dominio:
            esta_bien = False
            print("Error: Alguna de las partes introducidas está vacía")
        
        if esta_bien:
            break

    return True

def validar_fecha(fecha: str) -> bool:
    try:
        ano, mes, dia = fecha.split('-')
        if fecha[4] != '-': # Separador
            return False
        if int(mes) > 12 or int(mes) < 1: # Mes
            print("Fallo en mes")
            return False
        if fecha[7] != '-': # Separador
            return False
        if int(dia) > 31 or int(dia) < 1: # Dia
            print("Fallo en dia")
            return False
        return True
    except ValueError:
        print("Error: La fecha es inválida: Sólo se permiten números y el separador '-'.")
    except Exception as e:
        print("Error: Se ha producido un error: ", e)
        

############################ Comprobar que existen ############################

def buscar_cliente(conexion: sqlite3.Connection, id_cliente: str) -> bool:
    try:
        cursor = conexion.cursor()
        contenido = cursor.execute(f'''
            SELECT * FROM Cliente WHERE id_cliente = "{id_cliente}"
        ''')
        datos = contenido.fetchall()
        if not datos:
            return False
        else:
            return True
    
    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print("Algo fue mal: ", e)
    
def buscar_empleado(conexion: sqlite3.Connection, id_empleado: str) -> bool:
    try:
        cursor = conexion.cursor()
        contenido = cursor.execute(f'''
            SELECT * FROM Empleado WHERE id_empleado = "{id_empleado}"
        ''')
        datos = contenido.fetchall()
        if not datos:
            return False
        else:
            return True
        
    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print("Algo fue mal: ", e)
    
def buscar_proyecto(conexion: sqlite3.Connection, id_proyecto: str) -> bool:
    try:
        cursor = conexion.cursor()
        contenido = cursor.execute(f'''
            SELECT * FROM Proyecto WHERE id_proyecto = {id_proyecto}
        ''')
        datos = contenido.fetchall()
        if not datos:
            return False
        else:
            return True
    
    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print("Algo fue mal: ", e)

def proyecto_repetido(conexion: sqlite3.Connection, nombre: str) -> bool:
    try:
        cursor = conexion.cursor()
        contenido = cursor.execute(f'''
            SELECT * FROM Proyecto WHERE titulo_proyecto = '{nombre}'
        ''')
        datos = contenido.fetchall()
        if not datos:
            return True
        else:
            return False
    
    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print("Algo fue mal: ", e)