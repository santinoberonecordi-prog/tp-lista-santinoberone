class Kiosco:
    def __init__(self,nombre,direccion):
      self.nombre = nombre
      self.direccion = direccion
      self.lista_productos = []

    def getInfo(self):
       print("Kiosco: ", self.nombre)
       print("Direccion: ", self.direccion)

    def getProductos(self):
       for producto in self.lista_productos:
          print(producto)

    def setProductos(self, productos):
       self.lista_productos.append(productos)
       print("Producto: " + productos, "agregado")
       