from kiosco import*

mi_kiosco = Kiosco("Merkiosco", "Bv. Los tranzas")


while True:
    print("1) Ver info")
    print("2) Ver productos")
    print("3) Ingresar producto")    
    op = int(input("Ingrese una opcion"))

    if op == 1:
        mi_kiosco.getInfo()

    elif op == 2:
        mi_kiosco.getProductos()

    elif op == 3:
        mi_kiosco.setProductos(input("Ingrese un producto"))

    else:
        break