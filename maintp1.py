from tp1 import*

lista_perros= []

def menu():
    print("1) Crear perro")
    print("2) Listar perros")
    print("3) Consultar etapa de vida de un perro")
    print("4) Ingresar dueño a la lista")
    print("5) Ver lista de dueños de un perro")
    print("6) Salir")

while True:
    menu()

    op = int(input("Ingrese una opción: "))

    if op == 1:
        nombre = input("Ingrese el nombre el perro que deseas agregar: ")
        raza = input("Ingrese la raza del perro: ")
        edad = int(input("Ingrese la edad del perro: "))
        perro = crear_perro(nombre, raza, edad)
        lista_perros.append(perro.copy())

    elif op == 2:
        listar_perro(lista_perros)

    elif op == 3:
        listar_nombres_perros(lista_perros)
        id = int(input("Ingrese el ID del perro: "))
        etapa = etapa_vida(lista_perros[id]["edad"])
        print("El perro", lista_perros[id]["nombre"],"es un", etapa)

    elif op == 4:
        listar_nombres_perros(lista_perros)
        id = int(input("Ingrese el ID del perro: "))
        nuevo_dueno = input("Ingrese el nombre del dueño: ")
        lista_perros[id]["dueños"].append(nuevo_dueno)
        print("Dueño ingresado correctamente")

    elif op == 5:
        listar_nombres_perros(lista_perros)
        id = int(input("Ingrese el ID del perro: "))
        print("Dueños registrados de",lista_perros[id]["nombre"], ":" )
        if len(lista_perros[id]["dueños"]) == 0:
            print("No tiene dueños ingresados")
        else:
            for dueno in lista_perros[id]["dueños"]:
                print("-", dueno)

    elif op == 6:
        print("saliste")
        break

    else:
        print("Opción errónea")