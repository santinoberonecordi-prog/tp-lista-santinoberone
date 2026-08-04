from nota import*

def mostrar_menu():
    print("1) Agregar nota")
    print("2) Ver notas")
    print("3) Calcular promedio")
    print("4) Buscar mayor")
    print("5) Calcular media")
    print("6) Ordenar notas")
    print("7) Salir")

def main(): 
    notas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            try:
                nueva_nota = float(input("Ingrese la nueva nota que deseas agregar? ")) 
                if nueva_nota < 0 or nueva_nota > 10:
                    print("Nota no valida ")
                else:
                    agregar_nota(notas, nueva_nota)
                    print("Nota", nueva_nota, "agregada correctamente")
            except ValueError:
                print("Ingrese un numero valido")
        elif opcion == "2":
            ver_notas(notas)
        elif opcion == "3":
            promedio = calcular_promedio(notas)
            if promedio is None:
                print("No hay notas registradas")
            else: 
                print("El promedio de las notas es: ",round(promedio, 2))
        elif opcion == "4":
            mayor = buscar_mayor(notas)
            if mayor is None:
                print("No hay notas registradas")
            else:
                print("La nota mayor es:", mayor)
        elif opcion == "5":
            media = calcular_media(notas)
            if media is None:
                print("No hay notas registradas")
            else:
                print("La media es:", round(media, 2))
        elif opcion == "6":
            impares = obtener_impares(notas)
            ver_notas(impares)
        elif opcion == "7":
            print("Saliste!")
            break
        else:
            print("Dato incorrecto")
if __name__ == "__main__":
    main()