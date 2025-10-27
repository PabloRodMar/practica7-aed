import conexion, actualizar, mostrar, consultar, insercion, tablas, eliminar, utilidades
import os

def menu() -> int:

    print("Base de datos de una empresa cualquiera.")
    print("\n1. Actualizar datos de un cliente o empleado.")
    print("2. Cambiar presupuesto de un proyecto.")
    print("3. Consultar proyectos de un cliente.")
    print("4. Consultar empleados de un proyecto.")
    print("5. Consultar proyectos de un empleado.")
    print("6. Eliminar un empleado de un proyecto")
    print("7. Consultar todo (propósito para comprobar que los datos se están cambiando bien, por eso es tan cutre)")
    print("0. Salir\n")

    while True:
        try:
            op = int(input("Escoja una opción: "))
            if op in [0, 1, 2, 3, 4, 5, 6, 7]:
                break
            print("Opción inválida: Debe de introducirse un número del 0 al 3")
        except ValueError:
            print("Error: El valor introducido debe ser un número entre 0 y 2")
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
                while True:
                    os.system('cls')
                    op_act = input("¿Quiere actualizar un cliente o un empleado? (c/e): ")
                    if op_act.lower() in ['c', 'e']:
                        break
                    print("Opción inválida: Introduzca 'c' o 'e'.")

                if op_act == "c":
                    mostrar.consultar_clientes(conexion_bd)
                    id_act = input("Introduzca el id de el cliente: ")
                    while not utilidades.buscar_cliente(conexion_bd, id_act):
                        print("Error: ID de el cliente no encontrado.")
                        id_act = input("Introduzca el id de el proyecto: ")

                else:
                    mostrar.consultar_empleados(conexion_bd)
                    id_act = input("Introduzca el id de el empleado: ")
                    while not utilidades.buscar_empleado(conexion_bd, id_act):
                        print("Error: ID de el empleado no encontrado.")
                        id_act = input("Introduzca el id de el empleado: ")

                actualizar.actualizar(conexion_bd, op_act, id_act)

                input("Pulse ENTER para continuar")
                os.system('cls')

            case 2:
                os.system('cls')
                mostrar.consultar_proyectos(conexion_bd)
                id_pro = input("Introduzca el id de el proyecto: ")
                while not utilidades.buscar_proyecto(conexion_bd, id_pro):
                    print("Error: ID de proyecto no encontrado.")
                    id_pro = input("Introduzca el id de el proyecto: ")

                actualizar.actualizar(conexion_bd, 'p', id_pro)

                input("Pulse ENTER para continuar")
                os.system('cls')

            case 3:
                os.system('cls')
                mostrar.consultar_clientes(conexion_bd)
                id_cli = input("Introduzca el id de el cliente: ")
                while not utilidades.buscar_cliente(conexion_bd, id_cli):
                    print("Error: ID de el cliente no encontrado.")
                    id_cli = input("Introduzca el id de el proyecto: ")
                
                consultar.consultar(conexion_bd, id_cli, 'c')

                input("Pulse ENTER para continuar")
                os.system('cls')

            case 4:
                os.system('cls')
                mostrar.consultar_proyectos(conexion_bd)
                id_pro_emp = input("Introduzca el id de el proyecto: ")
                while not utilidades.buscar_proyecto(conexion_bd, id_pro_emp):
                    print("Error: ID de proyecto no encontrado.")
                    id_pro_emp = input("Introduzca el id de el proyecto: ")

                consultar.consultar(conexion_bd, id_pro_emp, 'ep')

                input("Pulse ENTER para continuar")
                os.system('cls')

            case 5:
                os.system('cls')
                mostrar.consultar_empleados(conexion_bd)
                id_todos = input("Introduzca el id de el empleado: ")
                while not utilidades.buscar_empleado(conexion_bd, id_todos):
                    print("Error: ID de el empleado no encontrado.")
                    id_todos = input("Introduzca el id de el empleado: ")

                consultar.consultar(conexion_bd, id_todos, 'todos')
                
                input("Pulse ENTER para continuar")
                os.system('cls')

            case 6:
                os.system('cls')
                mostrar.consultar_empleados(conexion_bd)
                mostrar.consultar_proyectos(conexion_bd)

                id_empleado = input("Introduzca el id de el empleado: ")
                while not utilidades.buscar_empleado(conexion_bd, id_empleado):
                    print("Error: ID de el empleado no encontrado.")
                    id_empleado = input("Introduzca el id de el empleado: ")
                
                id_proyecto = input("Introduzca el id de el proyecto: ")
                while not utilidades.buscar_proyecto(conexion_bd, id_proyecto):
                    print("Error: ID de proyecto no encontrado.")
                    id_proyecto = input("Introduzca el id de el proyecto: ")

                eliminar.eliminar(conexion_bd, id_empleado, id_proyecto)

                input("Pulse ENTER para continuar")
                os.system('cls')
            
            case 7:
                os.system('cls')
                mostrar.consultar_todo(conexion_bd)
                input("Pulse ENTER para continuar")
                os.system('cls')