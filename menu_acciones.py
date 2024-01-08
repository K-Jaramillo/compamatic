from acciones_mouse import *

#MENU_ACCIONES

def programar_acciones():
    while True:
        print("\nMenú Programar Acciones:")
        print("1. Programar acciones para el mouse")
        print("2. Programar acciones para el teclado")
        print("3. Volver al menú principal")

        opcion_dispositivo = input("Seleccione un dispositivo (1/2/3): ")

        if opcion_dispositivo == "1":
            programar_acciones_mouse()
        elif opcion_dispositivo == "2":
            programar_acciones_teclado()
        elif opcion_dispositivo == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

#MENÚ_MOUSE
            
def programar_acciones_mouse():
    while True:
        print("\nMenú Programar Acciones para el Mouse:")
        print("1. Programar clic derecho")
        print("2. Programar clic izquierdo")
        print("3. Programar clic derecho sostenido por segundos")
        print("4. Programar clic izquierdo sostenido por segundos")
        print("5. Programar scroll hacia arriba")
        print("6. Programar scroll hacia abajo")
        print("7. Volver al menú anterior")

        opcion_accion_mouse = input("Seleccione una acción para el mouse (1/2/3/4/5/6/7): ")

        if opcion_accion_mouse == "1":
            clic_derecho()
        elif opcion_accion_mouse == "2":
            clic_izquierdo()
        elif opcion_accion_mouse == "3":
            clic_derecho_sostenido()
        elif opcion_accion_mouse == "4":
            clic_izquierdo_sostenido()
        elif opcion_accion_mouse == "5":
            programar_scroll_arriba()
        elif opcion_accion_mouse == "6":
            programar_scroll_abajo()
        elif opcion_accion_mouse == "7":
            print("Volviendo al menú anterior.")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2, 3, 4, 5, 6 o 7.")

#FUNCIONES_DE_MOUSE

def clic_derecho():
    print("Programando clic derecho...")

def clic_izquierdo():
    print("Programando clic izquierdo...")

def clic_derecho_sostenido():
    duracion = float(input("Ingrese la duración del clic derecho sostenido en segundos: "))
    print(f"Programando clic derecho sostenido por {duracion} segundos...")

def clic_izquierdo_sostenido():
    duracion = float(input("Ingrese la duración del clic izquierdo sostenido en segundos: "))
    print(f"Programando clic izquierdo sostenido por {duracion} segundos...")

def programar_scroll_arriba():
    magnitud = int(input("Ingrese la magnitud del scroll hacia arriba: "))
    print(f"Programando scroll hacia arriba con magnitud {magnitud}...")

def programar_scroll_abajo():
    magnitud = int(input("Ingrese la magnitud del scroll hacia abajo: "))
    print(f"Programando scroll hacia abajo con magnitud {magnitud}...")

# MENU_TELCADO
def programar_acciones_teclado():
    while True:
        print("\nMenú Programar Acciones para el Teclado:")
        print("1. Programar pulsación de una tecla")
        print("2. Programar combinación de teclas")
        print("3. Programar escribir texto")
        print("4. Volver al menú anterior")

        opcion_accion_teclado = input("Seleccione una acción para el teclado (1/2/3/4): ")

        if opcion_accion_teclado == "1":
            programar_pulsacion_tecla()
        elif opcion_accion_teclado == "2":
            programar_combinacion_teclas()
        elif opcion_accion_teclado == "3":
            programar_escribir_texto()
        elif opcion_accion_teclado == "4":
            print("Volviendo al menú anterior.")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2, 3 o 4.")

#  FUNCIONES_DE_TECLADO
            
def programar_pulsacion_tecla():
    tecla = input("Ingrese la tecla a programar: ")
    print(f"Programando pulsación de la tecla {tecla}...")

def programar_combinacion_teclas():
    combinacion = input("Ingrese la combinación de teclas a programar (separadas por espacios): ")
    print(f"Programando combinación de teclas {combinacion}...")     

def programar_escribir_texto():
    texto = input("Ingrese el texto a programar: ")
    print(f"Programando escribir el texto: {texto}")
