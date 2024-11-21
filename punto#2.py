#Tendríamos que lograr ejecutar el siguiente código con la clase creada

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Declarando variable
class Persona:
    def __init__(self, n, e):
        self.nombre=n
        self.edad=e

#Iniciando funcion
    def cumpleaños(self):
        self.edad += 1
p=Persona(input("Ingrese su nombre: "),int(input("Ingrese edad: ")))
p.cumpleaños()
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")