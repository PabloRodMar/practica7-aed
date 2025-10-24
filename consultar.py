import sqlite3

def consultar(conn: sqlite3.Connection, id: str, op_c: str):
    try:
        cursor = conn.cursor()
        if op_c == 'c':
            contenido = cursor.execute(f'''
                SELECT id_proyecto FROM Proyecto WHERE id_cliente = "{id}"
            ''')
            datos = contenido.fetchall()
            print(f"Proyectos en los que el cliente '{id}' ha solicitado: ")
            for proyectos in datos:
                print("\nProyecto con id:", proyectos[0])
            print()
        
        elif op_c == 'ep':
            contenido = cursor.execute(f'''
                SELECT id_empleado FROM EmpleadosProyecto WHERE id_proyecto = "{id}"
            ''')
            datos = contenido.fetchall()
            print(f"Empleados asignados en el proyecto con id: '{id}'")
            for proyectos in datos:
                print("\nEmpleado con id:", proyectos[0])
            print()
        
        elif op_c == 'todos':
            contenido = cursor.execute(f'''
                SELECT id_proyecto FROM EmpleadosProyecto WHERE id_empleado = "{id}"
            ''')
            datos = contenido.fetchall()
            print(f"Todos los proyectos en los que el empleado '{id}' ha participado: ")
            for proyectos in datos:
                print("\nProyecto con id:", proyectos[0])
            print()
    
    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print("Algo fue mal: ", e)
        