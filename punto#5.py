#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio

print (" ")
print ("Torres Olvera Gael")
print (" ")


#Definiendo variables
class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas=llantas
        self._color=color
        self._precio=precio


#Solicitando datos del tester
class Moto(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))

#Solicitando datos del tester
class Carro(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))

    print("OBJETO = moto")

#Solcitando mas datos
moto=Moto(2, str(input("Ingresa el color deseado: ")), "$200")
moto.cantidad()

print("OBJETO = carro")

#Mas datos
carro=Carro(4 ,str(input("Ingresa el color deseado: ")), "$600")
carro.cantidad()