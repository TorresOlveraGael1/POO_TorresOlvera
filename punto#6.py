#Crear una clase llamada Marino(), con un método que sea hablar, en donde muestre un mensaje que diga «Hola, soy un animal marino!»

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definiendo variable
class Marino():
    def hablar(self):
        print("Hola soy un animal marino!")

#Definiendo otra variable
class Pulpo(Marino):
    def hablar(self):
        print("Hola soy un pulpo!")

#Definiendo otra variable
class Foca(Marino):
    def hablar(self,mensaje):
        self.mensaje=mensaje
        print(mensaje)

#Resultados
marino=Marino()
marino.hablar()

pulpo=Pulpo()
pulpo.hablar()

foca=Foca()
foca.hablar("Hola soy una foca!")