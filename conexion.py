import sqlite3

def conectar_bd():
    try:
        conn = sqlite3.connect('base_datos/practica5.db')
    except Exception as e:
        print(f"Error: No se ha establecido la conexión: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    return conn