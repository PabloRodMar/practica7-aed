import sqlite3
import utilidades

def actualizar(conn: sqlite3.Connection, tipo: str, id: str) -> None:
    try:
        cursor = conn.cursor()
        if tipo == "c":
            contenido = cursor.execute(f'''
                SELECT * FROM Cliente WHERE id_cliente = "{id}"
            ''')
            datos = contenido.fetchone()
            nuevo_nombre = input("Introduzca el nuevo nombre de el cliente: ")
            nuevo_tlf = utilidades.validar_tlf()
            nuevo_email = utilidades.validar_email()
            if not nuevo_nombre:
                nuevo_nombre = datos[1]
            if not nuevo_tlf:
                nuevo_tlf = datos[2]
            if not nuevo_email:
                nuevo_email = datos[3]
            cursor.execute(f'''
                UPDATE Cliente 
                SET nombre_cliente = '{nuevo_nombre}', tlf_cliente = '{nuevo_tlf}', email_cliente = '{nuevo_email}'
                WHERE id_cliente = '{id}';
            ''')
            conn.commit()
            print(f"Cambios realizados: {cursor.rowcount}")
        elif tipo == "e":
            contenido = cursor.execute(f'''
                SELECT * FROM Empleado WHERE id_empleado = "{id}"
            ''')
            datos = contenido.fetchone()
            nuevo_puesto =  input("Introduzca el nuevo puesto del empleado: ")
            if not nuevo_puesto:
                nuevo_puesto = datos[2]
            cursor.execute(f'''
                UPDATE Empleado 
                SET puesto = '{nuevo_puesto}'
                WHERE id_empleado = '{id}';
            ''')
            conn.commit()
            print(f"Cambios realizados: {cursor.rowcount}")
        elif tipo == "p":
            contenido = cursor.execute(f'''
                SELECT * FROM Proyecto WHERE id_proyecto = "{id}"
            ''')
            datos = contenido.fetchone()
            while True:
                try:
                    nuevo_presupuesto = float(input("Introduzca el nuevo presupuesto de el proyecto: "))
                    break
                except ValueError:
                    print("Error: Introduzca un número válido")
            if not nuevo_presupuesto:
                nuevo_presupuesto = datos[7]
            cursor.execute(f'''
                UPDATE Proyecto 
                SET presupuesto = '{nuevo_presupuesto}'
                WHERE id_proyecto = '{id}';
            ''')
            conn.commit()
            print(f"Cambios realizados: {cursor.rowcount}")
    
    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print("Algo fue mal: ", e)
        