import sqlite3

def crearTablas(conn: sqlite3.Connection):
    try:
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cliente (
            id_cliente TEXT PRIMARY KEY,
            nombre_cliente TEXT NOT NULL,
            tlf_cliente INTEGER NOT NULL UNIQUE,
            email_cliente TEXT NOT NULL UNIQUE
        )           
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Empleado (
            id_empleado TEXT PRIMARY KEY,
            nombre_empleado TEXT NOT NULL,
            puesto TEXT NOT NULL,
            email_empleado TEXT NOT NULL UNIQUE
        )           
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Proyecto (
            id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente TEXT,
            id_jefe_proyecto TEXT,
            titulo_proyecto TEXT NOT NULL,
            descripcion TEXT,
            fecha_inicio DATE NOT NULL,
            fecha_fin DATE NOT NULL,
            presupuesto FLOAT NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente),
            FOREIGN KEY (id_jefe_proyecto) REFERENCES Empleado (id_empleado)
        )    
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS EmpleadosProyecto (
            id_empleado TEXT NOT NULL,
            id_proyecto INTEGER NOT NULL,
            PRIMARY KEY (id_empleado, id_proyecto),
            FOREIGN KEY (id_empleado) REFERENCES Empleado (id_empleado),
            FOREIGN KEY (id_proyecto) REFERENCES Proyecto (id_proyecto)
        )           
        ''')

        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")

    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")

    except Exception as e:
        print("No se ha podido crear la base de datos: ", e)