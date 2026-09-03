from notas import*

lista = []

def menu():
    print()
    print()
    print("1) Crear estudiante")
    print("2) Listar estudiante")
    print("3) Ingresar nota")
    print("4) Calcular promedio")
    print("5) Ingresar materia")
    print("6) Mostrar materias cursadas de un estudiante")
    print("7) Salir")
    print()
    print()



while True:
    menu()
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        legajo = len(lista) + 1000
        nombre = input("Ingrese nombre: ")
        curso = input("Ingrese curso: ")
        estudiante = crear_estudiante(nombre,curso,legajo,[],[])
        lista.append(estudiante.copy())
    elif op == 2:
        listar_estudiantes(lista)
    elif op == 3:
        listar_nombres(lista)
        id = int(input("Ingrese el ID: "))
        nota = int(input("Ingrese la nota: "))
        posicion = id - 1000
        lista[id]["notas"].append(nota)
    elif op == 4:
        listar_nombres(lista)
        id = int(input("Ingrese el id: "))
        promedio = calcular_promedio_temperatura(lista[id]["notas"])
        print("El promedio es:", promedio)
    elif op == 5:
        listar_nombres(lista)
        id = int(input("Ingrese el id de la persona: "))
        materia = input("Ingrese la materia que deseas agregar: ")
        lista[id]["materias"].append(materia)
        print("Materia ingresada con exito")
    elif op == 6:
        listar_nombres(lista)
        id = int(input("Ingrese el id de la persona: "))
        listar_materias_estudiantes(lista[id])
    elif op == 7:
        print("Saliste")
        break 
    else:
        print("Opcion incorrecta")
