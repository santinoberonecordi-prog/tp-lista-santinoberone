def agregar_nota(notas, nueva_nota):
    notas.append(nueva_nota)

def ver_notas (notas):
    if not notas:
        print("No hay notas registradas")
        return
    else:
        for i in range(len(notas)):
            print(" Nota", i + 1, ":" ,notas[i])

def calcular_promedio(notas):
    if not notas:
        return None
    suma = 0 
    cant = 0
    for nota in notas:
        suma += nota
        cant += 1
    return suma / cant

def buscar_mayor(notas):
    if not notas:
        return None
    mayor = notas[0]
    for nota in notas:
        if nota > mayor:
            mayor = nota
    return mayor

def calcular_media(notas):
    if not notas:
        return None
    notas_ordenadas = []
    for nota in notas:
        notas_ordenadas.append(nota)

    n = len(notas_ordenadas)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if notas_ordenadas[j] < notas_ordenadas[indice_minimo]:
                indice_minimo = j
        aux = notas_ordenadas[i]
        notas_ordenadas[i] = notas_ordenadas[indice_minimo]
        notas_ordenadas[indice_minimo] = aux
    if n % 2 != 0:
        return notas_ordenadas[n // 2]
    else:
        mitad1 = notas_ordenadas[(n // 2) - 1]
        mitad2 = notas_ordenadas[n // 2]
        return (mitad1 + mitad2) / 2

def obtener_impares(notas):
    impares = []
    for nota in notas:
        if nota % 2 != 0:
            impares.append(nota)
    return impares
        