from juego import*
from funcionesjuego import*

personaje = generar_personaje

while True:

    opcion = menu()

    if opcion == 1:
        mostrar_personaje
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        break
    else:
        print("Escribi una opcion")