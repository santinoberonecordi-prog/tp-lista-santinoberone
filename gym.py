class Gym:
    def __init__(self, nombre, edad, num_tel, membresia):
        self.nombre = nombre
        self.edad = edad
        self.num_tel = num_tel
        self.membresia = membresia

    def getInfo(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Telefono: ", self.num_tel)
        print("Membresia: ", self.membresia)

    def actualizar_telefono(self, nuevo_tel):
        self.num_tel = nuevo_tel

    def cambiar_membresia(self, nueva_membresia):
        self.membresia = nueva_membresia