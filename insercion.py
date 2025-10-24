import sqlite3

def insertar(conn: sqlite3.Connection):
    try:
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO Cliente (id_cliente, nombre_cliente, tlf_cliente, email_cliente) VALUES
        ('12345678A', 'María López', 612345678, 'maria.lopez@example.com'),
        ('87654321B', 'Juan Pérez', 698765432, 'juan.perez@example.com'),
        ('11223344C', 'Empresa Innovatech S.L.', 934567890, 'contacto@innovatech.es');
        ''')

        cursor.execute('''
        INSERT INTO Empleado (id_empleado, nombre_empleado, puesto, email_empleado) VALUES
        ('99887766D', 'Laura Gómez', 'Jefa de Proyecto', 'laura.gomez@empresa.com'),
        ('88776655E', 'Carlos Ruiz', 'Desarrollador', 'carlos.ruiz@empresa.com'),
        ('77665544F', 'Ana Torres', 'Diseñadora UX', 'ana.torres@empresa.com'),
        ('66554433G', 'Pedro Sánchez', 'Analista de Datos', 'pedro.sanchez@empresa.com');
        ''')
        
        cursor.execute('''
        INSERT INTO Proyecto (id_cliente, id_jefe_proyecto, titulo_proyecto, descripcion, fecha_inicio, fecha_fin, presupuesto) VALUES
        ('12345678A', '99887766D', 'App de Gestión Escolar', 'Desarrollo de una aplicación móvil para la gestión de centros educativos.', '2025-01-10', '2025-07-20', 35000.00),
        ('87654321B', '99887766D', 'Web Corporativa', 'Rediseño completo del sitio web de la empresa.', '2025-03-01', '2025-06-30', 18000.00),
        ('11223344C', '99887766D', 'Plataforma IoT', 'Desarrollo de plataforma de control para dispositivos inteligentes.', '2025-02-15', '2025-09-30', 60000.00),
        ('12345678A', '99887766D', 'App de Gestión de Cosas', 'Desarrollo de una aplicación móvil para la gestión de centros educativos.', '2025-01-10', '2025-07-20', 3000.00);
        ''')

        cursor.execute('''
        INSERT INTO EmpleadosProyecto (id_empleado, id_proyecto) VALUES
        ('88776655E', 1),
        ('77665544F', 1),
        ('66554433G', 1),
        ('88776655E', 2),
        ('77665544F', 2),
        ('88776655E', 3),
        ('66554433G', 3);
        ''')

        conn.commit()
    except sqlite3.IntegrityError:
        print("No se ha podido insertar en la base de datos: Los datos insertados ya existen.")
        
    except sqlite3.OperationalError as e:
        print(f"Error de operación en SQLite: {e}")

    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")

    except Exception as e:
        print("Error inesperado: ", e)