class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.habilitados = []
        self.deshabilitados = []   

    def getInfo(self):
        print("La marca es: ", self.marca)
        print("El modelo es: ", self.modelo)
        print("El año es: ", self.año)

    def getconductores(self):
        for cond in self.habilitados:
            print("-", cond, "habilitado")
        for con in self.deshabilitados:
            print("-", con, "deshabilitado")

    def sethab(self, conductores):
        self.habilitados.append(conductores)

    def setdeshab(self, conductores):
        self.deshabilitados.append(conductores)