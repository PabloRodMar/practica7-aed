import conexion, mostrar, insercion, tablas, utilidades, crud_proyectos
import os

def menu() -> int:

    print("Base de datos de una empresa cualquiera.")
    print("1. Insertar proyecto.")
    print("2. Eliminar proyecto.")
    print("3. Transferir proyecto.")
    print("0. Salir\n")

    while True:
        try:
            op = int(input("Escoja una opción: "))
            if op in [0, 1, 2, 3]:
                break
            print("Opción inválida: Debe de introducirse un número del 0 al 3")
        except ValueError:
            print("Error: El valor introducido debe ser un número entre 0 y 3")
        except Exception as e:
            print("Error inesperado: ", e)
    return op


if __name__ == '__main__':
    conexion_bd = conexion.conectar_bd()
    if os.path.getsize("base_datos/practica5.db") == 0:
        tablas.crearTablas(conexion_bd)
        insercion.insertar(conexion_bd)
    while True:
        op_menu = menu()
        match op_menu:

            case 0:
                exit()

            case 1:
                os.system('cls')

                crud_proyectos.registrar_proyecto(conexion_bd)

                input("Pulse ENTER para continuar")
                os.system('cls')

            case 2:
                os.system('cls')

                crud_proyectos.eliminar_proyecto(conexion_bd)

                input("Pulse ENTER para continuar")
                os.system('cls')

            case 3:
                os.system('cls')

                crud_proyectos.transferir_proyecto(conexion_bd)

                input("Pulse ENTER para continuar")
                os.system('cls')