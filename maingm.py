from gym import*

def validar_telefono():
    while True:

        telefono = int(input("Ingrese tu numero de telefono"))
        if len(telefono) < 10:
            print("Telefono incorrecto crack")
        
        es_valido = True
        for caracter in telefono:
            if caracter not in "0123456789":
                es_valido = False
                break
        if es_valido:
            return telefono
        else:
            print("El telefono ddebe tener numeros nomas boludin")

def menu_principal():
    cliente_actual = None

    while True:
        print("1) Registrar nuevo cliente")
        print("2) Consultar informacion del cliente")
        print("3) Actualizar numero de telefono")
        print("4) Cambiar tipo de membresia")
        print("5) Salir")

        opcion = int(input("Ingrese una opcion"))

        if opcion == 1:
            if cliente_actual is not None:
                print("Ya tenes un cliente anotado se van a borrar los datos")

            nombre = input("Ingrese el nombre ")

            while True:
                edad_str = input("Ingrese la edad del cliente: ")
                edad_valida = True
                if len(edad_str) == 0:
                    edad_valida = False

                else: 
                    for c in edad_str:
                        if c not in "0123456789":
                            edad_valida = False
                            break

                if edad_valida:
                    edad = int(edad_str)
                    if edad > 0:
                        break
                    else:
                        print("Tenes que ingresar un numero valido")
            
            telefono = validar_telefono()

            print("Selecciona tu tipo de membresia")
            print("1) Mensual")
            print("2) Trimestral")
            print("3) Anual")

            while True:
                opc_m = int(input("Ingerese una opcion")) 

                if opc_m == 1:
                    