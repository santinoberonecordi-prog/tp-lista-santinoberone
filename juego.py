import random

vida_max = 100 

personaje_principal = {
    "nombre" : "",
    "vida maxima": vida_max,
    "vida actual" : vida_max,
    "fuerza" : 0,
    "suerte" : 0,
    "monedas" : 0,
    "porciones" : 0,
    "arma" : {},
    "armadura" : {},
}

if personaje_principal["monedas"] >= 3000:
    personaje_principal["monedas"] -= 3000
elif personaje_principal["monedas"] < 3000:
    print("pobre")
else:
    print("error")

armas = {
    "espada" : {
        "dano" : 40,
        "critico" : 90,
        "precio" : 1200,
    },
    "arco" : {
        "dano" : 20,
        "critico" : 70,
        "precio" : 800,
    }
}

print(personaje_principal)
personaje_principal["arma"] = armas["espada"]
print("")
print(personaje_principal)
print("el ultimo sesenta abajo!!")
print(personaje_principal["arma"]["dano"])

armaduras = {
    "casco" : {
        "resistencia" : 120,
        "precio" : 2000,
    },
    "chaleco" : {
        "resistencia" : 80,
        "precio" : 1500,
    }
}

enemigos = {
    "ciruja" : {
        "vida" : 10,
        "dano" : 20,
        "tesoro" : 50,
    },
    "zombie" : {
        "vida" : 10,
        "dano" : 20,
        "tesoro" : 50,
    }
}

def generar_personaje(nombre):
    global personaje_principal
    personaje = personaje_principal.copy()
    personaje["nombre"] = nombre
    personaje["fuerza"] = random.randint(1, 100)
    personaje["suerte"] = random.randint(1, 100)

    return personaje

def mostrar_personaje(personaje:dict):
    print("nombre: ", personaje["nombre"])
    print("vida: ", personaje["vida_actual"], "/", personaje["vida_max"])
    print("fuerza: ", personaje["fuerza"], "suerte: ", personaje["suerte"])
    print("monedas: ", personaje["monedas"])
    print("porciones: ", personaje["porciones"])
    print("arma: ")
    mostrar_arma(personaje["arma"])
    print("armadura: ")
    mostrar_armadura(personaje["armadura"])
    if personaje["arma"] != {}:
        print("Arma: ")
        mostrar_arma
    if personaje["armadura"] != {}:
        print("Armadura: ")
        mostrar_armadura

def mostrar_arma(arma:dict):
    print("Daño: ",arma["dano"])
    print("Daño critico: ", arma["critico"])
    print("precio: ", arma["precio"])

def mostrar_armadura(armadura:dict):
    print("resistencia",armadura["resistencia"])
    print("Precio: ", armadura["precio"])