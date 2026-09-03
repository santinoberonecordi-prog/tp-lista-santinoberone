def crear_perro(nombre, raza, edad):

    dic = {
        "nombre": nombre,
        "raza": raza,
        "edad": edad,
        "dueños": []
    }
    print("Perro registrado con exito")
    mostrar_perro(dic)
    return dic

def listar_perro(lista):
    if len(lista) == 0:
            print("No hay perros registrados")
    else:
        cont = 0
        for perro in lista:
            print("Id: ", cont)
            mostrar_perro(perro)
            cont += 1

def listar_nombres_perros(lista):
    if len(lista) == 0:
            print("No hay perros registrados")
    else:
        cont = 0
        for perro in lista:
            print("Id: ", cont, "nombre: ", perro["nombre"])
            cont += 1

def etapa_vida(edad):
    if edad > 0 and edad <= 5:
        return "cachorro"
    elif edad > 5 and edad <= 8:
        return "joven"
    else: 
        return "adulto"

def mostrar_perro(dic:dict):
    print("Nombre: ", dic["nombre"])
    print("Raza: ", dic["raza"])
    print("Edad: ", dic["edad"])
    print("Etapa de vida: ", etapa_vida(dic["edad"]))
    if len(dic["dueños"]) == 0:
        print("No hay dueños registrados")
    else:
        print("Dueños: ")
        cont = 1
        for dueno in dic["dueños"]:
            print("", cont, ".", dueno)
            cont += 1
