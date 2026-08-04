from temperatura import*

temperaturas= []

while True:
    print("1) Agregar temperaturas")
    print("2) Ver temperaturas")
    print("3) Calcular promedio")
    print("4) Buscar mayor")
    print("5) Buscar menor")
    print("6) Contar temperatura")
    print("7) Ordenar temperaturas")
    print("8) Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_temperatura(temperaturas)
    elif opcion == "2":
        ver_temperaturas(temperaturas)
    elif opcion == "3":
        calcular_promedio_temperatura(temperaturas)
    elif opcion == "4":
        buscar_mayor(temperaturas)
    elif opcion == "5":
        buscar_menor(temperaturas)
    elif opcion == "6":
        contar_temperatura(temperaturas)
    elif opcion == "7":
        ordenar_burbuja(temperaturas)
    elif opcion == "8":
        print("Programa finalizado")
        break
    else: print("Dato incorrecto")
