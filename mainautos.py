from auto import*

auto = Auto("Toyota", "Supra 3000", "2026")

while True:
    print("1) Ver informacion")
    print("2) Ver conductores")
    print("3) Ingresar habilitados")
    print("4) Ingresar deshabilitados")
    print("5) Salir")

    op = int(input("Ingrese una opcion: "))

    if op == 1:
        auto.getInfo()

    elif op == 2:
        auto.getconductores()

    elif op == 3:
        nombre = input("Ingresa un nombre: ")
        auto.sethab(nombre)

    elif op == 4:
        nombre = input("Ingresa un nombre: ")
        auto.setdeshab(nombre)

    elif op == 5:
        break

    else: 
        print("No elegiste ninguna opcion fraca")