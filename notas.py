lista = []
def crear_estudiante(nombre, curso, legajo, notas, materias):
    dic = {"nombre" : nombre,
               "legajo" : legajo,
               "notas" : notas,
               "curso" : curso,
               "materias" : materias
}
    print("Estudiante creado")
    mostrar_diccionario(dic)
    return dic

def listar_estudiantes(lista:list):
    if len(lista) == 0:
        print("No hay estudiantes")
    else:
        cont = 0
        for elem in lista:
            print("Id: ", cont)
            mostrar_diccionario(elem)
            cont += 1
       

def listar_nombres(lista):
    if len(lista) == 0:
            print("No hay estudiantes")
    else:
        cont = 0
        for elem in lista:
            print("Id: ", cont, "nombre: ", elem["nombre"])
            cont += 1

def calcular_promedio_temperatura(lista):
    if len(lista) == 0:
        print("No hay notas registradas para promediar")
    else:
        suma = 0
        for temp in lista:
            suma = suma + temp
            promedio = suma / len(lista)
            print("El promedio es: ", promedio)
        return promedio    

def mostrar_diccionario(dic:dict):
    print("Legajo: ", dic["legajo"])
    print("Nombre: ", dic["nombre"])
    print("Curso: ", dic["curso"])
    if len(dic["notas"]) == 0:
        print("No hay notas registradas")
    else:
        print("Notas:")
        cont = 1
        for notas in dic["notas"]:
            print("Nota",cont,":", notas)
            cont += 1
    if "materias" not in dic or len(dic["materias"]) == 0:
            print("No hay materias registradas")
    else:
        print("Materias: ")
        cont = 1
        for mat in dic["materias"]:
            print("Materia",cont,":", mat)
            cont += 1        

def listar_materias_estudiantes(dic):
    print("Nombre: ", dic["nombre"])
    if len(dic["materias"]) == 0:
        print("No hay materias registradas")
    else:
        print("Materias cursadas: ")
        for materia in dic["materias"]:
            print("-", materia)
            