from acciones_mouse import *
from menu_acciones import programar_acciones

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Programar nuevas acciones")
        print("2. Ejecutar acciones grabadas")
        print("3. Salir")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            programar_acciones()
        elif opcion == "2":
            print("Ejecutando presets")
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")


# Llamamos a la función del menú principal para iniciar el programa
menu_principal()
