import sqlite3

def eliminar(conn: sqlite3.Connection, id_emp: str, id_pro: int):
    try:
        cursor = conn.cursor()
        cursor.execute(f'''
                DELETE FROM EmpleadosProyecto WHERE id_empleado = '{id_emp}' AND id_proyecto = {id_pro};
            ''')
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print("Algo fue mal: ", e)