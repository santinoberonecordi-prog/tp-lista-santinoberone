def agregar_temperatura(lista):
    temp = float(input("Ingrese la temperatura que deseas agregar: "))
    lista.append(temp)
    print("Temperatura agregada")

def ver_temperaturas(lista):
    if len(lista) == 0:
        print("No hay temperaturas registradas")
    else:
        for temp in lista:
            print(temp)

def calcular_promedio_temperatura(lista):
    if len(lista) == 0:
        print("No hay temperaturas registradas para promediar")
    else:
        suma = 0
        for temp in lista:
            suma = suma + temp
            promedio = suma / len(lista)
            print("El promedio es: ", promedio)

def buscar_mayor(lista):
    if len(lista) == 0:
        print("No hay temperaturas registradas")
    else:
        mayor = lista[0]
        for temp in lista:
            if temp > mayor:
                mayor = temp
        print("La temperatura mayor es: ", mayor)

def buscar_menor(lista):
    if len(lista) == 0:
        print("No hay temperaturas registradas")
    else: 
        menor = lista[0]
        for temp in lista:
            if temp < menor:
                menor = temp
        print("La temperatura menor es:", menor)

def contar_temperatura(lista):
    if len(lista) == 0:
        print("No hay temperaturas registradas")
    else: 
        buscar = float(input("Ingrese la temperatura que deseas contar: "))
        contador = 0
        for temp in lista:
            if temp == buscar:
                contador = contador + 1
        print("La temperatura", buscar, "se repite", contador, "veces")

def ordenar_burbuja(lista):
    if len(lista) == 0:
        print("No hay temperaturas registradas")
    else:
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i -1):
                if lista[j] > lista[j + 1]:
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux
        print("Lista ordenada correctamente")